# Heavenly Foundations Written To Figma

- Date: 2026-03-11
- Brand: Heavenly
- Figma file: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Status: approved

## Decision

Heavenly color and typography foundations are approved and written into the Design System file.

## Scope

- `_Global: Color`
  - Added `heavenly/snow_flower_red/*`
  - Added `heavenly/deep_water_blue/*`
  - Added `heavenly/shore_blue/*`
- `_Global: Typography`
  - Added `heavenly/family/primary`
  - Added `heavenly/family/secondary`
  - Added shared raw weight `universal/weight/light`
- `Semantic: Typography`
  - Added base aliases `weight/heading/strong`, `weight/body/strong`, and `size/body/lg`
  - Added the `Heavenly` extension
  - Mapped `family/heading` to `heavenly/family/primary`
  - Mapped `family/body` to `heavenly/family/secondary`
  - Mapped `weight/heading/base` to `universal/weight/light`
  - Mapped `weight/heading/strong` to `universal/weight/bold`
  - Mapped `weight/body/base` to `universal/weight/normal`
  - Mapped `weight/body/strong` to `universal/weight/medium`
- `Semantic: Color`
  - Added the `Heavenly` extension
  - Mapped `brand/*` to `heavenly/snow_flower_red/*`
  - Mapped `brand_secondary/*` to `heavenly/deep_water_blue/*`
  - Mapped `brand_tertiary/*` to `heavenly/shore_blue/*`

## Notes

- Exact white and black remain inherited from the universal layer and were not duplicated under the Heavenly brand group.
- CTA typography remains inherited because the supplied source defined CTA tracking but did not explicitly define CTA family, size, or weight.
- Extension verification in the plugin runtime confirmed `33` color overrides and `6` typography overrides for Heavenly.
