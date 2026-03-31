# Beaver Creek Color Preview

Review state: written in figma. Verify live write state in `figma/brands/beaver_creek/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Beaver Creek Primary Silver`
  Provided value: `#5c6f7c`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 92 111 124 and PMS 7545.

- Source color: `Beaver Creek Medium Silver`
  Provided value: `#80a1b6`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 128 161 182 and PMS 5425.

- Source color: `Beaver Creek Light Silver`
  Provided value: `#b9c7d4`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 185 199 212 and PMS 5435.

- Source color: `Beaver Creek Light Silver 25% Tint`
  Provided value: `#dee3e9`
  Usage scope: `primary_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 222 227 233 and PMS 5435 Tint 50%.

- Source color: `Beaver Creek White`
  Provided value: `#ffffff`
  Usage scope: `neutral_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Exact match to the shared universal white primitive.

- Source color: `Beaver Creek Black`
  Provided value: `#0a2030`
  Usage scope: `neutral_brand_palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists RGB 10 3 3, but the displayed HEX is `#0a2030`. Governance preserves the displayed HEX as the canonical source value until the source artifact is corrected.

## Universal Reuse

- Source color: `Beaver Creek White`
  Proposed token: `universal/white`
  Notes: Exact match to the shared universal white primitive, so no duplicate brand token is created.

## Color Proportion Guidance

Source basis: User-provided Beaver Creek palette guidance describes hierarchy in prose but does not publish numeric percentages.

### Brand Touchpoints

- Intent: `Primary Silver and White lead the composition to create an understated luxury mood. Medium and Light Silver support that system, while black remains a restrained dark anchor.`
- Dominant palette:
  `Beaver Creek Primary Silver` -> `beaver_creek/silver/700`
  `Beaver Creek White` -> `universal/white`
- Supporting palette:
  `Beaver Creek Medium Silver` -> `beaver_creek/silver/500`
  `Beaver Creek Light Silver` -> `beaver_creek/silver/300`
  `Beaver Creek Light Silver 25% Tint` -> `beaver_creek/silver/200`
  `Beaver Creek Black` -> `beaver_creek/silver/900`
- Notes:
  The source describes the palette as minimal, led by three silver tones and supported by a rich black.
  The source explicitly says Primary Silver and White should lead in execution.

## Proposed Families

### Family: silver

Source anchors: `100_source / 300_source / 500_source / 700_source / 900_source`

<div>
  <span title="100 #eef1f4" style="display:inline-block;width:32px;height:32px;background:#eef1f4;border:1px solid #d1d5db;"></span>
  <span title="200 #dee3e9" style="display:inline-block;width:32px;height:32px;background:#dee3e9;border:1px solid #d1d5db;"></span>
  <span title="300 #b9c7d4" style="display:inline-block;width:32px;height:32px;background:#b9c7d4;border:1px solid #d1d5db;"></span>
  <span title="400 #9cb4c5" style="display:inline-block;width:32px;height:32px;background:#9cb4c5;border:1px solid #d1d5db;"></span>
  <span title="500 #80a1b6" style="display:inline-block;width:32px;height:32px;background:#80a1b6;border:1px solid #d1d5db;"></span>
  <span title="600 #6e8898" style="display:inline-block;width:32px;height:32px;background:#6e8898;border:1px solid #d1d5db;"></span>
  <span title="700 #5c6f7c" style="display:inline-block;width:32px;height:32px;background:#5c6f7c;border:1px solid #d1d5db;"></span>
  <span title="800 #3a4e5c" style="display:inline-block;width:32px;height:32px;background:#3a4e5c;border:1px solid #d1d5db;"></span>
  <span title="900 #0a2030" style="display:inline-block;width:32px;height:32px;background:#0a2030;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- The supplied palette behaves as one blue-silver neutral system, so the ramp keeps every provided swatch on one coherent OKLCH ladder instead of splitting the family into separate neutral and accent groups.
- Exact white is intentionally reused from `universal/white`, while the supplied near-black anchors the silver family at `950` so the family can support both neutral and expressive semantic roles.
- {"Approved exception"=>"the same silver family feeds semantic `neutral/*`, `brand/*`, and `brand_secondary/*` for Beaver Creek."}

## Review Readiness

- Subject: `Beaver Creek silver system`
  Channels: `web, email, ads`
  Rule: Use the governed silver ladder as the one approved Beaver Creek family, with exact white reused from `universal/white`.
  Source basis: Source image explicitly provides four silver steps plus white and black.

- Subject: `Beaver Creek semantic neutral mapping`
  Channels: `web, email, ads`
  Rule: Map the silver family to semantic `neutral/*` because the source behaves as a branded background and surface system.
  Source basis: Accepted neutral-family governance and the supplied light, tint, and near-black support swatches.

- Subject: `Beaver Creek expressive semantic exception`
  Channels: `web, email, ads`
  Rule: Also map the same silver family to semantic `brand/*` and `brand_secondary/*` per the explicit user-approved exception for this brand.
  Source basis: User approval of option 2 in chat on 2026-03-17.
