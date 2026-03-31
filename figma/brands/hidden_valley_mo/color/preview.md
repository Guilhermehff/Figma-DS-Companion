# Hidden Valley MO Color Preview

Review state: written in figma. Verify live write state in `figma/brands/hidden_valley_mo/brand.yml` and Figma.

## Original Source Swatches

- Source color: `HV Blue`
  Provided value: `#0e9fb4`
  Usage scope: `primary color system`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 7710C and 7711U, CMYK 78 19 26 0, web RGB 14 159 180, and HEX

- Source color: `Tagline Grey`
  Provided value: `#51544a`
  Usage scope: `primary color system`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 4230C and 419U, web RGB 81 84 74, and HEX

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `logo toolkit black variation`
  Channel restrictions: `not specified in source`
  Notes: The supplied logo toolkit includes a black variation that matches the shared universal black primitive.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `logo toolkit white variation`
  Channel restrictions: `not specified in source`
  Notes: The supplied logo toolkit includes a white variation that matches the shared universal white primitive.

## Universal Reuse

- Source color: `Black`
  Proposed token: `universal/black`
  Notes: Exact match to the shared universal black primitive, so no duplicate Hidden Valley MO black token should be created.

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact match to the shared universal white primitive, so no duplicate Hidden Valley MO white token should be created.

## Proposed Families

### Family: hv_blue

Source anchor: `500_source`

<div>
  <span title="100 #f2fcfd" style="display:inline-block;width:32px;height:32px;background:#f2fcfd;border:1px solid #d1d5db;"></span>
  <span title="200 #d8f3f7" style="display:inline-block;width:32px;height:32px;background:#d8f3f7;border:1px solid #d1d5db;"></span>
  <span title="300 #79d1de" style="display:inline-block;width:32px;height:32px;background:#79d1de;border:1px solid #d1d5db;"></span>
  <span title="400 #42bdd0" style="display:inline-block;width:32px;height:32px;background:#42bdd0;border:1px solid #d1d5db;"></span>
  <span title="500 #0e9fb4" style="display:inline-block;width:32px;height:32px;background:#0e9fb4;border:1px solid #d1d5db;"></span>
  <span title="600 #0c8497" style="display:inline-block;width:32px;height:32px;background:#0c8497;border:1px solid #d1d5db;"></span>
  <span title="700 #096a77" style="display:inline-block;width:32px;height:32px;background:#096a77;border:1px solid #d1d5db;"></span>
  <span title="800 #07525d" style="display:inline-block;width:32px;height:32px;background:#07525d;border:1px solid #d1d5db;"></span>
  <span title="900 #02242a" style="display:inline-block;width:32px;height:32px;background:#02242a;border:1px solid #d1d5db;"></span>
</div>

### Family: tagline_grey

Source anchor: `800_source`

<div>
  <span title="100 #f7f8f6" style="display:inline-block;width:32px;height:32px;background:#f7f8f6;border:1px solid #d1d5db;"></span>
  <span title="200 #ecede9" style="display:inline-block;width:32px;height:32px;background:#ecede9;border:1px solid #d1d5db;"></span>
  <span title="300 #babeb3" style="display:inline-block;width:32px;height:32px;background:#babeb3;border:1px solid #d1d5db;"></span>
  <span title="400 #9ba093" style="display:inline-block;width:32px;height:32px;background:#9ba093;border:1px solid #d1d5db;"></span>
  <span title="500 #7d8277" style="display:inline-block;width:32px;height:32px;background:#7d8277;border:1px solid #d1d5db;"></span>
  <span title="600 #686c61" style="display:inline-block;width:32px;height:32px;background:#686c61;border:1px solid #d1d5db;"></span>
  <span title="700 #5c5f56" style="display:inline-block;width:32px;height:32px;background:#5c5f56;border:1px solid #d1d5db;"></span>
  <span title="800 #51544a" style="display:inline-block;width:32px;height:32px;background:#51544a;border:1px solid #d1d5db;"></span>
  <span title="900 #262721" style="display:inline-block;width:32px;height:32px;background:#262721;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Exact black and white remain shared through the universal neutral primitives, so Hidden Valley MO only adds the two branded expressive families supplied by the source.
- `hv_blue` preserves the supplied source value as the mid expressive step and darkens enough to support accessible branded surfaces.
- `tagline_grey` preserves the source value as the readable secondary default step while remaining distinct from exact black.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> `inherited_base`
  Exact black and white are already governed by the shared universal primitives, so the first pass keeps the neutral role set inherited.
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `hidden_valley_mo/hv_blue`
  HV Blue is the signature Hidden Valley MO color and should drive the primary expressive semantic lane.
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `hidden_valley_mo/tagline_grey`
  Tagline Grey is the dark supporting brand color and should drive the secondary expressive lane.
- `assets/logo` -> `Hidden Valley MO`
  The live semantic color schema stores the governed brand display label in `assets/logo`.

## Review Readiness

- Subject: `Hidden Valley MO expressive lane order`
  Channels: `web, email, ads`
  Rule: Use `hv_blue` as the primary expressive lane and `tagline_grey` as the secondary expressive lane.
  Source basis: Source image names the supplied branded colors and distinguishes them from exact black and white logo variants.

- Subject: `Hidden Valley MO neutral reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` and `universal/white` rather than duplicating exact neutral primitives.
  Source basis: Source image provides black and white logo variants that match the shared universal tokens.
