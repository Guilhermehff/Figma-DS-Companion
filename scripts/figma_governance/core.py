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


def load_variable_index(root: Path = ROOT) -> dict[str, Any]:
    return load_yaml(root / "figma/variables/index.yml")


def validate_variable_index(root: Path = ROOT) -> list[str]:
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

    for item in index.get("extensions", []):
        path = resolve_repo_path(root, item["path"])
        if not path.exists():
            errors.append(f"{path.relative_to(root)}: missing extension snapshot")
            continue
        _, snapshot_errors = validate_extension_snapshot(path, base_collections, root)
        errors.extend(snapshot_errors)

    return errors


def build_registry(root: Path = ROOT) -> dict[str, Any]:
    index = load_variable_index(root)
    registry: dict[str, Any] = {
        "version": index["version"],
        "updated": index["updated"],
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


def write_registry(root: Path = ROOT) -> Path:
    index = load_variable_index(root)
    output_path = resolve_repo_path(root, index["generated_registry_path"])
    dump_yaml(output_path, build_registry(root))
    return output_path


def validate_repo(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_brand_registry(root))
    errors.extend(validate_active_docs(root))
    return errors
