# Heavenly Color Preview

Review state: written in figma. Verify live write state in `figma/brands/heavenly/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Fresh Powder White`
  Provided value: `#ffffff`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 255 255 255, CMYK 0 0 0 0, and HEX

- Source color: `Mountain Shadow Black`
  Provided value: `#000000`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 0 0 0, CMYK 75 68 67 90, and HEX

- Source color: `Snow Flower Red`
  Provided value: `#cb1f30`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 204 32 49, CMYK 13 100 89 4, and HEX

- Source color: `Deep Water Blue`
  Provided value: `#1e5eb9`
  Usage scope: `supporting_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 30 94 185, CMYK 88 67 0 0, and HEX

- Source color: `Shore Blue`
  Provided value: `#54c3f2`
  Usage scope: `supporting_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 84 195 242, CMYK 57 0 4 0, and HEX

## Universal Reuse

- Source color: `Fresh Powder White`
  Proposed token: `universal/white`
  Notes: Exact match to the existing universal white primitive.

- Source color: `Mountain Shadow Black`
  Proposed token: `universal/black`
  Notes: Exact match to the existing universal black primitive.

## Color Proportion Guidance

Source basis: User-provided Heavenly palette guidance defines primary and secondary color behavior in prose but does not publish numeric percentages.

### Brand Touchpoints

- Intent: `Fresh Powder White, Mountain Shadow Black, and Snow Flower Red define the primary Heavenly palette. Deep Water Blue and Shore Blue are secondary supporting colors inspired by Lake Tahoe.`
- Dominant palette:
  `Fresh Powder White` -> `universal/white`
  `Mountain Shadow Black` -> `universal/black`
  `Snow Flower Red` -> `heavenly/snow_flower_red/600`
- Supporting palette:
  `Deep Water Blue` -> `heavenly/deep_water_blue/700`
  `Shore Blue` -> `heavenly/shore_blue/300`
- Notes:
  The source says Mountain Shadow Black should be used for text and only very sparingly as a high-contrast logo color or minimal separating block.
  The source frames the blues as supporting lake-derived colors rather than primary brand fields.

## Proposed Families

### Family: snow_flower_red

Source anchor: `600_source`

<div>
  <span title="100 #fff1f3" style="display:inline-block;width:32px;height:32px;background:#fff1f3;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe0e5" style="display:inline-block;width:32px;height:32px;background:#ffe0e5;border:1px solid #d1d5db;"></span>
  <span title="300 #ff9aa8" style="display:inline-block;width:32px;height:32px;background:#ff9aa8;border:1px solid #d1d5db;"></span>
  <span title="400 #f8677c" style="display:inline-block;width:32px;height:32px;background:#f8677c;border:1px solid #d1d5db;"></span>
  <span title="500 #e33f54" style="display:inline-block;width:32px;height:32px;background:#e33f54;border:1px solid #d1d5db;"></span>
  <span title="600 #cb1f30" style="display:inline-block;width:32px;height:32px;background:#cb1f30;border:1px solid #d1d5db;"></span>
  <span title="700 #a10f21" style="display:inline-block;width:32px;height:32px;background:#a10f21;border:1px solid #d1d5db;"></span>
  <span title="800 #7b0918" style="display:inline-block;width:32px;height:32px;background:#7b0918;border:1px solid #d1d5db;"></span>
  <span title="900 #320107" style="display:inline-block;width:32px;height:32px;background:#320107;border:1px solid #d1d5db;"></span>
</div>

### Family: deep_water_blue

Source anchor: `700_source`

<div>
  <span title="100 #f2f8ff" style="display:inline-block;width:32px;height:32px;background:#f2f8ff;border:1px solid #d1d5db;"></span>
  <span title="200 #e2eeff" style="display:inline-block;width:32px;height:32px;background:#e2eeff;border:1px solid #d1d5db;"></span>
  <span title="300 #a6c6f8" style="display:inline-block;width:32px;height:32px;background:#a6c6f8;border:1px solid #d1d5db;"></span>
  <span title="400 #7ea8ea" style="display:inline-block;width:32px;height:32px;background:#7ea8ea;border:1px solid #d1d5db;"></span>
  <span title="500 #5c8ddc" style="display:inline-block;width:32px;height:32px;background:#5c8ddc;border:1px solid #d1d5db;"></span>
  <span title="600 #3c74cb" style="display:inline-block;width:32px;height:32px;background:#3c74cb;border:1px solid #d1d5db;"></span>
  <span title="700 #1e5eb9" style="display:inline-block;width:32px;height:32px;background:#1e5eb9;border:1px solid #d1d5db;"></span>
  <span title="800 #12428d" style="display:inline-block;width:32px;height:32px;background:#12428d;border:1px solid #d1d5db;"></span>
  <span title="900 #03173a" style="display:inline-block;width:32px;height:32px;background:#03173a;border:1px solid #d1d5db;"></span>
</div>

### Family: shore_blue

Source anchor: `300_source`

<div>
  <span title="100 #f1fcff" style="display:inline-block;width:32px;height:32px;background:#f1fcff;border:1px solid #d1d5db;"></span>
  <span title="200 #ddf7ff" style="display:inline-block;width:32px;height:32px;background:#ddf7ff;border:1px solid #d1d5db;"></span>
  <span title="300 #54c3f2" style="display:inline-block;width:32px;height:32px;background:#54c3f2;border:1px solid #d1d5db;"></span>
  <span title="400 #2baada" style="display:inline-block;width:32px;height:32px;background:#2baada;border:1px solid #d1d5db;"></span>
  <span title="500 #0f8fbc" style="display:inline-block;width:32px;height:32px;background:#0f8fbc;border:1px solid #d1d5db;"></span>
  <span title="600 #00729a" style="display:inline-block;width:32px;height:32px;background:#00729a;border:1px solid #d1d5db;"></span>
  <span title="700 #005979" style="display:inline-block;width:32px;height:32px;background:#005979;border:1px solid #d1d5db;"></span>
  <span title="800 #00405a" style="display:inline-block;width:32px;height:32px;background:#00405a;border:1px solid #d1d5db;"></span>
  <span title="900 #001824" style="display:inline-block;width:32px;height:32px;background:#001824;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Snow Flower Red lands at 600 because the supplied swatch behaves as a vivid mid-dark brand accent rather than an extreme dark tone.
- Deep Water Blue lands at 700 because the source value is already a dark, high-contrast support color with room for deeper white-contrast steps.
- Shore Blue lands at 300 because the supplied swatch reads as a bright highlight accent rather than a middle-value core brand tone.
- White and black are exact universal matches and should not be duplicated under the Heavenly group.

## Review Readiness

- Subject: `Heavenly white and black`
  Channels: `web, email, ads`
  Rule: Reuse universal white and universal black instead of creating duplicate Heavenly exact tokens.
  Source basis: The supplied palette matches the governed universal exact values.

- Subject: `Heavenly primary palette`
  Channels: `web, email, ads`
  Rule: Treat Snow Flower Red as the primary brand ladder, Deep Water Blue as the secondary ladder, and Shore Blue as the tertiary accent ladder unless a broader brand guide says otherwise.
  Source basis: The palette image presents these as the remaining non-neutral brand-defining colors and the typography sample visually emphasizes the red system.
