# Crested Butte Staged Foundations From Source Images

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

`Crested Butte` needs to be added to the governed brand registry, but the current request includes only source images for color and typography foundations. No Figma selection, node, or confirmed semantic-extension write target was provided for this brand.

## Decision

1. Add `crested_butte` to `figma/brands/registry.yml` as a planned brand.
2. Stage repo-governed color and typography intake and preview artifacts under `figma/brands/crested_butte`.
3. Reuse `universal/white` for the exact `#ffffff` source swatch.
4. Stage two raw color families for future review:
   - `crested_butte/wild_red/*`
   - `crested_butte/beyond_black/*`
5. Stage a single brand family token for typography:
   - `crested_butte/family/primary`
6. Stage `universal/weight/semibold` as the proposed raw weight needed to represent the source faithfully.
7. Do not add Crested Butte to the Figma-derived variable collection snapshots or semantic extension snapshots until a real write is confirmed through Figma Console MCP.

## Consequences

- The repo now tracks Crested Butte as a governed brand candidate without claiming that the DS file already contains its variables or semantic extensions.
- Future Figma work can use the staged artifacts as the approved starting point for global token creation and semantic extension overrides.
- `brand_secondary/*` and `brand_tertiary/*` remain inherited from the base semantic color collection until additional approved palette guidance exists.
