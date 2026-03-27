# Kirkwood Color Preview

Review state: retrospective review artifact documenting the pre-review write exception. Verify live write state in `figma/brands/kirkwood/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Black C`
  Provided value: `#000000`
  Usage scope: `foundational palette`
  Notes: Source image lists CMYK `0 0 0 100`.

- Source color: `Cool Grey 9`
  Provided value: `#6d6e70`
  Usage scope: `foundational palette`
  Notes: Source image lists CMYK `0 0 0 70`.

- Source color: `Cool Grey 1`
  Provided value: `#f1f1f2`
  Usage scope: `foundational palette`
  Notes: Source image lists CMYK `0 0 0 5`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `foundational palette`
  Notes: Source image lists CMYK `0 0 0 0`.

- Source color: `Orange 021 C`
  Provided value: `#f15a2b`
  Usage scope: `accent palette`
  Notes: Source note says orange is used as the highlight.

- Source color: `648 C`
  Provided value: `#004c69`
  Usage scope: `accent palette`
  Notes: Darkest branded accent.

- Source color: `633 C`
  Provided value: `#0f758b`
  Usage scope: `accent palette`
  Notes: Mid-tone branded accent.

- Source color: `642 C`
  Provided value: `#d0e2e9`
  Usage scope: `neutral-support palette`
  Notes: Approved to expand the branded neutral ladder rather than a fourth accent slot.

## Universal Reuse

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact match.

- Source color: `Black C`
  Proposed token: `universal/black`
  Notes: Exact match, preserved inside the brand neutral ladder as the darkest anchor.

## Color Proportion Guidance

### Outdoor Photography Compositions

- Intent: Foundational neutrals dominate. `Orange 021 C` stays as the main highlight color. The blue accents should usually arrive through photography or smaller supporting moments rather than as the leading solid field.
- Dominant palette:
  `White` -> `universal/white`
  `Cool Grey 1` -> `kirkwood/cool_gray/300`
  `Cool Grey 9` -> `kirkwood/cool_gray/700`
  `Black C` -> `universal/black`
- Supporting palette:
  `Orange 021 C` -> `kirkwood/orange_021_c/500`
  `648 C` -> `kirkwood/blue_648_c/800`
  `633 C` -> `kirkwood/teal_633_c/600`
  `642 C` -> `kirkwood/cool_gray/100`
- Notes:
  The source explicitly says orange is used as the highlight.
  The source explicitly says the palette blues often occur naturally in outdoor photography.

## Proposed Families

### Family: orange_021_c

Source anchor: `500_source`

<div>
  <span title="50 #fff4ef" style="display:inline-block;width:32px;height:32px;background:#fff4ef;border:1px solid #d1d5db;"></span>
  <span title="100 #ffe4d7" style="display:inline-block;width:32px;height:32px;background:#ffe4d7;border:1px solid #d1d5db;"></span>
  <span title="200 #ffccb9" style="display:inline-block;width:32px;height:32px;background:#ffccb9;border:1px solid #d1d5db;"></span>
  <span title="300 #ffae92" style="display:inline-block;width:32px;height:32px;background:#ffae92;border:1px solid #d1d5db;"></span>
  <span title="400 #ff8561" style="display:inline-block;width:32px;height:32px;background:#ff8561;border:1px solid #d1d5db;"></span>
  <span title="500 #f15a2b" style="display:inline-block;width:32px;height:32px;background:#f15a2b;border:1px solid #d1d5db;"></span>
  <span title="600 #c34c28" style="display:inline-block;width:32px;height:32px;background:#c34c28;border:1px solid #d1d5db;"></span>
  <span title="700 #9c381a" style="display:inline-block;width:32px;height:32px;background:#9c381a;border:1px solid #d1d5db;"></span>
  <span title="800 #742a13" style="display:inline-block;width:32px;height:32px;background:#742a13;border:1px solid #d1d5db;"></span>
  <span title="900 #4e1c0d" style="display:inline-block;width:32px;height:32px;background:#4e1c0d;border:1px solid #d1d5db;"></span>
  <span title="950 #2e1109" style="display:inline-block;width:32px;height:32px;background:#2e1109;border:1px solid #d1d5db;"></span>
</div>

### Family: blue_648_c

Source anchor: `800_source`

<div>
  <span title="50 #f2fafe" style="display:inline-block;width:32px;height:32px;background:#f2fafe;border:1px solid #d1d5db;"></span>
  <span title="100 #e2f1fa" style="display:inline-block;width:32px;height:32px;background:#e2f1fa;border:1px solid #d1d5db;"></span>
  <span title="200 #cbe6f5" style="display:inline-block;width:32px;height:32px;background:#cbe6f5;border:1px solid #d1d5db;"></span>
  <span title="300 #abd1e6" style="display:inline-block;width:32px;height:32px;background:#abd1e6;border:1px solid #d1d5db;"></span>
  <span title="400 #87b9d4" style="display:inline-block;width:32px;height:32px;background:#87b9d4;border:1px solid #d1d5db;"></span>
  <span title="500 #67a1bf" style="display:inline-block;width:32px;height:32px;background:#67a1bf;border:1px solid #d1d5db;"></span>
  <span title="600 #4689ab" style="display:inline-block;width:32px;height:32px;background:#4689ab;border:1px solid #d1d5db;"></span>
  <span title="700 #277194" style="display:inline-block;width:32px;height:32px;background:#277194;border:1px solid #d1d5db;"></span>
  <span title="800 #004c69" style="display:inline-block;width:32px;height:32px;background:#004c69;border:1px solid #d1d5db;"></span>
  <span title="900 #002d41" style="display:inline-block;width:32px;height:32px;background:#002d41;border:1px solid #d1d5db;"></span>
  <span title="950 #011925" style="display:inline-block;width:32px;height:32px;background:#011925;border:1px solid #d1d5db;"></span>
