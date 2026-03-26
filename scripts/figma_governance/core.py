from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import os
import re
import signal
import subprocess
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
MCP_PORT_START = 9223
MCP_PORT_END = 9235
MCP_MANAGED_COMMANDS = frozenset({"node", "bun"})
BRAND_FONT_INVENTORY_PATH = Path("figma/brands/font-inventory.yml")
BRAND_FONT_DIRECTORY_PATH = Path("figma/brands/font-directory.md")
EXPORT_INDEX_PATH = Path("figma/exports/index.yml")
EXPORT_ROOT_PATH = Path("figma/exports")
EXPORT_DATE_PREFIX_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-")
ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ACTIVE_DOC_PATHS = [
    Path("AGENTS.md"),
    Path("docs/mcp-setup.md"),
    Path("figma/docs/brand-color-foundations.md"),
    Path("figma/docs/brand-typography-foundations.md"),
]
DOC_RULES = {
    "legacy global collection names": re.compile(r"\b_global_(color|typography|dimensions)\b"),
    "legacy semantic collection names": re.compile(r"\bsemantic_(color|typography)\b"),
    "remote MCP governance guidance": re.compile(
        r"remote MCP server|remote server endpoint|mcp\.figma\.com/mcp",
        re.IGNORECASE,
    ),
}


class GovernanceError(RuntimeError):
    """Raised when validation cannot proceed."""


@dataclass(frozen=True)
class McpPortListener:
    pid: int
    port: int
    command: str
    endpoint: str


@dataclass(frozen=True)
class McpResetResult:
    listeners: list[McpPortListener]
    terminated: list[McpPortListener]
    preserved: list[McpPortListener]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_yaml(path: Path, data: Any) -> None:
    text = yaml.safe_dump(data, sort_keys=False)
    write_text(path, text)


