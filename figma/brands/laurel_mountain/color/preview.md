# Laurel Mountain Color Preview

Review state: written in figma. Verify live write state in `figma/brands/laurel_mountain/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Red`
  Provided value: `#cf463c`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 207 70 60.

- Source color: `Dark Blue`
  Provided value: `#363745`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 54 55 69.

- Source color: `Light Blue`
  Provided value: `#52799c`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 82 121 156.

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `shared neutral`
  Notes: Exact shared black.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `shared neutral`
  Notes: Exact shared white.

## Universal Reuse

- Source color: `Black`
  Proposed token: `universal/black`
  Notes: Exact shared black.

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact shared white.

## Proposed Families

### Family: red

Source anchor: `500_source`

<div>
  <span title="100 #fdf3f2" style="display:inline-block;width:32px;height:32px;background:#fdf3f2;border:1px solid #d1d5db;"></span>
  <span title="200 #f9e1de" style="display:inline-block;width:32px;height:32px;background:#f9e1de;border:1px solid #d1d5db;"></span>
  <span title="300 #e99a93" style="display:inline-block;width:32px;height:32px;background:#e99a93;border:1px solid #d1d5db;"></span>
  <span title="400 #de6f66" style="display:inline-block;width:32px;height:32px;background:#de6f66;border:1px solid #d1d5db;"></span>
  <span title="500 #cf463c" style="display:inline-block;width:32px;height:32px;background:#cf463c;border:1px solid #d1d5db;"></span>
  <span title="600 #b7372e" style="display:inline-block;width:32px;height:32px;background:#b7372e;border:1px solid #d1d5db;"></span>
  <span title="700 #922c25" style="display:inline-block;width:32px;height:32px;background:#922c25;border:1px solid #d1d5db;"></span>
  <span title="800 #6e211c" style="display:inline-block;width:32px;height:32px;background:#6e211c;border:1px solid #d1d5db;"></span>
  <span title="900 #2b0c0a" style="display:inline-block;width:32px;height:32px;background:#2b0c0a;border:1px solid #d1d5db;"></span>
</div>

### Family: blue

Source anchor: `light_blue_500_source + dark_blue_900_source`

- laurel_mountain/blue/500 preserves the Light Blue source swatch.
- laurel_mountain/blue/900 preserves the Dark Blue source swatch.
- The reviewed ladder redesigns the surrounding steps to keep a smoother blue hue progression than the initial reuse-only merge.

<div>
  <span title="100 #f2f6fa" style="display:inline-block;width:32px;height:32px;background:#f2f6fa;border:1px solid #d1d5db;"></span>
  <span title="200 #e2eaf1" style="display:inline-block;width:32px;height:32px;background:#e2eaf1;border:1px solid #d1d5db;"></span>
  <span title="300 #aec0d1" style="display:inline-block;width:32px;height:32px;background:#aec0d1;border:1px solid #d1d5db;"></span>
  <span title="400 #819db8" style="display:inline-block;width:32px;height:32px;background:#819db8;border:1px solid #d1d5db;"></span>
  <span title="500 #52799c" style="display:inline-block;width:32px;height:32px;background:#52799c;border:1px solid #d1d5db;"></span>
  <span title="600 #4f6582" style="display:inline-block;width:32px;height:32px;background:#4f6582;border:1px solid #d1d5db;"></span>
  <span title="700 #4b566c" style="display:inline-block;width:32px;height:32px;background:#4b566c;border:1px solid #d1d5db;"></span>
  <span title="800 #404559" style="display:inline-block;width:32px;height:32px;background:#404559;border:1px solid #d1d5db;"></span>
  <span title="900 #363745" style="display:inline-block;width:32px;height:32px;background:#363745;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- The live reduction keeps one `blue` family for Laurel Mountain and redesigns the ladder after the initial reuse-only merge.
- The governed source anchors remain exact at `laurel_mountain/blue/500` for Light Blue and `laurel_mountain/blue/900` for Dark Blue.
- The redesigned intermediate steps keep the family on a more consistent blue hue axis across the scale.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `laurel_mountain/blue`
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `laurel_mountain/red`
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `laurel_mountain/blue`
- `variables/assets/logo` -> `Laurel Mountain`
  The semantic color extension stores the governed display label.

## Review Readiness

- Subject: `Laurel Mountain blue ramp redesign`
  Channels: `web, email, ads`
  Rule: Use one `blue` family. Preserve Light Blue at `blue/500`, preserve Dark Blue at `blue/900`, and redesign the surrounding steps for a smoother hue progression.
  Source basis: The reviewed ladder keeps both source swatches exact while replacing the visible seams from the initial reuse-only merge.
