# Decision Log

- Date: 2026-03-31
- Title: Hidden Valley PA beige consolidation
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): hidden_valley_pa
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes:
- Superseded by: figma/decisions/2026-03-31-hidden-valley-pa-beige-ramp-redesign.md

## Context

Hidden Valley PA was live in `Foundations` with four raw color families: `laurel_blue`, `dark_beige`, `light_beige`, and a composite `hidden_valley_pa_neutral` family. The source brand sheet only justifies one beige lane, and the composite neutral ramp duplicated beige structure while also carrying shared white at the lightest step.

## Decision

Consolidate the Hidden Valley PA beige-related raw colors into a single global family named `hidden_valley_pa/beige/*`.

- Rename the composite neutral ramp to `beige`.
- Replace the former white `50` step with a derived very light beige `#FBF8F2`.
- Preserve the source-provided Light Beige swatch at `beige/100` and the source-provided Dark Beige swatch at `beige/400`.
- Remap both the semantic neutral override set and the semantic `brand_secondary` override set to the same `beige` family.
- Remove the duplicate `dark_beige/*` and `light_beige/*` raw families from `_Global: Color`.

## Scope

- Affected collections:
  `_Global: Color`, `Semantic: Theme` extension `Hidden Valley PA`
- Affected tokens or artifact paths:
  `hidden_valley_pa/beige/*`
  `figma/brands/hidden_valley_pa/color/intake.yml`
  `figma/brands/hidden_valley_pa/color/preview.md`
  `figma/brands/hidden_valley_pa/brand.yml`
- Explicit exceptions:
  `beige/50` is a derived light beige rather than a direct source swatch so the brand ramp does not duplicate shared white.
- Inherited or deferred items:
  `universal/white` and `universal/black` remain the governed shared neutral reuse path.
  `laurel_blue` remains unchanged as the primary expressive lane.

## Consequences

Hidden Valley PA now carries two raw global color families instead of four. The semantic extension still supports distinct neutral and brand-secondary role groups, but both groups alias the same underlying beige family with different step mappings. No taxonomy change was required because this is a brand-specific consolidation, not a system-wide rule change.

## Follow-up

- Update:
  Keep future Hidden Valley PA color changes on `hidden_valley_pa/beige/*` and do not reintroduce split beige ramps without a new approved decision.
- Link from:
  `figma/brands/hidden_valley_pa/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `2 ramps`, `22` tokens, a `Beige` section, and no stale `dark_beige`, `light_beige`, or `hidden_valley_pa_neutral` references.
