# Beaver Creek Color Preview

Review state: approved preview artifact after explicit approval to let the Beaver Creek silver system drive neutral, brand, and brand-secondary semantic lanes. Verify live write state in `figma/brands/beaver_creek/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Beaver Creek Primary Silver`
  Provided value: `#5c6f7c`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `92 111 124`.

- Source color: `Beaver Creek Medium Silver`
  Provided value: `#80a1b6`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `128 161 182`.

- Source color: `Beaver Creek Light Silver`
  Provided value: `#b9c7d4`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `185 199 212`.

- Source color: `Beaver Creek Light Silver 25% Tint`
  Provided value: `#dee3e9`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `222 227 233`.

- Source color: `Beaver Creek White`
  Provided value: `#ffffff`
  Usage scope: `neutral brand palette`
  Notes: Exact shared white.

- Source color: `Beaver Creek Black`
  Provided value: `#0a2030`
  Usage scope: `neutral brand palette`
  Notes: Governance preserves the displayed HEX from the source image.

## Universal Reuse

- `Beaver Creek White` reuses `universal/white`.

## Color Proportion Guidance

### Brand Touchpoints

- Intent: `Primary Silver` and `White` lead the composition to create an understated luxury mood. `Medium Silver` and `Light Silver` support that system, while `Black` remains a restrained dark anchor.
- Dominant palette:
  `Beaver Creek Primary Silver` -> `beaver_creek/silver/700`
  `Beaver Creek White` -> `universal/white`
- Supporting palette:
  `Beaver Creek Medium Silver` -> `beaver_creek/silver/500`
  `Beaver Creek Light Silver` -> `beaver_creek/silver/300`
  `Beaver Creek Light Silver 25% Tint` -> `beaver_creek/silver/100`
  `Beaver Creek Black` -> `beaver_creek/silver/950`
- Notes:
  The source describes the palette as minimal, led by three silver tones and supported by a rich black.
  The source explicitly says `Primary Silver` and `White` should lead in execution.

## Proposed Family

### Family: silver

Source anchor: `100_source`, `300_source`, `500_source`, `700_source`, and `950_source`

Swatch strip:

<div>
  <span title="50 #eef1f4" style="display:inline-block;width:32px;height:32px;background:#eef1f4;border:1px solid #d1d5db;"></span>
  <span title="100 #dee3e9" style="display:inline-block;width:32px;height:32px;background:#dee3e9;border:1px solid #d1d5db;"></span>
  <span title="200 #cbd5de" style="display:inline-block;width:32px;height:32px;background:#cbd5de;border:1px solid #d1d5db;"></span>
  <span title="300 #b9c7d4" style="display:inline-block;width:32px;height:32px;background:#b9c7d4;border:1px solid #d1d5db;"></span>
  <span title="400 #9cb4c5" style="display:inline-block;width:32px;height:32px;background:#9cb4c5;border:1px solid #d1d5db;"></span>
  <span title="500 #80a1b6" style="display:inline-block;width:32px;height:32px;background:#80a1b6;border:1px solid #d1d5db;"></span>
  <span title="600 #6e8898" style="display:inline-block;width:32px;height:32px;background:#6e8898;border:1px solid #d1d5db;"></span>
  <span title="700 #5c6f7c" style="display:inline-block;width:32px;height:32px;background:#5c6f7c;border:1px solid #d1d5db;"></span>
  <span title="800 #3a4e5c" style="display:inline-block;width:32px;height:32px;background:#3a4e5c;border:1px solid #d1d5db;"></span>
  <span title="900 #1a2f3e" style="display:inline-block;width:32px;height:32px;background:#1a2f3e;border:1px solid #d1d5db;"></span>
  <span title="950 #0a2030" style="display:inline-block;width:32px;height:32px;background:#0a2030;border:1px solid #d1d5db;"></span>
</div>

Hex values:

- `50`: `#eef1f4`
- `100`: `#dee3e9`
- `200`: `#cbd5de`
- `300`: `#b9c7d4`
- `400`: `#9cb4c5`
- `500`: `#80a1b6`
- `600`: `#6e8898`
- `700`: `#5c6f7c`
- `800`: `#3a4e5c`
- `900`: `#1a2f3e`
- `950`: `#0a2030`

## Review Notes

- Beaver Creek stages on one silver family that absorbs the provided tint, light, medium, primary, and near-black swatches into one coherent ladder.
- Exact white remains a shared universal primitive and is not duplicated under the Beaver Creek brand group.
- Approved exception: `beaver_creek/silver/*` also drives `brand/*` and `brand_secondary/*`, not only `neutral/*`.

## Recommended Semantic Mapping

- `neutral/*` -> `beaver_creek/silver/*`
- `brand/*` -> `beaver_creek/silver/*`
- `brand_secondary/*` -> `beaver_creek/silver/*`
- Global-only extra families: none

## Review Readiness

- Subject: `Beaver Creek silver system`
  Channels: `web, email, ads`
  Rule: Keep the staged silver ladder as the one approved Beaver Creek family, with exact white reused from `universal/white`.
  Source basis: Source image explicitly provides the silver, tint, white, and near-black system.

- Subject: `Beaver Creek semantic exception`
  Channels: `web, email, ads`
  Rule: Reuse the silver ladder for neutral, brand, and brand-secondary semantic lanes.
  Source basis: Explicit user approval in chat on `2026-03-17`.
