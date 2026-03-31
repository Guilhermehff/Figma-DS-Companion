# Decision Log

- Date: 2026-03-18
- Title: Park City Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Park City
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by: figma/decisions/2026-03-31-park-city-neutral-lane-correction.md (color neutral interpretation only)

## Context

Park City introduces a red-led palette with two expressive reds and a three-swatch low-chroma system made from `Pale Red`, `Cool Gray`, and `Park City Gray`.

The typography guidance uses `Futura Std` for headline, body, and CTA work, but a separate `Trade Gothic LT Std Bold Condensed No. 20` face for subheads. The current semantic typography schema exposes only `heading`, `body`, and `action` family lanes, so the distinct condensed subhead treatment cannot be represented as a fourth live semantic family without changing the shared schema.

## Decision

1. Add three Park City raw color families in `_Global: Color`:
   - `park_city/park_city_red/*`
   - `park_city/bright_red/*`
   - `park_city/park_city_gray/*`
2. Reuse `universal/white` for the supplied Park City white swatch instead of duplicating it under the brand group.
3. Treat `park_city/park_city_gray/*` as the absorbed Park City neutral ladder that preserves the supplied pale pink wash, cool gray mid-tone, and dark brand gray in one governed family.
4. Create a Park City semantic color extension that maps:
   - `neutral/*` and readable neutral foreground and border roles to `park_city/park_city_gray/*`
   - `brand/*` to `park_city/park_city_red/*`
   - `brand_secondary/*` to `park_city/bright_red/*`
   - `assets/logo` to the string `Park City`
5. Add two Park City raw typography family primitives in `_Global: Typography`:
   - `park_city/family/primary` -> `Futura Std`
   - `park_city/family/utility` -> `Trade Gothic LT Std Bold Condensed No. 20`
6. Create a Park City semantic typography extension that maps `family/heading`, `family/body`, and `family/action` to `park_city/family/primary`, with weight overrides of Bold, Light, and Bold respectively.
7. Keep `park_city/family/utility` as a raw-only primitive in this pass because the current semantic typography schema has no dedicated subhead family lane.

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `park_city/park_city_red/*`
  - `park_city/bright_red/*`
  - `park_city/park_city_gray/*`
  - `park_city/family/primary`
  - `park_city/family/utility`
  - `figma/brands/park_city/brand.yml`
  - `figma/brands/park_city/color/intake.yml`
  - `figma/brands/park_city/color/preview.md`
  - `figma/brands/park_city/typography/intake.yml`
  - `figma/brands/park_city/typography/preview.md`
- Explicit exceptions:
  - Park City's neutral lane is intentionally absorbed into one family, `park_city/park_city_gray`, rather than splitting `Pale Red`, `Cool Gray`, and `Park City Gray` into separate semantic lanes.
  - Park City's distinct condensed subhead face is preserved as a raw utility primitive instead of being forced into the live semantic typography extension.
- Inherited or deferred items:
  - `surface/positive/*`, `surface/warning/*`, and `surface/critical/*` remain inherited from the shared semantic base.
  - Park City safe family aliases remain inherited from the shared semantic typography base.
  - Park City size semantics remain inherited from the shared typography baseline.

## Consequences

Park City can now consume the current role-based semantic color and typography contracts in the active Foundations file without introducing a new shared semantic family lane or a parallel neutral schema.

The non-obvious decisions are now durable in repo governance rather than living only inside the Figma extension objects: the low-chroma palette is absorbed into one neutral family, and the condensed subhead face remains raw-only until the semantic typography schema grows a stable subhead lane.

## Follow-up

- Update:
  - Park City global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/park_city/brand.yml`.
- Link from:
  - `figma/brands/park_city/brand.yml`
- Verify:
  - `Park City` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `park_city/park_city_gray/200`, `park_city/park_city_red/700`, `park_city/bright_red/600`, and `park_city/family/primary` as intended.
