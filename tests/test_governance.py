from __future__ import annotations

from pathlib import Path
import signal
import subprocess

import pytest
import yaml

from scripts.figma_governance.core import (
    DOC_RULES,
    GovernanceError,
    MCP_PORT_END,
    MCP_PORT_START,
    ROOT,
    build_registry,
    list_mcp_port_listeners,
    reset_mcp_listeners,
    validate_brand_manifest,
    validate_export_inputs,
    validate_extension_snapshot,
    validate_repo,
    write_registry,
)


FIXTURES = ROOT / "tests/fixtures"


def _write_yaml(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = yaml.safe_dump(data, sort_keys=False)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def _make_export_repo(
    root: Path,
    *,
    include_extension_entry: bool = False,
    include_extension_snapshot: bool = False,
) -> Path:
    _write_yaml(
        root / "figma/brands/registry.yml",
        {
            "version": 1,
            "updated": "2026-03-11",
            "brands": [
                {
                    "brand_id": "demo",
                    "display_name": "Demo",
                    "status": "active",
                    "manifest_path": "figma/brands/demo/brand.yml",
                    "owners": ["design_system_governance"],
                    "supported_channels": ["web"],
                    "foundation_status": {"color": "approved", "typography": "planned"},
                    "design_system_file_url": "https://example.com/file",
                }
            ],
        },
    )
    _write_yaml(
        root / "figma/brands/demo/brand.yml",
        {
            "brand_id": "demo",
            "display_name": "Demo",
            "figma": {
                "semantic_extensions": {
                    "color": {
                        "collection_name": "Demo",
                        "collection_id": "ext-color",
                        "parent_collection": "Semantic: Color",
                        "parent_collection_id": "base-color",
                    },
                    "typography": {},
                }
            },
            "semantic_overrides": {
                "color": {"status": "active"},
                "typography": {"status": "pending"},
            },
        },
    )
    _write_yaml(
        root / "figma/variables/collections/semantic-color-base.yml",
        {
            "version": 1,
            "updated": "2026-03-11",
            "figma_url": "https://example.com/file",
            "collection": {
                "name": "Semantic: Color",
                "id": "base-color",
                "level": "semantic",
                "category": "color",
                "mode": "values",
                "status": "active",
                "figma_variable_count": 1,
            },
            "tokens": [
                {
                    "name": "brand/500",
                    "type": "color",
                    "value": "#006CD1",
                    "alias_of": "universal/blue/500",
                    "status": "active",
                }
            ],
        },
    )

    index = {
        "version": 1,
        "updated": "2026-03-11",
        "generated_registry_path": "figma/variables/registry.yml",
        "collections": [
            {
                "key": "semantic-color-base",
                "path": "figma/variables/collections/semantic-color-base.yml",
                "collection": "Semantic: Color",
                "category": "color",
                "level": "semantic",
            }
        ],
        "extensions": [],
    }
    if include_extension_entry:
        index["extensions"].append(
            {
                "key": "demo-semantic-color",
                "path": "figma/variables/extensions/demo-semantic-color.yml",
                "brand_id": "demo",
                "category": "color",
                "parent_collection": "Semantic: Color",
            }
        )
    _write_yaml(root / "figma/variables/index.yml", index)

    if include_extension_snapshot:
        _write_yaml(
            root / "figma/variables/extensions/demo-semantic-color.yml",
            {
                "version": 1,
                "updated": "2026-03-11",
                "figma_url": "https://example.com/file",
                "extension": {
                    "brand_id": "demo",
                    "brand_display_name": "Demo",
                    "category": "color",
                    "collection_name": "Demo",
                    "collection_id": "ext-color",
                    "parent_collection": "Semantic: Color",
                    "parent_collection_id": "base-color",
                    "mode": "values",
                    "status": "active",
                    "figma_variable_count": 1,
                    "tracked_override_count": 1,
                },
                "overrides": [
                    {
                        "name": "brand/500",
                        "type": "color",
                        "value": "#D71920",
                        "alias_of": "demo/red/500",
                        "status": "active",
                    }
                ],
            },
        )

    return root


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


def test_validate_export_inputs_requires_extension_snapshots_for_full_export(tmp_path: Path) -> None:
    root = _make_export_repo(tmp_path)

    errors = validate_export_inputs(root)

    assert any("missing extension export entry" in error for error in errors)
    assert validate_export_inputs(root, base_only=True) == []


def test_validate_export_inputs_base_only_skips_extension_snapshot_requirements(tmp_path: Path) -> None:
    root = _make_export_repo(tmp_path, include_extension_entry=True)

    assert validate_export_inputs(root, base_only=True) == []


def test_build_registry_base_only_uses_whatever_base_collections_are_indexed(tmp_path: Path) -> None:
    root = _make_export_repo(tmp_path)

    registry = build_registry(root, base_only=True)
    index = yaml.safe_load((root / "figma/variables/index.yml").read_text(encoding="utf-8"))

    assert registry["scope"] == "base_only"
    assert len(registry["collections"]) == len(index["collections"])
    assert [item["collection"] for item in registry["collections"]] == ["Semantic: Color"]


def test_write_registry_base_only_uses_a_distinct_output_path(tmp_path: Path) -> None:
    root = _make_export_repo(tmp_path)

    output_path = write_registry(root, base_only=True)
    registry = yaml.safe_load(output_path.read_text(encoding="utf-8"))

    assert output_path.name == "registry.base-only.yml"
    assert registry["scope"] == "base_only"


def test_build_registry_full_export_fails_when_extension_snapshots_are_missing(tmp_path: Path) -> None:
    root = _make_export_repo(tmp_path)

    with pytest.raises(GovernanceError, match="missing extension export entry"):
        build_registry(root)


def test_build_registry_full_export_passes_when_extension_snapshots_are_prepared(
    tmp_path: Path,
) -> None:
    root = _make_export_repo(
        tmp_path,
        include_extension_entry=True,
        include_extension_snapshot=True,
    )

    assert validate_export_inputs(root) == []
    registry = build_registry(root)

    assert registry["scope"] == "full"
    assert any(item.get("extension_of") == "Semantic: Color" for item in registry["collections"])


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("brand_id", "wrong-brand"),
        ("category", "typography"),
    ],
)
def test_validate_export_inputs_rejects_extension_snapshot_identity_mismatch(
    tmp_path: Path,
    field: str,
    bad_value: str,
) -> None:
    root = _make_export_repo(
        tmp_path,
        include_extension_entry=True,
        include_extension_snapshot=True,
    )
    snapshot_path = root / "figma/variables/extensions/demo-semantic-color.yml"
    snapshot = yaml.safe_load(snapshot_path.read_text(encoding="utf-8"))
    snapshot["extension"][field] = bad_value
    _write_yaml(snapshot_path, snapshot)

    errors = validate_export_inputs(root)

    assert any(f"extension `{field}`" in error for error in errors)


