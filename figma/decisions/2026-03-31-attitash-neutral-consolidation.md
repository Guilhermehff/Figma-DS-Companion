# Decision Log

- Date: 2026-03-31
- Title: Attitash neutral consolidation
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): attitash
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes:
- Superseded by:

## Context

Attitash was live in `Foundations` with six raw color families, including three raw-only grey families: `mogul_shadow`, `mogul_shadow_20`, and `sharp_edge_grey`. The live `attitash_neutral` family already contained those source anchors exactly, so the extra grey ramps were duplicating values rather than preserving distinct governed primitives.

## Decision

Reduce Attitash to three raw color families by keeping `attitash_blue`, `daybreak`, and `attitash_neutral`, and removing the duplicate raw-only grey ramps.

- Keep `attitash/attitash_neutral/*` as the single governed grey family.
- Preserve the accent-sheet source anchors inside `attitash_neutral` at:
  `attitash_neutral/100` for `Mogul Shadow 20%`
  `attitash_neutral/300` for `Mogul Shadow`
  `attitash_neutral/800` for `Sharp Edge Grey`
- Remove `attitash/mogul_shadow/*`, `attitash/mogul_shadow_20/*`, and `attitash/sharp_edge_grey/*`.
- Leave the existing semantic neutral, brand, and brand-secondary mappings unchanged.

## Scope

- Affected collections:
  `_Global: Color`
- Affected tokens or artifact paths:
  `attitash/attitash_neutral/*`
  `figma/brands/attitash/color/intake.yml`
  `figma/brands/attitash/color/preview.md`
  `figma/brands/attitash/brand.yml`
- Explicit exceptions:
  None.
- Inherited or deferred items:
  `attitash_blue` and `daybreak` remain unchanged.
  `Semantic: Theme` extension `Attitash` keeps the same mappings because the removed families were never referenced there.

## Consequences

Attitash now carries three raw color families instead of six. The original source swatches remain documented, but their grey token references now point into `attitash_neutral` rather than standalone duplicate ramps. This is a brand-specific reduction and does not change the shared taxonomy.

## Follow-up

- Update:
  Keep future Attitash grey adjustments on `attitash/attitash_neutral/*` and do not reintroduce split grey ramps without a new approved decision.
- Link from:
  `figma/brands/attitash/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `3 ramps`, `33` tokens, no `mogul_shadow`, `mogul_shadow_20`, or `sharp_edge_grey` tokenized sections, and source aliases for `Mogul Shadow` and `Sharp Edge Grey` that point into `attitash_neutral`.
