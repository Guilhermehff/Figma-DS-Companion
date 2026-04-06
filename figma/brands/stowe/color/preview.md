# Stowe Color Preview

Review state: written in figma. Verify live write state in `figma/brands/stowe/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Powder White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Exact shared white. The source image also shows CMYK 0 0 0 0.

- Source color: `Stowe Red`
  Provided value: `#c4272f`
  Usage scope: `primary brand palette and visual brand identifier`
  Channel restrictions: `not specified in source`
  Notes: Source image shows RGB 197 38 47 and CMYK 22 100 95 0.

- Source color: `Ice Blue`
  Provided value: `#74838e`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image shows CMYK 57 41 36 5.

- Source color: `Winter Blue`
  Provided value: `#384851`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: The source image clearly shows the HEX value; the remaining CMYK line is not fully legible in the attachment.

## Universal Reuse

- Source color: `Powder White`
  Proposed token: `universal/white`
  Notes: Exact shared white should remain on the governed universal primitive rather than being duplicated under the Stowe group.

## Color Proportion Guidance

Source basis: Approximate ratios inferred from the relative field widths in the user-provided Stowe guide image. The source says the page shows the recommended ratios for color usage across touchpoints but does not publish exact percentages.

### Brand Touchpoints

- Intent: `Powder White is the dominant canvas. Stowe Red is the primary expressive lane. Ice Blue and Winter Blue share the supporting structural blue-gray system, with Ice Blue carrying more area than Winter Blue.`
- Proportions:
  `Powder White` -> `universal/white` (`50%`) Largest field in the composition and the main whitespace carrier.
  `Stowe Red` -> `stowe/stowe_red/600` (`20%`) Largest non-white block and the clearest brand-identifying color.
  `Ice Blue` -> `stowe/stowe_blue/500` (`18%`) Wider of the two blue-gray support blocks in the recommended ratio strip.
  `Winter Blue` -> `stowe/stowe_blue/800` (`12%`) Narrowest support block and the darkest contrast lane in the source strip.
- Notes:
  These percentages are approximate documentation guidance inferred from the displayed ratio fields rather than exact published source values.
  Ice Blue and Winter Blue are governed inside one raw family even though the usage page shows them as separate visual shares.

## Proposed Families

### Family: stowe_red

Source anchor: `600_source`

<div>
  <span title="100 #fff6f5" style="display:inline-block;width:32px;height:32px;background:#fff6f5;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe5e2" style="display:inline-block;width:32px;height:32px;background:#ffe5e2;border:1px solid #d1d5db;"></span>
  <span title="300 #efa099" style="display:inline-block;width:32px;height:32px;background:#efa099;border:1px solid #d1d5db;"></span>
  <span title="400 #e27c76" style="display:inline-block;width:32px;height:32px;background:#e27c76;border:1px solid #d1d5db;"></span>
  <span title="500 #d45653" style="display:inline-block;width:32px;height:32px;background:#d45653;border:1px solid #d1d5db;"></span>
  <span title="600 #c4272f" style="display:inline-block;width:32px;height:32px;background:#c4272f;border:1px solid #d1d5db;"></span>
  <span title="700 #961e23" style="display:inline-block;width:32px;height:32px;background:#961e23;border:1px solid #d1d5db;"></span>
  <span title="800 #6a1417" style="display:inline-block;width:32px;height:32px;background:#6a1417;border:1px solid #d1d5db;"></span>
  <span title="900 #2f0707" style="display:inline-block;width:32px;height:32px;background:#2f0707;border:1px solid #d1d5db;"></span>
</div>

### Family: stowe_blue

Source anchors: `500_source / 800_source`

<div>
  <span title="100 #f7fbfe" style="display:inline-block;width:32px;height:32px;background:#f7fbfe;border:1px solid #d1d5db;"></span>
  <span title="200 #e7edf1" style="display:inline-block;width:32px;height:32px;background:#e7edf1;border:1px solid #d1d5db;"></span>
  <span title="300 #acb7be" style="display:inline-block;width:32px;height:32px;background:#acb7be;border:1px solid #d1d5db;"></span>
  <span title="400 #8f9ca6" style="display:inline-block;width:32px;height:32px;background:#8f9ca6;border:1px solid #d1d5db;"></span>
  <span title="500 #74838e" style="display:inline-block;width:32px;height:32px;background:#74838e;border:1px solid #d1d5db;"></span>
  <span title="600 #5f6f79" style="display:inline-block;width:32px;height:32px;background:#5f6f79;border:1px solid #d1d5db;"></span>
  <span title="700 #4b5b65" style="display:inline-block;width:32px;height:32px;background:#4b5b65;border:1px solid #d1d5db;"></span>
  <span title="800 #384851" style="display:inline-block;width:32px;height:32px;background:#384851;border:1px solid #d1d5db;"></span>
  <span title="900 #12181c" style="display:inline-block;width:32px;height:32px;background:#12181c;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Stowe Red lands cleanly at `600`, keeping the supplied red in the expected mid-dark expressive band while preserving usable lighter and darker extensions.
- Ice Blue and Winter Blue sit naturally at `500` and `800`, which supports a single blue-gray system spanning cool surfaces, readable default text, and darker emphasis.
- Exact white remains shared through `universal/white` instead of creating a duplicate Stowe white family.
- User-approved live write. The supporting expressive lane uses `stowe_blue`, but its semantic `default/strong/emphasis` steps stage on `600/700/800` because the raw `500` source anchor does not support the shared white on-surface contract.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `stowe/stowe_blue`
  Stowe's supplied blues are already doing structural work in the brand specimen pages, so the first governed recommendation is to let the blue-gray family drive neutral surfaces, borders, and readable default foregrounds.
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `stowe/stowe_red`
  Stowe Red is the dominant expressive brand identifier and should drive the primary expressive semantic lane.
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `stowe/stowe_blue`
  Approved live write. `stowe_blue` is the only supporting non-red hue in the supplied palette, so it stages as the supporting expressive lane, with the semantic default/strong/emphasis steps landing at `600/700/800` for readable white foreground use.
- `color/surface/neutral/canvas` -> `universal/white`
  Powder White is an exact shared white and the specimen pages use it as the dominant page canvas.

## Review Readiness

- Subject: `Stowe blue-gray neutral system`
  Channels: `web, email, ads`
  Rule: Keep Ice Blue and Winter Blue in one governed structural lane so cool surfaces and readable default text stay visually related.
  Source basis: The supplied palette and typography specimen both use the darker blue-gray as the default readable text color and the lighter blue-gray as a supporting brand color.

- Subject: `Stowe expressive lane order`
  Channels: `web, email, ads`
  Rule: Use Stowe Red as the primary expressive lane and treat the blue-gray family as the supporting system lane.
  Source basis: The supplied palette page positions Stowe Red as the dominant visual brand identifier.
