# Decision Log

- Date: 2026-03-19
- Title: Mount Sunapee Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Mount Sunapee
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Mount Sunapee introduces three distinct primary colors in the source palette, but the governed semantic color model only provides two expressive lanes beyond the structural neutral system. The source usage page also gives structural emphasis to white space, large dark blocks, and subdued supporting accents, which made the semantic split non-obvious.

The typography source is explicit about the H1, H2, body, and H3 roles, but the current semantic typography schema still has no dedicated subhead family lane and the source provides no CTA recipe.

The user approved the recommended mapping in chat and authorized the live write.

## Decision

1. Add three Mount Sunapee raw color families in `_Global: Color`:
   - `mount_sunapee/sunapee_neutral/*`
   - `mount_sunapee/cold_wax/*`
   - `mount_sunapee/golden_hour/*`
2. Create a Mount Sunapee semantic color extension that:
   - maps `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, and `border/subtle` to `sunapee_neutral`
   - maps `brand/*` to `cold_wax`
   - maps `brand_secondary/*` to `golden_hour`
   - overrides `assets/logo` to the string `Mount Sunapee`
3. Use the following live Mount Sunapee color staging choices:
   - `surface/brand/default` -> `mount_sunapee/cold_wax/700`
   - `surface/brand/strong` -> `mount_sunapee/cold_wax/800`
   - `surface/brand/emphasis` -> `mount_sunapee/cold_wax/900`
   - `foreground/brand` -> `mount_sunapee/cold_wax/800`
   - `border/brand` -> `mount_sunapee/cold_wax/600`
   - `surface/brand_secondary/default` -> `mount_sunapee/golden_hour/600`
   - `surface/brand_secondary/strong` -> `mount_sunapee/golden_hour/700`
   - `surface/brand_secondary/emphasis` -> `mount_sunapee/golden_hour/800`
   - `foreground/brand_secondary` -> `mount_sunapee/golden_hour/700`
   - `border/brand_secondary` -> `mount_sunapee/golden_hour/500`
4. Add two Mount Sunapee raw typography family primitives in `_Global: Typography`:
   - `mount_sunapee/family/primary` -> `Graphik`
   - `mount_sunapee/family/utility` -> `Neutraface Text Bold Italic`
5. Create a Mount Sunapee semantic typography extension that maps:
   - `family/heading` -> `mount_sunapee/family/primary`
   - `family/body` -> `mount_sunapee/family/primary`
   - `weight/heading/base` -> `universal/weight/bold`
   - `weight/body/base` -> `universal/weight/light`
   - `weight/body/strong` -> `universal/weight/normal`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `mount_sunapee/sunapee_neutral/*`
  - `mount_sunapee/cold_wax/*`
  - `mount_sunapee/golden_hour/*`
  - `mount_sunapee/family/primary`
  - `mount_sunapee/family/utility`
  - `figma/brands/mount_sunapee/brand.yml`
  - `figma/brands/mount_sunapee/color/intake.yml`
  - `figma/brands/mount_sunapee/color/preview.md`
  - `figma/brands/mount_sunapee/typography/intake.yml`
  - `figma/brands/mount_sunapee/typography/preview.md`
- Explicit exceptions:
  - The approved mapping absorbs Snow Gun, Verde Slate, and Lake Sunapee into one branded structural neutral family instead of preserving Lake Sunapee as its own expressive lane.
  - The brand lane stages on `cold_wax/700`, `800`, and `900` rather than the raw `500` source anchor so the shared white on-surface contract holds for semantic brand surfaces.
  - The supporting expressive lane stages on `golden_hour/600`, `700`, and `800` rather than the raw `300` source anchor so the shared white on-surface contract also holds there.
  - `Neutraface Text Bold Italic` is preserved as a raw utility family primitive only; it is not forced into the current semantic typography lanes.
- Inherited or deferred items:
  - Positive, warning, and critical semantic color roles remain inherited from the shared base semantic collection.
  - Safe family aliases, the action family, action weights, and all size semantics remain inherited from the shared semantic typography base.

## Consequences

Mount Sunapee can now consume the governed semantic color and typography contracts in the Foundations file without requiring a one-off semantic structure or a third expressive color lane.

The approved non-obvious color split is now durable in governance history instead of living only in intake notes or chat context.

The typography write preserves the distinct H3 treatment in raw form while keeping the live semantic extension aligned to the current shared typography schema.

## Follow-up

- Update:
  - Mount Sunapee global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/mount_sunapee/brand.yml`.
- Link from:
  - `figma/brands/mount_sunapee/brand.yml`
- Verify:
  - `Mount Sunapee` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `mount_sunapee/sunapee_neutral/50`, `mount_sunapee/cold_wax/700`, `mount_sunapee/golden_hour/600`, `mount_sunapee/family/primary`, `Neutraface Text Bold Italic`, `universal/weight/bold`, `universal/weight/light`, and `universal/weight/normal` as intended.
