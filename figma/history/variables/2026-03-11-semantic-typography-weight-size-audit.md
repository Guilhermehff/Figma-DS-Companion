# Variable Audit

Status: historical reference

- Date: 2026-03-11
- Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Scope: semantic_typography completeness for typography weight and size aliases
- Collections reviewed: `_global_typography`, `semantic_typography`, `vail`
- Modes reviewed: `values`

## Summary

`_global_typography` contains the approved universal raw weight primitives and the full universal size ladder, and `semantic_typography` now includes the approved role-scoped baseline additions for weight and size. The base semantic typography collection is aligned with the shared baseline captured at the time of this audit, while `vail` remains a family-only extension.

## Findings

- Naming issues: none in the current live baseline; the written aliases follow the approved role-scoped model.
- Alias issues: `semantic_typography` now includes the approved role-scoped baseline aliases for heading, body, and action.
- Missing modes: none.
- Duplicate meanings: none identified in the reviewed collections.
- Deprecated candidates: the earlier flat-alias proposal for semantic typography weight and size is superseded by the approved role-scoped model.

## Recommended Actions

1. Keep the approved role-scoped baseline inventory documented and extend it only when new shared-baseline needs or reviewed brand recipes introduce a distinct reusable role step.
2. Keep future semantic typography additions role-scoped and justified by approved shared baseline needs or reviewed brand recipes.
3. Leave `vail` unchanged unless a brand-specific semantic weight or size divergence is explicitly approved, because the current Vail typography artifacts already reuse the universal weight and size baselines.
