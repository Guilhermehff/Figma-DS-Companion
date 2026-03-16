# Initial Semantic Color Family Model

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
Superseded by: figma/decisions/2026-03-13-proposed-semantic-role-channel-color-model.md

## Context

Semantic Typography now has a governed baseline. Semantic Color is the next layer to define.

The current governed color inventory includes:

- universal neutrals in `_Global: Color` under `universal/slate/*`
- a universal accent family under `universal/cyan/*`
- exact primitives `universal/white` and `universal/black`
- reviewed Vail families under `vail/digital_blue/*`, `vail/navy/*`, and `vail/yellow/*`

The taxonomy already shows examples such as `neutral/50`, `gray/50`, and `blue/600`, but it did not yet resolve which semantic family model should be used for cross-brand color ladders.

## Ambiguity

The semantic color layer needs a stable family model before any aliases are written into Figma.

## Options

1. Use hue-normalized semantic families.
   - Example: `neutral/50`, `cyan/500`, `blue/600`, `yellow/300`
   - Tradeoff: closest to raw families and current taxonomy examples, but weak as a shared cross-brand schema because not every brand will expose the same hue set.
2. Use palette-slot semantic families.
   - Example: `neutral/50`, `brand/500`, `brand_secondary/700`, `accent/300`
   - Tradeoff: stronger cross-brand stability and still lighter than channel meaning, but more interpretive and dependent on a governed slot list.
3. Use a conservative palette-slot baseline first.
   - Example: `neutral/50-950`, `brand/50-950`, `brand_secondary/50-950`, and `brand_tertiary/50-950`
   - Tradeoff: keeps a stable cross-brand slot schema in place now while still deferring any extra slot families beyond the primary, secondary, and tertiary brand ladder.

## Recommended Direction

Use option 3.

Start Semantic: Color with the smallest stable cross-brand baseline that is justified by the current governed inventory and expected future brand needs:

1. `neutral/*` aliases `universal/slate/*` in the base `Semantic: Color` collection.
2. `brand/*`, `brand_secondary/*`, and `brand_tertiary/*` all exist in the base `Semantic: Color` collection on the full `50-950` ladder.
3. In the shared base collection, the three brand-facing ladders may point to the same universal raw family until more distinct shared universal baselines are approved.
4. Brand extensions override only the tokens that materially differ from the universal baseline.
5. If a brand does not define secondary or tertiary brand colors, its extension maps `brand_secondary/*` and `brand_tertiary/*` to the same raw family used by `brand/*`.
6. Raw brand families that do not yet have a stable shared slot stay in `_Global: Color` until another approved decision adds that slot.

## Consequences

- The first Semantic: Color write should create the base `neutral/*`, `brand/*`, `brand_secondary/*`, and `brand_tertiary/*` ladders.
- The current Vail color extension should override `brand/*` to `vail/digital_blue/*`, `brand_secondary/*` to `vail/navy/*`, and `brand_tertiary/*` to `vail/yellow/*`.
- Other brands that do not yet define distinct secondary or tertiary families may still map those semantic slots back to the primary brand family until their brand-color review adds more approved families.
- The live Figma file now uses a second bare `Vail` extension collection for `Semantic: Color`, parallel to the existing `Vail` extension for `Semantic: Typography`. In practice, extension display names may repeat across semantic categories and are differentiated by their parent collection.
