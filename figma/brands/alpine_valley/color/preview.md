# Alpine Valley Color Preview

Review state: written in figma. Verify live write state in `figma/brands/alpine_valley/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Valley Black`
  Provided value: `#000000`
  Usage scope: `primary palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK 0 0 0 100, RGB 0 0 0, and HEX

- Source color: `Alpine`
  Provided value: `#b0c6ce`
  Usage scope: `secondary palette supporting brand campaign elements`
  Channel restrictions: `not specified in source`
  Notes: Source image lists CMYK 31 13 14 0, RGB 176 198 206, and HEX

## Universal Reuse

- Source color: `Valley Black`
  Proposed token: `universal/black`
  Notes: Exact match to the shared universal black primitive, so no duplicate Alpine Valley black token should be created.

## Proposed Families

### Family: alpine

Source anchor: `300_source`

<div>
  <span title="100 #f7fbfc" style="display:inline-block;width:32px;height:32px;background:#f7fbfc;border:1px solid #d1d5db;"></span>
  <span title="200 #ecf1f3" style="display:inline-block;width:32px;height:32px;background:#ecf1f3;border:1px solid #d1d5db;"></span>
  <span title="300 #b0c6ce" style="display:inline-block;width:32px;height:32px;background:#b0c6ce;border:1px solid #d1d5db;"></span>
  <span title="400 #a5b6bc" style="display:inline-block;width:32px;height:32px;background:#a5b6bc;border:1px solid #d1d5db;"></span>
  <span title="500 #89969b" style="display:inline-block;width:32px;height:32px;background:#89969b;border:1px solid #d1d5db;"></span>
  <span title="600 #6e787c" style="display:inline-block;width:32px;height:32px;background:#6e787c;border:1px solid #d1d5db;"></span>
  <span title="700 #545c5f" style="display:inline-block;width:32px;height:32px;background:#545c5f;border:1px solid #d1d5db;"></span>
  <span title="800 #3c4245" style="display:inline-block;width:32px;height:32px;background:#3c4245;border:1px solid #d1d5db;"></span>
  <span title="900 #141718" style="display:inline-block;width:32px;height:32px;background:#141718;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Alpine lands at `300` because the supplied swatch sits in the bright, pale blue lightness band.
- Exact black should remain shared through `universal/black` rather than duplicated under the Alpine Valley group.
- The generated `alpine` ladder darkens into a blue-gray family that can support readable dark expressive surfaces while keeping the source swatch intact as the light anchor.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `inherited_base`
  Exact black is reused as the universal primitive and no Alpine Valley light neutral or white swatch was supplied, so the shared neutral role set remains inherited in the first pass.
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `alpine_valley/alpine`
  Recommended first pass. `alpine/*` is the only non-neutral supplied family, so it is the most stable expressive lane under the current semantic model.
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `alpine_valley/alpine`
  Recommended first pass. The source does not provide a second expressive hue, so the accepted semantic color model allows `brand_secondary/*` to reuse the same raw family as `brand/*`.
- `variables/assets/logo` -> `Alpine Valley`
  The live `Semantic: Theme` schema includes `variables/assets/logo`, and each brand extension overrides it to the brand display name string.

## Review Readiness

- Subject: `Alpine Valley exact black reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` for Valley Black rather than creating a duplicate raw token.
  Source basis: Source image explicitly provides exact black as

- Subject: `Alpine Valley expressive semantic promotion`
  Channels: `web, email, ads`
  Rule: Recommended first pass promotes `alpine/*` into both expressive semantic lanes because it is the only non-neutral supplied family.
  Source basis: Source image provides exact black plus one supporting Alpine color.
