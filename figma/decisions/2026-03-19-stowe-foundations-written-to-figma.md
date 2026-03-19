# Decision Log

- Date: 2026-03-19
- Title: Stowe Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Stowe
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Stowe introduces one dominant red, one light-to-dark blue-gray system, and an exact shared white. The palette is structurally simple, but the semantic write still required one approved interpretation because the same blue-gray family needed to support both structural neutrals and the supporting expressive lane.

The typography guidance also contains a contradiction. The source explicitly labels the headline family as `Athena Regular`, but the supporting headline rule sentence says headlines are `bold`. The source provides no dedicated CTA recipe.

The user approved the live write with two explicit choices:

1. treat the headline prose word `bold` as a source copy mistake and follow `Athena Regular`
2. map the action lane to the same family and weight as heading

## Decision

1. Add two Stowe raw color families in `_Global: Color`:
   - `stowe/stowe_red/*`
   - `stowe/stowe_blue/*`
2. Reuse `universal/white` instead of duplicating a Stowe white primitive.
3. Create a Stowe semantic color extension that:
   - keeps `surface/neutral/canvas` on `universal/white`
   - maps the remaining neutral structural roles to `stowe/stowe_blue/*`
   - maps `brand/*` to `stowe/stowe_red/*`
   - maps `brand_secondary/*` to `stowe/stowe_blue/*`
   - overrides `assets/logo` to the string `Stowe`
4. Use the following live Stowe color staging choices:
   - `brand/default` -> `stowe/stowe_red/600`
   - `brand_secondary/default` -> `stowe/stowe_blue/600`
   - `foreground/brand` -> `stowe/stowe_red/700`
   - `foreground/brand_secondary` -> `stowe/stowe_blue/700`
5. Add two Stowe raw typography family primitives in `_Global: Typography`:
   - `stowe/family/display` -> `Athena`
   - `stowe/family/primary` -> `Raleway`
6. Create a Stowe semantic typography extension that maps:
   - `family/heading` -> `stowe/family/display`
   - `family/body` -> `stowe/family/primary`
   - `family/action` -> `stowe/family/display`
7. Apply the approved Stowe typography mapping:
   - `weight/heading/base` -> `universal/weight/normal`
   - `weight/body/base` -> `universal/weight/normal`
   - `weight/body/strong` -> `universal/weight/bold`
   - `weight/action/base` -> `universal/weight/normal`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `stowe/stowe_red/*`
  - `stowe/stowe_blue/*`
  - `stowe/family/display`
  - `stowe/family/primary`
  - `figma/brands/stowe/brand.yml`
  - `figma/brands/stowe/color/intake.yml`
  - `figma/brands/stowe/color/preview.md`
  - `figma/brands/stowe/typography/intake.yml`
  - `figma/brands/stowe/typography/preview.md`
- Explicit exceptions:
  - The live write treats the headline prose word `bold` as a source copy mistake and follows the explicit `Athena Regular` label.
  - The action lane follows the same family and weight as heading even though the source provides no dedicated CTA recipe.
  - `surface/neutral/canvas` remains on shared `universal/white` while the rest of the Stowe neutral structural lane maps to `stowe_blue`.
  - The supporting expressive default lane stages on `stowe/stowe_blue/600` rather than the raw `500` source anchor because `500` does not support the shared white on-surface contract used by semantic default surfaces.
- Inherited or deferred items:
  - Safe family aliases and all size semantics remain inherited from the shared semantic typography base.
  - `weight/heading/strong` remains inherited from the shared semantic typography base.
  - Raleway Light remains documented in the intake and preview artifacts as a raw contrasting-body option rather than a dedicated semantic lane.

## Consequences

Stowe can now consume the active role-based semantic color and typography contracts in the Foundations file without requiring a parallel one-off semantic structure.

The user-approved headline and action interpretations are now durable in governance history rather than living only in chat context or in staged preview notes.

The live semantic color write also records why the supporting expressive lane starts at `stowe_blue/600` even though the raw source anchor is `500`: the semantic default lane still needs readable white on-surface behavior.

## Follow-up

- Update:
  - Stowe global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/stowe/brand.yml`.
- Link from:
  - `figma/brands/stowe/brand.yml`
- Verify:
  - `Stowe` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `universal/white`, `stowe/stowe_red/600`, `stowe/stowe_blue/600`, `stowe/family/display`, `stowe/family/primary`, `universal/weight/normal`, and `universal/weight/bold` as intended.
