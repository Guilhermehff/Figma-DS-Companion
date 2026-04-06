# Decision Log

- Date: 2026-03-26
- Title: Semantic theme unification and published global typography sizes
- Status: accepted
- Scope: Token model, semantic extensions, and channel typography contract
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations and Email Library
- Stakeholders: Design system governance, channel library authors
- Supersedes:
  - `2026-03-10-global-and-semantic-collections.md`
  - `2026-03-11-shared-semantic-collections-with-brand-extensions.md`
  - `2026-03-11-role-scoped-semantic-typography-ladders.md`
- Superseded by:
  - `2026-04-06-semantic-theme-ad-typography-size-recipes.md`

## Context

The active Foundations file had two published semantic contracts for downstream consumers: `Semantic: Color` for color and assets, and `Semantic: Typography` for typography family, weight, and size. In practice, channel authors were already treating brand switching as one cohesive decision while Email still had to consume two upstream semantic collections.

That split added migration overhead for every brand write and made the channel contract harder to explain. At the same time, the typography size aliases in `Semantic: Typography` duplicated information that channels could consume directly from the governed raw global size ladder.

## Decision

1. The semantic layer is unified into one published collection named `Semantic: Theme`.
2. `Semantic: Theme` owns:
   - semantic color roles
   - `assets/logo`
   - semantic typography family aliases
   - semantic typography weight aliases
3. Typography size aliases are removed from the live semantic contract.
4. `_Global: Typography` is renamed to `Global: Typography` and becomes a published global exception.
5. Only the shared size ladder is publish-visible from `Global: Typography`; raw family and raw weight primitives remain hidden from publishing.
6. Channel text styles bind `fontFamily` and `fontWeight` from `Semantic: Theme` and bind `fontSize` directly from `Global: Typography`.
7. Brand semantic overrides are now recorded as one theme extension per brand in repo manifests and live Figma state.

## Scope

- Affected collections:
  - `Semantic: Theme`
  - `Global: Typography`
- Affected tokens or artifact paths:
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/AGENTS.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/config/variable-taxonomy.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-manifest.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/docs/semantic-extension-write-workflow.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/docs/brand-color-foundations.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/docs/brand-typography-foundations.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/brands/*/brand.yml`
- Explicit exceptions:
  - `Global: Typography` is the approved published global exception for typography size only.
  - Raw typography family and weight primitives stay hidden from publishing.
- Inherited or deferred items:
  - Intake and preview artifacts stay split into color and typography tracks.
  - Web and Ads adopt the new contract after Email; this decision does not require their live migration in the same write.

## Consequences

Brand changes now route through one semantic extension collection instead of separate color and typography semantic extensions.

Channel typography no longer consumes semantic size aliases. Future library authors should expect family and weight from `Semantic: Theme` and size from `Global: Typography`.

Historical artifacts remain unchanged, but active governance docs, templates, manifests, and live Foundations documentation must describe the unified semantic theme model.

## Follow-up

- Update:
  - Keep repo manifests, active docs, and taxonomy aligned with the single-theme semantic contract.
- Link from:
  - Active brand manifests through their canonical `semantic_extensions.theme` records.
- Verify:
  - Foundations exposes `Semantic: Theme` and publish-visible global typography sizes.
  - Email text styles bind family and weight from `Semantic: Theme` and size from `Global: Typography`.
