# Decision Log

- Date: 2026-03-19
- Title: Seven Springs Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Seven Springs
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by: figma/decisions/2026-03-31-seven-springs-wildin-yellow-global-promotion.md (terrain-park yellow exception only)

## Context

Seven Springs introduces a green-led resort palette with one primary green, one lighter supporting green, one dark secondary green, and a branded light-to-dark neutral pair. The supplied source also includes a separate Terrain Park palette that explicitly should not be treated as the Seven Springs resort brand colors.

The source for `Mini Golf Green` contains a contradiction: the explicit HEX field is `#89EBAD`, while the displayed RGB line does not match that HEX value. The user asked to proceed with the write after approving `Tupelo` as the separate secondary expressive lane.

The typography guidance uses one family, `Hoss Sharp`, across all roles, but the current semantic typography schema has no dedicated subhead role. The live write therefore needed one explicit staging choice for the Bold subhead treatment.

## Decision

1. Add three Seven Springs raw color families in `_Global: Color`:
   - `seven_springs/springs_green/*`
   - `seven_springs/tupelo/*`
   - `seven_springs/springs_neutral/*`
2. Keep the Terrain Park colors out of the Seven Springs resort-brand write path.
3. Create a Seven Springs semantic color extension that:
   - maps `neutral/*` to `seven_springs/springs_neutral/*`
   - maps `brand/*` to `seven_springs/springs_green/*`
   - maps `brand_secondary/*` to `seven_springs/tupelo/*`
   - overrides `assets/logo` to the string `Seven Springs`
4. Apply the user-approved source-resolution exception for the live write:
   - `Mini Golf Green` uses the explicit HEX field `#89EBAD` despite the conflicting RGB line in the source image
5. Add one Seven Springs raw typography family primitive in `_Global: Typography`:
   - `seven_springs/family/primary` -> `Hoss Sharp`
6. Create a Seven Springs semantic typography extension that maps `family/heading`, `family/body`, and `family/action` to `seven_springs/family/primary`.
7. Apply the live Seven Springs typography mapping:
   - `weight/heading/base` -> `universal/weight/black`
   - `weight/heading/strong` -> `universal/weight/bold`
   - `weight/body/base` -> `universal/weight/medium`
   - `weight/action/base` -> `universal/weight/black`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `seven_springs/springs_green/*`
  - `seven_springs/tupelo/*`
  - `seven_springs/springs_neutral/*`
  - `seven_springs/family/primary`
  - `figma/brands/seven_springs/brand.yml`
  - `figma/brands/seven_springs/color/intake.yml`
  - `figma/brands/seven_springs/color/preview.md`
  - `figma/brands/seven_springs/typography/intake.yml`
  - `figma/brands/seven_springs/typography/preview.md`
- Explicit exceptions:
  - The live write uses the explicit `Mini Golf Green` HEX field `#89EBAD` despite the conflicting RGB line in the source image.
  - The Seven Springs Terrain Park palette remains excluded from the resort-brand foundations.
  - The Bold Seven Springs subhead recipe stages through `weight/heading/strong` because the current semantic typography schema has no dedicated subhead role.
  - `Heavy` stages on `universal/weight/black` because the shared raw typography ladder has no dedicated heavy primitive.
- Inherited or deferred items:
  - Safe family aliases and all size semantics remain inherited from the shared semantic typography base.
  - `weight/body/strong` remains inherited from the shared semantic typography base.
  - Terrain Park governance remains deferred until explicitly requested.

## Consequences

Seven Springs can now consume the active role-based semantic color and typography contracts in the Foundations file while keeping the resort palette separate from the Terrain Park sub-brand.

The Mini Golf Green source discrepancy is now durable in governance history rather than hidden only in local intake notes or chat context. Future downstream work can use the manifest and decision log to understand why the live write trusts the explicit HEX field.

## Follow-up

- Update:
  - Seven Springs global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/seven_springs/brand.yml`.
- Link from:
  - `figma/brands/seven_springs/brand.yml`
- Verify:
  - `Seven Springs` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `seven_springs/springs_green/700`, `seven_springs/tupelo/800`, `seven_springs/springs_neutral/800`, `seven_springs/family/primary`, `universal/weight/bold`, and `universal/weight/black` as intended.
