# Decision Log

- Date: 2026-03-23
- Title: Semantic Color Full Inverse Matrix
- Status: active
- Scope: systemwide
- Brand (if brand-specific): n/a
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders:
  - design_system_governance
- Supersedes:
  - figma/decisions/2026-03-17-semantic-color-live-schema-alignment.md
- Superseded by:

## Context

The live `Foundations` file had already removed `on_surface/neutral/*` and introduced a partial `_inverse` set in `Semantic: Color`, but the active governed schema still documented the earlier March 17 alignment that excluded inverse coverage beyond the initial neutral and standalone foreground or border tokens.

That partial state was sufficient for the current Email contrast experiment, but it was not a complete semantic foundation for future 1:1 dark-mode mapping in Web. The governed schema needed a full inverse companion set across semantic color roles while preserving the existing non-inverse ladders.

## Decision

The active governed semantic color schema now uses a full `_inverse` companion matrix for every semantic color token except `assets/logo`.

- `Semantic: Color` remains a single-mode collection with the base mode name `Default`.
- `assets/logo` remains in the base semantic color collection and does not receive an inverse variant.
- `on_surface/neutral/*` is not part of the active schema. Neutral surfaces use shared foreground tokens instead.
- Existing non-inverse semantic steps remain unchanged. `muted`, `subtle`, `default`, `strong`, and `emphasis` are still the normal emphasis axis and are not renamed.
- `_inverse` is the governed semantic polarity suffix.
- Brand extensions must cover normal and inverse `neutral`, `brand`, and `brand_secondary` targets when those scopes are overridden, while shared status lanes remain inherited from the base collection.

The live `Foundations` write completed the missing inverse matrix for:

- `surface/{brand,brand_secondary,positive,warning,critical}/{muted,subtle,default,strong,emphasis}_inverse`
- `on_surface/{brand,brand_secondary,positive,warning,critical}/{muted,subtle,default,strong,emphasis}_inverse`
- `foreground/{positive,warning,critical}_inverse`
- `border/{brand,brand_secondary,positive,warning,critical}_inverse`

The base collection now contains `139` semantic color variables.

## Scope

- Affected collections:
  - `Semantic: Color`
  - All brand semantic color extensions in the `Foundations` file
- Affected tokens or artifact paths:
  - All active semantic color `_inverse` tokens
  - `figma/config/variable-taxonomy.yml`
  - `figma/templates/brand-manifest.yml`
  - `figma/templates/brand-color-intake.yml`
  - `figma/templates/brand-color-preview.md`
  - `figma/brands/*/brand.yml`
- Explicit exceptions:
  - `Boston Mills / Brandywine` maps both expressive normal lanes to `universal/black`, which is not a numeric family. Its inverse expressive tokens therefore use the governed fallback `universal/slate/{950,900,800,700,600,300,100}` ladder instead of inheriting the base cyan inverse defaults.
  - Historical decisions and archived artifacts may retain earlier proposed schemas for traceability.
- Inherited or deferred items:
  - Shared positive, warning, and critical inverse role sets remain inherited from the base semantic color collection.
  - `Email Library` channel remapping is deferred to a later phase; the current author-facing mode name `Primary - Contrast` remains unchanged for now.

## Consequences

Canonical local governance files must align to the live `Foundations` semantic color schema instead of the older partial inverse model.

Future channel work should consume the completed semantic inverse matrix rather than approximating inverse behavior with stronger non-inverse semantic tokens. That is especially important for Web dark mode, where channels need a true 1:1 semantic polarity map.

## Follow-up

- Update:
  - Align taxonomy, templates, and canonical brand manifests to the completed semantic inverse schema.
- Link from:
  - No brand-specific manifest link required; this is a systemwide governance decision.
- Verify:
  - Confirm the live `Semantic: Color` collection still reports `Default` mode, contains `139` variables, excludes `on_surface/neutral/*`, and provides inverse companions for every semantic color token except `assets/logo`.
