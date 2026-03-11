from __future__ import annotations

from pathlib import Path
import re
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
ACTIVE_DOCS = [
    ROOT / "AGENTS.md",
    ROOT / "docs/mcp-setup.md",
    ROOT / "docs/workspace-guide.md",
    ROOT / "figma/docs/brand-color-foundations.md",
    ROOT / "figma/docs/brand-typography-foundations.md",
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


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_yaml(path: Path, data: Any) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=False)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def resolve_repo_path(root: Path, relative_path: str) -> Path:
    return root / relative_path


def validate_active_docs(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in ACTIVE_DOCS:
        text = path.read_text(encoding="utf-8")
        for rule_name, pattern in DOC_RULES.items():
            match = pattern.search(text)
            if match:
                errors.append(f"{path.relative_to(root)}: {rule_name}: `{match.group(0)}`")
    return errors


def validate_brand_manifest(path: Path, root: Path = ROOT) -> list[str]:
    data = load_yaml(path)
    errors: list[str] = []
    required_scalars = ["brand_id", "display_name", "status", "design_system_file_url"]
    for field in required_scalars:
        if not data.get(field):
            errors.append(f"{path.relative_to(root)}: missing `{field}`")

    if not data.get("owners"):
        errors.append(f"{path.relative_to(root)}: missing `owners`")
    if not data.get("supported_channels"):
        errors.append(f"{path.relative_to(root)}: missing `supported_channels`")

    staged_paths = data.get("staged_paths", {})
    for field in ["color_dir", "typography_dir"]:
        staged_path = staged_paths.get(field)
        if not staged_path:
            errors.append(f"{path.relative_to(root)}: missing `staged_paths.{field}`")
            continue
        if not resolve_repo_path(root, staged_path).exists():
            errors.append(f"{path.relative_to(root)}: staged path `{staged_path}` does not exist")

    for source_path in data.get("source_references", []):
        if not resolve_repo_path(root, source_path).exists():
            errors.append(f"{path.relative_to(root)}: source reference `{source_path}` does not exist")

    figma = data.get("figma", {})
    if not figma.get("design_system_file_url"):
        errors.append(f"{path.relative_to(root)}: missing `figma.design_system_file_url`")
    global_collections = figma.get("global_collections", {})
    for field in ["color_id", "typography_id", "dimensions_id"]:
        if not global_collections.get(field):
            errors.append(f"{path.relative_to(root)}: missing `figma.global_collections.{field}`")

    semantic_extensions = figma.get("semantic_extensions", {})
    for category in ["color", "typography"]:
        entry = semantic_extensions.get(category, {})
        for field in ["collection_name", "collection_id", "parent_collection", "parent_collection_id"]:
            if not entry.get(field):
                errors.append(
                    f"{path.relative_to(root)}: missing `figma.semantic_extensions.{category}.{field}`"
                )

    artifacts = data.get("artifacts", {})
    for category in ["color", "typography"]:
        artifact_group = artifacts.get(category, {})
        for field in ["intake_artifact", "preview_artifact"]:
            artifact_path = artifact_group.get(field)
            if not artifact_path:
                errors.append(f"{path.relative_to(root)}: missing `artifacts.{category}.{field}`")
                continue
            if not resolve_repo_path(root, artifact_path).exists():
                errors.append(
                    f"{path.relative_to(root)}: artifact `{artifact_path}` does not exist"
                )
        for decision_path in artifact_group.get("decision_artifacts", []):
            if not resolve_repo_path(root, decision_path).exists():
                errors.append(
                    f"{path.relative_to(root)}: decision artifact `{decision_path}` does not exist"
                )

    return errors


def validate_brand_registry(root: Path = ROOT) -> list[str]:
    path = root / "figma/brands/registry.yml"
    data = load_yaml(path)
    errors: list[str] = []
    if not isinstance(data.get("brands"), list) or not data["brands"]:
        return [f"{path.relative_to(root)}: `brands` must be a non-empty list"]

    seen: set[str] = set()
    for brand in data["brands"]:
        for field in [
            "brand_id",
            "display_name",
            "status",
            "manifest_path",
            "owners",
            "supported_channels",
            "foundation_status",
            "design_system_file_url",
        ]:
            if field not in brand or brand[field] in (None, "", []):
                errors.append(f"{path.relative_to(root)}: missing `{field}` for brand entry")
        brand_id = brand.get("brand_id")
        if brand_id in seen:
            errors.append(f"{path.relative_to(root)}: duplicate brand_id `{brand_id}`")
        else:
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


def validate_collection_snapshot(path: Path, root: Path) -> tuple[dict[str, Any], list[str]]:
    data = load_yaml(path)
    errors: list[str] = []
    collection = data.get("collection", {})
    for field in ["name", "id", "level", "category", "mode", "status", "figma_variable_count"]:
        if field not in collection or collection[field] in (None, ""):
            errors.append(f"{path.relative_to(root)}: missing `collection.{field}`")
    tokens = data.get("tokens")
    if not isinstance(tokens, list) or not tokens:
        errors.append(f"{path.relative_to(root)}: `tokens` must be a non-empty list")
    else:
        for token in tokens:
            for field in ["name", "type", "status"]:
                if field not in token or token[field] in (None, ""):
                    errors.append(f"{path.relative_to(root)}: token missing `{field}`")
            if "value" not in token:
                errors.append(f"{path.relative_to(root)}: token `{token.get('name')}` missing `value`")
    return data, errors


def validate_extension_snapshot(
    path: Path,
    base_collections: dict[str, dict[str, Any]],
    root: Path,
) -> tuple[dict[str, Any], list[str]]:
    data = load_yaml(path)
    errors: list[str] = []
    extension = data.get("extension", {})
    for field in [
        "brand_id",
        "brand_display_name",
        "category",
        "collection_name",
        "collection_id",
        "parent_collection",
        "parent_collection_id",
        "mode",
        "status",
        "figma_variable_count",
        "tracked_override_count",
    ]:
        if field not in extension or extension[field] in (None, ""):
            errors.append(f"{path.relative_to(root)}: missing `extension.{field}`")

    overrides = data.get("overrides")
    if not isinstance(overrides, list):
        errors.append(f"{path.relative_to(root)}: `overrides` must be a list")
        return data, errors

    if extension.get("tracked_override_count") != len(overrides):
        errors.append(
            f"{path.relative_to(root)}: `tracked_override_count` does not match override list length"
        )

    parent_name = extension.get("parent_collection")
    base_snapshot = base_collections.get(parent_name)
    if not base_snapshot:
        errors.append(f"{path.relative_to(root)}: missing base collection `{parent_name}`")
        return data, errors

    base_tokens = {token["name"]: token for token in base_snapshot["tokens"]}
    for override in overrides:
        for field in ["name", "type", "status", "value"]:
            if field not in override or override[field] in (None, ""):
                errors.append(f"{path.relative_to(root)}: override missing `{field}`")
        base_token = base_tokens.get(override.get("name"))
        if base_token is None:
            errors.append(
                f"{path.relative_to(root)}: override `{override.get('name')}` is not present in base collection"
            )
            continue
        base_target = base_token.get("alias_of", base_token.get("value"))
        override_target = override.get("alias_of", override.get("value"))
        if base_target == override_target:
            errors.append(
                f"{path.relative_to(root)}: override `{override.get('name')}` repeats the base target `{base_target}`"
            )

    return data, errors


def load_brand_registry_data(root: Path = ROOT) -> dict[str, Any]:
    return load_yaml(root / "figma/brands/registry.yml")


def load_variable_index(root: Path = ROOT) -> dict[str, Any]:
    return load_yaml(root / "figma/variables/index.yml")


def validate_collection_index(root: Path = ROOT) -> tuple[dict[str, dict[str, Any]], list[str]]:
    index = load_variable_index(root)
    errors: list[str] = []
    base_collections: dict[str, dict[str, Any]] = {}

    for item in index.get("collections", []):
        path = resolve_repo_path(root, item["path"])
        if not path.exists():
            errors.append(f"{path.relative_to(root)}: missing collection snapshot")
            continue
        data, snapshot_errors = validate_collection_snapshot(path, root)
        errors.extend(snapshot_errors)
        collection_name = data.get("collection", {}).get("name")
        if collection_name:
            base_collections[collection_name] = data

    return base_collections, errors


def validate_variable_index(root: Path = ROOT) -> list[str]:
    base_collections, errors = validate_collection_index(root)
    index = load_variable_index(root)

    for item in index.get("extensions", []):
        path = resolve_repo_path(root, item["path"])
        if not path.exists():
            errors.append(f"{path.relative_to(root)}: missing extension snapshot")
            continue
        _, snapshot_errors = validate_extension_snapshot(path, base_collections, root)
        errors.extend(snapshot_errors)

    return errors


def expected_extension_exports(root: Path = ROOT) -> list[dict[str, str]]:
    registry = load_brand_registry_data(root)
    expected: list[dict[str, str]] = []

    for brand in registry.get("brands", []):
        manifest_path = brand.get("manifest_path")
        if not manifest_path:
            continue
        manifest = load_yaml(resolve_repo_path(root, manifest_path))
        semantic_extensions = manifest.get("figma", {}).get("semantic_extensions", {})
        semantic_overrides = manifest.get("semantic_overrides", {})

        for category in ("color", "typography"):
            extension = semantic_extensions.get(category, {})
            if not extension.get("collection_id"):
                continue

            status = semantic_overrides.get(category, {}).get("status")
            if status in {"pending", "planned", "removed"}:
                continue

            expected.append(
                {
                    "brand_id": manifest.get("brand_id", brand.get("brand_id", "")),
                    "category": category,
                    "collection_name": extension.get("collection_name", ""),
                    "parent_collection": extension.get("parent_collection", ""),
                }
            )

    expected.sort(key=lambda item: (item["brand_id"], item["category"]))
    return expected


def validate_extension_exports(
    root: Path = ROOT,
    *,
    base_collections: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
    if base_collections is None:
        base_collections, collection_errors = validate_collection_index(root)
        errors = collection_errors
    else:
        errors: list[str] = []

    index = load_variable_index(root)
    index_path = root / "figma/variables/index.yml"
    indexed_extensions: dict[tuple[str | None, str | None], dict[str, Any]] = {}
    snapshot_data_by_key: dict[tuple[str | None, str | None], dict[str, Any]] = {}

    for item in index.get("extensions", []):
        key = (item.get("brand_id"), item.get("category"))
        if key in indexed_extensions:
            errors.append(
                f"{index_path.relative_to(root)}: duplicate extension entry for brand "
                f"`{item.get('brand_id')}` category `{item.get('category')}`"
            )
            continue

        indexed_extensions[key] = item
        path = resolve_repo_path(root, item["path"])
        if not path.exists():
            errors.append(f"{path.relative_to(root)}: missing extension snapshot")
            continue

        snapshot_data, snapshot_errors = validate_extension_snapshot(path, base_collections, root)
        errors.extend(snapshot_errors)
        snapshot_data_by_key[key] = snapshot_data

        extension = snapshot_data.get("extension", {})
        for field, expected_value in (
            ("brand_id", item.get("brand_id")),
            ("category", item.get("category")),
            ("parent_collection", item.get("parent_collection")),
        ):
            actual_value = extension.get(field)
            if expected_value and actual_value != expected_value:
                errors.append(
                    f"{path.relative_to(root)}: extension `{field}` is `{actual_value}` but "
                    f"index expects `{expected_value}`"
                )

    for requirement in expected_extension_exports(root):
        key = (requirement["brand_id"], requirement["category"])
        extension_item = indexed_extensions.get(key)
        if extension_item is None:
            errors.append(
                f"{index_path.relative_to(root)}: missing extension export entry for brand "
                f"`{requirement['brand_id']}` category `{requirement['category']}`; "
                "export the local extension snapshot before building the compatibility "
                "registry or rerun with `--base-only`"
            )
            continue

        parent_collection = extension_item.get("parent_collection")
        if parent_collection != requirement["parent_collection"]:
            errors.append(
                f"{index_path.relative_to(root)}: extension export entry for brand "
                f"`{requirement['brand_id']}` category `{requirement['category']}` "
                f"targets parent `{parent_collection}` but manifest expects "
                f"`{requirement['parent_collection']}`"
            )

        snapshot_data = snapshot_data_by_key.get(key)
        if snapshot_data is None:
            continue

        path = resolve_repo_path(root, extension_item["path"])
        extension = snapshot_data.get("extension", {})
        for field, expected_value in (
            ("brand_id", requirement["brand_id"]),
            ("category", requirement["category"]),
            ("parent_collection", requirement["parent_collection"]),
            ("collection_name", requirement["collection_name"]),
        ):
            actual_value = extension.get(field)
            if expected_value and actual_value != expected_value:
                errors.append(
                    f"{path.relative_to(root)}: extension `{field}` is `{actual_value}` but "
                    f"manifest expects `{expected_value}`"
                )

    return errors


def validate_export_inputs(root: Path = ROOT, *, base_only: bool = False) -> list[str]:
    base_collections, errors = validate_collection_index(root)
    if base_only:
        return errors

    errors.extend(validate_extension_exports(root, base_collections=base_collections))
    return errors


def build_registry(root: Path = ROOT, *, base_only: bool = False) -> dict[str, Any]:
    errors = validate_export_inputs(root, base_only=base_only)
    if errors:
        raise GovernanceError("\n".join(errors))

    index = load_variable_index(root)
    registry: dict[str, Any] = {
        "version": index["version"],
        "updated": index["updated"],
        "scope": "base_only" if base_only else "full",
        "collections": [],
        "variables": [],
    }

    for item in index.get("collections", []):
        snapshot = load_yaml(resolve_repo_path(root, item["path"]))
        collection = snapshot["collection"]
        registry["collections"].append(
            {
                "figma_url": snapshot["figma_url"],
                "id": collection["id"],
                "level": collection["level"],
                "collection": collection["name"],
                "mode": collection["mode"],
                "status": collection["status"],
                "variable_count": collection["figma_variable_count"],
            }
        )
        for token in snapshot["tokens"]:
            entry = {
                "figma_url": snapshot["figma_url"],
                "level": collection["level"],
                "collection": collection["name"],
                "mode": collection["mode"],
                "name": token["name"],
                "type": token["type"],
                "value": token["value"],
                "status": token["status"],
            }
            if "alias_of" in token:
                entry["alias_of"] = token["alias_of"]
            if "notes" in token:
                entry["notes"] = token["notes"]
            registry["variables"].append(entry)

    if not base_only:
        for item in index.get("extensions", []):
            snapshot = load_yaml(resolve_repo_path(root, item["path"]))
            extension = snapshot["extension"]
            registry["collections"].append(
                {
                    "figma_url": snapshot["figma_url"],
                    "id": extension["collection_id"],
                    "level": "semantic",
                    "collection": extension["collection_name"],
                    "mode": extension["mode"],
                    "status": extension["status"],
                    "variable_count": extension["figma_variable_count"],
                    "extension_of": extension["parent_collection"],
                    "parent_collection_id": extension["parent_collection_id"],
                    "override_count": extension["tracked_override_count"],
                }
            )
            for override in snapshot["overrides"]:
                entry = {
                    "figma_url": snapshot["figma_url"],
                    "level": "semantic",
                    "collection": extension["collection_name"],
                    "extension_of": extension["parent_collection"],
                    "mode": extension["mode"],
                    "name": override["name"],
                    "type": override["type"],
                    "value": override["value"],
                    "status": override["status"],
                }
                if "alias_of" in override:
                    entry["alias_of"] = override["alias_of"]
                if "notes" in override:
                    entry["notes"] = override["notes"]
                registry["variables"].append(entry)

    return registry


def resolve_registry_output_path(root: Path, *, base_only: bool = False) -> Path:
    index = load_variable_index(root)
    output_path = resolve_repo_path(root, index["generated_registry_path"])
    if not base_only:
        return output_path

    suffix = "".join(output_path.suffixes)
    stem = output_path.name[: -len(suffix)] if suffix else output_path.name
    base_only_name = f"{stem}.base-only{suffix}"
    return output_path.with_name(base_only_name)


def write_registry(root: Path = ROOT, *, base_only: bool = False) -> Path:
    output_path = resolve_registry_output_path(root, base_only=base_only)
    dump_yaml(output_path, build_registry(root, base_only=base_only))
    return output_path


def validate_repo(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_brand_registry(root))
    errors.extend(validate_active_docs(root))
    return errors
