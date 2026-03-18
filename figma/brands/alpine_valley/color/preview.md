# Alpine Valley Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/alpine_valley/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Valley Black`
  Provided value: `#000000`
  Usage scope: `primary palette`
  Notes: Source image lists CMYK `0 0 0 100`, RGB `0 0 0`, and HEX `#000000`.

- Source color: `Alpine`
  Provided value: `#b0c6ce`
  Usage scope: `secondary palette supporting brand campaign elements`
  Notes: Source image lists CMYK `31 13 14 0`, RGB `176 198 206`, and HEX `#B0C6CE`.

## Universal Reuse

- `Valley Black` reuses `universal/black`.

## Proposed Families

### Family: alpine

Source anchor: `300_source`

Swatch strip:

<div>
  <span title="50 #f7fbfc" style="display:inline-block;width:32px;height:32px;background:#f7fbfc;border:1px solid #d1d5db;"></span>
  <span title="100 #ecf1f3" style="display:inline-block;width:32px;height:32px;background:#ecf1f3;border:1px solid #d1d5db;"></span>
  <span title="200 #dae3e6" style="display:inline-block;width:32px;height:32px;background:#dae3e6;border:1px solid #d1d5db;"></span>
  <span title="300 #b0c6ce" style="display:inline-block;width:32px;height:32px;background:#b0c6ce;border:1px solid #d1d5db;"></span>
  <span title="400 #a5b6bc" style="display:inline-block;width:32px;height:32px;background:#a5b6bc;border:1px solid #d1d5db;"></span>
  <span title="500 #89969b" style="display:inline-block;width:32px;height:32px;background:#89969b;border:1px solid #d1d5db;"></span>
  <span title="600 #6e787c" style="display:inline-block;width:32px;height:32px;background:#6e787c;border:1px solid #d1d5db;"></span>
  <span title="700 #545c5f" style="display:inline-block;width:32px;height:32px;background:#545c5f;border:1px solid #d1d5db;"></span>
  <span title="800 #3c4245" style="display:inline-block;width:32px;height:32px;background:#3c4245;border:1px solid #d1d5db;"></span>
  <span title="900 #252a2b" style="display:inline-block;width:32px;height:32px;background:#252a2b;border:1px solid #d1d5db;"></span>
  <span title="950 #141718" style="display:inline-block;width:32px;height:32px;background:#141718;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Alpine Valley supplies one exact universal neutral and one pale blue expressive family.
- The live first pass keeps exact black on `universal/black`, leaves neutral roles inherited from the shared base, and uses `alpine/*` for both expressive semantic lanes.

## Live Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> inherit shared base
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `alpine_valley/alpine/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `alpine_valley/alpine/*`
- `assets/logo` -> `Alpine Valley`

## Review Readiness

- Subject: `Alpine Valley exact black reuse`
  Channels: `web, email, ads`
  Rule: Reuse `universal/black` for Valley Black rather than creating a duplicate raw token.
  Source basis: Source image explicitly provides exact black as `#000000`.

- Subject: `Alpine Valley expressive semantic promotion`
  Channels: `web, email, ads`
  Rule: Approved live pass promotes `alpine/*` into both expressive semantic lanes because it is the only non-neutral supplied family.
  Source basis: Source image provides exact black plus one supporting Alpine color.
