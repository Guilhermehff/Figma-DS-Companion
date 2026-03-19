# Stowe Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/stowe/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Powder White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Notes: Exact shared white. The source image also shows CMYK `0 0 0 0`.

- Source color: `Stowe Red`
  Provided value: `#c4272f`
  Usage scope: `primary brand palette and visual brand identifier`
  Notes: Source image shows RGB `197 38 47` and CMYK `22 100 95 0`.

- Source color: `Ice Blue`
  Provided value: `#74838e`
  Usage scope: `primary brand palette`
  Notes: Source image shows CMYK `57 41 36 5`.

- Source color: `Winter Blue`
  Provided value: `#384851`
  Usage scope: `primary brand palette`
  Notes: The source image clearly shows the HEX value; the remaining CMYK line is not fully legible in the attachment.

## Universal Reuse

- `Powder White` reuses `universal/white`.

## Proposed Families

### Family: stowe_red

Source anchor: `600_source`

Swatch strip:

<div>
  <span title="50 #fff6f5" style="display:inline-block;width:32px;height:32px;background:#fff6f5;border:1px solid #d1d5db;"></span>
  <span title="100 #ffe5e2" style="display:inline-block;width:32px;height:32px;background:#ffe5e2;border:1px solid #d1d5db;"></span>
  <span title="200 #f9c2bd" style="display:inline-block;width:32px;height:32px;background:#f9c2bd;border:1px solid #d1d5db;"></span>
  <span title="300 #efa099" style="display:inline-block;width:32px;height:32px;background:#efa099;border:1px solid #d1d5db;"></span>
  <span title="400 #e27c76" style="display:inline-block;width:32px;height:32px;background:#e27c76;border:1px solid #d1d5db;"></span>
  <span title="500 #d45653" style="display:inline-block;width:32px;height:32px;background:#d45653;border:1px solid #d1d5db;"></span>
  <span title="600 #c4272f" style="display:inline-block;width:32px;height:32px;background:#c4272f;border:1px solid #d1d5db;"></span>
  <span title="700 #961e23" style="display:inline-block;width:32px;height:32px;background:#961e23;border:1px solid #d1d5db;"></span>
  <span title="800 #6a1417" style="display:inline-block;width:32px;height:32px;background:#6a1417;border:1px solid #d1d5db;"></span>
  <span title="900 #420b0c" style="display:inline-block;width:32px;height:32px;background:#420b0c;border:1px solid #d1d5db;"></span>
  <span title="950 #2f0707" style="display:inline-block;width:32px;height:32px;background:#2f0707;border:1px solid #d1d5db;"></span>
</div>

### Family: stowe_blue

Source anchors: `500_source = Ice Blue`, `800_source = Winter Blue`

Swatch strip:

<div>
  <span title="50 #f7fbfe" style="display:inline-block;width:32px;height:32px;background:#f7fbfe;border:1px solid #d1d5db;"></span>
  <span title="100 #e7edf1" style="display:inline-block;width:32px;height:32px;background:#e7edf1;border:1px solid #d1d5db;"></span>
  <span title="200 #c9d1d7" style="display:inline-block;width:32px;height:32px;background:#c9d1d7;border:1px solid #d1d5db;"></span>
  <span title="300 #acb7be" style="display:inline-block;width:32px;height:32px;background:#acb7be;border:1px solid #d1d5db;"></span>
  <span title="400 #8f9ca6" style="display:inline-block;width:32px;height:32px;background:#8f9ca6;border:1px solid #d1d5db;"></span>
  <span title="500 #74838e" style="display:inline-block;width:32px;height:32px;background:#74838e;border:1px solid #d1d5db;"></span>
  <span title="600 #5f6f79" style="display:inline-block;width:32px;height:32px;background:#5f6f79;border:1px solid #d1d5db;"></span>
  <span title="700 #4b5b65" style="display:inline-block;width:32px;height:32px;background:#4b5b65;border:1px solid #d1d5db;"></span>
  <span title="800 #384851" style="display:inline-block;width:32px;height:32px;background:#384851;border:1px solid #d1d5db;"></span>
  <span title="900 #1e272d" style="display:inline-block;width:32px;height:32px;background:#1e272d;border:1px solid #d1d5db;"></span>
  <span title="950 #12181c" style="display:inline-block;width:32px;height:32px;background:#12181c;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- `stowe_red` is the clear expressive identity lane and lands cleanly at `600`.
- `stowe_blue` stages Ice Blue and Winter Blue as one low-chroma blue-gray system that can support both structural neutrals and the readable default text color seen in the source specimen.
- Exact white stays shared through `universal/white`.
- The live semantic write keeps `surface/neutral/canvas` on `universal/white` and stages `brand_secondary/default`, `strong`, and `emphasis` on `stowe_blue/600`, `700`, and `800` so the supporting lane preserves readable white on-surface behavior.

## Proposed Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> `stowe/stowe_blue/*`
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `stowe/stowe_red/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `stowe/stowe_blue/*`, with the live semantic `default/strong/emphasis` steps staged on `600/700/800`
- Global-only extra families: none
- Role exceptions: `surface/neutral/canvas` should stay on `universal/white`
- Inherited or deferred notes: none

## Review Readiness

- Subject: `Stowe blue-gray neutral system`
  Channels: `web, email, ads`
  Rule: Keep Ice Blue and Winter Blue in one governed structural lane so cool surfaces and readable default text stay visually related.
  Source basis: The supplied palette and typography specimen both use the darker blue-gray as the default readable text color and the lighter blue-gray as a supporting brand color.

- Subject: `Stowe expressive lane order`
  Channels: `web, email, ads`
  Rule: Use Stowe Red as the primary expressive lane and treat the blue-gray family as the supporting system lane.
  Source basis: The supplied palette page positions Stowe Red as the dominant visual brand identifier.
