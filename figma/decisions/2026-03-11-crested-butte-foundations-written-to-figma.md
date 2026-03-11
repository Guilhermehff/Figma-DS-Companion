# Crested Butte Foundations Written To Figma

Date: 2026-03-11
Status: accepted
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Context

The staged Crested Butte color and typography artifacts were approved for write into the Design System file. The approved semantic mapping differs from the original staged assumption by using `wild_red/*` for every brand semantic ladder and `beyond_black/*` for the semantic neutral ladder.

## Decision

1. Write the Crested Butte raw color ladders into `_Global: Color`:
   - `crested_butte/wild_red/*`
   - `crested_butte/beyond_black/*`
2. Write the Crested Butte raw typography family into `_Global: Typography`:
   - `crested_butte/family/primary`
3. Add the shared raw weight `universal/weight/semibold` to `_Global: Typography`.
4. Create the `Crested Butte` semantic color extension and map:
   - `neutral/*` -> `crested_butte/beyond_black/*`
   - `brand/*` -> `crested_butte/wild_red/*`
   - `brand_secondary/*` -> `crested_butte/wild_red/*`
   - `brand_tertiary/*` -> `crested_butte/wild_red/*`
5. Create the `Crested Butte` semantic typography extension and map:
   - `family/heading` -> `crested_butte/family/primary`
   - `family/body` -> `crested_butte/family/primary`
   - `family/action` -> `crested_butte/family/primary`
   - `weight/heading/base` -> `universal/weight/semibold`
   - `weight/body/base` -> `universal/weight/normal`
   - `weight/action/base` -> `universal/weight/semibold`

## Consequences

- Crested Butte is now live in the Design System file with both raw globals and semantic extensions.
- `universal/weight/semibold` is now available as a shared raw primitive for future typography reviews.
- Repo governance artifacts must track the real extension collection IDs `VariableCollectionId:46:393` and `VariableCollectionId:46:394` and the approved override counts.
