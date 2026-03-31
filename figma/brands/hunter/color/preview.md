# Hunter Color Preview

Review state: written in figma. Verify live write state in `figma/brands/hunter/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Mountain Blue`
  Provided value: `#222233`
  Usage scope: `primary brand palette and foundational type/background color`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 34 34 51 and CMYK 82 77 52 61.

- Source color: `Sunrise Orange`
  Provided value: `#ea3410`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 234 52 16 and CMYK 0 78 93 8.

- Source color: `Flurry White`
  Provided value: `#faf9f3`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 250 249 243 and CMYK 1 1 4 0.

- Source color: `Snow Blue`
  Provided value: `#e7f1ff`
  Usage scope: `secondary brand palette`
  Channel restrictions: `source says secondary colors should be used as accent colors to highlight or compliment the primary colors in a campaign`
  Notes: Source image lists RGB 231 241 255 and CMYK 7 2 0 0.

- Source color: `Forest Green`
  Provided value: `#2b5d4c`
  Usage scope: `secondary brand palette`
  Channel restrictions: `source says secondary colors should be used as accent colors to highlight or compliment the primary colors in a campaign`
  Notes: Source image lists RGB 43 93 76 and CMYK 82 42 71 32.

- Source color: `City Grey`
  Provided value: `#808080`
  Usage scope: `secondary brand palette`
  Channel restrictions: `source says secondary colors should be used as accent colors to highlight or compliment the primary colors in a campaign`
  Notes: Source image lists RGB 128 128 128 and CMYK 52 43 43 0.

## Universal Reuse

- No exact Hunter source swatch reuses an existing universal color primitive in this pass.

## Color Proportion Guidance

Source basis: User-provided Hunter brand guidance defines primary versus secondary palette behavior in prose but does not publish numeric percentages.

### Campaign Work

- Intent: `Mountain Blue, Sunrise Orange, and Flurry White form the core Hunter palette for primary branding pieces, backgrounds, and type. Snow Blue, Forest Green, and City Grey remain accent colors that highlight or complement the primary palette.`
- Dominant palette:
  `Mountain Blue` -> `hunter/mountain_blue/900`
  `Sunrise Orange` -> `hunter/sunrise_orange/500`
  `Flurry White` -> `hunter/hunter_neutral/200`
- Supporting palette:
  `Snow Blue` -> `hunter/mountain_blue/200`
  `Forest Green` -> `hunter/forest_green/700`
  `City Grey` -> `hunter/hunter_neutral/500`
- Notes:
  The source says the primary colors are used for primary branding pieces, backgrounds, type, and other foundational brand moments.
  The source says the secondary colors should be used as accents to highlight or complement the primary colors in a campaign.

## Proposed Families

### Family: hunter_neutral

Source anchors: `100_source / 500_source`

<div>
  <span title="100 #faf9f3" style="display:inline-block;width:32px;height:32px;background:#faf9f3;border:1px solid #d1d5db;"></span>
  <span title="200 #f0efea" style="display:inline-block;width:32px;height:32px;background:#f0efea;border:1px solid #d1d5db;"></span>
  <span title="300 #c7c7c4" style="display:inline-block;width:32px;height:32px;background:#c7c7c4;border:1px solid #d1d5db;"></span>
  <span title="400 #acacaa" style="display:inline-block;width:32px;height:32px;background:#acacaa;border:1px solid #d1d5db;"></span>
  <span title="500 #808080" style="display:inline-block;width:32px;height:32px;background:#808080;border:1px solid #d1d5db;"></span>
  <span title="600 #707071" style="display:inline-block;width:32px;height:32px;background:#707071;border:1px solid #d1d5db;"></span>
  <span title="700 #555658" style="display:inline-block;width:32px;height:32px;background:#555658;border:1px solid #d1d5db;"></span>
  <span title="800 #3d3e41" style="display:inline-block;width:32px;height:32px;background:#3d3e41;border:1px solid #d1d5db;"></span>
  <span title="900 #15171b" style="display:inline-block;width:32px;height:32px;background:#15171b;border:1px solid #d1d5db;"></span>
</div>

### Family: mountain_blue

Source anchors: `100_source / 900_source`

<div>
  <span title="100 #f2fcff" style="display:inline-block;width:32px;height:32px;background:#f2fcff;border:1px solid #d1d5db;"></span>
  <span title="200 #e7f1ff" style="display:inline-block;width:32px;height:32px;background:#e7f1ff;border:1px solid #d1d5db;"></span>
  <span title="300 #bfc7d7" style="display:inline-block;width:32px;height:32px;background:#bfc7d7;border:1px solid #d1d5db;"></span>
  <span title="400 #a5acbd" style="display:inline-block;width:32px;height:32px;background:#a5acbd;border:1px solid #d1d5db;"></span>
  <span title="500 #878d9e" style="display:inline-block;width:32px;height:32px;background:#878d9e;border:1px solid #d1d5db;"></span>
  <span title="600 #6b7081" style="display:inline-block;width:32px;height:32px;background:#6b7081;border:1px solid #d1d5db;"></span>
  <span title="700 #525567" style="display:inline-block;width:32px;height:32px;background:#525567;border:1px solid #d1d5db;"></span>
  <span title="800 #3b3d4e" style="display:inline-block;width:32px;height:32px;background:#3b3d4e;border:1px solid #d1d5db;"></span>
  <span title="900 #222233" style="display:inline-block;width:32px;height:32px;background:#222233;border:1px solid #d1d5db;"></span>
