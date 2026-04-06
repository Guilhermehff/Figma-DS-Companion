# Wilmot Color Preview

Review state: written in figma. Verify live write state in `figma/brands/wilmot/brand.yml` and Figma.

## Original Source Swatches

- Source color: `PMS 201C`
  Provided value: `#a42036`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 163 33 54.

- Source color: `PMS 704U`
  Provided value: `#a5565f`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 165 86 95.

- Source color: `Grey`
  Provided value: `#58595b`
  Usage scope: `core brand color`
  Notes: Source image lists RGB 88 89 91.

## Universal Reuse

- No exact Wilmot source swatch reuses an existing universal color primitive in this pass.

## Proposed Families

### Family: wilmot_red

Source anchor: `600_source`

<div>
  <span title="100 #fbedee" style="display:inline-block;width:32px;height:32px;background:#fbedee;border:1px solid #d1d5db;"></span>
  <span title="200 #f5d7d9" style="display:inline-block;width:32px;height:32px;background:#f5d7d9;border:1px solid #d1d5db;"></span>
  <span title="300 #e48389" style="display:inline-block;width:32px;height:32px;background:#e48389;border:1px solid #d1d5db;"></span>
  <span title="400 #d95c63" style="display:inline-block;width:32px;height:32px;background:#d95c63;border:1px solid #d1d5db;"></span>
  <span title="500 #c73f4a" style="display:inline-block;width:32px;height:32px;background:#c73f4a;border:1px solid #d1d5db;"></span>
  <span title="600 #a42036" style="display:inline-block;width:32px;height:32px;background:#a42036;border:1px solid #d1d5db;"></span>
  <span title="700 #851a2c" style="display:inline-block;width:32px;height:32px;background:#851a2c;border:1px solid #d1d5db;"></span>
  <span title="800 #671423" style="display:inline-block;width:32px;height:32px;background:#671423;border:1px solid #d1d5db;"></span>
  <span title="900 #320912" style="display:inline-block;width:32px;height:32px;background:#320912;border:1px solid #d1d5db;"></span>
</div>

### Family: wilmot_rose

Source anchor: `600_source`

<div>
  <span title="100 #fbeff0" style="display:inline-block;width:32px;height:32px;background:#fbeff0;border:1px solid #d1d5db;"></span>
  <span title="200 #f4d9db" style="display:inline-block;width:32px;height:32px;background:#f4d9db;border:1px solid #d1d5db;"></span>
  <span title="300 #d98a90" style="display:inline-block;width:32px;height:32px;background:#d98a90;border:1px solid #d1d5db;"></span>
  <span title="400 #c96770" style="display:inline-block;width:32px;height:32px;background:#c96770;border:1px solid #d1d5db;"></span>
  <span title="500 #b24e58" style="display:inline-block;width:32px;height:32px;background:#b24e58;border:1px solid #d1d5db;"></span>
  <span title="600 #a5565f" style="display:inline-block;width:32px;height:32px;background:#a5565f;border:1px solid #d1d5db;"></span>
  <span title="700 #87434b" style="display:inline-block;width:32px;height:32px;background:#87434b;border:1px solid #d1d5db;"></span>
  <span title="800 #693238" style="display:inline-block;width:32px;height:32px;background:#693238;border:1px solid #d1d5db;"></span>
  <span title="900 #34181c" style="display:inline-block;width:32px;height:32px;background:#34181c;border:1px solid #d1d5db;"></span>
</div>

### Family: wilmot_grey

Source anchor: `500_source`

<div>
  <span title="100 #f5f6f7" style="display:inline-block;width:32px;height:32px;background:#f5f6f7;border:1px solid #d1d5db;"></span>
  <span title="200 #e6e8ea" style="display:inline-block;width:32px;height:32px;background:#e6e8ea;border:1px solid #d1d5db;"></span>
  <span title="300 #a9adb4" style="display:inline-block;width:32px;height:32px;background:#a9adb4;border:1px solid #d1d5db;"></span>
  <span title="400 #838891" style="display:inline-block;width:32px;height:32px;background:#838891;border:1px solid #d1d5db;"></span>
  <span title="500 #58595b" style="display:inline-block;width:32px;height:32px;background:#58595b;border:1px solid #d1d5db;"></span>
  <span title="600 #45464a" style="display:inline-block;width:32px;height:32px;background:#45464a;border:1px solid #d1d5db;"></span>
  <span title="700 #323336" style="display:inline-block;width:32px;height:32px;background:#323336;border:1px solid #d1d5db;"></span>
  <span title="800 #242528" style="display:inline-block;width:32px;height:32px;background:#242528;border:1px solid #d1d5db;"></span>
  <span title="900 #101114" style="display:inline-block;width:32px;height:32px;background:#101114;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- User-corrected naming pass. The live namespace and extension names now use `Wilmot`, not `Wilmot Mountain`.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `wilmot/wilmot_grey`
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `wilmot/wilmot_red`
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `wilmot/wilmot_rose`
- `variables/assets/logo` -> `Wilmot`
  The semantic color extension stores the governed display label.

## Review Readiness

- Subject: `Wilmot naming`
  Channels: `web, email, ads`
  Rule: Use `Wilmot` as the governed display name across repo artifacts and live Figma extensions.
  Source basis: User correction in chat after the first pass.
