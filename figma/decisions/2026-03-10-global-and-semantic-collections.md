# Decision Log

- Date: 2026-03-10
- Title: Separate Global And Semantic Collections
- Status: Superseded in part
- Superseded in part by: `2026-03-11-user-facing-collection-naming.md`, `2026-03-16-global-first-spacing-and-published-dimensions.md`, and `2026-03-26-semantic-theme-and-published-global-typography.md`
- Historical naming note: References to `_global_*` and `semantic_*` describe the pre-rename Figma state. Current display names are `_Global: *`, `Global: Dimensions`, and `Semantic: *`.
- Stakeholders: Design System Governance

## Context

While preparing the initial global token setup for the Design System file, the collection rules needed clarification. The target file is `https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1`.

## Decision

Each global token category and each semantic token category must live in its own dedicated Figma variable collection.

Global collections must always start with `_` so they remain unpublished. Current baseline collection names are:

- `_global_color`
- `_global_typography`
- `_global_dimensions`
- `semantic_color`
- `semantic_typography`

## Consequences

Global and semantic governance now depends on collection-level separation, not just naming groups inside a broader shared level.

Any future inventories, audits, or write operations must validate that:

- global collections use the `_global_*` naming pattern
- semantic collections use separate category collections
- new global collections are not published
