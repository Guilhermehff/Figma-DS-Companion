# Afton Alps Color Preview

Review state: written in figma. Verify live write state in `figma/brands/afton_alps/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Blue`
  Provided value: `#112d5b`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: User approved Blue as the primary expressive lane in chat.

- Source color: `Yellow`
  Provided value: `#ffaf20`
  Usage scope: `secondary brand palette`
  Channel restrictions: `not specified in source`
  Notes: User approved Yellow as the secondary expressive lane in chat.

## Universal Reuse

- No exact Afton Alps source swatch reuses an existing universal color primitive in this pass.

## Proposed Families

### Family: blue

Source anchor: `900_source`

<div>
  <span title="100 #f8fafd" style="display:inline-block;width:32px;height:32px;background:#f8fafd;border:1px solid #d1d5db;"></span>
  <span title="200 #eef1f5" style="display:inline-block;width:32px;height:32px;background:#eef1f5;border:1px solid #d1d5db;"></span>
  <span title="300 #c4ceda" style="display:inline-block;width:32px;height:32px;background:#c4ceda;border:1px solid #d1d5db;"></span>
  <span title="400 #a5b4c8" style="display:inline-block;width:32px;height:32px;background:#a5b4c8;border:1px solid #d1d5db;"></span>
  <span title="500 #8097b2" style="display:inline-block;width:32px;height:32px;background:#8097b2;border:1px solid #d1d5db;"></span>
  <span title="600 #5e7b9a" style="display:inline-block;width:32px;height:32px;background:#5e7b9a;border:1px solid #d1d5db;"></span>
  <span title="700 #426185" style="display:inline-block;width:32px;height:32px;background:#426185;border:1px solid #d1d5db;"></span>
  <span title="800 #28466f" style="display:inline-block;width:32px;height:32px;background:#28466f;border:1px solid #d1d5db;"></span>
  <span title="900 #112d5b" style="display:inline-block;width:32px;height:32px;background:#112d5b;border:1px solid #d1d5db;"></span>
</div>

### Family: yellow

Source anchor: `300_source`

<div>
  <span title="100 #fff9f1" style="display:inline-block;width:32px;height:32px;background:#fff9f1;border:1px solid #d1d5db;"></span>
  <span title="200 #ffedd6" style="display:inline-block;width:32px;height:32px;background:#ffedd6;border:1px solid #d1d5db;"></span>
  <span title="300 #ffaf20" style="display:inline-block;width:32px;height:32px;background:#ffaf20;border:1px solid #d1d5db;"></span>
  <span title="400 #eca000" style="display:inline-block;width:32px;height:32px;background:#eca000;border:1px solid #d1d5db;"></span>
  <span title="500 #be8529" style="display:inline-block;width:32px;height:32px;background:#be8529;border:1px solid #d1d5db;"></span>
  <span title="600 #8e6d40" style="display:inline-block;width:32px;height:32px;background:#8e6d40;border:1px solid #d1d5db;"></span>
  <span title="700 #66563f" style="display:inline-block;width:32px;height:32px;background:#66563f;border:1px solid #d1d5db;"></span>
  <span title="800 #463f35" style="display:inline-block;width:32px;height:32px;background:#463f35;border:1px solid #d1d5db;"></span>
  <span title="900 #161614" style="display:inline-block;width:32px;height:32px;background:#161614;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Afton Alps Blue lands at `900` because the supplied swatch sits in the dark-navy lightness band and is materially darker than the existing `800` blue anchors used by other brands.
- Afton Alps Yellow lands at `300` because the supplied swatch behaves as a bright accent rather than a midtone.
- The first semantic pass inherits the shared neutral role set because no branded neutral swatch was supplied.
- The primary blue semantic lane uses `blue/800` for default surfaces so the exact source `blue/900` can remain the stronger branded text and emphasis step.

## Live Semantic Mapping

- `color/surface/neutral/*`, `color/on_surface/neutral/*`, `color/foreground/default`, `color/foreground/subtle`, `color/border/default`, `color/border/subtle` -> `inherited_base`
  No Afton Alps neutral swatches were supplied, so the shared neutral role set remains inherited from the semantic base collection.
- `color/surface/brand/*`, `color/on_surface/brand/*`, `color/foreground/brand`, `color/border/brand` -> `afton_alps/blue`
  Blue is the user-approved primary expressive lane and behaves as a dark brand family.
- `color/surface/brand_secondary/*`, `color/on_surface/brand_secondary/*`, `color/foreground/brand_secondary`, `color/border/brand_secondary` -> `afton_alps/yellow`
  Yellow is the user-approved secondary expressive lane and behaves as a bright accent family.
- `variables/assets/logo` -> `Afton Alps`
  The live `Semantic: Theme` schema includes `variables/assets/logo`, and each brand extension overrides it to the brand display name string.

## Review Readiness

- Subject: `Afton Alps lane order`
  Channels: `web, email, ads`
  Rule: Use `blue` as the primary expressive lane and `yellow` as the secondary expressive lane.
  Source basis: User-approved lane order in chat.

- Subject: `Afton Alps neutral inheritance`
  Channels: `web, email, ads`
  Rule: Keep neutral roles inherited from the shared base because no branded neutral swatch was supplied.
  Source basis: Source image provides only blue and yellow.
