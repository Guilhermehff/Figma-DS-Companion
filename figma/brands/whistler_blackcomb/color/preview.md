# Whistler Blackcomb Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/whistler_blackcomb/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Red`
  Provided value: `#cc0000`
  Usage scope: `primary brand palette`
  Notes: Source image lists HEX `CC0000`, RGB `204 0 0`, and CMYK `13 100 100 4`.

- Source color: `Black`
  Provided value: `#000000`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `0 0 0` and CMYK `0 0 0 100`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `255 255 255` and CMYK `0 0 0 0`.

## Universal Reuse

- `Black` reuses `universal/black`.
- `White` reuses `universal/white`.

## Color Proportion Guidance

### Brand Touchpoints

- Intent: Red, black, and white should be held in balance so no single one of the three becomes the only field color in a design.
- `Red`: `33%`
  DS mapping: `whistler_blackcomb/red/600`
- `Black`: `33%`
  DS mapping: `universal/black`
- `White`: `33%`
  DS mapping: `universal/white`
- Notes: Treat these as equal thirds rather than as audited integer totals. The source also states that no design should resolve to all red, all black, or all white.

## Proposed Families

### Family: red

Source anchor: `600_source`

Swatch strip:

<div>
  <span title="50 #fff1ef" style="display:inline-block;width:32px;height:32px;background:#fff1ef;border:1px solid #d1d5db;"></span>
  <span title="100 #ffded8" style="display:inline-block;width:32px;height:32px;background:#ffded8;border:1px solid #d1d5db;"></span>
  <span title="200 #ffb8ab" style="display:inline-block;width:32px;height:32px;background:#ffb8ab;border:1px solid #d1d5db;"></span>
  <span title="300 #ff8f7e" style="display:inline-block;width:32px;height:32px;background:#ff8f7e;border:1px solid #d1d5db;"></span>
  <span title="400 #ff604e" style="display:inline-block;width:32px;height:32px;background:#ff604e;border:1px solid #d1d5db;"></span>
  <span title="500 #ff0000" style="display:inline-block;width:32px;height:32px;background:#ff0000;border:1px solid #d1d5db;"></span>
  <span title="600 #cc0000" style="display:inline-block;width:32px;height:32px;background:#cc0000;border:1px solid #d1d5db;"></span>
  <span title="700 #9c0000" style="display:inline-block;width:32px;height:32px;background:#9c0000;border:1px solid #d1d5db;"></span>
  <span title="800 #6e0000" style="display:inline-block;width:32px;height:32px;background:#6e0000;border:1px solid #d1d5db;"></span>
  <span title="900 #440000" style="display:inline-block;width:32px;height:32px;background:#440000;border:1px solid #d1d5db;"></span>
  <span title="950 #300000" style="display:inline-block;width:32px;height:32px;background:#300000;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Whistler Blackcomb can inherit the shared neutral system because the supplied black and white are exact universal matches.
- The official guidance asks for an even ratio of red, black, and white. That usage rule belongs in downstream compositions, not in duplicate raw exact tokens.
- `red` is the only expressive family supplied, so the first semantic pass uses it for both expressive slots supported by the live schema.

## Proposed Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> inherit shared base because the supplied neutrals are exact universal black and white
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `whistler_blackcomb/red/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `whistler_blackcomb/red/*`
- Global-only extra families: none
- `assets/logo` -> `Whistler Blackcomb`

## Review Readiness

- Subject: `Whistler Blackcomb neutral system`
  Channels: `web, email, ads`
  Rule: Keep black and white on the shared universal primitives rather than creating duplicate Whistler Blackcomb exact tokens.
  Source basis: The supplied palette exactly matches the governed universal values.

- Subject: `Whistler Blackcomb expressive lane coverage`
  Channels: `web, email, ads`
  Rule: Use the red family for both `brand/*` and `brand_secondary/*` in the first semantic pass because the official palette supplies only one expressive hue.
  Source basis: The supplied palette defines red, black, and white only, and the accepted semantic family model permits same-family mapping when no second expressive hue is defined.
