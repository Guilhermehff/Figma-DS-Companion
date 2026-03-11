# Workspace Guide

This repository is organized to keep design-system governance durable as more brands are added.

## Recommended Workflow

1. Start from the active governance references before making assumptions:
   - `figma/config/variable-taxonomy.yml` for naming, ladder, and review rules
   - `figma/brands/registry.yml` for governed brand membership
   - `figma/brands/<brand>/brand.yml` for the canonical brand record
   - `figma/variables/index.yml` for split inventory sources
   - `figma/variables/registry.yml` for the generated compatibility export
2. Pull Figma context with Figma Console MCP when the task depends on live file state.
3. Normalize findings into the brand manifest, brand artifacts, or split variable inventories instead of creating parallel notes.
4. Record cross-cutting governance changes in `figma/decisions/`.
5. Regenerate `figma/variables/registry.yml` after inventory changes.
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
- `figma/variables/collections/`: base collection snapshots
- `figma/variables/extensions/`: tracked semantic overrides only
- `figma/variables/index.yml`: source manifest for generated inventories
- `figma/variables/registry.yml`: generated compatibility export
- `figma/history/variables/`: migrated dated variable artifacts that are kept for reference only
- `figma/decisions/`: accepted governance decisions
- `figma/docs/`: stable process guidance

## Governance Commands

- `python -m scripts.figma_governance validate`
- `python -m scripts.figma_governance build-registry`
- `python -m scripts.figma_governance check-docs`

## Good Task Examples

- Add a new brand by creating `figma/brands/<brand>/brand.yml` plus its reviewed color and typography artifacts
- Refresh a semantic extension snapshot in `figma/variables/extensions/` and regenerate the compatibility registry
- Audit active docs for legacy collection naming or stale MCP guidance
- Document a new governance decision that changes slot admission or deprecation behavior
