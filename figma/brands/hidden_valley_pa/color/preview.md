# Hidden Valley PA Color Preview

Review state: written in figma. Verify live write state in `figma/brands/hidden_valley_pa/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Laurel Blue`
  Provided value: `#00447c`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 0 68 124.

- Source color: `Dark Beige`
  Provided value: `#8a724e`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 138 114 78.

- Source color: `Light Beige`
  Provided value: `#e3d4b8`
  Usage scope: `core brand color`
  Notes: Source image labels this swatch tentative and lists RGB 227 212 184.

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

### Family: laurel_blue

Source anchor: `500_source`

<div>
  <span title="100 #f2f7ff" style="display:inline-block;width:32px;height:32px;background:#f2f7ff;border:1px solid #d1d5db;"></span>
  <span title="200 #e1eeff" style="display:inline-block;width:32px;height:32px;background:#e1eeff;border:1px solid #d1d5db;"></span>
  <span title="300 #8fbdf5" style="display:inline-block;width:32px;height:32px;background:#8fbdf5;border:1px solid #d1d5db;"></span>
  <span title="400 #4f93d6" style="display:inline-block;width:32px;height:32px;background:#4f93d6;border:1px solid #d1d5db;"></span>
  <span title="500 #00447c" style="display:inline-block;width:32px;height:32px;background:#00447c;border:1px solid #d1d5db;"></span>
  <span title="600 #003a6b" style="display:inline-block;width:32px;height:32px;background:#003a6b;border:1px solid #d1d5db;"></span>
  <span title="700 #003059" style="display:inline-block;width:32px;height:32px;background:#003059;border:1px solid #d1d5db;"></span>
  <span title="800 #002648" style="display:inline-block;width:32px;height:32px;background:#002648;border:1px solid #d1d5db;"></span>
  <span title="900 #001c36" style="display:inline-block;width:32px;height:32px;background:#001c36;border:1px solid #d1d5db;"></span>
</div>

### Family: beige

Source anchors: `300_source / 500_source`

- hidden_valley_pa/beige/300 preserves the Light Beige source swatch.
- hidden_valley_pa/beige/500 preserves the Dark Beige source swatch.

<div>
  <span title="100 #fbf8f2" style="display:inline-block;width:32px;height:32px;background:#fbf8f2;border:1px solid #d1d5db;"></span>
  <span title="200 #f2e7d5" style="display:inline-block;width:32px;height:32px;background:#f2e7d5;border:1px solid #d1d5db;"></span>
  <span title="300 #e3d4b8" style="display:inline-block;width:32px;height:32px;background:#e3d4b8;border:1px solid #d1d5db;"></span>
  <span title="400 #ad9670" style="display:inline-block;width:32px;height:32px;background:#ad9670;border:1px solid #d1d5db;"></span>
  <span title="500 #8a724e" style="display:inline-block;width:32px;height:32px;background:#8a724e;border:1px solid #d1d5db;"></span>
  <span title="600 #705a39" style="display:inline-block;width:32px;height:32px;background:#705a39;border:1px solid #d1d5db;"></span>
  <span title="700 #594423" style="display:inline-block;width:32px;height:32px;background:#594423;border:1px solid #d1d5db;"></span>
  <span title="800 #43300f" style="display:inline-block;width:32px;height:32px;background:#43300f;border:1px solid #d1d5db;"></span>
  <span title="900 #1b1200" style="display:inline-block;width:32px;height:32px;background:#1b1200;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- The Pennsylvania suffix is a governance distinguisher so this brand stays separate from Hidden Valley MO.
- The live reduction consolidates the former `dark_beige`, `light_beige`, and composite neutral split into one `beige` family.
- The beige ladder was redesigned after the initial consolidation so the ramp stays visually continuous while preserving both source swatches.
- `beige/300` preserves the Light Beige source swatch and `beige/500` preserves the Dark Beige source swatch.
- `beige/100` is a derived very light beige so white stays governed through `universal/white` instead of the brand ramp.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `hidden_valley_pa/beige`
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `hidden_valley_pa/laurel_blue`
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `hidden_valley_pa/beige`
- `variables/assets/logo` -> `Hidden Valley PA`
  The semantic color extension stores the governed display label.

## Review Readiness

- Subject: `Hidden Valley PA beige ramp redesign`
  Channels: `web, email, ads`
  Rule: Use one `beige` family for both structural neutral and supporting expressive roles, keep white out of the beige ramp, preserve Light Beige at `beige/300`, and preserve Dark Beige at `beige/500`.
  Source basis: The source sheet presents beige as one family, and the reviewed ramp preserves both source swatches exactly while redesigning the surrounding steps for a smoother ladder.
