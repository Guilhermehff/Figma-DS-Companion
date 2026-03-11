# Figma-First Governance Exports

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

Brand onboarding was slowed down by maintaining repo-side mirrors of semantic extension overrides and a generated compatibility registry even though live Figma variables are the source of truth.

Those mirrors improved local diffability, but they added repetitive sync work after every Figma write and duplicated data that can be exported later if an audit or compatibility artifact is actually needed.

## Decision

1. Treat live Figma variables and extension collections as the only active token source of truth.
2. Keep `figma/brands/<brand>/brand.yml` as the canonical repo record for brand targeting metadata, source references, and governance notes, but stop mirroring live token counts in that manifest.
3. Stop treating `figma/variables/extensions/*.yml` as required live governance artifacts. Create them only when a local audit or compatibility export is explicitly requested.
4. Stop treating `figma/variables/registry.yml` as a required post-write artifact. Generate it only on demand.
5. Keep existing collection snapshots and export tooling as optional local export paths rather than mandatory write-follow-up steps.

## Consequences

- The default post-write workflow is now: verify in Figma, update minimal brand metadata when needed, and stop.
- Repo validation no longer fails just because local token export files were not refreshed.
- When a downstream audit needs local YAML, the export can be generated at that time from Figma instead of being preserved continuously.
