# Workspace Guide

This repository is organized to keep design-system governance durable as more brands are added.

## Recommended Workflow

1. Start from the active governance references before making assumptions:
   - `figma/config/variable-taxonomy.yml` for naming, ladder, and review rules
   - `figma/brands/registry.yml` for governed brand membership
   - `figma/brands/<brand>/brand.yml` for the canonical brand record
   - `figma/variables/index.yml` only when a local collection or compatibility export is intentionally being generated
2. Pull Figma context with Figma Console MCP when the task depends on live file state.
3. Normalize findings into the brand manifest, brand artifacts, or decision logs instead of creating parallel notes.
4. Record cross-cutting governance changes in `figma/decisions/`.
5. Create or refresh local variable exports only when an audit or compatibility export is explicitly requested.
6. Run the governance validator before treating the repo snapshot as current.
7. For Semantic extension writes, use the native extension workflow in `figma/docs/semantic-extension-write-workflow.md`.

## Tool Selection

- Live variable and collection work: `mcp__figma_console__figma_get_status`, `mcp__figma_console__figma_list_open_files`, then `mcp__figma_console__figma_get_variables`
- Semantic extension writes: `mcp__figma_console__figma_execute` using the native Variables API route documented in `figma/docs/semantic-extension-write-workflow.md`
- Focused token checks: `mcp__figma_console__figma_get_token_values`
- Component documentation: `mcp__figma_console__figma_get_component`
- Selection-based workflows: `mcp__figma_console__figma_get_selection`

## Directory Use

- `figma/brands/`: brand registry, per-brand manifests, and staged brand artifacts
- `figma/variables/collections/`: optional collection snapshots exported from Figma
- `figma/variables/extensions/`: on-demand extension export staging only
- `figma/variables/index.yml`: optional manifest for local exports
- `figma/variables/registry.yml`: on-demand compatibility export when present
- `figma/history/variables/`: migrated dated variable artifacts that are kept for reference only
- `figma/decisions/`: accepted governance decisions
- `figma/docs/`: stable process guidance

## Governance Commands

- `python -m scripts.figma_governance validate`
- `python -m scripts.figma_governance build-registry` for optional compatibility exports only
- `python -m scripts.figma_governance check-docs`

## Good Task Examples

- Add a new brand by creating `figma/brands/<brand>/brand.yml` plus its reviewed color and typography artifacts
- Export current Figma collection or extension state to local YAML only when an audit or compatibility export is requested
- Audit active docs for legacy collection naming or stale MCP guidance
- Document a new governance decision that changes slot admission or deprecation behavior
