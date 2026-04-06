# Crotched Color Preview

Review state: written in figma. Verify live write state in `figma/brands/crotched/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Rocket Fuel`
  Provided value: `#b2db44`
  Usage scope: `primary color system plus sub-brand system`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 375C and 381U, CMYK 35 0 87 0, web RGB 178 219 68, and HEX

- Source color: `Snow Gun`
  Provided value: `#413c37`
  Usage scope: `primary color system plus sub-brand system`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 418C and 419U, CMYK 63 61 65 52, web RGB 65 60 55, and HEX

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `rich black when applicable`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK 0 0 0 100 and HEX

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `neutral support`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK 0 0 0 0 and HEX

## Universal Reuse

- Source color: `Black`
  Proposed token: `universal/black`
  Notes: Exact match to the shared universal black primitive, so no duplicate Crotched black token should be created.

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact match to the shared universal white primitive, so no duplicate Crotched white token should be created.

## Proposed Families

### Family: rocket_fuel

Source anchor: `400_source`

<div>
  <span title="100 #fbfdf4" style="display:inline-block;width:32px;height:32px;background:#fbfdf4;border:1px solid #d1d5db;"></span>
  <span title="200 #f1f8df" style="display:inline-block;width:32px;height:32px;background:#f1f8df;border:1px solid #d1d5db;"></span>
  <span title="300 #c8e777" style="display:inline-block;width:32px;height:32px;background:#c8e777;border:1px solid #d1d5db;"></span>
  <span title="400 #b2db44" style="display:inline-block;width:32px;height:32px;background:#b2db44;border:1px solid #d1d5db;"></span>
  <span title="500 #94be35" style="display:inline-block;width:32px;height:32px;background:#94be35;border:1px solid #d1d5db;"></span>
  <span title="600 #789f2b" style="display:inline-block;width:32px;height:32px;background:#789f2b;border:1px solid #d1d5db;"></span>
  <span title="700 #5d7d22" style="display:inline-block;width:32px;height:32px;background:#5d7d22;border:1px solid #d1d5db;"></span>
  <span title="800 #445c1a" style="display:inline-block;width:32px;height:32px;background:#445c1a;border:1px solid #d1d5db;"></span>
  <span title="900 #192108" style="display:inline-block;width:32px;height:32px;background:#192108;border:1px solid #d1d5db;"></span>
</div>

### Family: snow_gun

Source anchor: `900_source`

<div>
  <span title="100 #fbfaf9" style="display:inline-block;width:32px;height:32px;background:#fbfaf9;border:1px solid #d1d5db;"></span>
  <span title="200 #f1efed" style="display:inline-block;width:32px;height:32px;background:#f1efed;border:1px solid #d1d5db;"></span>
  <span title="300 #c3bab3" style="display:inline-block;width:32px;height:32px;background:#c3bab3;border:1px solid #d1d5db;"></span>
  <span title="400 #a69a90" style="display:inline-block;width:32px;height:32px;background:#a69a90;border:1px solid #d1d5db;"></span>
  <span title="500 #897c72" style="display:inline-block;width:32px;height:32px;background:#897c72;border:1px solid #d1d5db;"></span>
  <span title="600 #71655d" style="display:inline-block;width:32px;height:32px;background:#71655d;border:1px solid #d1d5db;"></span>
  <span title="700 #5b524c" style="display:inline-block;width:32px;height:32px;background:#5b524c;border:1px solid #d1d5db;"></span>
  <span title="800 #4c443f" style="display:inline-block;width:32px;height:32px;background:#4c443f;border:1px solid #d1d5db;"></span>
  <span title="900 #413c37" style="display:inline-block;width:32px;height:32px;background:#413c37;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Exact black and white remain shared through the universal neutral primitives, so Crotched only adds the two branded expressive families supplied by the source.
- `rocket_fuel` stays bright at the source step and darkens quickly enough to support accessible branded surfaces.
- `snow_gun` remains a deep brown-charcoal family distinct from exact black while preserving the supplied source swatch as the stronger secondary step.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `inherited_base`
  Exact black and white are already governed by the shared universal primitives, so the first pass keeps the neutral role set inherited.
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `crotched/rocket_fuel`
  Rocket Fuel is the signature bright brand color and should drive the primary expressive semantic lane.
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `crotched/snow_gun`
  Snow Gun is the dark supporting brand color and should drive the secondary expressive lane.
- `variables/assets/logo` -> `Crotched`
  The live semantic color schema stores the governed brand display label in `variables/assets/logo`; the source image shows longer logo lockups, but the user requested the brand be added as Crotched.

## Review Readiness

- Subject: `Crotched expressive lane order`
  Channels: `web, email, ads`
  Rule: Use `rocket_fuel` as the primary expressive lane and `snow_gun` as the secondary expressive lane.
  Source basis: Source image names the supplied branded colors and distinguishes them from exact black and white.

- Subject: `Crotched neutral reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` and `universal/white` rather than duplicating exact neutral primitives.
  Source basis: Source image provides exact black and white values that match the shared universal tokens.
