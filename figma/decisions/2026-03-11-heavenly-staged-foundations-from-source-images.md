# Heavenly Staged Foundations From Source Images

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

Heavenly was not yet represented in the governed brand registry, but the source images supplied in chat were explicit enough to stage initial color and typography governance artifacts in the repository.

The provided material included:

- one Heavenly color palette image with exact RGB, CMYK, and HEX values
- one Heavenly typography guidance image with named families, named weights, case rules, and a sample composition

## Decision

1. Add `heavenly` to `figma/brands/registry.yml` as a staged brand.
2. Create a canonical brand manifest at `figma/brands/heavenly/brand.yml`.
3. Stage Heavenly color foundations in repo only:
   - reuse `universal/white`
   - reuse `universal/black`
   - propose brand families `heavenly/snow_flower_red/*`, `heavenly/deep_water_blue/*`, and `heavenly/shore_blue/*`
4. Stage Heavenly typography foundations in repo only:
   - propose `heavenly/family/primary` for Din Condensed
   - propose `heavenly/family/secondary` for Brandon Grotesque
   - propose shared raw weight `universal/weight/light`
5. Do not claim a live Figma write for Heavenly yet.
6. Keep CTA typography as an explicit review hold because the source only defines CTA tracking, not CTA family, weight, or size.

## Consequences

- Heavenly is now governable in the repository with canonical intake and preview artifacts.
- Figma semantic extension targets are identified, but Heavenly remains `pending_write` until a deliberate Figma write is performed and verified.
- Any future live write should confirm whether the staged semantic color slot order of red, dark blue, then light blue matches the broader Heavenly brand system.
