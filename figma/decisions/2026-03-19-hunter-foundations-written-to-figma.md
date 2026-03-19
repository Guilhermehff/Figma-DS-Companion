# Decision Log

- Date: 2026-03-19
- Title: Hunter Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Hunter
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Hunter introduces a palette where both the pale `Snow Blue` and the dark `Mountain Blue` read as core brand color, while `Flurry White` and `City Grey` support a quieter neutral lane. The staged recommendation originally treated the entire blue-gray family as structural neutral and used `Forest Green` as the supporting expressive lane.

The user approved a different mapping in chat:

1. `Forest Green` should remain global-only in the first pass
2. `Sunrise Orange` should map to `brand_secondary`
3. `Snow Blue` and `Mountain Blue` should share the same primary expressive ramp
4. `Flurry White` and `City Grey` should form the neutral ramp

The typography source is straightforward by comparison: one `Galano Grotesque` family carries the hierarchy through weight changes, and the source provides no CTA recipe.

## Decision

1. Add four Hunter raw color families in `_Global: Color`:
   - `hunter/hunter_neutral/*`
   - `hunter/mountain_blue/*`
   - `hunter/sunrise_orange/*`
   - `hunter/forest_green/*`
2. Create a Hunter semantic color extension that:
   - maps `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, and `border/subtle` to `hunter_neutral`
   - maps `brand/*` to `mountain_blue`
   - maps `brand_secondary/*` to `sunrise_orange`
   - overrides `assets/logo` to the string `Hunter`
3. Preserve `forest_green` as a governed raw global-only family and do not map it into the first semantic pass.
4. Use the following live Hunter color staging choices:
   - `surface/brand/default` -> `hunter/mountain_blue/600`
   - `surface/brand/strong` -> `hunter/mountain_blue/700`
   - `surface/brand/emphasis` -> `hunter/mountain_blue/800`
   - `foreground/brand` -> `hunter/mountain_blue/700`
   - `border/brand` -> `hunter/mountain_blue/500`
   - `surface/brand_secondary/default` -> `hunter/sunrise_orange/600`
   - `surface/brand_secondary/strong` -> `hunter/sunrise_orange/700`
   - `surface/brand_secondary/emphasis` -> `hunter/sunrise_orange/800`
   - `foreground/brand_secondary` -> `hunter/sunrise_orange/700`
   - `border/brand_secondary` -> `hunter/sunrise_orange/500`
5. Add one Hunter raw typography family primitive in `_Global: Typography`:
   - `hunter/family/primary` -> `Galano Grotesque`
6. Create a Hunter semantic typography extension that maps:
   - `family/heading` -> `hunter/family/primary`
   - `family/body` -> `hunter/family/primary`
   - `weight/heading/base` -> `universal/weight/bold`
   - `weight/body/base` -> `universal/weight/normal`
   - `weight/body/strong` -> `universal/weight/semibold`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `hunter/hunter_neutral/*`
  - `hunter/mountain_blue/*`
  - `hunter/sunrise_orange/*`
  - `hunter/forest_green/*`
  - `hunter/family/primary`
  - `figma/brands/hunter/brand.yml`
  - `figma/brands/hunter/color/intake.yml`
  - `figma/brands/hunter/color/preview.md`
  - `figma/brands/hunter/typography/intake.yml`
  - `figma/brands/hunter/typography/preview.md`
- Explicit exceptions:
  - The live write does not follow the staged recommendation that absorbed Snow Blue and Mountain Blue into the structural neutral system.
  - `forest_green` is intentionally preserved as a governed raw family only and is not mapped to `brand_secondary` in the first pass.
  - The primary expressive lane stages on `mountain_blue/600`, `700`, and `800` because those are the first steps that preserve the approved blue family while meeting the shared white on-surface contract.
  - The supporting expressive lane stages on `sunrise_orange/600`, `700`, and `800` because the raw `500` anchor does not provide the same white on-surface safety for semantic default surfaces.
- Inherited or deferred items:
  - Positive, warning, and critical semantic color roles remain inherited from the shared base semantic collection.
  - Safe family aliases, the action family, action weights, and all size semantics remain inherited from the shared semantic typography base.
  - `Galano Grotesque Light` remains documented as a raw contrasting-body option rather than a separate semantic lane.

## Consequences

Hunter can now consume the shared semantic color and typography contracts in the Foundations file while preserving the user-approved split between structural neutral, expressive blue, expressive orange, and global-only green.

The non-obvious Hunter color interpretation is now durable in governance history instead of living only in chat context or staged review notes.

The typography write stays aligned to the existing shared semantic model and does not invent a CTA lane the source never defined.

## Follow-up

- Update:
  - Hunter global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/hunter/brand.yml`.
- Link from:
  - `figma/brands/hunter/brand.yml`
- Verify:
  - `Hunter` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `hunter/hunter_neutral/50`, `hunter/mountain_blue/600`, `hunter/sunrise_orange/600`, `Hunter`, `hunter/family/primary`, `universal/weight/bold`, `universal/weight/normal`, and `universal/weight/semibold` as intended.
