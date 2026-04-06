# Mad River Mountain Color Preview

Review state: written in figma. Verify live write state in `figma/brands/mad_river_mountain/brand.yml` and Figma.

## Original Source Swatches

- Source color: `River Blue`
  Provided value: `#4097db`

- Source color: `Mountain Green`
  Provided value: `#8fd16a`

## Universal Reuse

- Source color: `Black logo variation`
  Proposed token: `universal/black`
  Notes: Exact black remains inherited through the shared neutral baseline.

- Source color: `White logo variation`
  Proposed token: `universal/white`
  Notes: Exact white remains inherited through the shared neutral baseline.

## Proposed Families

### Family: river_blue

Source anchor: `500_source`

<div>
  <span title="100 #d5e8f7" style="display:inline-block;width:32px;height:32px;background:#d5e8f7;border:1px solid #d1d5db;"></span>
  <span title="200 #bad9f2" style="display:inline-block;width:32px;height:32px;background:#bad9f2;border:1px solid #d1d5db;"></span>
  <span title="300 #81bbe7" style="display:inline-block;width:32px;height:32px;background:#81bbe7;border:1px solid #d1d5db;"></span>
  <span title="400 #63aae2" style="display:inline-block;width:32px;height:32px;background:#63aae2;border:1px solid #d1d5db;"></span>
  <span title="500 #4097db" style="display:inline-block;width:32px;height:32px;background:#4097db;border:1px solid #d1d5db;"></span>
  <span title="600 #3276ac" style="display:inline-block;width:32px;height:32px;background:#3276ac;border:1px solid #d1d5db;"></span>
  <span title="700 #265a83" style="display:inline-block;width:32px;height:32px;background:#265a83;border:1px solid #d1d5db;"></span>
  <span title="800 #1b3f5c" style="display:inline-block;width:32px;height:32px;background:#1b3f5c;border:1px solid #d1d5db;"></span>
  <span title="900 #102536" style="display:inline-block;width:32px;height:32px;background:#102536;border:1px solid #d1d5db;"></span>
</div>

### Family: mountain_green

Source anchor: `500_source`

<div>
  <span title="100 #e6f5de" style="display:inline-block;width:32px;height:32px;background:#e6f5de;border:1px solid #d1d5db;"></span>
  <span title="200 #d7eec9" style="display:inline-block;width:32px;height:32px;background:#d7eec9;border:1px solid #d1d5db;"></span>
  <span title="300 #b5e19d" style="display:inline-block;width:32px;height:32px;background:#b5e19d;border:1px solid #d1d5db;"></span>
  <span title="400 #a4d985" style="display:inline-block;width:32px;height:32px;background:#a4d985;border:1px solid #d1d5db;"></span>
  <span title="500 #8fd16a" style="display:inline-block;width:32px;height:32px;background:#8fd16a;border:1px solid #d1d5db;"></span>
  <span title="600 #70a453" style="display:inline-block;width:32px;height:32px;background:#70a453;border:1px solid #d1d5db;"></span>
  <span title="700 #557d3f" style="display:inline-block;width:32px;height:32px;background:#557d3f;border:1px solid #d1d5db;"></span>
  <span title="800 #3c582c" style="display:inline-block;width:32px;height:32px;background:#3c582c;border:1px solid #d1d5db;"></span>
  <span title="900 #23341a" style="display:inline-block;width:32px;height:32px;background:#23341a;border:1px solid #d1d5db;"></span>
</div>

## Live Semantic Mapping

- Scope: `neutral` -> `inherited_base`
  Exact black and white remain inherited from the shared neutral baseline.
- Scope: `brand` -> `mad_river_mountain/river_blue`
  River Blue drives the primary expressive lane.
- Scope: `brand_secondary` -> `mad_river_mountain/mountain_green`
  Mountain Green drives the supporting expressive lane.
- `variables/assets/logo` -> `Mad River Mountain`

## Review Readiness

- Subject: `Mad River Mountain expressive mapping`
  Rule: Use `river_blue` for `brand/*` and `mountain_green` for `brand_secondary/*`.
