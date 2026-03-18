# Decision Log

- Date: 2026-03-18
- Title: Alpine Valley approved live mapping in Foundations
- Status: accepted
- Scope: Brand-specific Figma foundations write
- Brand (if brand-specific): Alpine Valley
- Figma file (if applicable): Foundations
- Stakeholders: user, design_system_governance
- Supersedes:
- Superseded by:

## Context

Alpine Valley source guidance provided one exact neutral, `Valley Black`, one expressive supporting color, `Alpine`, and explicit Prompt typography for H1, H2, and body copy. The first semantic pass required two non-obvious decisions before a live write: whether to duplicate exact black as a raw brand family or reuse the shared universal primitive, and how to map the single expressive `alpine` family into a schema that includes both `brand/*` and `brand_secondary/*`. The source also did not define CTA typography, so the action lane required explicit approval before overriding the live semantic base.

## Decision

Reuse `universal/black` for `Valley Black` instead of creating a duplicate Alpine Valley black family. Create one raw expressive color family, `alpine_valley/alpine/*`, anchored at the provided `#B0C6CE` source swatch, and use that same family for both `brand/*` and `brand_secondary/*` in the Alpine Valley semantic color extension. Create one raw typography family primitive, `alpine_valley/family/primary = Prompt`, and map `family/heading`, `family/body`, and `family/action` to that family. Keep heading weight on the inherited bold base, set `weight/body/base` to `universal/weight/normal`, and set both `weight/body/strong` and `weight/action/base` to `universal/weight/bold`. The CTA Prompt/Bold mapping is an approved follow-up interpretation from chat rather than a source-explicit rule.

## Scope

- Affected collections:
  `_Global: Color`, `_Global: Typography`, `Semantic: Color` extension `Alpine Valley`, and `Semantic: Typography` extension `Alpine Valley`
- Affected tokens or artifact paths:
  `alpine_valley/alpine/*`, `alpine_valley/family/primary`, `surface/brand/*`, `surface/brand_secondary/*`, `foreground/brand`, `foreground/brand_secondary`, `border/brand`, `border/brand_secondary`, `assets/logo`, `family/heading`, `family/body`, `family/action`, `weight/body/base`, `weight/body/strong`, `weight/action/base`, `figma/brands/alpine_valley/brand.yml`, `figma/brands/alpine_valley/color/intake.yml`, `figma/brands/alpine_valley/color/preview.md`, `figma/brands/alpine_valley/typography/intake.yml`, `figma/brands/alpine_valley/typography/preview.md`
- Explicit exceptions:
  CTA is mapped to Prompt Bold even though the supplied Alpine Valley typography page does not explicitly define CTA behavior.
- Inherited or deferred items:
  Neutral roles remain inherited from the shared base, safe family aliases remain on the universal safe family, and semantic size tokens remain inherited because the source does not define governed size values.

## Consequences

Alpine Valley now uses the shared neutral system for exact black while gaining one governed expressive raw family and one raw typography family primitive. Both expressive semantic color lanes resolve through the same `alpine` family, which preserves schema stability without inventing a second unsupported hue. Prompt now consistently spans heading, body, and CTA roles in the first live Alpine Valley typography pass, while sizes and safe-family fallbacks remain centrally governed.

## Follow-up

- Update:
  Persist the extension IDs and approved mappings in `figma/brands/alpine_valley/brand.yml` and mark the intake and preview artifacts as written in Figma.
- Link from:
  `figma/brands/alpine_valley/brand.yml`
- Verify:
  Confirm Alpine Valley semantic color and typography aliases in the Figma runtime and ensure no duplicate Alpine Valley semantic extension collections exist.