def write_text(path: Path, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def resolve_repo_path(root: Path, relative_path: str) -> Path:
    return root / relative_path


def _load_yaml_from_repo(root: Path, relative_path: str) -> Any:
    path = resolve_repo_path(root, relative_path)
    try:
        return load_yaml(path)
    except FileNotFoundError as exc:
        raise GovernanceError(f"{path.relative_to(root)}: file does not exist") from exc
    except yaml.YAMLError as exc:
        raise GovernanceError(f"{path.relative_to(root)}: invalid YAML: {exc}") from exc


def _append_unique(items: list[str], value: Any) -> None:
    if isinstance(value, str) and value and value not in items:
        items.append(value)


def _coerce_iso_date(value: Any) -> str | None:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and ISO_DATE_PATTERN.match(value):
        return value
    return None


def _latest_iso_date(values: list[Any]) -> str | None:
    dates = [coerced for value in values if (coerced := _coerce_iso_date(value)) is not None]
    if not dates:
        return None
    return max(dates)


def _normalize_yaml_scalars(value: Any) -> Any:
    coerced = _coerce_iso_date(value)
    if coerced is not None:
        return coerced
    if isinstance(value, list):
        return [_normalize_yaml_scalars(item) for item in value]
    if isinstance(value, dict):
        return {key: _normalize_yaml_scalars(item) for key, item in value.items()}
    return value


def _extract_brand_fonts(intake: Any) -> list[dict[str, Any]]:
    if not isinstance(intake, dict):
        return []

    fonts_by_name: dict[str, dict[str, list[str]]] = {}
    font_order: list[str] = []

    primitive_recommendations = intake.get("primitive_recommendations", {})
    if isinstance(primitive_recommendations, dict):
        proposed_primitives = primitive_recommendations.get("proposed_primitives", {})
        if isinstance(proposed_primitives, dict):
            proposed_families = proposed_primitives.get("families", [])
            if isinstance(proposed_families, list):
                for family in proposed_families:
                    if not isinstance(family, dict):
                        continue
                    family_name = family.get("source_family_name")
                    if not isinstance(family_name, str) or not family_name:
                        continue
                    if family_name not in fonts_by_name:
                        fonts_by_name[family_name] = {
                            "token_names": [],
                            "source_style_references": [],
                        }
                        font_order.append(family_name)
                    entry = fonts_by_name[family_name]
                    _append_unique(entry["token_names"], family.get("token_name"))
                    _append_unique(entry["source_style_references"], family.get("source_style_reference"))

    if not font_order:
        source_roles = intake.get("source_roles", [])
        if isinstance(source_roles, list):
            for role in source_roles:
                if not isinstance(role, dict):
                    continue
                family_name = role.get("source_family_name")
                if not isinstance(family_name, str) or not family_name:
                    continue
                if family_name not in fonts_by_name:
                    fonts_by_name[family_name] = {
                        "token_names": [],
                        "source_style_references": [],
                    }
                    font_order.append(family_name)
                entry = fonts_by_name[family_name]
                _append_unique(entry["source_style_references"], role.get("source_style_name"))

    fonts: list[dict[str, Any]] = []
    for family_name in font_order:
        entry = {"family_name": family_name}
        details = fonts_by_name[family_name]
        if details["token_names"]:
            entry["token_names"] = details["token_names"]
        if details["source_style_references"]:
            entry["source_style_references"] = details["source_style_references"]
        fonts.append(entry)
    return fonts


def _build_brand_font_directory_entries(inventory: dict[str, Any]) -> list[dict[str, Any]]:
    font_to_brands: dict[str, list[str]] = {}
    brands = inventory.get("brands", [])
    if not isinstance(brands, list):
        return []

    for brand in brands:
        if not isinstance(brand, dict):
            continue
        display_name = brand.get("display_name")
        if not isinstance(display_name, str) or not display_name:
            continue
        fonts = brand.get("fonts", [])
        if not isinstance(fonts, list):
            continue
        for font in fonts:
            if not isinstance(font, dict):
                continue
            family_name = font.get("family_name")
            if not isinstance(family_name, str) or not family_name:
                continue
            brand_names = font_to_brands.setdefault(family_name, [])
            if display_name not in brand_names:
                brand_names.append(display_name)

    entries: list[dict[str, Any]] = []
    for family_name in sorted(font_to_brands, key=str.casefold):
        entries.append(
            {
                "family_name": family_name,
                "brands": sorted(font_to_brands[family_name], key=str.casefold),
            }
        )
    return entries


def _escape_markdown_cell(value: str) -> str:
    return value.replace("|", "\\|")


def build_brand_font_directory_markdown(inventory: dict[str, Any]) -> str:
    entries = _build_brand_font_directory_entries(inventory)
    updated = inventory.get("updated")

    lines = ["# Font Directory", ""]
    if isinstance(updated, str) and updated:
        lines.extend([f"Updated: {updated}", ""])
    lines.extend(
        [
            "| Font | Brands |",
            "| --- | --- |",
        ]
    )
    if not entries:
        lines.append("| None recorded | - |")
    else:
        for entry in entries:
            family_name = _escape_markdown_cell(entry["family_name"])
            brands = ", ".join(entry["brands"])
            lines.append(f"| {family_name} | {_escape_markdown_cell(brands)} |")
    return "\n".join(lines)


def build_brand_font_inventory(root: Path = ROOT) -> dict[str, Any]:
    registry_path = root / "figma/brands/registry.yml"
    try:
        registry = load_yaml(registry_path)
    except FileNotFoundError as exc:
        raise GovernanceError(f"{registry_path.relative_to(root)}: file does not exist") from exc
    except yaml.YAMLError as exc:
        raise GovernanceError(f"{registry_path.relative_to(root)}: invalid YAML: {exc}") from exc

    if not isinstance(registry, dict):
        raise GovernanceError(f"{registry_path.relative_to(root)}: top-level YAML must be a mapping")

    brands = registry.get("brands")
    if not isinstance(brands, list):
        raise GovernanceError(f"{registry_path.relative_to(root)}: `brands` must be a list")

    source_dates: list[Any] = [registry.get("updated")]
    inventory_brands: list[dict[str, Any]] = []

    for brand in brands:
        if not isinstance(brand, dict):
            continue

        manifest_path = brand.get("manifest_path")
        if not isinstance(manifest_path, str) or not manifest_path:
            raise GovernanceError(f"{registry_path.relative_to(root)}: brand entry is missing `manifest_path`")
        manifest = _load_yaml_from_repo(root, manifest_path)
        if not isinstance(manifest, dict):
            raise GovernanceError(f"{manifest_path}: top-level YAML must be a mapping")

        artifacts = manifest.get("artifacts", {})
        if not isinstance(artifacts, dict):
            raise GovernanceError(f"{manifest_path}: `artifacts` must be a mapping")
        typography = artifacts.get("typography", {})
        if not isinstance(typography, dict):
            raise GovernanceError(f"{manifest_path}: `artifacts.typography` must be a mapping")

        intake_artifact = typography.get("intake_artifact")
        if not isinstance(intake_artifact, str) or not intake_artifact:
            raise GovernanceError(f"{manifest_path}: missing `artifacts.typography.intake_artifact`")
        intake = _load_yaml_from_repo(root, intake_artifact)

        source_dates.extend([manifest.get("updated")])
        if isinstance(intake, dict):
            source_dates.append(intake.get("date"))

        inventory_brands.append(
            {
                "brand_id": manifest.get("brand_id") or brand.get("brand_id"),
                "display_name": manifest.get("display_name") or brand.get("display_name"),
                "status": manifest.get("status") or brand.get("status"),
                "typography_intake_artifact": intake_artifact,
                "fonts": _extract_brand_fonts(intake),
            }
        )

    return {
        "version": 1,
        "updated": _latest_iso_date(source_dates),
        "purpose": "generated_brand_font_inventory",
        "generated_from": {
            "registry": "figma/brands/registry.yml",
            "extraction_rule": (
                "Collect unique family names from each brand typography intake artifact, "
                "preferring `primitive_recommendations.proposed_primitives.families`."
            ),
        },
        "brands": inventory_brands,
    }


def sync_brand_font_inventory(root: Path = ROOT) -> tuple[Path, Path]:
    inventory = build_brand_font_inventory(root)
    inventory_path = root / BRAND_FONT_INVENTORY_PATH
    directory_path = root / BRAND_FONT_DIRECTORY_PATH
    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    write_yaml(inventory_path, inventory)
    write_text(directory_path, build_brand_font_directory_markdown(inventory))
    return inventory_path, directory_path


def validate_brand_font_inventory(root: Path = ROOT) -> list[str]:
    try:
        expected = build_brand_font_inventory(root)
        expected_directory = build_brand_font_directory_markdown(expected)
    except GovernanceError as exc:
        return [str(exc)]

    errors: list[str] = []

    inventory_path = root / BRAND_FONT_INVENTORY_PATH
    inventory_relative_path = inventory_path.relative_to(root).as_posix()
    if not inventory_path.exists():
        errors.append(
            (
                f"{inventory_relative_path}: generated brand font inventory is missing; run "
                "`python3 -m scripts.figma_governance sync-brand-fonts`"
            )
        )
    else:
        try:
            current = _normalize_yaml_scalars(load_yaml(inventory_path))
        except yaml.YAMLError as exc:
            errors.append(f"{inventory_relative_path}: invalid YAML: {exc}")
        else:
            if current != _normalize_yaml_scalars(expected):
                errors.append(
                    (
                        f"{inventory_relative_path}: generated brand font inventory is stale; run "
                        "`python3 -m scripts.figma_governance sync-brand-fonts`"
                    )
                )

    directory_path = root / BRAND_FONT_DIRECTORY_PATH
    directory_relative_path = directory_path.relative_to(root).as_posix()
    if not directory_path.exists():
        errors.append(
            (
                f"{directory_relative_path}: generated font directory is missing; run "
                "`python3 -m scripts.figma_governance sync-brand-fonts`"
            )
        )
    else:
        current_directory = directory_path.read_text(encoding="utf-8")
        if current_directory != f"{expected_directory}\n":
            errors.append(
                (
                    f"{directory_relative_path}: generated font directory is stale; run "
                    "`python3 -m scripts.figma_governance sync-brand-fonts`"
                )
            )

    return errors


def _has_dated_export_filename(relative_path: str) -> bool:
    return EXPORT_DATE_PREFIX_PATTERN.match(Path(relative_path).name) is not None


def _path_is_within(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
    except ValueError:
        return False
    return True


def _validate_export_entry_path(
    *,
    index_path: Path,
    root: Path,
    field_name: str,
    relative_path: Any,
) -> tuple[Path | None, list[str]]:
    errors: list[str] = []
    if not relative_path:
        errors.append(f"{index_path.relative_to(root)}: missing `{field_name}`")
        return None, errors
    if not isinstance(relative_path, str):
        errors.append(f"{index_path.relative_to(root)}: `{field_name}` must be a string path")
        return None, errors

    normalized_candidate = (root / relative_path).resolve(strict=False)
    export_root = (root / EXPORT_ROOT_PATH).resolve(strict=False)

    if not _path_is_within(export_root, normalized_candidate):
        errors.append(
            f"{index_path.relative_to(root)}: `{field_name}` must live under `{EXPORT_ROOT_PATH.as_posix()}/`"
        )

    if not _has_dated_export_filename(relative_path):
        errors.append(
            f"{index_path.relative_to(root)}: `{field_name}` must use a filename starting with `YYYY-MM-DD-`"
        )

    return normalized_candidate, errors


def _parse_mcp_listener_output(text: str) -> list[McpPortListener]:
    listeners: list[McpPortListener] = []
    pid: int | None = None
    command: str | None = None

    for raw_line in text.splitlines():
        if not raw_line:
            continue
        field = raw_line[0]
        value = raw_line[1:]
        if field == "p":
            pid = int(value)
            command = None
            continue
        if field == "c":
            command = value
            continue
        if field != "n" or pid is None or command is None:
            continue

        match = re.search(r":(\d+)$", value)
        if match is None:
            continue
        listeners.append(
            McpPortListener(
                pid=pid,
                port=int(match.group(1)),
                command=command,
                endpoint=value,
            )
        )

    listeners.sort(key=lambda item: (item.port, item.pid))
    return listeners


def list_mcp_port_listeners(
    *,
    port_start: int = MCP_PORT_START,
    port_end: int = MCP_PORT_END,
    runner: Any = subprocess.run,
) -> list[McpPortListener]:
    command = [
        "lsof",
        "-nP",
        f"-iTCP:{port_start}-{port_end}",
        "-sTCP:LISTEN",
        "-Fpcn",
    ]
    completed = runner(command, capture_output=True, text=True, check=False)
    if completed.returncode not in {0, 1}:
        detail = completed.stderr.strip() or completed.stdout.strip() or "lsof failed"
        raise GovernanceError(detail)
    if completed.returncode == 1 and not completed.stdout.strip():
        return []
    return _parse_mcp_listener_output(completed.stdout)


def reset_mcp_listeners(
    *,
    port_start: int = MCP_PORT_START,
    port_end: int = MCP_PORT_END,
    keep_ports: set[int] | None = None,
    dry_run: bool = False,
    runner: Any = subprocess.run,
    killer: Any = os.kill,
) -> McpResetResult:
    listeners = list_mcp_port_listeners(
        port_start=port_start,
        port_end=port_end,
        runner=runner,
    )
    managed = [listener for listener in listeners if listener.command in MCP_MANAGED_COMMANDS]
    unmanaged = [listener for listener in listeners if listener.command not in MCP_MANAGED_COMMANDS]
    if unmanaged:
        details = ", ".join(
            f"pid={listener.pid} port={listener.port} command={listener.command}"
            for listener in unmanaged
        )
        raise GovernanceError(
            "refusing to reset reserved MCP ports because non-MCP listeners were found: "
            f"{details}"
        )

    requested_keep_ports = set() if keep_ports is None else set(keep_ports)
    found_ports = {listener.port for listener in managed}
    missing_keep_ports = sorted(requested_keep_ports - found_ports)
    if missing_keep_ports:
        missing = ", ".join(str(port) for port in missing_keep_ports)
        raise GovernanceError(f"requested keep port is not listening: {missing}")

    preserved = [listener for listener in managed if listener.port in requested_keep_ports]
    terminated = [listener for listener in managed if listener.port not in requested_keep_ports]

    if not dry_run:
        killed_pids: set[int] = set()
        for listener in terminated:
            if listener.pid in killed_pids:
                continue
            killer(listener.pid, signal.SIGTERM)
            killed_pids.add(listener.pid)

    return McpResetResult(
        listeners=managed,
        terminated=terminated,
        preserved=preserved,
    )


def validate_active_docs(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative_path in ACTIVE_DOC_PATHS:
        path = root / relative_path
        if not path.exists():
            errors.append(f"{relative_path.as_posix()}: active doc is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for rule_name, pattern in DOC_RULES.items():
            match = pattern.search(text)
            if match:
                errors.append(f"{path.relative_to(root)}: {rule_name}: `{match.group(0)}`")
    return errors


def validate_brand_manifest(path: Path, root: Path = ROOT) -> list[str]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        return [f"{path.relative_to(root)}: top-level YAML must be a mapping"]

    errors: list[str] = []
    required_scalars = ["brand_id", "display_name", "status"]
    for field in required_scalars:
        if not data.get(field):
            errors.append(f"{path.relative_to(root)}: missing `{field}`")

    if not data.get("owners"):
        errors.append(f"{path.relative_to(root)}: missing `owners`")
    if not data.get("supported_channels"):
        errors.append(f"{path.relative_to(root)}: missing `supported_channels`")

    figma = data.get("figma", {})
    if not isinstance(figma, dict):
        errors.append(f"{path.relative_to(root)}: `figma` must be a mapping")
        return errors
    if not figma.get("design_system_file_url"):
        errors.append(f"{path.relative_to(root)}: missing `figma.design_system_file_url`")
    global_collections = figma.get("global_collections", {})
    if not isinstance(global_collections, dict):
        errors.append(f"{path.relative_to(root)}: `figma.global_collections` must be a mapping")
        global_collections = {}
    for field in ["color_id", "typography_id", "dimensions_id"]:
        if not global_collections.get(field):
            errors.append(f"{path.relative_to(root)}: missing `figma.global_collections.{field}`")

    semantic_extensions = figma.get("semantic_extensions", {})
    if not isinstance(semantic_extensions, dict):
        errors.append(f"{path.relative_to(root)}: `figma.semantic_extensions` must be a mapping")
        semantic_extensions = {}
    theme_extension = semantic_extensions.get("theme", {})
    if not isinstance(theme_extension, dict):
        errors.append(f"{path.relative_to(root)}: `figma.semantic_extensions.theme` must be a mapping")
        theme_extension = {}
    for field in ["collection_name", "collection_id", "parent_collection", "parent_collection_id"]:
        if not theme_extension.get(field):
            errors.append(
                f"{path.relative_to(root)}: missing `figma.semantic_extensions.theme.{field}`"
            )

    artifacts = data.get("artifacts", {})
    if not isinstance(artifacts, dict):
        errors.append(f"{path.relative_to(root)}: `artifacts` must be a mapping")
        return errors
    for category in ["color", "typography"]:
        artifact_group = artifacts.get(category, {})
        if not isinstance(artifact_group, dict):
            errors.append(f"{path.relative_to(root)}: `artifacts.{category}` must be a mapping")
            continue
        for field in ["intake_artifact", "preview_artifact"]:
            artifact_path = artifact_group.get(field)
            if not artifact_path:
                errors.append(f"{path.relative_to(root)}: missing `artifacts.{category}.{field}`")
                continue
            resolved_artifact = resolve_repo_path(root, artifact_path)
            if not resolved_artifact.exists():
                errors.append(
                    f"{path.relative_to(root)}: artifact `{artifact_path}` does not exist"
                )
                continue
            if resolved_artifact.suffix in {".yml", ".yaml"}:
                try:
                    load_yaml(resolved_artifact)
                except yaml.YAMLError as exc:
                    errors.append(
                        f"{path.relative_to(root)}: artifact `{artifact_path}` is invalid YAML: {exc}"
                    )
        decision_artifacts = artifact_group.get("decision_artifacts", [])
        if not isinstance(decision_artifacts, list):
            errors.append(
                f"{path.relative_to(root)}: `artifacts.{category}.decision_artifacts` must be a list"
            )
            continue
        for decision_path in decision_artifacts:
            if not resolve_repo_path(root, decision_path).exists():
                errors.append(
                    f"{path.relative_to(root)}: decision artifact `{decision_path}` does not exist"
                )

    semantic_overrides = data.get("semantic_overrides", {})
    if not isinstance(semantic_overrides, dict):
        errors.append(f"{path.relative_to(root)}: `semantic_overrides` must be a mapping")
        return errors

    theme_overrides = semantic_overrides.get("theme", {})
    if not isinstance(theme_overrides, dict):
        errors.append(f"{path.relative_to(root)}: `semantic_overrides.theme` must be a mapping")
        theme_overrides = {}
    status = theme_overrides.get("status")
    if not isinstance(status, str) or not status:
        errors.append(f"{path.relative_to(root)}: missing `semantic_overrides.theme.status`")

    color_overrides = theme_overrides.get("color", {})
    if not isinstance(color_overrides, dict):
        errors.append(f"{path.relative_to(root)}: `semantic_overrides.theme.color` must be a mapping")
        color_overrides = {}
    for field in ["override_scopes", "inherited_from_base", "notes"]:
        if field not in color_overrides:
            errors.append(f"{path.relative_to(root)}: missing `semantic_overrides.theme.color.{field}`")

    color_override_scopes = color_overrides.get("override_scopes", [])
    if not isinstance(color_override_scopes, list):
        errors.append(
            f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes` must be a list"
        )
    else:
        for index, scope in enumerate(color_override_scopes):
            if not isinstance(scope, dict):
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes[{index}]` must be a mapping"
                )
                continue
            scope_keys = set(scope.keys())
            allowed_keys = {"scope", "source_family", "source_value", "targets"}
            has_source_family = isinstance(scope.get("source_family"), str) and bool(scope.get("source_family"))
            has_source_value = isinstance(scope.get("source_value"), str) and bool(scope.get("source_value"))
            if (
                scope_keys - allowed_keys
                or "scope" not in scope_keys
                or "targets" not in scope_keys
                or has_source_family == has_source_value
            ):
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes[{index}]` "
                    "must use exactly `scope`, one of `source_family` or `source_value`, and `targets`"
                )
            if not scope.get("scope"):
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes[{index}].scope` is required"
                )
            if not has_source_family and not has_source_value:
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes[{index}]` "
                    "must define either `source_family` or `source_value`"
                )
            targets = scope.get("targets")
            if not isinstance(targets, list) or not all(isinstance(item, str) and item for item in targets):
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.color.override_scopes[{index}].targets` "
                    "must be a non-empty string list"
                )

    for field in ["inherited_from_base", "notes"]:
        items = color_overrides.get(field, [])
        if not isinstance(items, list):
            errors.append(f"{path.relative_to(root)}: `semantic_overrides.theme.color.{field}` must be a list")

    typography_overrides = theme_overrides.get("typography", {})
    if not isinstance(typography_overrides, dict):
        errors.append(f"{path.relative_to(root)}: `semantic_overrides.theme.typography` must be a mapping")
        typography_overrides = {}
    for field in ["override_scopes", "inherited_from_base", "notes"]:
        if field not in typography_overrides:
            errors.append(f"{path.relative_to(root)}: missing `semantic_overrides.theme.typography.{field}`")
            continue
        if not isinstance(typography_overrides[field], list):
            errors.append(
                f"{path.relative_to(root)}: `semantic_overrides.theme.typography.{field}` must be a list"
            )

    typography_override_scopes = typography_overrides.get("override_scopes", [])
    if isinstance(typography_override_scopes, list):
        for index, scope in enumerate(typography_override_scopes):
            if not isinstance(scope, dict):
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.typography.override_scopes[{index}]` must be a mapping"
                )
                continue
            if set(scope.keys()) != {"semantic_token", "alias_of"}:
                errors.append(
                    f"{path.relative_to(root)}: `semantic_overrides.theme.typography.override_scopes[{index}]` "
                    "must use exactly `semantic_token` and `alias_of`"
                )
            for field in ["semantic_token", "alias_of"]:
                if not isinstance(scope.get(field), str) or not scope.get(field):
                    errors.append(
                        f"{path.relative_to(root)}: `semantic_overrides.theme.typography.override_scopes[{index}].{field}` is required"
                    )

    return errors


def validate_brand_registry(root: Path = ROOT) -> list[str]:
    path = root / "figma/brands/registry.yml"
    data = load_yaml(path)
    if not isinstance(data, dict):
        return [f"{path.relative_to(root)}: top-level YAML must be a mapping"]

    errors: list[str] = []
    brands = data.get("brands")
    if not isinstance(brands, list) or not brands:
        return [f"{path.relative_to(root)}: `brands` must be a non-empty list"]

    seen: set[str] = set()
    for brand in brands:
        if not isinstance(brand, dict):
            errors.append(f"{path.relative_to(root)}: each brand entry must be a mapping")
            continue
        for field in ["brand_id", "display_name", "status", "manifest_path"]:
            if field not in brand or brand[field] in (None, "", []):
                errors.append(f"{path.relative_to(root)}: missing `{field}` for brand entry")
        brand_id = brand.get("brand_id")
        if brand_id in seen:
            errors.append(f"{path.relative_to(root)}: duplicate brand_id `{brand_id}`")
        elif brand_id:
            seen.add(brand_id)

        manifest_path = brand.get("manifest_path")
        if manifest_path:
            resolved = resolve_repo_path(root, manifest_path)
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(root)}: manifest `{manifest_path}` does not exist"
                )
            else:
                errors.extend(validate_brand_manifest(resolved, root))

    return errors


def validate_export_inputs(root: Path = ROOT) -> list[str]:
    index_path = root / EXPORT_INDEX_PATH
    if not index_path.exists():
        return []

    index = load_yaml(index_path)
    if not isinstance(index, dict):
        return [f"{index_path.relative_to(root)}: top-level YAML must be a mapping"]

    errors: list[str] = []
    for section_name in ("collections", "extensions"):
        entries = index.get(section_name, [])
        if not isinstance(entries, list):
            errors.append(f"{index_path.relative_to(root)}: `{section_name}` must be a list")
            continue

        for item in entries:
            key = item.get("key", "?") if isinstance(item, dict) else "?"
            field_name = f"{section_name}[{key}].path"
            if not isinstance(item, dict):
                errors.append(
                    f"{index_path.relative_to(root)}: `{section_name}` entries must be mappings"
                )
                continue

            resolved_path, path_errors = _validate_export_entry_path(
                index_path=index_path,
                root=root,
                field_name=field_name,
                relative_path=item.get("path"),
            )
            errors.extend(path_errors)
            if resolved_path is None or path_errors:
                continue
            if not resolved_path.exists():
                errors.append(f"{item['path']}: listed export file does not exist")
                continue
            if not resolved_path.is_file():
                errors.append(f"{item['path']}: listed export path must point to a file")
                continue
            if resolved_path.suffix in {".yml", ".yaml"}:
                try:
                    load_yaml(resolved_path)
                except yaml.YAMLError as exc:
                    errors.append(f"{item['path']}: invalid YAML export: {exc}")

    return errors


def validate_repo(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    brand_errors = validate_brand_registry(root)
    errors.extend(brand_errors)
    if not brand_errors:
        errors.extend(validate_brand_font_inventory(root))
    errors.extend(validate_active_docs(root))
    errors.extend(validate_export_inputs(root))
    return errors
