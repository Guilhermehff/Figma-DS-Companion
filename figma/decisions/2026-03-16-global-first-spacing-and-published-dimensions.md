# Decision Log

- Date: 2026-03-16
- Title: Global-First Spacing And Published Dimensions Collection
- Status: accepted
- Scope: dimensions governance
- Brand (if brand-specific):
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance
- Supersedes:
  - figma/decisions/2026-03-11-user-facing-collection-naming.md in part
  - figma/decisions/2026-03-10-global-and-semantic-collections.md in part
- Superseded by:

## Context

Spacing review concluded that the current multi-brand system does not need brand-specific spacing semantics. All brands are expected to share the same raw 8-point spacing ladder, while downstream channels may still need different responsive behaviors.

The main divergence is channel-specific, not brand-specific:

- Web is likely to need multiple responsive modes.
- Email may also need a smaller responsive mode set.
- Ads currently do not justify responsive spacing modes.

At the same time, the dimensions collection needs to be published to consumers in the library, unlike the other current global collections. After the live rename in Figma, cached `figma_get_variables` results still reported `_Global: Dimensions`, but direct plugin-runtime inspection through `figma.variables.getLocalVariableCollectionsAsync()` confirmed that the live collection name is now `Global: Dimensions`.

## Decision

1. Adopt a global-first spacing model for now.
2. Treat `Global: Dimensions` as the raw spacing source of truth, using the existing universal space ladder and a single `values` mode.
3. Do not create `Semantic: Dimensions` by default. Introduce it only if repeated cross-channel alias roles later justify a shared abstraction layer.
4. If `Semantic: Dimensions` is introduced later, keep it universal only. Do not use brand extensions for spacing semantics.
5. Put responsive spacing behavior in channel collections only.
6. Allow future channel collections such as `Channel: Web Dimensions` and `Channel: Email Dimensions` to use only the modes they need, while `Channel: Ads Dimensions` should remain single-mode unless a real downstream need appears.
7. Rename `_Global: Dimensions` to `Global: Dimensions` and publish it as an approved exception to the default unpublished `_Global: *` naming rule used by the other global collections.

## Scope

- Affected collections:
  - `Global: Dimensions`
  - future `Semantic: Dimensions` if later approved
  - future `Channel: Ads Dimensions`
  - future `Channel: Email Dimensions`
  - future `Channel: Web Dimensions`
- Affected tokens or artifact paths:
  - `figma/config/variable-taxonomy.yml`
  - the existing `space/*` variables in the dimensions collection
- Explicit exceptions:
  - `Global: Dimensions` is published even though the default global naming rule remains `_Global: *`
- Inherited or deferred items:
  - `Semantic: Dimensions` remains deferred
  - breakpoint threshold definitions remain a channel-governance concern outside variable mode names

## Consequences

The canonical repo taxonomy must treat dimensions as a published exception to the default global collection rule.

Spacing governance now defaults to `Global -> Channel` instead of forcing a semantic layer before there is evidence that one is needed. Future semantic spacing work requires a new accepted decision before tokens are added to Figma.

Channel libraries can introduce responsive spacing modes where justified, but those modes must not be back-propagated into `Global: Dimensions`.

## Follow-up

- Update: `figma/config/variable-taxonomy.yml`
- Link from: none required
- Verify: when a recent Figma collection rename looks stale in `figma_get_variables`, verify the live runtime state with `figma_execute` before syncing repo artifacts
