# Decision Log

- Date: 2026-03-17
- Title: JFBB Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): JFBB
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance
- Supersedes:
- Superseded by:

## Context

The supplied JFBB source introduces six distinct brand swatches, but the current semantic color model still admits only one neutral lane and two expressive brand lanes.

The typography guidance uses one family across every role, but the body example is internally inconsistent because it lists `100px difference` and `24px / 124px leading`, which cannot be treated as a governed size recipe.

## Decision

1. Add JFBB raw color families in `_Global: Color`:
   - `jfbb/early_sunrise/*`
   - `jfbb/last_chair/*`
   - `jfbb/snow_day/*`
   - `jfbb/frost/*`
   - `jfbb/bluebird/*`
   - `jfbb/night_ski/*`
2. Map semantic color as follows:
   - neutral surfaces and neutral borders -> `jfbb/snow_day/*`
   - readable neutral copy roles -> `jfbb/last_chair/*`
   - `brand/*` -> `jfbb/early_sunrise/*`
   - `brand_secondary/*` -> `jfbb/bluebird/*`
3. Keep `jfbb/frost/*` and `jfbb/night_ski/*` as governed global-only extra families in this first pass.
4. Override `assets/logo` in the JFBB semantic color extension to the string `JFBB`.
5. Add one JFBB raw typography family in `_Global: Typography`:
   - `jfbb/family/primary` -> `Vista Sans NAR OTCE`
6. Map the source weights as follows:
   - `Black` -> `universal/weight/black`
   - `Bold` -> `universal/weight/bold`
   - `Book` -> `universal/weight/normal`
7. Keep action-family and size semantics inherited in the live typography extension because the source does not define CTA behavior and the body-leading example is defective.

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `jfbb/*`
  - `assets/logo`
  - `figma/brands/jfbb/brand.yml`
  - `figma/brands/jfbb/color/intake.yml`
  - `figma/brands/jfbb/color/preview.md`
  - `figma/brands/jfbb/typography/intake.yml`
  - `figma/brands/jfbb/typography/preview.md`
- Explicit exceptions:
  - Readable neutral copy roles reuse `jfbb/last_chair/*` while the neutral surface stack stays on `jfbb/snow_day/*`.
  - `Book` stages on `universal/weight/normal` because there is no separate approved raw book primitive.
- Inherited or deferred items:
  - `jfbb/frost/*` and `jfbb/night_ski/*` remain global-only.
  - `family/action`, `weight/action/*`, and `size/*` remain inherited in the JFBB typography extension.

## Consequences

JFBB can now plug into the current shared semantic model without adding a third expressive lane or a new typography weight primitive.

The live extension preserves the user-approved `assets/logo = JFBB` rule and documents the source body-leading defect instead of silently converting it into a token.

## Follow-up

- Update:
  - JFBB global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/jfbb/brand.yml`.
- Link from:
  - `figma/brands/jfbb/brand.yml`
- Verify:
  - `JFBB` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - `assets/logo` resolves to `JFBB` in the color extension.