</div>

### Family: teal_633_c

Source anchor: `600_source`

<div>
  <span title="50 #eefbff" style="display:inline-block;width:32px;height:32px;background:#eefbff;border:1px solid #d1d5db;"></span>
  <span title="100 #d5f5fe" style="display:inline-block;width:32px;height:32px;background:#d5f5fe;border:1px solid #d1d5db;"></span>
  <span title="200 #b5ecfc" style="display:inline-block;width:32px;height:32px;background:#b5ecfc;border:1px solid #d1d5db;"></span>
  <span title="300 #83d9f1" style="display:inline-block;width:32px;height:32px;background:#83d9f1;border:1px solid #d1d5db;"></span>
  <span title="400 #4fc2df" style="display:inline-block;width:32px;height:32px;background:#4fc2df;border:1px solid #d1d5db;"></span>
  <span title="500 #01a6c6" style="display:inline-block;width:32px;height:32px;background:#01a6c6;border:1px solid #d1d5db;"></span>
  <span title="600 #0f758b" style="display:inline-block;width:32px;height:32px;background:#0f758b;border:1px solid #d1d5db;"></span>
  <span title="700 #00617a" style="display:inline-block;width:32px;height:32px;background:#00617a;border:1px solid #d1d5db;"></span>
  <span title="800 #004659" style="display:inline-block;width:32px;height:32px;background:#004659;border:1px solid #d1d5db;"></span>
  <span title="900 #002d3a" style="display:inline-block;width:32px;height:32px;background:#002d3a;border:1px solid #d1d5db;"></span>
  <span title="950 #001a22" style="display:inline-block;width:32px;height:32px;background:#001a22;border:1px solid #d1d5db;"></span>
</div>

### Family: cool_gray

Source anchor: `300_source`

<div>
  <span title="50 #ffffff" style="display:inline-block;width:32px;height:32px;background:#ffffff;border:1px solid #d1d5db;"></span>
  <span title="100 #f1f1f2" style="display:inline-block;width:32px;height:32px;background:#f1f1f2;border:1px solid #d1d5db;"></span>
  <span title="200 #e1eaee" style="display:inline-block;width:32px;height:32px;background:#e1eaee;border:1px solid #d1d5db;"></span>
  <span title="300 #d0e2e9" style="display:inline-block;width:32px;height:32px;background:#d0e2e9;border:1px solid #d1d5db;"></span>
  <span title="400 #b6c4c9" style="display:inline-block;width:32px;height:32px;background:#b6c4c9;border:1px solid #d1d5db;"></span>
  <span title="500 #9da6ab" style="display:inline-block;width:32px;height:32px;background:#9da6ab;border:1px solid #d1d5db;"></span>
  <span title="600 #858a8d" style="display:inline-block;width:32px;height:32px;background:#858a8d;border:1px solid #d1d5db;"></span>
  <span title="700 #6d6e70" style="display:inline-block;width:32px;height:32px;background:#6d6e70;border:1px solid #d1d5db;"></span>
  <span title="800 #48494b" style="display:inline-block;width:32px;height:32px;background:#48494b;border:1px solid #d1d5db;"></span>
  <span title="900 #262728" style="display:inline-block;width:32px;height:32px;background:#262728;border:1px solid #d1d5db;"></span>
  <span title="950 #000000" style="display:inline-block;width:32px;height:32px;background:#000000;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Kirkwood now stages three semantic accent lanes and one branded neutral ladder.
- `642 C` is no longer competing for a fourth accent slot; it expands the cool-gray neutral family instead.
- White and black remain exact source anchors inside the neutral family because the palette explicitly treats them as part of the foundational system.
- Process exception: this preview artifact was reviewed after the live Figma write, not before it.

## Recommended Semantic Mapping

- `brand/*` -> `kirkwood/orange_021_c/*`
- `brand_secondary/*` -> `kirkwood/blue_648_c/*`
- `neutral/*` -> `kirkwood/cool_gray/*`
- Global-only extra families: `kirkwood/teal_633_c/*`

## Review Readiness

- Subject: `Kirkwood neutral treatment`
  Channels: `web, email, ads`
  Rule: Use the branded `cool_gray` ladder for neutral surfaces, including `642 C` as the approved pale neutral-support anchor.
  Source basis: Kirkwood foundational palette image plus approved chat decision.

- Subject: `Kirkwood accent treatment`
  Channels: `web, email, ads`
  Rule: Reserve Orange 021 C for primary highlight usage and use 648 C and 633 C as the secondary and tertiary support lanes.
  Source basis: Kirkwood foundational palette image and source note that orange is used as the highlight.
