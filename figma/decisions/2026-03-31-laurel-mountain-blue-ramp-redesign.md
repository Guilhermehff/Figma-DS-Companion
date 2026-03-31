# Decision Log

- Date: 2026-03-31
- Title: Laurel Mountain blue ramp redesign
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): laurel_mountain
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes: figma/decisions/2026-03-31-laurel-mountain-blue-consolidation.md
- Superseded by:

## Context

The initial Laurel Mountain blue consolidation removed the duplicate `dark_blue` and `light_blue` raw families, but its reuse-only ladder introduced visible seams where hue and value changed too abruptly. The requested follow-up standard was to keep both original source colors exact on the unified ladder while redesigning the surrounding steps so the family reads as one intentional blue progression.

## Decision

Keep the single `laurel_mountain/blue/*` family and redesign its ladder around the preserved source swatches.

- Preserve `Light Blue` exactly at `laurel_mountain/blue/500`.
- Preserve `Dark Blue` exactly at `laurel_mountain/blue/900`.
- Redesign the remaining steps around those anchors so the unified ladder stays on a more consistent blue hue axis.
- Keep both semantic neutral and semantic `brand_secondary` overrides on the same `blue` family.
- Retain the earlier raw-family reduction so `dark_blue/*` and `light_blue/*` are not reintroduced.

## Scope

- Affected collections:
  `_Global: Color`, `Semantic: Theme` extension `Laurel Mountain`
- Affected tokens or artifact paths:
  `laurel_mountain/blue/*`
  `figma/brands/laurel_mountain/color/intake.yml`
  `figma/brands/laurel_mountain/color/preview.md`
  `figma/brands/laurel_mountain/brand.yml`
- Explicit exceptions:
  The redesigned ladder intentionally replaces the initial reuse-only composite values between the preserved source anchors.
- Inherited or deferred items:
  `laurel_mountain/red/*` remains unchanged.
  The one-family blue consolidation itself remains in force from the superseded decision.

## Consequences

Laurel Mountain still carries one blue family instead of split raw blue ramps, but the governed source anchor positions are now `500` and `900` rather than the earlier reuse-only `600` and `800`. The live semantic extension continues to map both neutral and `brand_secondary` to the same family, and the documentation frame and repo artifacts now reflect the redesigned ladder and updated source callouts.

## Follow-up

- Update:
  Keep future Laurel Mountain blue changes on `laurel_mountain/blue/*` and preserve the `500` and `900` source anchors unless a newer decision explicitly changes them.
- Link from:
  `figma/brands/laurel_mountain/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `Dark Blue -> laurel_mountain/blue/900`, `Light Blue -> laurel_mountain/blue/500`, and the redesigned blue swatches with neutral card bodies intact.
