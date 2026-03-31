# Decision Log

- Date: 2026-03-31
- Title: Seven Springs Wildin' Yellow Global Promotion
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Seven Springs
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=348-30629
- Stakeholders: Design System Governance, user approval in chat
- Supersedes: figma/decisions/2026-03-19-seven-springs-foundations-written-to-figma.md (terrain-park yellow exclusion only)
- Superseded by:

## Context

The original Seven Springs foundations pass intentionally excluded the Terrain Park colors from the resort-brand write path because the source explicitly says they are not the Seven Springs resort brand colors.

The user later requested a yellow ramp on `_Global: Color` for Seven Springs and explicitly chose the family name `Wildin' Yellow`. That request changes the earlier exclusion rule for one source color but does not require a semantic lane remap.

## Decision

1. Add one new Seven Springs raw color family in `_Global: Color`:
   - `seven_springs/wildin_yellow/*`
2. Preserve the original source value `Wildin' Yellow` `#FBCE0A` at `seven_springs/wildin_yellow/400`.
3. Keep `seven_springs/wildin_yellow/*` global-only in this pass.
4. Leave the Seven Springs `Semantic: Theme` extension unchanged:
   - `brand/*` remains `seven_springs/springs_green/*`
   - `brand_secondary/*` remains `seven_springs/tupelo/*`
   - `neutral/*` remains `seven_springs/springs_neutral/*`
5. Keep `Black Rails` excluded from the resort-brand write path until Terrain Park governance is explicitly requested.

## Scope

- Affected collections:
  - `_Global: Color`
- Affected tokens or artifact paths:
  - `seven_springs/wildin_yellow/*`
  - `figma/brands/seven_springs/brand.yml`
  - `figma/brands/seven_springs/color/intake.yml`
  - `figma/brands/seven_springs/color/preview.md`
- Explicit exceptions:
  - `Wildin' Yellow` is approved as a raw global family even though the source classifies it under the Terrain Park palette.
  - The semantic override contract remains unchanged.

## Consequences

Seven Springs now carries four raw color families in `_Global: Color`, but only three of them participate in the resort-brand semantic mapping. The documentation and local governance artifacts must therefore distinguish between semantic families and the global-only `wildin_yellow` family.

This decision narrows, rather than fully replaces, the original Terrain Park exclusion rule. `Black Rails` and any future Terrain Park-specific colors remain deferred.

## Follow-up

- Update:
  - The Seven Springs Global Tokens frame should show `Wildin' Yellow` as its own ramp and the original source alias should resolve to `seven_springs/wildin_yellow/400`.
  - Repo artifacts should describe `wildin_yellow/*` as a global-only family.
- Link from:
  - `figma/brands/seven_springs/brand.yml`
- Verify:
  - `_Global: Color` contains exactly one `seven_springs/wildin_yellow/*` family.
  - No Seven Springs semantic override aliases resolve to `seven_springs/wildin_yellow/*`.
