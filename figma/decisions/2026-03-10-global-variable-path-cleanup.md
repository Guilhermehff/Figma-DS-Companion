# Decision Log

- Date: 2026-03-10
- Title: Global Variable Path Cleanup
- Status: Accepted
- Superseded in part by: `2026-03-11-user-facing-collection-naming.md`
- Historical naming note: References to `_global_*` describe the pre-rename collection display names. The path rule remains active, but current display names use `_Global: *`.
- Stakeholders: Design System Governance

## Context

After the initial global baseline was created in the Design System file, the variable paths still repeated the category already implied by the collection name, and the typography family primitives did not match the intended raw-value model.

## Decision

Inside `_global_*` collections, variable names start at the child path instead of repeating the collection category.

Examples:

- `_global_color`: `universal/slate/50`
- `_global_typography`: `universal/family/sans`
- `_global_dimensions`: `space/4`

For global typography families, keep the current keys as `sans` and `web_safe`, with both values set to `Inter` because Figma does not support multi-value family fallbacks in a single variable. Semantic typography can later alias these into channel-ready usage.

For global dimensions, remove `space/0` and `space/px`. The baseline space ladder starts at `space/0_5`.

## Consequences

The repository taxonomy and registries must mirror the shorter collection-local paths.

Any future semantic or channel work should alias from these normalized global paths rather than reintroducing category prefixes inside the collections.
