# Kirkwood Color Preview

Review state: written in figma. Verify live write state in `figma/brands/kirkwood/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Black C`
  Provided value: `#000000`
  Usage scope: `foundational palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `0 0 0 100` and HEX `#000000`.

- Source color: `Cool Grey 9`
  Provided value: `#6d6e70`
  Usage scope: `foundational palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `0 0 0 70` and HEX `#6D6E70`.

- Source color: `Cool Grey 1`
  Provided value: `#f1f1f2`
  Usage scope: `foundational palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `0 0 0 5` and HEX `#F1F1F2`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `foundational palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `0 0 0 0` and HEX `#FFFFFF`.

- Source color: `Orange 021 C`
  Provided value: `#f15a2b`
  Usage scope: `accent palette`
  Channel restrictions: `used as highlight in source note`
  Notes: Source image lists CMYK `0 80 93 0` and HEX `#F15A2B`.

- Source color: `648 C`
  Provided value: `#004c69`
  Usage scope: `accent palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `87 42 20 47` and HEX `#004C69`.

- Source color: `633 C`
  Provided value: `#0f758b`
  Usage scope: `accent palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `87 42 36 7` and HEX `#0F758B`.

- Source color: `642 C`
  Provided value: `#d0e2e9`
  Usage scope: `accent palette approved for neutral-support use`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK `17 8 7 1` and HEX `#D0E2E9`.

## Universal Reuse

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact match to the existing universal white primitive.

- Source color: `Black C`
  Proposed token: `universal/black`
  Notes: Exact match to the existing universal black primitive.

## Color Proportion Guidance

Source basis: The supplied Kirkwood visual-guidelines page states that black, white, and gray should dominate the design when blue tones are already present through outdoor photography, and that orange should be used as the highlight. The adjacent pie chart describes content distribution rather than a direct color percentage table.

### Outdoor Photography Compositions

- Intent: `Foundational neutrals dominate. Orange 021 C stays as the main highlight color. The blue accents should usually arrive through photography or smaller supporting moments rather than as the leading solid field.`
- Dominant palette:
  `White` -> `universal/white`
  `Cool Grey 1` -> `kirkwood/cool_gray/300`
  `Cool Grey 9` -> `kirkwood/cool_gray/700`
  `Black C` -> `universal/black`
- Supporting palette:
  `Orange 021 C` -> `kirkwood/orange_021_c/500`
  `648 C` -> `kirkwood/blue_648_c/800`
  `633 C` -> `kirkwood/teal_633_c/600`
  `642 C` -> `kirkwood/cool_gray/200`
- Notes:
  The source explicitly says orange is used as the highlight.
  The source explicitly says the palette blues often occur naturally in outdoor photography.

## Proposed Families

### Family: orange_021_c

Source anchor: `500_source`

<div>
  <span title="100 #fff4ef" style="display:inline-block;width:32px;height:32px;background:#fff4ef;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe4d7" style="display:inline-block;width:32px;height:32px;background:#ffe4d7;border:1px solid #d1d5db;"></span>
  <span title="300 #ffae92" style="display:inline-block;width:32px;height:32px;background:#ffae92;border:1px solid #d1d5db;"></span>
  <span title="400 #ff8561" style="display:inline-block;width:32px;height:32px;background:#ff8561;border:1px solid #d1d5db;"></span>
  <span title="500 #f15a2b" style="display:inline-block;width:32px;height:32px;background:#f15a2b;border:1px solid #d1d5db;"></span>
  <span title="600 #c34c28" style="display:inline-block;width:32px;height:32px;background:#c34c28;border:1px solid #d1d5db;"></span>
  <span title="700 #9c381a" style="display:inline-block;width:32px;height:32px;background:#9c381a;border:1px solid #d1d5db;"></span>
  <span title="800 #742a13" style="display:inline-block;width:32px;height:32px;background:#742a13;border:1px solid #d1d5db;"></span>
  <span title="900 #2e1109" style="display:inline-block;width:32px;height:32px;background:#2e1109;border:1px solid #d1d5db;"></span>
</div>

### Family: blue_648_c

Source anchor: `800_source`

