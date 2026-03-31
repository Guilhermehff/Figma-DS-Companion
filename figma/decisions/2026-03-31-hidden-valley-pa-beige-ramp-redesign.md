# Decision Log

- Date: 2026-03-31
- Title: Hidden Valley PA beige ramp redesign
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): hidden_valley_pa
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes: figma/decisions/2026-03-31-hidden-valley-pa-beige-consolidation.md
- Superseded by:

## Context

The initial Hidden Valley PA beige consolidation correctly removed duplicate raw families, but it anchored the preserved source swatches too early in the ladder and left the surrounding steps closer to a stitched carry-over than a fully reviewed ramp. The requested follow-up standard was stricter: the original brand values must remain exact somewhere on the ladder, but the rest of the family may be redesigned to produce a better progression.

## Decision

Keep the single `hidden_valley_pa/beige/*` family and redesign its ladder around the preserved source swatches.

- Preserve `Light Beige` exactly at `hidden_valley_pa/beige/200`.
- Preserve `Dark Beige` exactly at `hidden_valley_pa/beige/500`.
- Redesign the remaining beige steps around those anchors for a smoother single-family progression.
- Keep `hidden_valley_pa/beige/50` as a very light beige instead of shared white so the brand ramp does not duplicate `universal/white`.
- Keep both semantic neutral and semantic `brand_secondary` overrides on the same `beige` family.

## Scope

- Affected collections:
  `_Global: Color`, `Semantic: Theme` extension `Hidden Valley PA`
- Affected tokens or artifact paths:
  `hidden_valley_pa/beige/*`
  `figma/brands/hidden_valley_pa/color/intake.yml`
  `figma/brands/hidden_valley_pa/color/preview.md`
  `figma/brands/hidden_valley_pa/brand.yml`
- Explicit exceptions:
  `beige/50` remains derived rather than source-provided so white stays governed through `universal/white`.
- Inherited or deferred items:
  `hidden_valley_pa/laurel_blue/*` remains unchanged.
  The one-family beige consolidation itself remains in force from the superseded decision.

## Consequences

Hidden Valley PA still carries one beige family instead of split beige ramps, but the governed anchor positions are now `200` and `500` rather than the earlier `100` and `400`. The live semantic extension keeps the same family-level mapping strategy, while the documentation frame and repo artifacts now reflect the redesigned ladder values and updated source callouts.

## Follow-up

- Update:
  Keep future Hidden Valley PA beige changes on `hidden_valley_pa/beige/*` and preserve the `200` and `500` source anchors unless a newer decision explicitly changes them.
- Link from:
  `figma/brands/hidden_valley_pa/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `Dark Beige -> hidden_valley_pa/beige/500`, `Light Beige -> hidden_valley_pa/beige/200`, and the redesigned beige swatches with neutral card bodies intact.
