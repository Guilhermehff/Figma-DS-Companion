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
    list_mcp_port_listeners,
    reset_mcp_listeners,
    sync_brand_font_inventory,
    validate_brand_manifest,
    validate_brand_font_inventory,
    validate_export_inputs,
    validate_repo,
)


FIXTURES = ROOT / "tests/fixtures"


def _write_yaml(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = yaml.safe_dump(data, sort_keys=False)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def _write_active_docs(root: Path) -> None:
    (root / "AGENTS.md").write_text("Companion rules.\n", encoding="utf-8")
    (root / "docs/mcp-setup.md").parent.mkdir(parents=True, exist_ok=True)
    (root / "docs/mcp-setup.md").write_text("MCP setup.\n", encoding="utf-8")
    (root / "figma/docs").mkdir(parents=True, exist_ok=True)
    (root / "figma/docs/brand-color-foundations.md").write_text(
        "Brand color foundations.\n",
        encoding="utf-8",
    )
    (root / "figma/docs/brand-typography-foundations.md").write_text(
        "Brand typography foundations.\n",
        encoding="utf-8",
    )


def _make_valid_brand_repo(root: Path) -> None:
    _write_active_docs(root)
    _write_yaml(
        root / "figma/brands/registry.yml",
        {
            "version": 1,
            "updated": "2026-03-12",
            "brands": [
                {
                    "brand_id": "demo",
                    "display_name": "Demo",
                    "status": "active",
                    "manifest_path": "figma/brands/demo/brand.yml",
                }
            ],
        },
    )
    (root / "figma/brands/demo").mkdir(parents=True, exist_ok=True)
    (root / "figma/brands/demo/color-intake.yml").write_text("date: 2026-03-12\n", encoding="utf-8")
    (root / "figma/brands/demo/color-preview.md").write_text("# Color\n", encoding="utf-8")
    (root / "figma/brands/demo/typography-intake.yml").write_text(
        "date: 2026-03-12\n",
        encoding="utf-8",
    )
    (root / "figma/brands/demo/typography-preview.md").write_text(
        "# Typography\n",
        encoding="utf-8",
    )
    _write_yaml(
        root / "figma/brands/demo/brand.yml",
        {
            "version": 1,
            "updated": "2026-03-12",
            "brand_id": "demo",
            "display_name": "Demo",
            "status": "active",
            "owners": ["design_system_governance"],
            "supported_channels": ["web"],
            "figma": {
                "design_system_file_url": "https://example.com/file",
                "global_collections": {
                    "color_id": "global-color",
                    "typography_id": "global-typography",
                    "dimensions_id": "global-dimensions",
                },
                "semantic_extensions": {
                    "color": {
                        "collection_name": "Demo",
                        "collection_id": "ext-color",
                        "parent_collection": "Semantic: Color",
                        "parent_collection_id": "base-color",
                    },
                    "typography": {
                        "collection_name": "Demo",
                        "collection_id": "ext-typography",
                        "parent_collection": "Semantic: Typography",
                        "parent_collection_id": "base-typography",
                    },
                },
            },
            "artifacts": {
                "color": {
                    "intake_artifact": "figma/brands/demo/color-intake.yml",
                    "preview_artifact": "figma/brands/demo/color-preview.md",
                    "decision_artifacts": [],
                },
                "typography": {
                    "intake_artifact": "figma/brands/demo/typography-intake.yml",
                    "preview_artifact": "figma/brands/demo/typography-preview.md",
                    "decision_artifacts": [],
                },
            },
            "semantic_overrides": {
                "color": {"status": "active", "override_scopes": [], "inherited_from_base": [], "notes": []},
                "typography": {"status": "active", "override_scopes": [], "inherited_from_base": [], "notes": []},
            },
            "notes": [],
        },
    )


def _write_export_index(
    root: Path,
    *,
    collections: list[dict[str, object]] | None = None,
    extensions: list[dict[str, object]] | None = None,
) -> None:
    _write_yaml(
        root / "figma/exports/index.yml",
        {
            "version": 1,
            "updated": "2026-03-12",
            "purpose": "optional_local_exports",
            "freshness_warning": (
                "Exports are dated snapshots and may be out of date relative to live Figma."
            ),
            "collections": [] if collections is None else collections,
            "extensions": [] if extensions is None else extensions,
            "notes": [
                "Use exports only for optional audits and manual reference snapshots.",
            ],
        },
    )


def test_fixture_brand_manifests_validate() -> None:
    fixture_paths = [
        FIXTURES / "brands/primary-only/brand.yml",
        FIXTURES / "brands/multi-family/brand.yml",
        FIXTURES / "brands/typography-override/brand.yml",
    ]
    for path in fixture_paths:
        assert validate_brand_manifest(path, FIXTURES) == []


def test_validate_brand_manifest_rejects_legacy_color_override_shape(tmp_path: Path) -> None:
    intake_path = tmp_path / "brands/demo/color-intake.yml"
    intake_path.parent.mkdir(parents=True, exist_ok=True)
    intake_path.write_text("date: 2026-03-14\n", encoding="utf-8")
    (tmp_path / "brands/demo/color-preview.md").write_text("# Preview\n", encoding="utf-8")
    (tmp_path / "brands/demo/typography-intake.yml").write_text("date: 2026-03-14\n", encoding="utf-8")
    (tmp_path / "brands/demo/typography-preview.md").write_text("# Preview\n", encoding="utf-8")
    manifest_path = tmp_path / "brands/demo/brand.yml"
    _write_yaml(
        manifest_path,
        {
            "version": 1,
            "updated": "2026-03-14",
            "brand_id": "demo",
            "display_name": "Demo",
            "status": "active",
            "owners": ["design_system_governance"],
            "supported_channels": ["web"],
            "figma": {
                "design_system_file_url": "https://example.com/file",
                "global_collections": {
                    "color_id": "global-color",
                    "typography_id": "global-typography",
                    "dimensions_id": "global-dimensions",
                },
                "semantic_extensions": {
                    "color": {
                        "collection_name": "Demo",
                        "collection_id": "ext-color",
                        "parent_collection": "Semantic: Color",
                        "parent_collection_id": "base-color",
                    },
                    "typography": {
                        "collection_name": "Demo",
                        "collection_id": "ext-typography",
                        "parent_collection": "Semantic: Typography",
                        "parent_collection_id": "base-typography",
                    },
                },
            },
            "artifacts": {
                "color": {
                    "intake_artifact": "brands/demo/color-intake.yml",
                    "preview_artifact": "brands/demo/color-preview.md",
                    "decision_artifacts": [],
                },
                "typography": {
                    "intake_artifact": "brands/demo/typography-intake.yml",
                    "preview_artifact": "brands/demo/typography-preview.md",
                    "decision_artifacts": [],
                },
            },
            "semantic_overrides": {
                "color": {
                    "status": "active",
                    "override_scopes": [{"semantic_slot": "brand", "raw_family": "demo/blue"}],
                    "inherited_from_base": [],
                    "notes": [],
                },
                "typography": {
                    "status": "active",
                    "override_scopes": [],
                    "inherited_from_base": [],
                    "notes": [],
                },
            },
            "notes": [],
        },
    )

    errors = validate_brand_manifest(manifest_path, tmp_path)

    assert any(
        "must use exactly `scope`, one of `source_family` or `source_value`, and `targets`" in error
        for error in errors
    )


def test_validate_brand_manifest_rejects_invalid_intake_yaml(tmp_path: Path) -> None:
    intake_path = tmp_path / "brands/demo/color-intake.yml"
    intake_path.parent.mkdir(parents=True, exist_ok=True)
    intake_path.write_text("date: 2026-03-12\nbroken: [\n", encoding="utf-8")
    (tmp_path / "brands/demo/color-preview.md").write_text("# Preview\n", encoding="utf-8")
    (tmp_path / "brands/demo/typography-intake.yml").write_text("date: 2026-03-12\n", encoding="utf-8")
    (tmp_path / "brands/demo/typography-preview.md").write_text("# Preview\n", encoding="utf-8")
    manifest_path = tmp_path / "brands/demo/brand.yml"
    _write_yaml(
        manifest_path,
        {
            "version": 1,
            "updated": "2026-03-12",
            "brand_id": "demo",
            "display_name": "Demo",
            "status": "active",
            "owners": ["design_system_governance"],
            "supported_channels": ["web"],
            "figma": {
                "design_system_file_url": "https://example.com/file",
                "global_collections": {
                    "color_id": "global-color",
                    "typography_id": "global-typography",
                    "dimensions_id": "global-dimensions",
                },
                "semantic_extensions": {
                    "color": {
                        "collection_name": "Demo",
                        "collection_id": "ext-color",
                        "parent_collection": "Semantic: Color",
                        "parent_collection_id": "base-color",
                    },
                    "typography": {
                        "collection_name": "Demo",
                        "collection_id": "ext-typography",
                        "parent_collection": "Semantic: Typography",
                        "parent_collection_id": "base-typography",
                    },
                },
            },
            "artifacts": {
                "color": {
                    "intake_artifact": "brands/demo/color-intake.yml",
                    "preview_artifact": "brands/demo/color-preview.md",
                    "decision_artifacts": [],
                },
                "typography": {
                    "intake_artifact": "brands/demo/typography-intake.yml",
                    "preview_artifact": "brands/demo/typography-preview.md",
                    "decision_artifacts": [],
                },
            },
            "semantic_overrides": {
                "color": {"status": "active", "override_scopes": [], "inherited_from_base": [], "notes": []},
                "typography": {"status": "pending", "override_scopes": [], "inherited_from_base": [], "notes": []},
            },
            "notes": [],
        },
    )

    errors = validate_brand_manifest(manifest_path, tmp_path)

    assert any("invalid YAML" in error for error in errors)


def test_validate_export_inputs_accepts_empty_index(tmp_path: Path) -> None:
    _write_export_index(tmp_path)

    assert validate_export_inputs(tmp_path) == []


def test_validate_export_inputs_rejects_undated_export_paths(tmp_path: Path) -> None:
    _write_export_index(
        tmp_path,
        collections=[
            {
                "key": "semantic-color-base",
                "path": "figma/exports/semantic-color-base.yml",
            }
        ],
    )

    errors = validate_export_inputs(tmp_path)

    assert any("must use a filename starting with `YYYY-MM-DD-`" in error for error in errors)


def test_validate_export_inputs_rejects_escaped_export_paths(tmp_path: Path) -> None:
    _write_yaml(
        tmp_path / "figma/brands/2026-03-12-escaped.yml",
        {"snapshot": "outside exports"},
    )
    _write_export_index(
        tmp_path,
        collections=[
            {
                "key": "escaped",
                "path": "figma/exports/../brands/2026-03-12-escaped.yml",
            }
        ],
    )

    errors = validate_export_inputs(tmp_path)

    assert any("must live under `figma/exports/`" in error for error in errors)


def test_validate_export_inputs_reports_missing_path_instead_of_crashing(tmp_path: Path) -> None:
    _write_export_index(
        tmp_path,
        collections=[
            {
                "key": "semantic-color-base",
            }
        ],
    )

    errors = validate_export_inputs(tmp_path)

    assert any("missing `collections[semantic-color-base].path`" in error for error in errors)


def test_validate_export_inputs_rejects_invalid_yaml_exports(tmp_path: Path) -> None:
    export_path = tmp_path / "figma/exports/2026-03-12-bad-export.yml"
    export_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.write_text("broken: [\n", encoding="utf-8")
    _write_export_index(
        tmp_path,
        collections=[
            {
                "key": "bad-export",
                "path": "figma/exports/2026-03-12-bad-export.yml",
            }
        ],
    )

    errors = validate_export_inputs(tmp_path)

    assert any("invalid YAML export" in error for error in errors)


def test_sync_brand_font_inventory_collects_fonts_by_brand(tmp_path: Path) -> None:
    _make_valid_brand_repo(tmp_path)
    _write_yaml(
        tmp_path / "figma/brands/demo/typography-intake.yml",
        {
            "date": "2026-03-13",
            "primitive_recommendations": {
                "proposed_primitives": {
                    "families": [
                        {
                            "token_name": "demo/family/primary",
                            "source_family_name": "Inter",
                            "source_style_reference": "Inter Bold",
                        },
                        {
                            "token_name": "demo/family/secondary",
                            "source_family_name": "Avenir Next",
                            "source_style_reference": "Avenir Next Regular",
                        },
                        {
                            "token_name": "demo/family/utility",
                            "source_family_name": "Avenir Next",
                            "source_style_reference": "Avenir Next Demi Bold",
                        },
                    ]
                }
            },
        },
    )

    sync_brand_font_inventory(tmp_path)

    inventory = yaml.safe_load((tmp_path / "figma/brands/font-inventory.yml").read_text(encoding="utf-8"))
    directory = (tmp_path / "figma/brands/font-directory.md").read_text(encoding="utf-8")

    assert inventory == {
        "version": 1,
        "updated": "2026-03-13",
        "purpose": "generated_brand_font_inventory",
        "generated_from": {
            "registry": "figma/brands/registry.yml",
            "extraction_rule": (
                "Collect unique family names from each brand typography intake artifact, "
                "preferring `primitive_recommendations.proposed_primitives.families`."
            ),
        },
        "brands": [
            {
                "brand_id": "demo",
                "display_name": "Demo",
                "status": "active",
                "typography_intake_artifact": "figma/brands/demo/typography-intake.yml",
                "fonts": [
                    {
                        "family_name": "Inter",
                        "token_names": ["demo/family/primary"],
                        "source_style_references": ["Inter Bold"],
                    },
                    {
                        "family_name": "Avenir Next",
                        "token_names": ["demo/family/secondary", "demo/family/utility"],
                        "source_style_references": [
                            "Avenir Next Regular",
                            "Avenir Next Demi Bold",
                        ],
                    },
                ],
            }
        ],
    }
    assert directory == (
        "# Font Directory\n\n"
        "Updated: 2026-03-13\n\n"
        "| Font | Brands |\n"
        "| --- | --- |\n"
        "| Avenir Next | Demo |\n"
        "| Inter | Demo |\n"
    )


def test_validate_brand_font_inventory_rejects_stale_generated_file(tmp_path: Path) -> None:
    _make_valid_brand_repo(tmp_path)
    _write_yaml(
        tmp_path / "figma/brands/demo/typography-intake.yml",
        {
            "date": "2026-03-13",
            "primitive_recommendations": {
                "proposed_primitives": {
                    "families": [
                        {
                            "token_name": "demo/family/primary",
                            "source_family_name": "Inter",
                            "source_style_reference": "Inter Regular",
                        }
                    ]
                }
            },
        },
    )
    sync_brand_font_inventory(tmp_path)
    _write_yaml(
        tmp_path / "figma/brands/demo/typography-intake.yml",
        {
            "date": "2026-03-14",
            "primitive_recommendations": {
                "proposed_primitives": {
                    "families": [
                        {
                            "token_name": "demo/family/primary",
                            "source_family_name": "Prompt",
                            "source_style_reference": "Prompt Regular",
                        }
                    ]
                }
            },
        },
    )

    errors = validate_brand_font_inventory(tmp_path)

    assert any("generated brand font inventory is stale" in error for error in errors)
    assert any("generated font directory is stale" in error for error in errors)


def test_validate_repo_includes_export_guardrails(tmp_path: Path) -> None:
    _make_valid_brand_repo(tmp_path)
    _write_export_index(
        tmp_path,
        collections=[
            {
                "key": "semantic-color-base",
                "path": "figma/exports/semantic-color-base.yml",
            }
        ],
    )

    errors = validate_repo(tmp_path)

    assert any("must use a filename starting with `YYYY-MM-DD-`" in error for error in errors)


def test_check_docs_rejects_legacy_guidance(tmp_path: Path) -> None:
    doc = tmp_path / "legacy.md"
    doc.write_text("Use the remote MCP server and _global_color.", encoding="utf-8")
    text = doc.read_text(encoding="utf-8")
    errors = [
        rule_name for rule_name, pattern in DOC_RULES.items() if pattern.search(text)
    ]
    assert errors


def test_list_mcp_port_listeners_uses_fallback_safe_default_range() -> None:
    def fake_runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        command = args[0]
        assert f"-iTCP:{MCP_PORT_START}-{MCP_PORT_END}" in command
        return subprocess.CompletedProcess(
            args=["lsof"],
            returncode=0,
            stdout="\n".join(
                [
                    "p60652",
                    "cnode",
                    "f18",
                    "n[::1]:9228",
                    "p70117",
                    "cbun",
                    "f19",
                    "n127.0.0.1:9230",
                ]
            ),
            stderr="",
        )

    listeners = list_mcp_port_listeners(runner=fake_runner)

    assert [(listener.pid, listener.port, listener.command) for listener in listeners] == [
        (60652, 9228, "node"),
        (70117, 9230, "bun"),
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
                    "n[::1]:9228",
                    "p65997",
                    "cnode",
                    "f18",
                    "n[::1]:9230",
                ]
            ),
            stderr="",
        )

    def fake_killer(pid: int, sig: int) -> None:
        killed.append((pid, sig))

    result = reset_mcp_listeners(
        keep_ports={9230},
        runner=fake_runner,
        killer=fake_killer,
    )

    assert [(listener.pid, listener.port) for listener in result.terminated] == [(60652, 9228)]
    assert [(listener.pid, listener.port) for listener in result.preserved] == [(65997, 9230)]
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
                    "n[::1]:9230",
                ]
            ),
            stderr="",
        )

    result = reset_mcp_listeners(
        dry_run=True,
        runner=fake_runner,
        killer=lambda pid, sig: killed.append((pid, sig)),
    )

    assert [(listener.pid, listener.port) for listener in result.terminated] == [(70117, 9230)]
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
                    "n[::1]:9228",
                ]
            ),
            stderr="",
        )

    with pytest.raises(GovernanceError, match="non-MCP listeners were found"):
        reset_mcp_listeners(runner=fake_runner)


def test_validate_repo_passes() -> None:
    assert validate_repo(ROOT) == []