<div>
  <span title="100 #f2fafe" style="display:inline-block;width:32px;height:32px;background:#f2fafe;border:1px solid #d1d5db;"></span>
  <span title="200 #e2f1fa" style="display:inline-block;width:32px;height:32px;background:#e2f1fa;border:1px solid #d1d5db;"></span>
  <span title="300 #abd1e6" style="display:inline-block;width:32px;height:32px;background:#abd1e6;border:1px solid #d1d5db;"></span>
  <span title="400 #87b9d4" style="display:inline-block;width:32px;height:32px;background:#87b9d4;border:1px solid #d1d5db;"></span>
  <span title="500 #67a1bf" style="display:inline-block;width:32px;height:32px;background:#67a1bf;border:1px solid #d1d5db;"></span>
  <span title="600 #4689ab" style="display:inline-block;width:32px;height:32px;background:#4689ab;border:1px solid #d1d5db;"></span>
  <span title="700 #277194" style="display:inline-block;width:32px;height:32px;background:#277194;border:1px solid #d1d5db;"></span>
  <span title="800 #004c69" style="display:inline-block;width:32px;height:32px;background:#004c69;border:1px solid #d1d5db;"></span>
  <span title="900 #011925" style="display:inline-block;width:32px;height:32px;background:#011925;border:1px solid #d1d5db;"></span>
</div>

### Family: teal_633_c

Source anchor: `600_source`

<div>
  <span title="100 #eefbff" style="display:inline-block;width:32px;height:32px;background:#eefbff;border:1px solid #d1d5db;"></span>
  <span title="200 #d5f5fe" style="display:inline-block;width:32px;height:32px;background:#d5f5fe;border:1px solid #d1d5db;"></span>
  <span title="300 #83d9f1" style="display:inline-block;width:32px;height:32px;background:#83d9f1;border:1px solid #d1d5db;"></span>
  <span title="400 #4fc2df" style="display:inline-block;width:32px;height:32px;background:#4fc2df;border:1px solid #d1d5db;"></span>
  <span title="500 #01a6c6" style="display:inline-block;width:32px;height:32px;background:#01a6c6;border:1px solid #d1d5db;"></span>
  <span title="600 #0f758b" style="display:inline-block;width:32px;height:32px;background:#0f758b;border:1px solid #d1d5db;"></span>
  <span title="700 #00617a" style="display:inline-block;width:32px;height:32px;background:#00617a;border:1px solid #d1d5db;"></span>
  <span title="800 #004659" style="display:inline-block;width:32px;height:32px;background:#004659;border:1px solid #d1d5db;"></span>
  <span title="900 #001a22" style="display:inline-block;width:32px;height:32px;background:#001a22;border:1px solid #d1d5db;"></span>
</div>

### Family: cool_gray

Source anchor: `300_source`

<div>
  <span title="100 #ffffff" style="display:inline-block;width:32px;height:32px;background:#ffffff;border:1px solid #d1d5db;"></span>
  <span title="200 #f1f1f2" style="display:inline-block;width:32px;height:32px;background:#f1f1f2;border:1px solid #d1d5db;"></span>
  <span title="300 #d0e2e9" style="display:inline-block;width:32px;height:32px;background:#d0e2e9;border:1px solid #d1d5db;"></span>
  <span title="400 #b6c4c9" style="display:inline-block;width:32px;height:32px;background:#b6c4c9;border:1px solid #d1d5db;"></span>
  <span title="500 #9da6ab" style="display:inline-block;width:32px;height:32px;background:#9da6ab;border:1px solid #d1d5db;"></span>
  <span title="600 #858a8d" style="display:inline-block;width:32px;height:32px;background:#858a8d;border:1px solid #d1d5db;"></span>
  <span title="700 #6d6e70" style="display:inline-block;width:32px;height:32px;background:#6d6e70;border:1px solid #d1d5db;"></span>
  <span title="800 #48494b" style="display:inline-block;width:32px;height:32px;background:#48494b;border:1px solid #d1d5db;"></span>
  <span title="900 #000000" style="display:inline-block;width:32px;height:32px;background:#000000;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Orange 021 C lands at `500` because the supplied swatch behaves as a vivid mid-tone highlight rather than a dark foundation color.
- `648 C` lands at `800` because the supplied swatch is already a deep, high-contrast accent in the source palette.
- `633 C` lands at `600` because it reads as a darker mid-tone support accent rather than a pale highlight.
- The approved Kirkwood neutral family absorbs `642 C` at `300` and keeps exact source anchors at `50`, `100`, `300`, `700`, and `950`.

## Review Readiness

- Subject: `Kirkwood branded neutral ladder`
  Channels: `web, email, ads`
  Rule: Treat `642 C` as a neutral-support source value inside `kirkwood/cool_gray/*`, not as a fourth semantic accent family.
  Source basis: User approval in chat plus the foundational palette image.

- Subject: `Kirkwood accent slot mapping`
  Channels: `web, email, ads`
  Rule: Use Orange 021 C as `brand/*`, 648 C as `brand_secondary/*`, and keep 633 C as a global-only family.
  Source basis: The supplied palette image and approved semantic mapping choice.
