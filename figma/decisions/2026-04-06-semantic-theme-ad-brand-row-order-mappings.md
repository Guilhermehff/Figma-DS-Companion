# Decision Log

- Date: 2026-04-06
- Title: Semantic theme Ads brand row-order mappings
- Status: accepted
- Scope: Typography token model, Ads brand switching, Foundations write behavior
- Brand (if brand-specific): multiple active brands
- Figma file (if applicable): Foundations
- Stakeholders: Design system governance, Ads library authors
- Supersedes:
  - `2026-04-06-semantic-theme-ad-typography-size-recipes.md` for the deferred brand-extension mapping
- Superseded by:

## Context

The Ads semantic size recipe decision approved a narrow `typography/size/ad/*` exception and deferred brand extension overrides until the brand-to-scale mapping was approved.

The live Foundations board already shows the intended row order for those Ads brand cards. The approved mapping is not the same as the base row, so the brand-specific extension collections need explicit row-to-scale assignments instead of inheriting the base raw column everywhere.

## Decision

1. Keep the base row inherited with no brand extension override.
2. Apply the `0.75x` Ads heading size column to:
   - Afton Alps
   - Roundtop Mountain
   - Vail
3. Apply the `0.875x` Ads heading size column to:
   - Hidden Valley MO
   - Mt. Brighton
   - Paoli Peaks
   - Park City
   - Wilmot
4. Apply the `1.125x` Ads heading size column to:
   - Attitash
   - Beaver Creek
   - Crested Butte
   - Hunter
   - Liberty Mountain
   - Mount Sunapee
   - Northstar
   - Snow Creek
5. Apply the `1.375x` Ads heading size column to:
   - Heavenly

## Scope

- Affected collections:
  - `Semantic: Theme`
  - Brand extension collections for the 17 listed brands
- Affected tokens or artifact paths:
  - `typography/size/ad/heading/xs`
  - `typography/size/ad/heading/s`
  - `typography/size/ad/heading/md`
  - `typography/size/ad/heading/lg`
  - `typography/size/ad/heading/xl`
- Explicit exceptions:
  - The middle row remains inherited and receives no override.
  - Only the listed brands receive brand-specific Ads size overrides.
- Inherited or deferred items:
  - Email remains on the existing raw shared size ladder.
  - No general semantic typography size system is introduced beyond the approved Ads exception.

## Consequences

The Ads row-order mapping is now explicit and traceable. Brand extension writes can use the live screenshot order without inventing a separate naming model for the size ladder.

This closes the deferred brand-mapping gap from the earlier Ads size recipe decision and keeps the semantic size exception narrow.

## Follow-up

- Update:
  - `figma/brands/*/brand.yml` for the 17 affected brand manifests with the approved row-scale note.
- Link from:
  - Future Ads brand governance artifacts that need the same row-order mapping.
- Verify:
  - `Foundations` brand extensions resolve the correct raw column for the 17 listed brands and the remaining brands inherit the base row.
