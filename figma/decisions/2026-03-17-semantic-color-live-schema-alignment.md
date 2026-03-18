# Decision Log

- Date: 2026-03-17
- Title: Semantic Color Live Schema Alignment
- Status: active
- Scope: systemwide
- Brand (if brand-specific): n/a
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders:
  - design_system_governance
- Supersedes:
  - figma/decisions/2026-03-13-proposed-semantic-role-channel-color-model.md (active semantic color base-schema references only)
- Superseded by:

## Context

The live `Foundations` file is the source of truth for active semantic color inventory. A runtime comparison on 2026-03-17 showed that the active `Semantic: Color` collection no longer matches some older local governance references.

The live base collection uses the mode name `Default`, includes the governed string token `assets/logo`, and does not include `foreground/inverse`. Several local manifests and the taxonomy still documented the older proposed inventory.

## Decision

The active governed semantic color schema follows the live `Foundations` file.

- `Semantic: Color` uses the base mode name `Default`.
- `assets/logo` remains part of the active base semantic color schema and each brand extension must override it to the brand display name when present.
- `foreground/inverse` is not part of the active governed semantic color inventory and must be removed from active taxonomy and manifest references unless it is reintroduced through a later approved write.

## Scope

- Affected collections:
  - `Semantic: Color`
  - All brand semantic color extensions in the `Foundations` file
- Affected tokens or artifact paths:
  - `assets/logo`
  - `foreground/inverse`
  - `figma/config/variable-taxonomy.yml`
  - `figma/docs/semantic-extension-write-workflow.md`
  - `figma/brands/*/brand.yml`
- Explicit exceptions:
  - Historical decisions and archived artifacts may retain earlier proposed schemas for traceability.
- Inherited or deferred items:
  - Shared positive, warning, and critical role sets remain inherited from the base semantic color collection.

## Consequences

Canonical local governance files must align to the live `Foundations` semantic color schema instead of the older proposed role model. Historical decision logs are preserved as historical context, but they no longer define the active token inventory when they conflict with the live file.

Any future reintroduction of `foreground/inverse` would require a new approved semantic-slot decision and a corresponding live Figma write before canonical docs are updated again.

## Follow-up

- Update:
  - Align taxonomy, workflow docs, manifests, and intake provenance with the current `Foundations` state.
- Link from:
  - No brand-specific manifest link required; this is a systemwide governance decision.
- Verify:
  - Confirm the live `Semantic: Color` collection still reports `Default` mode, includes `assets/logo`, and excludes `foreground/inverse`.
