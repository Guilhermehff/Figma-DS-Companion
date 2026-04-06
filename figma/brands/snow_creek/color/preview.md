# Snow Creek Color Preview

Review state: written in figma. Verify live write state in `figma/brands/snow_creek/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Creek Blue`
  Provided value: `#00303e`

- Source color: `Tagline Gold`
  Provided value: `#dbae27`

- Source color: `Snow White`
  Provided value: `#f5f5f0`

## Universal Reuse

- Source color: `Black logo variation`
  Proposed token: `universal/black`
  Notes: Exact black remains inherited through the shared neutral baseline.

## Proposed Families

### Family: creek_blue

Source anchor: `900_source`

<div>
  <span title="100 #f2f8fa" style="display:inline-block;width:32px;height:32px;background:#f2f8fa;border:1px solid #d1d5db;"></span>
  <span title="200 #e1eff3" style="display:inline-block;width:32px;height:32px;background:#e1eff3;border:1px solid #d1d5db;"></span>
  <span title="300 #9ec7d3" style="display:inline-block;width:32px;height:32px;background:#9ec7d3;border:1px solid #d1d5db;"></span>
  <span title="400 #75adbe" style="display:inline-block;width:32px;height:32px;background:#75adbe;border:1px solid #d1d5db;"></span>
  <span title="500 #4f93a6" style="display:inline-block;width:32px;height:32px;background:#4f93a6;border:1px solid #d1d5db;"></span>
  <span title="600 #3b7688" style="display:inline-block;width:32px;height:32px;background:#3b7688;border:1px solid #d1d5db;"></span>
  <span title="700 #2a5b69" style="display:inline-block;width:32px;height:32px;background:#2a5b69;border:1px solid #d1d5db;"></span>
  <span title="800 #1c424d" style="display:inline-block;width:32px;height:32px;background:#1c424d;border:1px solid #d1d5db;"></span>
  <span title="900 #00303e" style="display:inline-block;width:32px;height:32px;background:#00303e;border:1px solid #d1d5db;"></span>
</div>

### Family: tagline_gold

Source anchor: `300_source`

<div>
  <span title="100 #fdf4d6" style="display:inline-block;width:32px;height:32px;background:#fdf4d6;border:1px solid #d1d5db;"></span>
  <span title="200 #f6e6b0" style="display:inline-block;width:32px;height:32px;background:#f6e6b0;border:1px solid #d1d5db;"></span>
  <span title="300 #dbae27" style="display:inline-block;width:32px;height:32px;background:#dbae27;border:1px solid #d1d5db;"></span>
  <span title="400 #c79a22" style="display:inline-block;width:32px;height:32px;background:#c79a22;border:1px solid #d1d5db;"></span>
  <span title="500 #ad831c" style="display:inline-block;width:32px;height:32px;background:#ad831c;border:1px solid #d1d5db;"></span>
  <span title="600 #8f6b17" style="display:inline-block;width:32px;height:32px;background:#8f6b17;border:1px solid #d1d5db;"></span>
  <span title="700 #725513" style="display:inline-block;width:32px;height:32px;background:#725513;border:1px solid #d1d5db;"></span>
  <span title="800 #57400f" style="display:inline-block;width:32px;height:32px;background:#57400f;border:1px solid #d1d5db;"></span>
  <span title="900 #2c2308" style="display:inline-block;width:32px;height:32px;background:#2c2308;border:1px solid #d1d5db;"></span>
</div>

### Family: snow_white

Source anchor: `100_source`

<div>
  <span title="100 #fafaf7" style="display:inline-block;width:32px;height:32px;background:#fafaf7;border:1px solid #d1d5db;"></span>
  <span title="200 #f5f5f0" style="display:inline-block;width:32px;height:32px;background:#f5f5f0;border:1px solid #d1d5db;"></span>
  <span title="300 #bbbbb7" style="display:inline-block;width:32px;height:32px;background:#bbbbb7;border:1px solid #d1d5db;"></span>
  <span title="400 #a1a19e" style="display:inline-block;width:32px;height:32px;background:#a1a19e;border:1px solid #d1d5db;"></span>
  <span title="500 #888886" style="display:inline-block;width:32px;height:32px;background:#888886;border:1px solid #d1d5db;"></span>
  <span title="600 #70706e" style="display:inline-block;width:32px;height:32px;background:#70706e;border:1px solid #d1d5db;"></span>
  <span title="700 #595957" style="display:inline-block;width:32px;height:32px;background:#595957;border:1px solid #d1d5db;"></span>
  <span title="800 #414140" style="display:inline-block;width:32px;height:32px;background:#414140;border:1px solid #d1d5db;"></span>
  <span title="900 #141413" style="display:inline-block;width:32px;height:32px;background:#141413;border:1px solid #d1d5db;"></span>
</div>

## Live Semantic Mapping

- Scope: `neutral` -> `inherited_base`
  The first pass keeps neutral roles inherited instead of promoting `snow_white` into the neutral ladder.
- Scope: `brand` -> `snow_creek/creek_blue`
  Creek Blue drives the primary expressive lane.
- Scope: `brand_secondary` -> `snow_creek/tagline_gold`
  Tagline Gold drives the supporting expressive lane.
- Global-only families: `snow_creek/snow_white`
- `variables/assets/logo` -> `Snow Creek`

## Review Readiness

- Subject: `Snow Creek expressive mapping`
  Rule: Use `creek_blue` for `brand/*` and `tagline_gold` for `brand_secondary/*`.

- Subject: `Snow Creek neutral treatment`
  Rule: Keep `snow_white` raw-only in the first pass rather than promoting it into the neutral semantic ladder.
