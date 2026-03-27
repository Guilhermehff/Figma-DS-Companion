# Decision Log

- Date: 2026-03-27
- Title: No mirrored typography primitives for brands without established font guidance
- Status: accepted
- Scope: Brand typography staging, semantic theme extension behavior, and Foundations documentation
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations
- Stakeholders: Design system governance, channel library authors
- Supersedes:
  - mirrored-baseline typography interpretations previously recorded in the affected brand typography intake, preview, and manifest artifacts
- Superseded by:

## Context

Several brands with no established typography guidance had been staged with raw `brand/family/primary` tokens that simply mirrored `universal/family/primary`. Their `Semantic: Theme` extensions also overrode typography family aliases back to those mirrored raw tokens.

That staging pattern added maintenance overhead without adding any real typography information. It also made the Foundations typography documentation imply that those brands had governed typography tokens when they actually inherited the universal baseline.

## Decision

1. Brands without established typography guidance must not receive raw typography family or weight primitives that only mirror universal values.
2. Those brands must inherit typography family and weight aliases directly from the shared `Semantic: Theme` base without extension overrides.
3. Foundations typography documentation for those brands must use a warning-only state instead of token or family-detail layouts.
4. Typography size behavior remains unchanged: channels bind size from published `Global: Typography`.

## Scope

- Affected collections:
  - `Global: Typography`
  - `Semantic: Theme`
- Affected tokens or artifact paths:
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/AGENTS.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/config/variable-taxonomy.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/brands/*/brand.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/brands/*/typography/intake.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/brands/*/typography/preview.md`
- Explicit exceptions:
  - none
- Inherited or deferred items:
  - Brands with established typography guidance continue to use raw typography primitives and semantic theme typography overrides when they materially differ from the universal base.

## Consequences

Foundations no longer carries mirrored brand typography primitives for brands without established font guidance. Their semantic theme extensions keep color and asset overrides where needed, but typography aliases now inherit the shared universal base directly.

Documentation for those brands now communicates the absence of established typography guidance instead of presenting placeholder token details. Future typography token creation for those brands now requires an actual brand-specific typography source.

## Follow-up

- Update:
  - Remove mirrored raw typography primitives and corresponding semantic typography overrides for affected brands.
  - Keep manifests, intake artifacts, previews, and taxonomy rules aligned with the inherited-baseline behavior.
- Link from:
  - the affected brand manifests through their typography artifact references
- Verify:
  - the affected brands have no mirrored raw typography primitives in `Global: Typography`
  - the affected `Semantic: Theme` extensions contain no typography overrides
  - Foundations typography docs for the affected brands use the warning-only state
