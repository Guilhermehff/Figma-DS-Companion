# Crested Butte Color Preview

Review state: written in figma. Verify live write state in `figma/brands/crested_butte/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Crested Butte Powder White`
  Provided value: `#ffffff`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 255 255 255 and CMYK 0 0 0 0.

- Source color: `Crested Butte Wild Red`
  Provided value: `#a5192e`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 165 25 46 and CMYK 25 100 100 12.

- Source color: `Crested Butte Beyond Black`
  Provided value: `#1a1a1a`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 26 26 26 and CMYK 73 67 65 79.

## Universal Reuse

- Source color: `Crested Butte Powder White`
  Proposed token: `universal/white`
  Notes: Exact match to the existing universal primitive.

## Color Proportion Guidance

Source basis: Approximate ratios inferred from the relative widths of the three swatches in the supplied Crested Butte palette strip. The source does not publish exact percentages in text.

### Brand Touchpoints

- Intent: `Powder White slightly leads. Wild Red holds nearly equal weight as the main expressive lane. Beyond Black remains a smaller but still substantial grounding neutral.`
- Proportions:
  `Crested Butte Powder White` -> `universal/white` (`40%`) Widest field in the source strip and the leading open-space carrier.
  `Crested Butte Wild Red` -> `crested_butte/wild_red/700` (`35%`) Near-equal central field and the main expressive brand color.
  `Crested Butte Beyond Black` -> `crested_butte/beyond_black/900` (`25%`) Narrowest field in the strip and the grounding dark neutral.
- Notes:
  These percentages are approximate documentation guidance inferred from the displayed block widths rather than exact published source values.

## Proposed Families

### Family: wild_red

Source anchor: `700_source`

<div>
  <span title="100 #fff8f8" style="display:inline-block;width:32px;height:32px;background:#fff8f8;border:1px solid #d1d5db;"></span>
  <span title="200 #ffebea" style="display:inline-block;width:32px;height:32px;background:#ffebea;border:1px solid #d1d5db;"></span>
  <span title="300 #feb7b6" style="display:inline-block;width:32px;height:32px;background:#feb7b6;border:1px solid #d1d5db;"></span>
  <span title="400 #f29292" style="display:inline-block;width:32px;height:32px;background:#f29292;border:1px solid #d1d5db;"></span>
  <span title="500 #dc666a" style="display:inline-block;width:32px;height:32px;background:#dc666a;border:1px solid #d1d5db;"></span>
  <span title="600 #c04049" style="display:inline-block;width:32px;height:32px;background:#c04049;border:1px solid #d1d5db;"></span>
  <span title="700 #a5192e" style="display:inline-block;width:32px;height:32px;background:#a5192e;border:1px solid #d1d5db;"></span>
  <span title="800 #7b041c" style="display:inline-block;width:32px;height:32px;background:#7b041c;border:1px solid #d1d5db;"></span>
  <span title="900 #310106" style="display:inline-block;width:32px;height:32px;background:#310106;border:1px solid #d1d5db;"></span>
</div>

### Family: beyond_black

Source anchor: `900_source`

<div>
  <span title="100 #fafafa" style="display:inline-block;width:32px;height:32px;background:#fafafa;border:1px solid #d1d5db;"></span>
  <span title="200 #f0f0f0" style="display:inline-block;width:32px;height:32px;background:#f0f0f0;border:1px solid #d1d5db;"></span>
  <span title="300 #cccccc" style="display:inline-block;width:32px;height:32px;background:#cccccc;border:1px solid #d1d5db;"></span>
  <span title="400 #b1b1b1" style="display:inline-block;width:32px;height:32px;background:#b1b1b1;border:1px solid #d1d5db;"></span>
  <span title="500 #909090" style="display:inline-block;width:32px;height:32px;background:#909090;border:1px solid #d1d5db;"></span>
  <span title="600 #737373" style="display:inline-block;width:32px;height:32px;background:#737373;border:1px solid #d1d5db;"></span>
  <span title="700 #585858" style="display:inline-block;width:32px;height:32px;background:#585858;border:1px solid #d1d5db;"></span>
  <span title="800 #404040" style="display:inline-block;width:32px;height:32px;background:#404040;border:1px solid #d1d5db;"></span>
  <span title="900 #1a1a1a" style="display:inline-block;width:32px;height:32px;background:#1a1a1a;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Wild Red lands at `700` because the provided source swatch already sits in a dark, high-contrast brand zone rather than a mid-scale accent zone.
- Beyond Black lands at `950` because the official source is nearly the darkest usable brand neutral and should remain distinct from universal black while preserving white contrast.
- Exact white is reused from the universal palette and is not duplicated under the Crested Butte brand group.
- The approved role-based semantic extension maps `brand/*` and `brand_secondary/*` to the Wild Red ladder while `neutral/*` maps to Beyond Black.

## Review Readiness

- Subject: `Crested Butte Powder White`
  Channels: `web, email, ads`
  Rule: Reuse `universal/white` instead of creating a duplicate brand white.
  Source basis: The source swatch is an exact `#ffffff` match.

- Subject: `Crested Butte Wild Red`
  Channels: `web, email, ads`
  Rule: Treat `wild_red/*` as the source for `brand/*` and `brand_secondary/*` while keeping any extra reuse global-only and separate from shared feedback semantics.
  Source basis: The source presents Wild Red as part of the core brand palette, not as a state color.

- Subject: `Crested Butte Beyond Black`
  Channels: `web, email, ads`
  Rule: Feed `beyond_black/*` into the semantic neutral ladder and use it for dark-on-light or light-on-dark brand surfaces.
  Source basis: The source names Beyond Black as a primary palette color alongside Wild Red and Powder White.
