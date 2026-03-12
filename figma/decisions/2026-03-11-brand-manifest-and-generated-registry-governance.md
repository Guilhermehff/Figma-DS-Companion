# Brand Manifest And Generated Registry Governance

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

Superseded in part by: `figma/decisions/2026-03-11-figma-first-governance-exports.md`

## Context

The repository had enough governance rules to model tokens, but not enough operational structure to scale to dozens of brands without documentation drift, extension sprawl, and manual registry maintenance.

## Decision

1. Govern brand membership through `figma/brands/registry.yml` instead of a hardcoded brand list in the taxonomy.
2. Create one canonical per-brand manifest at `figma/brands/<brand>/brand.yml`.
3. Stage future brand artifacts under `figma/brands/<brand>/color/` and `figma/brands/<brand>/typography/`.
4. Split optional local export sources into dated snapshots referenced by `figma/exports/index.yml`.
5. Treat dated compatibility exports under `figma/exports/` as generated snapshots built from the referenced exports.
6. Track only material semantic overrides in extension manifests. Do not restate inherited base aliases in repo inventories.
7. Use local Python governance tooling to validate manifests, rebuild the compatibility registry, and detect stale operating documentation.

## Consequences

- Vail is the first seeded brand manifest and staged folder example.
- Existing dated artifacts may remain in `figma/history/variables/` as historical reference, while any new optional exports should be written under `figma/exports/`.
- Governance automation now has one repo-native model to validate before future plugin work is considered.
