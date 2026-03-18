# Afton Alps Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/afton_alps/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Blue`
  Provided value: `#112d5b`
  Usage scope: `primary brand palette`
  Notes: User approved Blue as the primary expressive lane in chat.

- Source color: `Yellow`
  Provided value: `#ffaf20`
  Usage scope: `secondary brand palette`
  Notes: User approved Yellow as the secondary expressive lane in chat.

## Universal Reuse

- No direct universal reuse. The supplied swatches are both branded expressive colors rather than exact universal primitives.

## Proposed Families

### Family: blue

Source anchor: `900_source`

Swatch strip:

<div>
  <span title="50 #f8fafd" style="display:inline-block;width:32px;height:32px;background:#f8fafd;border:1px solid #d1d5db;"></span>
  <span title="100 #eef1f5" style="display:inline-block;width:32px;height:32px;background:#eef1f5;border:1px solid #d1d5db;"></span>
  <span title="200 #dde3eb" style="display:inline-block;width:32px;height:32px;background:#dde3eb;border:1px solid #d1d5db;"></span>
  <span title="300 #c4ceda" style="display:inline-block;width:32px;height:32px;background:#c4ceda;border:1px solid #d1d5db;"></span>
  <span title="400 #a5b4c8" style="display:inline-block;width:32px;height:32px;background:#a5b4c8;border:1px solid #d1d5db;"></span>
  <span title="500 #8097b2" style="display:inline-block;width:32px;height:32px;background:#8097b2;border:1px solid #d1d5db;"></span>
  <span title="600 #5e7b9a" style="display:inline-block;width:32px;height:32px;background:#5e7b9a;border:1px solid #d1d5db;"></span>
  <span title="700 #426185" style="display:inline-block;width:32px;height:32px;background:#426185;border:1px solid #d1d5db;"></span>
  <span title="800 #28466f" style="display:inline-block;width:32px;height:32px;background:#28466f;border:1px solid #d1d5db;"></span>
  <span title="900 #112d5b" style="display:inline-block;width:32px;height:32px;background:#112d5b;border:1px solid #d1d5db;"></span>
  <span title="950 #071939" style="display:inline-block;width:32px;height:32px;background:#071939;border:1px solid #d1d5db;"></span>
</div>

### Family: yellow

Source anchor: `300_source`

Swatch strip:

<div>
  <span title="50 #fff9f1" style="display:inline-block;width:32px;height:32px;background:#fff9f1;border:1px solid #d1d5db;"></span>
  <span title="100 #ffedd6" style="display:inline-block;width:32px;height:32px;background:#ffedd6;border:1px solid #d1d5db;"></span>
  <span title="200 #ffdbaa" style="display:inline-block;width:32px;height:32px;background:#ffdbaa;border:1px solid #d1d5db;"></span>
  <span title="300 #ffaf20" style="display:inline-block;width:32px;height:32px;background:#ffaf20;border:1px solid #d1d5db;"></span>
  <span title="400 #eca000" style="display:inline-block;width:32px;height:32px;background:#eca000;border:1px solid #d1d5db;"></span>
  <span title="500 #be8529" style="display:inline-block;width:32px;height:32px;background:#be8529;border:1px solid #d1d5db;"></span>
  <span title="600 #8e6d40" style="display:inline-block;width:32px;height:32px;background:#8e6d40;border:1px solid #d1d5db;"></span>
  <span title="700 #66563f" style="display:inline-block;width:32px;height:32px;background:#66563f;border:1px solid #d1d5db;"></span>
  <span title="800 #463f35" style="display:inline-block;width:32px;height:32px;background:#463f35;border:1px solid #d1d5db;"></span>
  <span title="900 #2a2925" style="display:inline-block;width:32px;height:32px;background:#2a2925;border:1px solid #d1d5db;"></span>
  <span title="950 #161614" style="display:inline-block;width:32px;height:32px;background:#161614;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Afton Alps supplies two expressive colors and no branded neutral, so the first semantic pass keeps neutral roles inherited from the shared base.
- `blue` is dark enough to anchor the primary expressive lane, but the live default surface will use `blue/800` so the exact source `blue/900` remains available as the stronger branded step.
- `yellow` is a bright accent, so its live secondary role set will use black on the lighter surfaces and reserve white only for the darker emphasis step.

## Proposed Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> inherit shared base because no Afton Alps neutral swatch was supplied
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `afton_alps/blue/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `afton_alps/yellow/*`
- Global-only extra families: none
- `assets/logo` -> `Afton Alps`

## Review Readiness

- Subject: `Afton Alps expressive lane order`
  Channels: `web, email, ads`
  Rule: Use `blue` as the primary expressive lane and `yellow` as the secondary expressive lane.
  Source basis: User-approved lane order in chat.

- Subject: `Afton Alps bright secondary behavior`
  Channels: `web, email, ads`
  Rule: Keep black foreground on the lighter yellow surfaces and reserve white for the darker yellow emphasis step.
  Source basis: Contrast checks for the generated yellow ladder.