def test_check_docs_rejects_legacy_guidance(tmp_path: Path) -> None:
    doc = tmp_path / "legacy.md"
    doc.write_text("Use the remote MCP server and _global_color.", encoding="utf-8")
    text = doc.read_text(encoding="utf-8")
    errors = [
        rule_name for rule_name, pattern in DOC_RULES.items() if pattern.search(text)
    ]
    assert errors


def test_list_mcp_port_listeners_parses_lsof_output() -> None:
    def fake_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(
            args=["lsof"],
            returncode=0,
            stdout="\n".join(
                [
                    "p60652",
                    "cnode",
                    "f18",
                    "n[::1]:9223",
                    "p70117",
                    "cbun",
                    "f19",
                    "n127.0.0.1:9226",
                ]
            ),
            stderr="",
        )

    listeners = list_mcp_port_listeners(
        port_start=MCP_PORT_START,
        port_end=MCP_PORT_END,
        runner=fake_runner,
    )

    assert [(listener.pid, listener.port, listener.command) for listener in listeners] == [
        (60652, 9223, "node"),
        (70117, 9226, "bun"),
    ]


def test_reset_mcp_listeners_terminates_all_non_preserved_ports() -> None:
    killed: list[tuple[int, int]] = []

    def fake_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(
            args=["lsof"],
            returncode=0,
            stdout="\n".join(
                [
                    "p60652",
                    "cnode",
                    "f18",
                    "n[::1]:9223",
                    "p65997",
                    "cnode",
                    "f18",
                    "n[::1]:9224",
                ]
            ),
            stderr="",
        )

    def fake_killer(pid: int, sig: int) -> None:
        killed.append((pid, sig))

    result = reset_mcp_listeners(
        keep_ports={9224},
        runner=fake_runner,
        killer=fake_killer,
    )

    assert [(listener.pid, listener.port) for listener in result.terminated] == [(60652, 9223)]
    assert [(listener.pid, listener.port) for listener in result.preserved] == [(65997, 9224)]
    assert killed == [(60652, signal.SIGTERM)]


def test_reset_mcp_listeners_dry_run_skips_sigterm() -> None:
    killed: list[tuple[int, int]] = []

    def fake_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(
            args=["lsof"],
            returncode=0,
            stdout="\n".join(
                [
                    "p70117",
                    "cnode",
                    "f19",
                    "n[::1]:9226",
                ]
            ),
            stderr="",
        )

    result = reset_mcp_listeners(
        dry_run=True,
        runner=fake_runner,
        killer=lambda pid, sig: killed.append((pid, sig)),
    )

    assert [(listener.pid, listener.port) for listener in result.terminated] == [(70117, 9226)]
    assert killed == []


def test_reset_mcp_listeners_rejects_non_mcp_listener() -> None:
    def fake_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(
            args=["lsof"],
            returncode=0,
            stdout="\n".join(
                [
                    "p60652",
                    "cpython",
                    "f18",
                    "n[::1]:9223",
                ]
            ),
            stderr="",
        )

    with pytest.raises(GovernanceError, match="non-MCP listeners were found"):
        reset_mcp_listeners(runner=fake_runner)


def test_validate_repo_passes() -> None:
    assert validate_repo(ROOT) == []
