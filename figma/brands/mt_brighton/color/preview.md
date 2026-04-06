# Mt. Brighton Color Preview

Review state: written in figma. Verify live write state in `figma/brands/mt_brighton/brand.yml` and Figma.

## Original Source Swatches

- Source color: `PMS 268C`
  Provided value: `#4f2683`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 78 38 131.

- Source color: `PMS 2617U`
  Provided value: `#735488`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 115 84 136.

- Source color: `Grey`
  Provided value: `#58595b`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 88 89 91.

## Universal Reuse

- No exact Mt. Brighton source swatch reuses an existing universal color primitive in this pass.

## Proposed Families

### Family: brighton_purple

Source anchor: `500_source`

<div>
  <span title="100 #f5f1fa" style="display:inline-block;width:32px;height:32px;background:#f5f1fa;border:1px solid #d1d5db;"></span>
  <span title="200 #e7ddf3" style="display:inline-block;width:32px;height:32px;background:#e7ddf3;border:1px solid #d1d5db;"></span>
  <span title="300 #b095d3" style="display:inline-block;width:32px;height:32px;background:#b095d3;border:1px solid #d1d5db;"></span>
  <span title="400 #8f6dbb" style="display:inline-block;width:32px;height:32px;background:#8f6dbb;border:1px solid #d1d5db;"></span>
  <span title="500 #4f2683" style="display:inline-block;width:32px;height:32px;background:#4f2683;border:1px solid #d1d5db;"></span>
  <span title="600 #41206d" style="display:inline-block;width:32px;height:32px;background:#41206d;border:1px solid #d1d5db;"></span>
  <span title="700 #321957" style="display:inline-block;width:32px;height:32px;background:#321957;border:1px solid #d1d5db;"></span>
  <span title="800 #241241" style="display:inline-block;width:32px;height:32px;background:#241241;border:1px solid #d1d5db;"></span>
  <span title="900 #0e071b" style="display:inline-block;width:32px;height:32px;background:#0e071b;border:1px solid #d1d5db;"></span>
</div>

### Family: brighton_purple_alt

Source anchor: `500_source`

<div>
  <span title="100 #f6f2fa" style="display:inline-block;width:32px;height:32px;background:#f6f2fa;border:1px solid #d1d5db;"></span>
  <span title="200 #e9e0f2" style="display:inline-block;width:32px;height:32px;background:#e9e0f2;border:1px solid #d1d5db;"></span>
  <span title="300 #b79fcc" style="display:inline-block;width:32px;height:32px;background:#b79fcc;border:1px solid #d1d5db;"></span>
  <span title="400 #9a79b2" style="display:inline-block;width:32px;height:32px;background:#9a79b2;border:1px solid #d1d5db;"></span>
  <span title="500 #735488" style="display:inline-block;width:32px;height:32px;background:#735488;border:1px solid #d1d5db;"></span>
  <span title="600 #5c4270" style="display:inline-block;width:32px;height:32px;background:#5c4270;border:1px solid #d1d5db;"></span>
  <span title="700 #453258" style="display:inline-block;width:32px;height:32px;background:#453258;border:1px solid #d1d5db;"></span>
  <span title="800 #312440" style="display:inline-block;width:32px;height:32px;background:#312440;border:1px solid #d1d5db;"></span>
  <span title="900 #120c18" style="display:inline-block;width:32px;height:32px;background:#120c18;border:1px solid #d1d5db;"></span>
</div>

### Family: brighton_grey

Source anchor: `500_source`

<div>
  <span title="100 #f5f6f8" style="display:inline-block;width:32px;height:32px;background:#f5f6f8;border:1px solid #d1d5db;"></span>
  <span title="200 #e7e8eb" style="display:inline-block;width:32px;height:32px;background:#e7e8eb;border:1px solid #d1d5db;"></span>
  <span title="300 #a9adb4" style="display:inline-block;width:32px;height:32px;background:#a9adb4;border:1px solid #d1d5db;"></span>
  <span title="400 #838891" style="display:inline-block;width:32px;height:32px;background:#838891;border:1px solid #d1d5db;"></span>
  <span title="500 #58595b" style="display:inline-block;width:32px;height:32px;background:#58595b;border:1px solid #d1d5db;"></span>
  <span title="600 #45464a" style="display:inline-block;width:32px;height:32px;background:#45464a;border:1px solid #d1d5db;"></span>
  <span title="700 #313236" style="display:inline-block;width:32px;height:32px;background:#313236;border:1px solid #d1d5db;"></span>
  <span title="800 #212226" style="display:inline-block;width:32px;height:32px;background:#212226;border:1px solid #d1d5db;"></span>
  <span title="900 #0c0d10" style="display:inline-block;width:32px;height:32px;background:#0c0d10;border:1px solid #d1d5db;"></span>
</div>

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `mt_brighton/brighton_grey`
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `mt_brighton/brighton_purple`
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `mt_brighton/brighton_purple_alt`
- `variables/assets/logo` -> `Mt. Brighton`
  The semantic color extension stores the governed display label.

## Review Readiness

- Subject: `Mt. Brighton lane order`
  Channels: `web, email, ads`
  Rule: Keep the darker purple on the primary expressive lane and the lighter purple on the supporting lane.
  Source basis: The logo sheet presents the darker purple as the dominant brand color.
