# Northstar Foundations Written To Figma

- Date: 2026-03-11
- Brand: Northstar
- Figma file: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Status: approved

## Decision

Northstar color and typography foundations are approved and written into the Design System file.

## Scope

- `_Global: Color`
  - Added `northstar/burgundy/*`
  - Added `northstar/copper/*`
  - Added `northstar/graphite/*`
- `_Global: Typography`
  - Added `northstar/family/primary`
- `Semantic: Color`
  - Added the `Northstar` extension
  - Mapped `brand/*` to `northstar/burgundy/*`
  - Mapped `brand_secondary/*` to `northstar/copper/*`
  - Mapped `brand_tertiary/*` to `northstar/burgundy/*`
  - Mapped `neutral/*` to `northstar/graphite/*`
- `Semantic: Typography`
  - Added the `Northstar` extension
  - Mapped `family/heading` and `family/body` to `northstar/family/primary`
  - Mapped `weight/heading/base` to `universal/weight/medium`
  - Mapped `weight/body/base` to `universal/weight/normal`

## Notes

- `brand_tertiary/*` was initially staged as inherited, then approved to reuse the burgundy ladder before the live write.
- The Northstar Snow White source artifact is internally inconsistent: the shown RGB is `242 240 234`, while the displayed HEX is `#f2f0ef`. Governance preserves the displayed HEX as canonical until the source artifact is corrected.
- Action typography remains inherited because the source guidance did not define a CTA or button-specific rule.
