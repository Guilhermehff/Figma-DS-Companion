# Decision Log

- Date: 2026-03-19
- Title: Liberty Mountain Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Liberty Mountain
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Liberty Mountain supplies a much larger source palette than the current semantic color model can consume directly. The user explicitly approved `Sunrise` as brand primary, `Spring` as brand secondary, and instructed `Limestone`, `Mineral`, and `Sand` to behave as one neutral ramp while all other source colors remain preserved as governed raw values.

The source typography page defines Brown as the primary font for print and web materials, lists Brown Regular and Brown Light across the headline and reading hierarchy, and also names Sentinel Book as an alternate family. The current semantic typography schema still has no alternate serif family slot and the source provides no CTA-specific recipe.

## Decision

1. Add the following raw color families in `_Global: Color`:
   - `liberty_mountain/twilight/*`
   - `liberty_mountain/summit/*`
   - `liberty_mountain/tundra/*`
   - `liberty_mountain/shale/*`
   - `liberty_mountain/stone/*`
   - `liberty_mountain/sand/*`
   - `liberty_mountain/mineral/*`
   - `liberty_mountain/limestone/*`
   - `liberty_mountain/sunrise/*`
   - `liberty_mountain/sunset/*`
   - `liberty_mountain/flora/*`
   - `liberty_mountain/spring/*`
   - `liberty_mountain/copper/*`
   - `liberty_mountain/liberty_neutral/*`
2. Preserve every source swatch as a raw family and add the composite `liberty_neutral` family so the semantic neutral lane can remain one coherent warm structural ramp.
3. Create a Liberty Mountain semantic color extension that:
   - maps `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, and `border/subtle` to `liberty_neutral`
   - maps `brand/*` to `sunrise`
   - maps `brand_secondary/*` to `spring`
   - overrides `assets/logo` to the string `Liberty Mountain`
4. Use the following live Liberty Mountain color staging choices:
   - `surface/brand/default` -> `liberty_mountain/sunrise/600`
   - `surface/brand/strong` -> `liberty_mountain/sunrise/700`
   - `surface/brand/emphasis` -> `liberty_mountain/sunrise/800`
   - `foreground/brand` -> `liberty_mountain/sunrise/700`
   - `border/brand` -> `liberty_mountain/sunrise/500`
   - `surface/brand_secondary/default` -> `liberty_mountain/spring/700`
   - `surface/brand_secondary/strong` -> `liberty_mountain/spring/800`
   - `surface/brand_secondary/emphasis` -> `liberty_mountain/spring/900`
   - `foreground/brand_secondary` -> `liberty_mountain/spring/800`
   - `border/brand_secondary` -> `liberty_mountain/spring/600`
5. Add two raw typography family primitives in `_Global: Typography`:
   - `liberty_mountain/family/primary` -> `Brown`
   - `liberty_mountain/family/alternate` -> `Sentinel Book`
6. Create a Liberty Mountain semantic typography extension that maps:
   - `family/heading` -> `liberty_mountain/family/primary`
   - `family/body` -> `liberty_mountain/family/primary`
   - `family/action` -> `liberty_mountain/family/primary`
   - `weight/heading/base` -> `universal/weight/normal`
   - `weight/heading/strong` -> `universal/weight/normal`
   - `weight/body/base` -> `universal/weight/light`
   - `weight/body/strong` -> `universal/weight/normal`
   - `weight/action/base` -> `universal/weight/normal`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `liberty_mountain/*`
  - `liberty_mountain/family/primary`
  - `liberty_mountain/family/alternate`
  - `figma/brands/liberty_mountain/brand.yml`
  - `figma/brands/liberty_mountain/color/intake.yml`
  - `figma/brands/liberty_mountain/color/preview.md`
  - `figma/brands/liberty_mountain/typography/intake.yml`
  - `figma/brands/liberty_mountain/typography/preview.md`
- Explicit exceptions:
  - `Limestone`, `Mineral`, and `Sand` are preserved as separate raw source families and also combined into the composite raw family `liberty_neutral` so the semantic neutral lane can remain coherent.
  - `Spring` needed the darker `700/800/900` staging set to satisfy the shared white on-surface contract, even though its raw source anchor lives at `500`.
  - `Sentinel Book` is preserved as a raw alternate family only; it is not forced into the current semantic typography lanes.
  - `weight/heading/strong` and `weight/action/base` are explicitly overridden away from the shared black default because the source never specifies a heavy Liberty Mountain treatment.
- Inherited or deferred items:
  - Positive, warning, and critical semantic color roles remain inherited from the shared base semantic collection.
  - Safe family aliases and all semantic size roles remain inherited from the shared semantic typography base.

## Consequences

Liberty Mountain can now consume the governed semantic color and typography contracts in the Foundations file without inventing a third expressive semantic lane or breaking the shared brand-extension model.

The source palette remains fully preserved in `_Global: Color`, including colors that are intentionally raw-only in the first pass.

The typography write keeps Brown as the live semantic family across the hierarchy while retaining Sentinel Book as a governed raw alternate for future schema expansion.

## Follow-up

- Update:
  - Liberty Mountain global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/liberty_mountain/brand.yml`.
- Link from:
  - `figma/brands/liberty_mountain/brand.yml`
- Verify:
  - `Liberty Mountain` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `liberty_mountain/liberty_neutral/200`, `liberty_mountain/sunrise/600`, `liberty_mountain/spring/700`, `liberty_mountain/family/primary`, `liberty_mountain/family/alternate`, `universal/weight/normal`, and `universal/weight/light` as intended.
