# Keystone Staged Foundations From Source Images

Date: 2026-03-12
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

Keystone was not yet represented in the governed brand registry, but the supplied source images are explicit enough to stage color and typography governance artifacts in the repository.

The provided material included:

- one Keystone color palette image with named source colors and exact HEX, RGB, CMYK, and PMS values
- one Keystone typography guidance image with named families, explicit weight labels, explicit size and leading examples, and one contradiction in CTA guidance

## Decision

1. Add `keystone` to `figma/brands/registry.yml` as a staged brand.
2. Create a canonical brand manifest at `figma/brands/keystone/brand.yml`.
3. Stage Keystone color foundations in repo only:
   - propose `keystone/valencia/*`
   - propose `keystone/curious_blue/*`
   - propose `keystone/cool_grey/*`
4. Stage Keystone typography foundations in repo only:
   - propose `keystone/family/primary` for Futura
   - propose `keystone/family/secondary` for Avenir
   - propose a new shared raw size step `universal/size/900 = 48` for the explicit headline example
5. Do not perform any live Figma write for Keystone yet.
6. Keep the following review holds explicit before any live write:
   - whether `Cool Grey` maps to `neutral/*` only or also to `brand_tertiary/*`
   - whether CTA follows the Avenir guidance text or the Futura CTA example
   - whether the shared raw size ladder should grow to include a 48px headline step

## Consequences

- Keystone is now governable in the repository with canonical intake and preview artifacts.
- No live Figma collection extensions or variable writes exist for Keystone yet.
- Any future live write must use the preview-reviewed mappings and resolve the CTA contradiction and headline size-step decision first.
