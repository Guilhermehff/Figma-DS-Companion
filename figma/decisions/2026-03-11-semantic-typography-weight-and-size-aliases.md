# Semantic Typography Weight And Size Aliases

Date: 2026-03-11
Status: superseded
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
Superseded by: `2026-03-11-role-scoped-semantic-typography-ladders.md`
Historical naming note: References to `semantic_typography` and `_global_typography` describe the pre-rename display names. Current display names are `Semantic: Typography` and `_Global: Typography`.

## Context

`semantic_typography` currently exposes only family aliases. Brand typography reviews already reuse the universal weight primitives and the universal size ladder, but downstream work still has to reach back into `_global_typography` for those values. That mixes semantic and raw references inside the same typography workflow.

## Decision

1. Expand `semantic_typography` to include weight and size aliases in addition to family aliases.
2. Standardize the semantic weight aliases on the approved universal weight keys:
   - `weight/normal`
   - `weight/medium`
   - `weight/black`
3. Standardize the semantic size aliases on the approved universal size ladder:
   - `size/100`
   - `size/200`
   - `size/300`
   - `size/400`
   - `size/500`
   - `size/600`
   - `size/700`
   - `size/800`
4. Keep safe-alias behavior family-only. Do not create `weight/*_safe` or `size/*_safe` variants.
5. Keep these aliases in the shared base collection unless a brand-specific semantic weight or size override is explicitly approved.

## Consequences

- Channel libraries can consume family, weight, and size from `semantic_typography` without mixing semantic and raw typography references.
- Brand typography intake and preview artifacts should record semantic weight and size mappings alongside semantic family mapping.
- The registry snapshot from 2026-03-11 still shows only the six family aliases, so the Design System file needs a follow-up Figma write to bring the collection into alignment with this decision.
