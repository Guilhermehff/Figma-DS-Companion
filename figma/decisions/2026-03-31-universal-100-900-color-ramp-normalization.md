# Decision Log

- Date: 2026-03-31
- Title: Universal 100-900 Color Ramp Normalization
- Status: accepted
- Scope: system-wide color governance
- Brand (if brand-specific): all brands
- Figma file (if applicable): Foundations (`https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations`)
- Stakeholders: design_system_governance, brand foundations review
- Supersedes: Prior 50-950 color ramp guidance embedded in `figma/config/variable-taxonomy.yml`, `figma/templates/brand-color-intake.yml`, and active brand color intake artifacts.
- Superseded by:

## Context

The active `_Global: Color` system had grown around an 11-step `50-950` ladder. That shape no longer matched the desired public token pattern, and it created extra migration work in the `Global Tokens` documentation, semantic theme aliases, and brand companion artifacts.

The approved change was to normalize all universal and brand color families to a shared 9-step `100-900` scale while preserving validated source colors on-ramp. Existing brand reviews already validated many of the raw values, so the migration needed to reuse current colors by default rather than regenerate every ladder from scratch.

## Decision

Adopt `100 200 300 400 500 600 700 800 900` as the standard public ramp for `_Global: Color`.

Use a reuse-first migration rule:

- Reuse validated ramp values whenever a family can be normalized without dropping a source color.
- Preserve every source color exactly on-ramp.
- If a source color would fall on a removed stop, treat that family as an exception and keep the source color on-ramp while only regenerating the surrounding non-source slots if needed.
- Keep semantic variable names unchanged and remap their alias targets by role intent.
- Keep `on_surface/*` contrast-driven against their paired semantic surfaces.

The live migration was executed in `Foundations` for `_Global: Color`, the base `Semantic: Theme` collection, all `Semantic: Theme` brand extensions, and the `Global Tokens` documentation page.

## Scope

- Affected collections:
  - `_Global: Color`
  - `Semantic: Theme`
- Affected tokens or artifact paths:
  - all universal color families
  - all brand color families
  - `figma/config/variable-taxonomy.yml`
  - `figma/templates/brand-color-intake.yml`
  - `figma/brands/*/color/intake.yml`
  - `figma/brands/*/color/preview.md`
  - `figma/brands/*/brand.yml`
- Explicit exceptions:
  - Families with source anchors that would otherwise fall on removed slots keep those source values on-ramp and adjust the surrounding steps to the normalized `100-900` ladder.
  - Source-anchor preservation takes precedence over reuse of a removed intermediate stop.
- Inherited or deferred items:
  - Historical decisions and archived variable inventories remain unchanged as records of the prior `50-950` system.
  - Channel-library migration is deferred to channel-specific follow-up work.

## Consequences

The active design-system color model now uses one universal 9-step ramp shape across universal and brand families.

This reduces token count, simplifies documentation, and aligns semantic alias targeting with a single public scale. It also means older notes or exports that reference `50` or `950` are historical and should not be treated as current guidance.

Brand companion artifacts now need to keep source-anchor notation, preview strips, semantic notes, and review guidance aligned to the new `100-900` system whenever a color family is updated again.

## Follow-up

- Update: Keep new brand color intake and preview work on the `100-900` ladder by default.
- Link from: `figma/brands/*/brand.yml` color decision artifact lists.
- Verify:
  - `_Global: Color` exposes only `100-900` steps in live Figma.
  - `Semantic: Theme` base and brand extensions do not alias removed `50` or `950` steps.
  - `Global Tokens` documentation shows 9 tokenized swatches per ramp with correct HEX values.
