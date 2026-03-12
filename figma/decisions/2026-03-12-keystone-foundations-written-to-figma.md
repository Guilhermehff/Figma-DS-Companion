# Keystone Foundations Written To Figma

- Date: 2026-03-12
- Brand: Keystone
- Figma file: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Status: approved

## Decision

Keystone color and typography foundations are approved and written into the Design System file.

## Scope

- `_Global: Color`
  - Added `keystone/valencia/*`
  - Added `keystone/curious_blue/*`
  - Added `keystone/cool_grey/*`
- `_Global: Typography`
  - Added `keystone/family/primary`
  - Added `keystone/family/secondary`
- `Semantic: Color`
  - Added the `Keystone` extension
  - Mapped `brand/*` to `keystone/valencia/*`
  - Mapped `brand_secondary/*` to `keystone/curious_blue/*`
  - Mapped `neutral/*` to `keystone/cool_grey/*`
  - Left `brand_tertiary/*` inherited from the semantic base
- `Semantic: Typography`
  - Added the `Keystone` extension
  - Mapped `family/heading` to `keystone/family/primary`
  - Mapped `family/body` to `keystone/family/secondary`
  - Mapped `family/action` to `keystone/family/primary`
  - Mapped `weight/heading/base` to `universal/weight/bold`
  - Mapped `weight/body/base` to `universal/weight/medium`
  - Mapped `weight/action/base` to `universal/weight/bold`
  - Mapped `size/action/base` to `universal/size/500`

## Notes

- Cool Grey is approved to map to the semantic neutral lane only.
- CTA is approved to use Futura Bold.
- No new shared raw size step was added in this pass, so the explicit 48px Keystone headline recipe remains documented for a future size-ladder review.
- Plugin-runtime verification confirmed `33` color overrides and `7` typography overrides for Keystone.
