# Breckenridge Color Preview

Review state: written in figma. Verify live write state in `figma/brands/breckenridge/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Breckenridge Navy`
  Provided value: `#004c80`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 0 76 128 and CMYK 90 50 0 40.

- Source color: `Breckenridge Red`
  Provided value: `#d71920`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 204 0 0 and CMYK 0 100 100 0, but the HEX shown in the source is

- Source color: `Breckenridge White`
  Provided value: `#ffffff`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 255 255 255 and CMYK 0 0 0 0.

- Source color: `Breckenridge Dark Gray`
  Provided value: `#444339`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 68 67 57 and CMYK 16 14 31 82.

## Universal Reuse

- Source color: `Breckenridge White`
  Proposed token: `universal/white`
  Notes: Exact match to the existing universal primitive.

## Color Proportion Guidance

Source basis: Approximate ratios inferred from the relative bar widths in the user-provided Breckenridge guide image. The source does not publish exact percentages.

### Brand Touchpoints

- Intent: `Navy is the dominant brand field, red is the secondary expressive lane, white provides open space, and dark_gray remains a restrained supporting neutral.`
- Proportions:
  `Breckenridge Navy` -> `breckenridge/navy/800` (`35%`) Longest bar in the source image and the primary brand color.
  `Breckenridge Red` -> `breckenridge/red/600` (`30%`) Second-longest bar in the source image and the key secondary expressive color.
  `Breckenridge White` -> `universal/white` (`20%`) Third bar in the source image and the primary open-space carrier.
  `Breckenridge Dark Gray` -> `breckenridge/dark_gray/800` (`15%`) Shortest bar in the source image and a supporting neutral rather than a leading brand lane.
- Notes:
  These percentages are documentation guidance inferred from the source artwork, not exact measured source values.
  This guidance informs composition and emphasis, not the governed token ramp values.

## Proposed Families

### Family: navy

Source anchor: `800_source`

<div>
  <span title="100 #f0fcff" style="display:inline-block;width:32px;height:32px;background:#f0fcff;border:1px solid #d1d5db;"></span>
  <span title="200 #e2f2ff" style="display:inline-block;width:32px;height:32px;background:#e2f2ff;border:1px solid #d1d5db;"></span>
  <span title="300 #b1d0ee" style="display:inline-block;width:32px;height:32px;background:#b1d0ee;border:1px solid #d1d5db;"></span>
  <span title="400 #8cb6de" style="display:inline-block;width:32px;height:32px;background:#8cb6de;border:1px solid #d1d5db;"></span>
  <span title="500 #6396c4" style="display:inline-block;width:32px;height:32px;background:#6396c4;border:1px solid #d1d5db;"></span>
  <span title="600 #3c77ac" style="display:inline-block;width:32px;height:32px;background:#3c77ac;border:1px solid #d1d5db;"></span>
  <span title="700 #195b91" style="display:inline-block;width:32px;height:32px;background:#195b91;border:1px solid #d1d5db;"></span>
  <span title="800 #004c80" style="display:inline-block;width:32px;height:32px;background:#004c80;border:1px solid #d1d5db;"></span>
  <span title="900 #001730" style="display:inline-block;width:32px;height:32px;background:#001730;border:1px solid #d1d5db;"></span>
</div>

### Family: red

Source anchor: `600_source`

<div>
  <span title="100 #fff1ec" style="display:inline-block;width:32px;height:32px;background:#fff1ec;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe1da" style="display:inline-block;width:32px;height:32px;background:#ffe1da;border:1px solid #d1d5db;"></span>
  <span title="300 #ffa699" style="display:inline-block;width:32px;height:32px;background:#ffa699;border:1px solid #d1d5db;"></span>
  <span title="400 #ff786c" style="display:inline-block;width:32px;height:32px;background:#ff786c;border:1px solid #d1d5db;"></span>
  <span title="500 #fa453f" style="display:inline-block;width:32px;height:32px;background:#fa453f;border:1px solid #d1d5db;"></span>
  <span title="600 #d71920" style="display:inline-block;width:32px;height:32px;background:#d71920;border:1px solid #d1d5db;"></span>
  <span title="700 #ac0003" style="display:inline-block;width:32px;height:32px;background:#ac0003;border:1px solid #d1d5db;"></span>
  <span title="800 #830000" style="display:inline-block;width:32px;height:32px;background:#830000;border:1px solid #d1d5db;"></span>
  <span title="900 #350000" style="display:inline-block;width:32px;height:32px;background:#350000;border:1px solid #d1d5db;"></span>
</div>

### Family: dark_gray

Source anchor: `800_source`

<div>
  <span title="100 #fafaf7" style="display:inline-block;width:32px;height:32px;background:#fafaf7;border:1px solid #d1d5db;"></span>
  <span title="200 #f1f0ec" style="display:inline-block;width:32px;height:32px;background:#f1f0ec;border:1px solid #d1d5db;"></span>
  <span title="300 #cdcdc4" style="display:inline-block;width:32px;height:32px;background:#cdcdc4;border:1px solid #d1d5db;"></span>
  <span title="400 #b2b2a8" style="display:inline-block;width:32px;height:32px;background:#b2b2a8;border:1px solid #d1d5db;"></span>
  <span title="500 #929186" style="display:inline-block;width:32px;height:32px;background:#929186;border:1px solid #d1d5db;"></span>
  <span title="600 #757469" style="display:inline-block;width:32px;height:32px;background:#757469;border:1px solid #d1d5db;"></span>
  <span title="700 #59594f" style="display:inline-block;width:32px;height:32px;background:#59594f;border:1px solid #d1d5db;"></span>
  <span title="800 #444339" style="display:inline-block;width:32px;height:32px;background:#444339;border:1px solid #d1d5db;"></span>
  <span title="900 #171611" style="display:inline-block;width:32px;height:32px;background:#171611;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Navy and dark_gray both anchor at 800 because the provided source values sit in the dark-brand range while still leaving room for 900 and 950 white-contrast steps.
- Red anchors at 600 because the provided source value behaves as a saturated mid-dark brand accent rather than an extreme dark tone.
- White is reused from the universal palette and is not duplicated under the Breckenridge brand group.

## Review Readiness

- Subject: `Breckenridge White`
  Channels: `web, email, ads`
  Rule: Reuse universal/white instead of creating a duplicated brand white.
  Source basis: Source lists white inside the primary palette and the provided HEX is an exact universal match.

- Subject: `Breckenridge Navy, Red, and Dark Gray`
  Channels: `web, email, ads`
  Rule: Treat navy and red as the primary Breckenridge brand ladders, feed dark_gray into semantic neutral, and avoid using dark_gray as the tertiary brand ladder.
  Source basis: Source image labels these colors as the primary Breckenridge palette used to keep brand work consistent across touchpoints.
