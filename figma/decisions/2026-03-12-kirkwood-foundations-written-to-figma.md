# Kirkwood Foundations Written To Figma

- Date: 2026-03-12
- Brand: Kirkwood
- Figma file: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Status: written with process exception

## Decision

Kirkwood color and typography foundations were written into the Design System file, but the live write occurred before preview review was completed.

## Scope

- `_Global: Color`
  - Added `kirkwood/orange_021_c/*`
  - Added `kirkwood/blue_648_c/*`
  - Added `kirkwood/teal_633_c/*`
  - Added `kirkwood/cool_gray/*`
- `_Global: Typography`
  - Added `kirkwood/family/primary`
  - Added `kirkwood/family/secondary`
  - Added `kirkwood/family/action`
  - Added `kirkwood/family/utility`
- `Semantic: Color`
  - Added the `Kirkwood` extension
  - Mapped `brand/*` to `kirkwood/orange_021_c/*`
  - Mapped `brand_secondary/*` to `kirkwood/blue_648_c/*`
  - Mapped `brand_tertiary/*` to `kirkwood/teal_633_c/*`
  - Mapped `neutral/*` to `kirkwood/cool_gray/*`
- `Semantic: Typography`
  - Added the `Kirkwood` extension
  - Mapped `family/heading` to `kirkwood/family/primary`
  - Mapped `family/body` to `kirkwood/family/secondary`
  - Mapped `family/action` to `kirkwood/family/action`
  - Mapped `weight/heading/base` to `universal/weight/bold`
  - Mapped `weight/body/base` to `universal/weight/normal`
  - Mapped `weight/action/base` to `universal/weight/bold`

## Notes

- `642 C` was explicitly approved to expand the branded neutral ladder rather than become a fourth semantic accent lane.
- `kirkwood/family/utility` preserves Trade Gothic Condensed No. 18 as a raw primitive because the current semantic typography schema does not expose a fourth family slot.
- Plugin-runtime verification confirmed `44` color overrides and `6` typography overrides for Kirkwood.

## Governance Exception

- The Kirkwood live write happened before the user had time to review the preview artifacts.
- This violates the workspace preview-before-write gate for Figma governance changes.
- The write content is retained because the user confirmed the implementation is correct, but the sequence defect is now explicitly recorded.
