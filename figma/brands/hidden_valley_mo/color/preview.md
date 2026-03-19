# Hidden Valley MO Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/hidden_valley_mo/brand.yml` and Figma.

## Original Source Swatches

- Source color: `HV Blue`
  Provided value: `#0e9fb4`
  Usage scope: `primary color system`
  Notes: Source image lists PMS `7710C` and `7711U`, RGB `14 159 180`, and HEX `#0E9FB4`.

- Source color: `Tagline Grey`
  Provided value: `#51544a`
  Usage scope: `primary color system`
  Notes: Source image lists RGB `81 84 74` and HEX `#51544A`.

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `logo toolkit black variation`
  Notes: Exact match to `universal/black`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `logo toolkit white variation`
  Notes: Exact match to `universal/white`.

## Universal Reuse

- `Black` reuses `universal/black`.
- `White` reuses `universal/white`.

## Proposed Families

### Family: hv_blue

Source anchor: `500_source`

<div>
  <span title="50 #f2fcfd" style="display:inline-block;width:32px;height:32px;background:#f2fcfd;border:1px solid #d1d5db;"></span>
  <span title="100 #d8f3f7" style="display:inline-block;width:32px;height:32px;background:#d8f3f7;border:1px solid #d1d5db;"></span>
  <span title="200 #ace3eb" style="display:inline-block;width:32px;height:32px;background:#ace3eb;border:1px solid #d1d5db;"></span>
  <span title="300 #79d1de" style="display:inline-block;width:32px;height:32px;background:#79d1de;border:1px solid #d1d5db;"></span>
  <span title="400 #42bdd0" style="display:inline-block;width:32px;height:32px;background:#42bdd0;border:1px solid #d1d5db;"></span>
  <span title="500 #0e9fb4" style="display:inline-block;width:32px;height:32px;background:#0e9fb4;border:1px solid #d1d5db;"></span>
  <span title="600 #0c8497" style="display:inline-block;width:32px;height:32px;background:#0c8497;border:1px solid #d1d5db;"></span>
  <span title="700 #096a77" style="display:inline-block;width:32px;height:32px;background:#096a77;border:1px solid #d1d5db;"></span>
  <span title="800 #07525d" style="display:inline-block;width:32px;height:32px;background:#07525d;border:1px solid #d1d5db;"></span>
  <span title="900 #053c45" style="display:inline-block;width:32px;height:32px;background:#053c45;border:1px solid #d1d5db;"></span>
  <span title="950 #02242a" style="display:inline-block;width:32px;height:32px;background:#02242a;border:1px solid #d1d5db;"></span>
</div>

### Family: tagline_grey

Source anchor: `800_source`

<div>
  <span title="50 #f7f8f6" style="display:inline-block;width:32px;height:32px;background:#f7f8f6;border:1px solid #d1d5db;"></span>
  <span title="100 #ecede9" style="display:inline-block;width:32px;height:32px;background:#ecede9;border:1px solid #d1d5db;"></span>
  <span title="200 #d7d9d2" style="display:inline-block;width:32px;height:32px;background:#d7d9d2;border:1px solid #d1d5db;"></span>
  <span title="300 #babeb3" style="display:inline-block;width:32px;height:32px;background:#babeb3;border:1px solid #d1d5db;"></span>
  <span title="400 #9ba093" style="display:inline-block;width:32px;height:32px;background:#9ba093;border:1px solid #d1d5db;"></span>
  <span title="500 #7d8277" style="display:inline-block;width:32px;height:32px;background:#7d8277;border:1px solid #d1d5db;"></span>
  <span title="600 #686c61" style="display:inline-block;width:32px;height:32px;background:#686c61;border:1px solid #d1d5db;"></span>
  <span title="700 #5c5f56" style="display:inline-block;width:32px;height:32px;background:#5c5f56;border:1px solid #d1d5db;"></span>
  <span title="800 #51544a" style="display:inline-block;width:32px;height:32px;background:#51544a;border:1px solid #d1d5db;"></span>
  <span title="900 #3e4038" style="display:inline-block;width:32px;height:32px;background:#3e4038;border:1px solid #d1d5db;"></span>
  <span title="950 #262721" style="display:inline-block;width:32px;height:32px;background:#262721;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Hidden Valley MO supplies two branded expressive colors plus exact black and white logo variants that already exist in the shared universal set.
- The live first pass keeps neutral roles inherited from base, uses `hv_blue/*` for the primary expressive lane, and uses `tagline_grey/*` for the secondary expressive lane.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> inherit shared base
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `hidden_valley_mo/hv_blue/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `hidden_valley_mo/tagline_grey/*`
- `assets/logo` -> `Hidden Valley MO`

## Review Readiness

- Subject: `Hidden Valley MO expressive lane order`
  Channels: `web, email, ads`
  Rule: Use `hv_blue` as the primary expressive lane and `tagline_grey` as the secondary expressive lane.
  Source basis: Source image names the supplied branded colors and distinguishes them from exact black and white logo variants.

- Subject: `Hidden Valley MO neutral reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` and `universal/white` rather than duplicating exact neutral primitives.
  Source basis: Source image provides black and white logo variants that match the shared universal tokens.