</div>

### Family: sunrise_orange

Source anchor: `500_source`

<div>
  <span title="100 #ffece0" style="display:inline-block;width:32px;height:32px;background:#ffece0;border:1px solid #d1d5db;"></span>
  <span title="200 #ffddcf" style="display:inline-block;width:32px;height:32px;background:#ffddcf;border:1px solid #d1d5db;"></span>
  <span title="300 #ffa58c" style="display:inline-block;width:32px;height:32px;background:#ffa58c;border:1px solid #d1d5db;"></span>
  <span title="400 #ff7c60" style="display:inline-block;width:32px;height:32px;background:#ff7c60;border:1px solid #d1d5db;"></span>
  <span title="500 #ea3410" style="display:inline-block;width:32px;height:32px;background:#ea3410;border:1px solid #d1d5db;"></span>
  <span title="600 #cc3013" style="display:inline-block;width:32px;height:32px;background:#cc3013;border:1px solid #d1d5db;"></span>
  <span title="700 #a21c01" style="display:inline-block;width:32px;height:32px;background:#a21c01;border:1px solid #d1d5db;"></span>
  <span title="800 #7b0800" style="display:inline-block;width:32px;height:32px;background:#7b0800;border:1px solid #d1d5db;"></span>
  <span title="900 #3a0000" style="display:inline-block;width:32px;height:32px;background:#3a0000;border:1px solid #d1d5db;"></span>
</div>

### Family: forest_green

Source anchor: `700_source`

<div>
  <span title="100 #f0fef8" style="display:inline-block;width:32px;height:32px;background:#f0fef8;border:1px solid #d1d5db;"></span>
  <span title="200 #e4f5ee" style="display:inline-block;width:32px;height:32px;background:#e4f5ee;border:1px solid #d1d5db;"></span>
  <span title="300 #b7d4c8" style="display:inline-block;width:32px;height:32px;background:#b7d4c8;border:1px solid #d1d5db;"></span>
  <span title="400 #98baac" style="display:inline-block;width:32px;height:32px;background:#98baac;border:1px solid #d1d5db;"></span>
  <span title="500 #749b8c" style="display:inline-block;width:32px;height:32px;background:#749b8c;border:1px solid #d1d5db;"></span>
  <span title="600 #527e6d" style="display:inline-block;width:32px;height:32px;background:#527e6d;border:1px solid #d1d5db;"></span>
  <span title="700 #2b5d4c" style="display:inline-block;width:32px;height:32px;background:#2b5d4c;border:1px solid #d1d5db;"></span>
  <span title="800 #22483b" style="display:inline-block;width:32px;height:32px;background:#22483b;border:1px solid #d1d5db;"></span>
  <span title="900 #061a14" style="display:inline-block;width:32px;height:32px;background:#061a14;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- User-approved live write. Flurry White and City Grey now stage as the structural neutral family, keeping the neutral lane separate from the expressive Hunter blue ramp.
- User-approved live write. Snow Blue and Mountain Blue now land together as the expressive `mountain_blue` family, preserving the Hunter blue identity from pale tint through dark navy emphasis.
- User-approved live write. Sunrise Orange stages as the supporting expressive lane, while Forest Green remains a governed global-only family in the first pass.
- The live semantic brand lane stages on `mountain_blue/600`, `700`, and `800`, and the live supporting expressive lane stages on `sunrise_orange/600`, `700`, and `800` so white on-surface text remains readable.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> `hunter/hunter_neutral`
  Approved live write. Flurry White and City Grey now form the structural neutral family, keeping the neutral lane separate from the expressive Hunter blue ramp.
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `hunter/mountain_blue`
  Approved live write. Snow Blue and Mountain Blue now form the primary expressive semantic brand lane, with semantic `default/strong/emphasis` staging on `600/700/800`.
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `hunter/sunrise_orange`
  Approved live write. Sunrise Orange now drives the supporting expressive semantic lane, with semantic `default/strong/emphasis` staging on `600/700/800`.
- Global-only families: `forest_green`

## Review Readiness

- Subject: `Hunter neutral and expressive split`
  Channels: `web, email, ads`
  Rule: Keep Flurry White and City Grey in the neutral lane while Snow Blue and Mountain Blue move together into the expressive blue family.
  Source basis: User-approved live write decision in chat.

- Subject: `Hunter expressive lane order`
  Channels: `web, email, ads`
  Rule: Use the blue `mountain_blue` ramp as the primary expressive lane, Sunrise Orange as the supporting expressive lane, and preserve Forest Green as global-only in the first pass.
  Source basis: User-approved live write decision in chat.
