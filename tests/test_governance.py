from __future__ import annotations

from pathlib import Path

import yaml

from scripts.figma_governance.core import (
    DOC_RULES,
    ROOT,
    validate_brand_manifest,
    validate_extension_snapshot,
    validate_repo,
)


FIXTURES = ROOT / "tests/fixtures"


def test_fixture_brand_manifests_validate() -> None:
    fixture_paths = [
        FIXTURES / "brands/primary-only/brand.yml",
        FIXTURES / "brands/multi-family/brand.yml",
        FIXTURES / "brands/typography-override/brand.yml",
    ]
    for path in fixture_paths:
        assert validate_brand_manifest(path, FIXTURES) == []


def test_extension_override_only_rule_rejects_redundant_override(tmp_path: Path) -> None:
    base_path = tmp_path / "base.yml"
    extension_path = tmp_path / "extension.yml"
    base_path.write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "updated": "2026-03-11",
                "figma_url": "https://example.com/file",
                "collection": {
                    "name": "Semantic: Typography",
                    "id": "base-1",
                    "level": "semantic",
                    "category": "typography",
                    "mode": "values",
                    "status": "active",
                    "figma_variable_count": 1,
                },
                "tokens": [
                    {
                        "name": "family/body",
                        "type": "string",
                        "value": "Inter",
                        "alias_of": "universal/family/primary",
                        "status": "active",
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    extension_path.write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "updated": "2026-03-11",
                "figma_url": "https://example.com/file",
                "extension": {
                    "brand_id": "demo",
                    "brand_display_name": "Demo",
                    "category": "typography",
                    "collection_name": "Demo",
                    "collection_id": "ext-1",
                    "parent_collection": "Semantic: Typography",
                    "parent_collection_id": "base-1",
                    "mode": "values",
                    "status": "active",
                    "figma_variable_count": 1,
                    "tracked_override_count": 1,
                },
                "overrides": [
                    {
                        "name": "family/body",
                        "type": "string",
                        "value": "Inter",
                        "alias_of": "universal/family/primary",
                        "status": "active",
                    }
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    _, errors = validate_extension_snapshot(
        extension_path,
        {"Semantic: Typography": yaml.safe_load(base_path.read_text(encoding="utf-8"))},
        tmp_path,
    )
    assert any("repeats the base target" in error for error in errors)

def test_check_docs_rejects_legacy_guidance(tmp_path: Path) -> None:
    doc = tmp_path / "legacy.md"
    doc.write_text("Use the remote MCP server and _global_color.", encoding="utf-8")
    text = doc.read_text(encoding="utf-8")
    errors = [
        rule_name for rule_name, pattern in DOC_RULES.items() if pattern.search(text)
    ]
    assert errors


def test_validate_repo_passes() -> None:
    assert validate_repo(ROOT) == []
