# User-Facing Collection Naming

Date: 2026-03-11
Status: accepted
Superseded in part by: `2026-03-16-global-first-spacing-and-published-dimensions.md`
Historical naming note: `Global: Dimensions` later became a published exception to the `_Global: *` display-name rule.
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

Collection names are now visible to broader consumers in Figma, so the previous machine-like naming pattern is no longer appropriate for governance or readability.

## Decision

1. Rename global collections from the `_global_*` pattern to the `_Global: *` pattern in title case.
2. Rename semantic collections from the `semantic_*` pattern to the `Semantic: *` pattern in title case.
3. Standardize channel collections on the `Channel: *` pattern in title case.
4. Use proper brand spelling with capitalization for user-facing brand collection names and extensions, for example `Vail`, `Beaver Creek`, `Breckenridge`, and `Park City`.
5. Keep variable paths unchanged unless a separate decision explicitly changes token naming. Collection display names and token paths are governed independently.

## Approved Naming

- `_Global: Color`
- `_Global: Typography`
- `_Global: Dimensions`
- `Semantic: Color`
- `Semantic: Typography`
- `Channel: <Category>`
- `<Brand>` for brand-specific extension collection names

## Consequences

- Current governance documentation must reference the new user-facing collection names.
- Historical decisions, audits, and registry snapshots may still show the prior names when they are describing earlier Figma states.
- Figma write operations that rename collections must update the live file first, then refresh the local registry artifacts from MCP.
