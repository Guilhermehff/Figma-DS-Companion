# Decision Log

- Date: 2026-03-31
- Title: Laurel Mountain blue consolidation
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): laurel_mountain
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes:
- Superseded by: figma/decisions/2026-03-31-laurel-mountain-blue-ramp-redesign.md

## Context

Laurel Mountain was live in `Foundations` with three raw color families: `red`, `dark_blue`, and `light_blue`. The two blue families were close enough in hue that they read as one brand lane, but they still occupied duplicate raw families in `_Global: Color` and in the Global Tokens documentation frame.

## Decision

Consolidate Laurel Mountain's split blue ramps into a single global family named `laurel_mountain/blue/*`.

- Reuse only existing live values from the former `dark_blue/*` and `light_blue/*` ramps.
- Preserve the source Light Blue swatch exactly at `laurel_mountain/blue/600`.
- Preserve the source Dark Blue swatch exactly at `laurel_mountain/blue/800`.
- Remap both the semantic neutral override set and the semantic `brand_secondary` override set to the same `blue` family.
- Remove the duplicate `dark_blue/*` and `light_blue/*` raw families from `_Global: Color`.

## Scope

- Affected collections:
  `_Global: Color`, `Semantic: Theme` extension `Laurel Mountain`
- Affected tokens or artifact paths:
  `laurel_mountain/blue/*`
  `figma/brands/laurel_mountain/color/intake.yml`
  `figma/brands/laurel_mountain/color/preview.md`
  `figma/brands/laurel_mountain/brand.yml`
- Explicit exceptions:
  The consolidated `blue` ladder is a reuse-only composite of the prior `dark_blue` and `light_blue` values rather than a freshly generated ramp.
- Inherited or deferred items:
  `laurel_mountain/red/*` remains unchanged as the primary expressive lane.
  `universal/white` and `universal/black` remain the governed shared neutral reuse path.

## Consequences

Laurel Mountain now carries two raw global color families instead of three. The semantic theme extension no longer distinguishes structural and supporting blue families at the raw level; both neutral and `brand_secondary` roles now alias the same `blue` ladder with different step mappings. No taxonomy change was required because this is a brand-specific reduction, not a system-wide naming change.

## Follow-up

- Update:
  Keep future Laurel Mountain blue changes on `laurel_mountain/blue/*` and do not reintroduce split blue ramps without a new approved decision.
- Link from:
  `figma/brands/laurel_mountain/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `2 ramps`, `22` tokens, a `Blue` section, and no stale `dark_blue` or `light_blue` tokenized ramp sections.
