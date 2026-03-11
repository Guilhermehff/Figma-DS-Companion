# Crested Butte Color Preview

Status: global ladders and semantic color extension are written in Figma

## Original Source Swatches

- Source color: `Crested Butte Powder White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `255 255 255`.

- Source color: `Crested Butte Wild Red`
  Provided value: `#a5192e`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `165 25 46`.

- Source color: `Crested Butte Beyond Black`
  Provided value: `#1a1a1a`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `26 26 26`.

## Universal Reuse

- Source color: `Crested Butte Powder White`
  Proposed token: `universal/white`
  Notes: Exact match.

## Proposed Families

### Family: wild_red

Source anchor: `700_source`

Swatch strip:

<div>
  <span title="50 #fff8f8" style="display:inline-block;width:32px;height:32px;background:#fff8f8;border:1px solid #d1d5db;"></span>
  <span title="100 #ffebea" style="display:inline-block;width:32px;height:32px;background:#ffebea;border:1px solid #d1d5db;"></span>
  <span title="200 #fed6d5" style="display:inline-block;width:32px;height:32px;background:#fed6d5;border:1px solid #d1d5db;"></span>
  <span title="300 #feb7b6" style="display:inline-block;width:32px;height:32px;background:#feb7b6;border:1px solid #d1d5db;"></span>
  <span title="400 #f29292" style="display:inline-block;width:32px;height:32px;background:#f29292;border:1px solid #d1d5db;"></span>
  <span title="500 #dc666a" style="display:inline-block;width:32px;height:32px;background:#dc666a;border:1px solid #d1d5db;"></span>
  <span title="600 #c04049" style="display:inline-block;width:32px;height:32px;background:#c04049;border:1px solid #d1d5db;"></span>
  <span title="700 #a5192e" style="display:inline-block;width:32px;height:32px;background:#a5192e;border:1px solid #d1d5db;"></span>
  <span title="800 #7b041c" style="display:inline-block;width:32px;height:32px;background:#7b041c;border:1px solid #d1d5db;"></span>
  <span title="900 #520210" style="display:inline-block;width:32px;height:32px;background:#520210;border:1px solid #d1d5db;"></span>
  <span title="950 #310106" style="display:inline-block;width:32px;height:32px;background:#310106;border:1px solid #d1d5db;"></span>
</div>

Hex values:

- `50`: `#fff8f8`
- `100`: `#ffebea`
- `200`: `#fed6d5`
- `300`: `#feb7b6`
- `400`: `#f29292`
- `500`: `#dc666a`
- `600`: `#c04049`
- `700`: `#a5192e`
- `800`: `#7b041c`
- `900`: `#520210`
- `950`: `#310106`

### Family: beyond_black

Source anchor: `950_source`

Swatch strip:

<div>
  <span title="50 #fafafa" style="display:inline-block;width:32px;height:32px;background:#fafafa;border:1px solid #d1d5db;"></span>
  <span title="100 #f0f0f0" style="display:inline-block;width:32px;height:32px;background:#f0f0f0;border:1px solid #d1d5db;"></span>
  <span title="200 #e1e1e1" style="display:inline-block;width:32px;height:32px;background:#e1e1e1;border:1px solid #d1d5db;"></span>
  <span title="300 #cccccc" style="display:inline-block;width:32px;height:32px;background:#cccccc;border:1px solid #d1d5db;"></span>
  <span title="400 #b1b1b1" style="display:inline-block;width:32px;height:32px;background:#b1b1b1;border:1px solid #d1d5db;"></span>
  <span title="500 #909090" style="display:inline-block;width:32px;height:32px;background:#909090;border:1px solid #d1d5db;"></span>
  <span title="600 #737373" style="display:inline-block;width:32px;height:32px;background:#737373;border:1px solid #d1d5db;"></span>
  <span title="700 #585858" style="display:inline-block;width:32px;height:32px;background:#585858;border:1px solid #d1d5db;"></span>
  <span title="800 #404040" style="display:inline-block;width:32px;height:32px;background:#404040;border:1px solid #d1d5db;"></span>
  <span title="900 #292929" style="display:inline-block;width:32px;height:32px;background:#292929;border:1px solid #d1d5db;"></span>
  <span title="950 #1a1a1a" style="display:inline-block;width:32px;height:32px;background:#1a1a1a;border:1px solid #d1d5db;"></span>
</div>

Hex values:

- `50`: `#fafafa`
- `100`: `#f0f0f0`
- `200`: `#e1e1e1`
- `300`: `#cccccc`
- `400`: `#b1b1b1`
- `500`: `#909090`
- `600`: `#737373`
- `700`: `#585858`
- `800`: `#404040`
- `900`: `#292929`
- `950`: `#1a1a1a`

## Review Notes

- The first Crested Butte palette pass keeps `powder_white` on the universal layer and stages only two brand families: `wild_red` and `beyond_black`.
- `wild_red/800` and darker plus `beyond_black/800` and darker all clear the white-contrast target, while the lightest steps remain safe for black foreground use.
- `beyond_black/*` should drive `neutral/*` rather than a second branded accent ladder.
- The approved semantic color extension now maps `brand/*`, `brand_secondary/*`, and `brand_tertiary/*` to `wild_red/*`, while `neutral/*` maps to `beyond_black/*`.

## Recommended Semantic Mapping

- `brand/*` -> `crested_butte/wild_red/*`
- `neutral/*` -> `crested_butte/beyond_black/*`
- `brand_secondary/*` -> `crested_butte/wild_red/*`
- `brand_tertiary/*` -> `crested_butte/wild_red/*`

## Review Readiness

- Subject: `Crested Butte primary palette`
  Channels: `web, email, ads`
  Rule: Reuse universal white, treat wild red as the primary brand ladder, and use beyond black as the neutral ladder.
  Source basis: Source image presents Powder White, Wild Red, and Beyond Black as the complete primary palette.
