# Paoli Peaks Color Preview

Review state: written in figma. Verify live write state in `figma/brands/paoli_peaks/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Paoli Blue`
  Provided value: `#192957`

- Source color: `Peak's Gradient`
  Provided value: `documented_gradient`

- Source color: `Peak's Peak`
  Provided value: `#d8dfe1`

- Source color: `Peak's Valley`
  Provided value: `#8fd16a`

## Universal Reuse

- Source color: `Black logo variation`
  Proposed token: `universal/black`
  Notes: Exact black remains inherited through the shared neutral baseline.

- Source color: `White logo variation`
  Proposed token: `universal/white`
  Notes: Exact white remains inherited through the shared neutral baseline.

## Proposed Families

### Family: paoli_blue

Source anchor: `800_source`

<div>
  <span title="100 #f3f6fb" style="display:inline-block;width:32px;height:32px;background:#f3f6fb;border:1px solid #d1d5db;"></span>
  <span title="200 #e3eaf4" style="display:inline-block;width:32px;height:32px;background:#e3eaf4;border:1px solid #d1d5db;"></span>
  <span title="300 #a4b6cf" style="display:inline-block;width:32px;height:32px;background:#a4b6cf;border:1px solid #d1d5db;"></span>
  <span title="400 #7f97b5" style="display:inline-block;width:32px;height:32px;background:#7f97b5;border:1px solid #d1d5db;"></span>
  <span title="500 #617a9c" style="display:inline-block;width:32px;height:32px;background:#617a9c;border:1px solid #d1d5db;"></span>
  <span title="600 #4a6283" style="display:inline-block;width:32px;height:32px;background:#4a6283;border:1px solid #d1d5db;"></span>
  <span title="700 #334a6a" style="display:inline-block;width:32px;height:32px;background:#334a6a;border:1px solid #d1d5db;"></span>
  <span title="800 #192957" style="display:inline-block;width:32px;height:32px;background:#192957;border:1px solid #d1d5db;"></span>
  <span title="900 #0e1a3a" style="display:inline-block;width:32px;height:32px;background:#0e1a3a;border:1px solid #d1d5db;"></span>
</div>

### Family: peaks_peak

Source anchor: `300_source`

<div>
  <span title="100 #f1f3f4" style="display:inline-block;width:32px;height:32px;background:#f1f3f4;border:1px solid #d1d5db;"></span>
  <span title="200 #e5eaeb" style="display:inline-block;width:32px;height:32px;background:#e5eaeb;border:1px solid #d1d5db;"></span>
  <span title="300 #d8dfe1" style="display:inline-block;width:32px;height:32px;background:#d8dfe1;border:1px solid #d1d5db;"></span>
  <span title="400 #9fa4a6" style="display:inline-block;width:32px;height:32px;background:#9fa4a6;border:1px solid #d1d5db;"></span>
  <span title="500 #868a8b" style="display:inline-block;width:32px;height:32px;background:#868a8b;border:1px solid #d1d5db;"></span>
  <span title="600 #6e7172" style="display:inline-block;width:32px;height:32px;background:#6e7172;border:1px solid #d1d5db;"></span>
  <span title="700 #565959" style="display:inline-block;width:32px;height:32px;background:#565959;border:1px solid #d1d5db;"></span>
  <span title="800 #3f4141" style="display:inline-block;width:32px;height:32px;background:#3f4141;border:1px solid #d1d5db;"></span>
  <span title="900 #111212" style="display:inline-block;width:32px;height:32px;background:#111212;border:1px solid #d1d5db;"></span>
</div>

### Family: peaks_valley

Source anchor: `500_source`

<div>
  <span title="100 #f2f8fb" style="display:inline-block;width:32px;height:32px;background:#f2f8fb;border:1px solid #d1d5db;"></span>
  <span title="200 #e2f0f5" style="display:inline-block;width:32px;height:32px;background:#e2f0f5;border:1px solid #d1d5db;"></span>
  <span title="300 #9fd0dd" style="display:inline-block;width:32px;height:32px;background:#9fd0dd;border:1px solid #d1d5db;"></span>
  <span title="400 #6ea8bd" style="display:inline-block;width:32px;height:32px;background:#6ea8bd;border:1px solid #d1d5db;"></span>
  <span title="500 #4f8fa6" style="display:inline-block;width:32px;height:32px;background:#4f8fa6;border:1px solid #d1d5db;"></span>
  <span title="600 #3c7489" style="display:inline-block;width:32px;height:32px;background:#3c7489;border:1px solid #d1d5db;"></span>
  <span title="700 #2c596a" style="display:inline-block;width:32px;height:32px;background:#2c596a;border:1px solid #d1d5db;"></span>
  <span title="800 #1f404c" style="display:inline-block;width:32px;height:32px;background:#1f404c;border:1px solid #d1d5db;"></span>
  <span title="900 #142a33" style="display:inline-block;width:32px;height:32px;background:#142a33;border:1px solid #d1d5db;"></span>
</div>

## Live Semantic Mapping

- Scope: `neutral` -> `inherited_base`
  Exact black and white remain inherited from the shared neutral baseline.
- Scope: `brand` -> `paoli_peaks/paoli_blue`
  Paoli Blue drives the primary expressive lane.
- Scope: `brand_secondary` -> `paoli_peaks/peaks_valley`
  Peak's Valley provides the most reusable supporting accent in the first pass.
- Global-only families: `paoli_peaks/peaks_peak`
- `variables/assets/logo` -> `Paoli Peaks`

## Review Readiness

- Subject: `Paoli Peaks expressive mapping`
  Rule: Use `paoli_blue` for `brand/*` and `peaks_valley` for `brand_secondary/*`.

- Subject: `Paoli Peaks gradient handling`
  Rule: Keep the documented gradient out of the current solid-color variable model and stage its supporting solids instead.
