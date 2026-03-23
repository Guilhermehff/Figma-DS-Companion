# Decision Log

- Date: 2026-03-23
- Title: On Surface Contrast Uses Universal Neutrals
- Status: active
- Scope: systemwide
- Brand (if brand-specific): n/a
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders:
  - design_system_governance
- Supersedes:
- Superseded by:

## Context

After the full semantic inverse matrix was written into `Foundations`, a runtime contrast audit across the base semantic color collection and all brand extensions found failing `on_surface` pairs. The failures were concentrated in status roles and in several expressive inverse steps where lane-tinted content aliases did not meet WCAG contrast requirements against the actual paired semantic surfaces.

The corrective requirement is that `on_surface` tokens must be driven by readability on their paired surface instead of inheriting hue from the surface lane.

## Decision

All semantic `on_surface/*` tokens are now contrast-derived from the universal neutral primitives `universal/black` or `universal/white`.

- `on_surface` tokens are not lane-tinted.
- The chosen alias for each `on_surface` token must be whichever of `universal/black` or `universal/white` delivers the stronger readable contrast on the paired semantic surface in the base collection or extension collection where it is used.
- This rule applies to both normal and `_inverse` semantic polarity.
- Expressive inverse `on_surface/brand/*_inverse` and `on_surface/brand_secondary/*_inverse` therefore resolve from universal neutral contrast tokens rather than from brand hue ramps.

## Scope

- Affected collections:
  - `Semantic: Color`
  - All brand semantic color extensions in the `Foundations` file
- Affected tokens or artifact paths:
  - All `on_surface/*` semantic color tokens
  - `figma/config/variable-taxonomy.yml`
  - `figma/templates/brand-manifest.yml`
  - `figma/templates/brand-color-intake.yml`
  - `figma/templates/brand-color-preview.md`
  - `figma/brands/*/brand.yml`
- Explicit exceptions:
  - None. The contrast rule is universal across expressive and status lanes.
- Inherited or deferred items:
  - Surface, foreground, and border lane mappings remain governed by the active inverse matrix decision.
  - Channel-level remapping remains deferred.

## Consequences

Brand manifests and intake or preview templates must not imply that `on_surface` inherits the same source family as the paired surface. `on_surface` is a contrast contract, not a hue contract.

Future semantic writes must verify `on_surface` tokens against the actual surface they are intended to sit on before repo sync is considered complete.

## Follow-up

- Update:
  - Align taxonomy, templates, and brand-manifest notes to the universal-neutral `on_surface` rule.
- Link from:
  - No brand-specific manifest link required; this is a systemwide governance decision.
- Verify:
  - Confirm the live `Foundations` semantic color base and all brand extensions have no failing `on_surface` contrast pairs below `4.5:1`.
