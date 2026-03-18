# Crotched Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/crotched/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Rocket Fuel`
  Provided value: `#b2db44`
  Usage scope: `primary color system plus sub-brand system`
  Notes: Source image lists PMS `375C` and `381U`, RGB `178 219 68`, and HEX `#B2DB44`.

- Source color: `Snow Gun`
  Provided value: `#413c37`
  Usage scope: `primary color system plus sub-brand system`
  Notes: Source image lists PMS `418C` and `419U`, RGB `65 60 55`, and HEX `#413C37`.

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `rich black when applicable`
  Notes: Exact match to `universal/black`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `neutral support`
  Notes: Exact match to `universal/white`.

## Universal Reuse

- `Black` reuses `universal/black`.
- `White` reuses `universal/white`.

## Proposed Families

### Family: rocket_fuel

Source anchor: `400_source`

<div>
  <span title="50 #fbfdf4" style="display:inline-block;width:32px;height:32px;background:#fbfdf4;border:1px solid #d1d5db;"></span>
  <span title="100 #f1f8df" style="display:inline-block;width:32px;height:32px;background:#f1f8df;border:1px solid #d1d5db;"></span>
  <span title="200 #deefb3" style="display:inline-block;width:32px;height:32px;background:#deefb3;border:1px solid #d1d5db;"></span>
  <span title="300 #c8e777" style="display:inline-block;width:32px;height:32px;background:#c8e777;border:1px solid #d1d5db;"></span>
  <span title="400 #b2db44" style="display:inline-block;width:32px;height:32px;background:#b2db44;border:1px solid #d1d5db;"></span>
  <span title="500 #94be35" style="display:inline-block;width:32px;height:32px;background:#94be35;border:1px solid #d1d5db;"></span>
  <span title="600 #789f2b" style="display:inline-block;width:32px;height:32px;background:#789f2b;border:1px solid #d1d5db;"></span>
  <span title="700 #5d7d22" style="display:inline-block;width:32px;height:32px;background:#5d7d22;border:1px solid #d1d5db;"></span>
  <span title="800 #445c1a" style="display:inline-block;width:32px;height:32px;background:#445c1a;border:1px solid #d1d5db;"></span>
  <span title="900 #2e3e12" style="display:inline-block;width:32px;height:32px;background:#2e3e12;border:1px solid #d1d5db;"></span>
  <span title="950 #192108" style="display:inline-block;width:32px;height:32px;background:#192108;border:1px solid #d1d5db;"></span>
</div>

### Family: snow_gun

Source anchor: `900_source`

<div>
  <span title="50 #fbfaf9" style="display:inline-block;width:32px;height:32px;background:#fbfaf9;border:1px solid #d1d5db;"></span>
  <span title="100 #f1efed" style="display:inline-block;width:32px;height:32px;background:#f1efed;border:1px solid #d1d5db;"></span>
  <span title="200 #ddd7d2" style="display:inline-block;width:32px;height:32px;background:#ddd7d2;border:1px solid #d1d5db;"></span>
  <span title="300 #c3bab3" style="display:inline-block;width:32px;height:32px;background:#c3bab3;border:1px solid #d1d5db;"></span>
  <span title="400 #a69a90" style="display:inline-block;width:32px;height:32px;background:#a69a90;border:1px solid #d1d5db;"></span>
  <span title="500 #897c72" style="display:inline-block;width:32px;height:32px;background:#897c72;border:1px solid #d1d5db;"></span>
  <span title="600 #71655d" style="display:inline-block;width:32px;height:32px;background:#71655d;border:1px solid #d1d5db;"></span>
  <span title="700 #5b524c" style="display:inline-block;width:32px;height:32px;background:#5b524c;border:1px solid #d1d5db;"></span>
  <span title="800 #4c443f" style="display:inline-block;width:32px;height:32px;background:#4c443f;border:1px solid #d1d5db;"></span>
  <span title="900 #413c37" style="display:inline-block;width:32px;height:32px;background:#413c37;border:1px solid #d1d5db;"></span>
  <span title="950 #25221f" style="display:inline-block;width:32px;height:32px;background:#25221f;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Crotched supplies two branded expressive colors plus exact black and white neutrals that already exist in the shared universal set.
- The live first pass keeps neutral roles inherited from base, uses `rocket_fuel/*` for the primary expressive lane, and uses `snow_gun/*` for the secondary expressive lane.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> inherit shared base
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `crotched/rocket_fuel/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `crotched/snow_gun/*`
- `assets/logo` -> `Crotched`

## Review Readiness

- Subject: `Crotched expressive lane order`
  Channels: `web, email, ads`
  Rule: Use `rocket_fuel` as the primary expressive lane and `snow_gun` as the secondary expressive lane.
  Source basis: Source image names the supplied branded colors and distinguishes them from exact black and white.

- Subject: `Crotched neutral reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` and `universal/white` rather than duplicating exact neutral primitives.
  Source basis: Source image provides exact black and white values that match the shared universal tokens.
