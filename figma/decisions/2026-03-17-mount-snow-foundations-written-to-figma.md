# Decision Log

- Date: 2026-03-17
- Title: Mount Snow Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Mount Snow
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance
- Supersedes:
- Superseded by:

## Context

Mount Snow introduces a larger raw palette than the current semantic color model can promote. The supplied palette includes three primary swatches, three secondary swatches, and an exact black that should not be duplicated under the brand group.

The typography guidance uses `Heavy`, `Extra Bold`, and `Medium`, but it does not provide numeric font-weight values or an action-specific typography rule.

## Decision

1. Add Mount Snow raw color families in `_Global: Color`:
   - `mount_snow/bluebird_express/*`
   - `mount_snow/heart_red/*`
   - `mount_snow/whipped_cream/*`
   - `mount_snow/somerset_blue/*`
   - `mount_snow/rosy_cheeks/*`
2. Reuse `universal/black` for the supplied `Carinthia Rail` swatch instead of duplicating it under the brand group.
3. Map semantic color as follows:
   - `brand/*` -> `mount_snow/bluebird_express/*`
   - `brand_secondary/*` -> `mount_snow/heart_red/*`
   - neutral surfaces and borders -> `mount_snow/whipped_cream/*`
   - exact black neutral foreground roles -> `universal/black`
4. Keep `somerset_blue` and `rosy_cheeks` as governed global-only extra families in this first pass.
5. Override `assets/logo` in the Mount Snow semantic color extension to the string `Mount Snow`.
6. Add Mount Snow raw typography families in `_Global: Typography`:
   - `mount_snow/family/primary` -> `Vastago Grotesk`
   - `mount_snow/family/secondary` -> `Area Extended`
7. Map both `Heavy` and `Extra Bold` to `universal/weight/black` in the Mount Snow semantic typography extension, and map body copy to `universal/weight/medium`.
8. Keep action-family and size semantics inherited in the live typography extension.

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `mount_snow/*`
  - `assets/logo`
  - `figma/brands/mount_snow/brand.yml`
  - `figma/brands/mount_snow/color/intake.yml`
  - `figma/brands/mount_snow/color/preview.md`
  - `figma/brands/mount_snow/typography/intake.yml`
  - `figma/brands/mount_snow/typography/preview.md`
- Explicit exceptions:
  - Neutral readable foreground roles reuse `universal/black` instead of deriving every dark neutral from the brand family.
  - `Heavy` and `Extra Bold` both stage on the existing shared black raw weight in this first pass.
- Inherited or deferred items:
  - `somerset_blue` and `rosy_cheeks` remain global-only.
  - `family/action`, `weight/action/*`, and `size/*` remain inherited in the Mount Snow typography extension.

## Consequences

Mount Snow can now plug into the current two-lane semantic color model without adding another shared expressive slot.

The live extension preserves the brand-name override for `assets/logo` and avoids duplicating the supplied exact black.

## Follow-up

- Update:
  - Mount Snow global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/mount_snow/brand.yml`.
- Link from:
  - `figma/brands/mount_snow/brand.yml`
- Verify:
  - `Mount Snow` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - `assets/logo` resolves to `Mount Snow` in the color extension.
