# Liberty Mountain Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/liberty_mountain/brand.yml` and Figma.

## Original Source Swatches

- Twilight: `#3f5364`
- Summit: `#748693`
- Tundra: `#748693`
- Shale: `#51879f`
- Stone: `#4e5758`
- Sand: `#b8b09b`
- Mineral: `#d7d2cb`
- Limestone: `#ebe7e3`
- Sunrise: `#ff5a34`
- Sunset: `#e18431`
- Flora: `#6a1f45`
- Spring: `#b8bf09`
- Copper: `#9d5f15`

## Source Notes

- The source text duplicates the numeric values for Summit and Tundra. The intake preserves the supplied text as-is rather than inventing a corrected raw value.
- The user approved `Sunrise` as the primary expressive lane and `Spring` as the supporting expressive lane.
- The user approved `Limestone`, `Mineral`, and `Sand` as one structural neutral ramp.

## Proposed Families

- `liberty_mountain/liberty_neutral/*`
  Source anchors: Limestone, Mineral, and Sand
  Purpose: structural neutral ramp for semantic neutral roles
- `liberty_mountain/sunrise/*`
  Source anchor: `#ff5a34`
  Purpose: primary expressive lane
- `liberty_mountain/spring/*`
  Source anchor: `#b8bf09`
  Purpose: supporting expressive lane

## Global-Only Raw Families

- `liberty_mountain/twilight/*`
- `liberty_mountain/summit/*`
- `liberty_mountain/tundra/*`
- `liberty_mountain/shale/*`
- `liberty_mountain/stone/*`
- `liberty_mountain/sand/*`
- `liberty_mountain/mineral/*`
- `liberty_mountain/limestone/*`
- `liberty_mountain/sunset/*`
- `liberty_mountain/flora/*`
- `liberty_mountain/copper/*`

## Proposed Semantic Mapping

- `surface/neutral/*`, `on_surface/neutral/*`, `foreground/default`, `foreground/subtle`, `border/default`, `border/subtle` -> `liberty_mountain/liberty_neutral/*`
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `liberty_mountain/sunrise/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `liberty_mountain/spring/*`
- Global-only extra families: Twilight, Summit, Tundra, Shale, Stone, Sand, Mineral, Limestone, Sunset, Flora, Copper
- Role exceptions: `assets/logo` -> `Liberty Mountain`

## Review Notes

- The live write should preserve every supplied palette color as a governed raw family, even when a subset also informs the composite neutral lane.
- The semantic neutral lane needs one coherent warm ladder, so the live write stages on `liberty_neutral` rather than aliasing three unrelated raw families one token at a time.

## Review Readiness

- Subject: `Liberty Mountain expressive lane order`
  Channels: `web`, `email`, `ads`
  Rule: Sunrise stages as brand primary and Spring stages as brand secondary.
  Source basis: User instruction in chat
- Subject: `Liberty Mountain neutral composition`
  Channels: `web`, `email`, `ads`
  Rule: Limestone, Mineral, and Sand form the structural neutral ramp.
  Source basis: User instruction in chat
