# Attitash Color Preview

Review state: written in figma. Verify live write state in `figma/brands/attitash/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Attitash Blue`
  Provided value: `#2a51a3`
  Usage scope: `core brand color`
  Notes: Source image lists PMS 2728C, RGB 42 81 163, and CMYK 93 78 0 0.

- Source color: `Daybreak`
  Provided value: `#ffc629`
  Usage scope: `core brand color`
  Notes: Source image lists PMS 1235C, RGB 255 198 41, and CMYK 0 23 91 0.

- Source color: `Pure White`
  Provided value: `#ffffff`
  Usage scope: `accent sub-palette`
  Notes: Exact shared white.

- Source color: `Mogul Shadow`
  Provided value: `#c6c8c8`
  Usage scope: `accent sub-palette`
  Notes: Source image lists PMS 420.

- Source color: `Mogul Shadow 20%`
  Provided value: `#f2f2f2`
  Usage scope: `accent sub-palette`
  Notes: Source image explicitly labels the tint as 20%.

- Source color: `Sharp Edge Grey`
  Provided value: `#3d4347`
  Usage scope: `accent sub-palette`
  Notes: Source image lists PMS 423C.

## Universal Reuse

- Source color: `Pure White`
  Proposed token: `universal/white`
  Notes: Exact shared white.

## Proposed Families

### Family: attitash_blue

Source anchor: `500_source`

<div>
  <span title="100 #f2f6ff" style="display:inline-block;width:32px;height:32px;background:#f2f6ff;border:1px solid #d1d5db;"></span>
  <span title="200 #e3ecff" style="display:inline-block;width:32px;height:32px;background:#e3ecff;border:1px solid #d1d5db;"></span>
  <span title="300 #9fb8f5" style="display:inline-block;width:32px;height:32px;background:#9fb8f5;border:1px solid #d1d5db;"></span>
  <span title="400 #6f95d6" style="display:inline-block;width:32px;height:32px;background:#6f95d6;border:1px solid #d1d5db;"></span>
  <span title="500 #2a51a3" style="display:inline-block;width:32px;height:32px;background:#2a51a3;border:1px solid #d1d5db;"></span>
  <span title="600 #14398b" style="display:inline-block;width:32px;height:32px;background:#14398b;border:1px solid #d1d5db;"></span>
  <span title="700 #012173" style="display:inline-block;width:32px;height:32px;background:#012173;border:1px solid #d1d5db;"></span>
  <span title="800 #00035c" style="display:inline-block;width:32px;height:32px;background:#00035c;border:1px solid #d1d5db;"></span>
  <span title="900 #09002f" style="display:inline-block;width:32px;height:32px;background:#09002f;border:1px solid #d1d5db;"></span>
</div>

### Family: daybreak

Source anchor: `500_source`

<div>
  <span title="100 #ede2ca" style="display:inline-block;width:32px;height:32px;background:#ede2ca;border:1px solid #d1d5db;"></span>
  <span title="200 #f1ddb2" style="display:inline-block;width:32px;height:32px;background:#f1ddb2;border:1px solid #d1d5db;"></span>
  <span title="300 #f8d27c" style="display:inline-block;width:32px;height:32px;background:#f8d27c;border:1px solid #d1d5db;"></span>
  <span title="400 #fccc5b" style="display:inline-block;width:32px;height:32px;background:#fccc5b;border:1px solid #d1d5db;"></span>
  <span title="500 #ffc629" style="display:inline-block;width:32px;height:32px;background:#ffc629;border:1px solid #d1d5db;"></span>
  <span title="600 #cb9300" style="display:inline-block;width:32px;height:32px;background:#cb9300;border:1px solid #d1d5db;"></span>
  <span title="700 #996200" style="display:inline-block;width:32px;height:32px;background:#996200;border:1px solid #d1d5db;"></span>
  <span title="800 #693200" style="display:inline-block;width:32px;height:32px;background:#693200;border:1px solid #d1d5db;"></span>
  <span title="900 #0a0200" style="display:inline-block;width:32px;height:32px;background:#0a0200;border:1px solid #d1d5db;"></span>
</div>

### Family: attitash_neutral

Source anchors: `100_source / 100_source / 300_source / 800_source`

<div>
  <span title="100 #ffffff" style="display:inline-block;width:32px;height:32px;background:#ffffff;border:1px solid #d1d5db;"></span>
  <span title="200 #f2f2f2" style="display:inline-block;width:32px;height:32px;background:#f2f2f2;border:1px solid #d1d5db;"></span>
  <span title="300 #c6c8c8" style="display:inline-block;width:32px;height:32px;background:#c6c8c8;border:1px solid #d1d5db;"></span>
  <span title="400 #a8acac" style="display:inline-block;width:32px;height:32px;background:#a8acac;border:1px solid #d1d5db;"></span>
  <span title="500 #8c9091" style="display:inline-block;width:32px;height:32px;background:#8c9091;border:1px solid #d1d5db;"></span>
  <span title="600 #707577" style="display:inline-block;width:32px;height:32px;background:#707577;border:1px solid #d1d5db;"></span>
  <span title="700 #565c5f" style="display:inline-block;width:32px;height:32px;background:#565c5f;border:1px solid #d1d5db;"></span>
  <span title="800 #3d4347" style="display:inline-block;width:32px;height:32px;background:#3d4347;border:1px solid #d1d5db;"></span>
  <span title="900 #000102" style="display:inline-block;width:32px;height:32px;background:#000102;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Live semantic mapping uses `attitash_blue` for the primary expressive lane and `daybreak` for the supporting expressive lane.
- `attitash_neutral` preserves the `Mogul Shadow 20%`, `Mogul Shadow`, and `Sharp Edge Grey` source anchors directly.
- The duplicate raw-only grey ramps were removed because they introduced no additional governed values beyond `attitash_neutral`.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> `attitash/attitash_neutral`
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `attitash/attitash_blue`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `attitash/daybreak`
- `assets/logo` -> `Attitash`
  The semantic color extension stores the governed display label.

## Review Readiness

- Subject: `Attitash neutral consolidation`
  Channels: `web, email, ads`
  Rule: Keep `attitash_neutral` as the single grey family because it already preserves the accent-sheet grey anchors.
  Source basis: `Mogul Shadow 20%`, `Mogul Shadow`, and `Sharp Edge Grey` all land exactly on existing `attitash_neutral` steps.
