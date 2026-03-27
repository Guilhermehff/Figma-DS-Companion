# Park City Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/park_city/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Park City Red`
  Provided value: `#971b1f`
  Usage scope: `primary brand palette`
  Notes: Source image lists PMS `187 C`, CMYK `25-100-100-25`, and RGB `151-27-31`.

- Source color: `Bright Red`
  Provided value: `#db0032`
  Usage scope: `primary brand palette`
  Notes: Source image lists PMS `199 C`, CMYK `0-98-71-0`, and RGB `219-0-50`.

- Source color: `Pale Red`
  Provided value: `#f0d9ea`
  Usage scope: `primary brand palette`
  Notes: Source image lists PMS `7436 C`, CMYK `4-16-0-0`, and RGB `240-217-234`.

- Source color: `Park City Gray`
  Provided value: `#414042`
  Usage scope: `primary brand palette`
  Notes: Source image lists PMS `447 C`, CMYK `0-0-0-90`, and RGB `65-64-66`.

- Source color: `Cool Gray`
  Provided value: `#b1b3b6`
  Usage scope: `primary brand palette`
  Notes: Source image lists PMS `Cool Gray 5 C`, CMYK `0-0-0-30`, and RGB `177-179-182`.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Notes: Exact shared white.

## Universal Reuse

- `White` reuses `universal/white`.

## Color Proportion Guidance

### Brand Touchpoints

- Intent: `Pale Red` and `Park City Red` carry most of the brand field. `Bright Red` stays accent-sized even when it is fully saturated. `Cool Gray`, `Park City Gray`, and `White` remain supporting neutrals outside the ratio bar.
- `Pale Red`: `50%`
  DS mapping: `park_city/park_city_gray/200`
- `Park City Red`: `30%`
  DS mapping: `park_city/park_city_red/700`
- `Bright Red`: `20%`
  DS mapping: `park_city/bright_red/600`
- Notes: These values are approximate documentation guidance inferred from the displayed ratio diagram rather than exact published values. The source text explicitly says `Bright Red` should be treated more like an accent color, like arrow trios.

## Proposed Families

### Family: park_city_red

Source anchor: `700_source`

Swatch strip:

<div>
  <span title="50 #fff6f4" style="display:inline-block;width:32px;height:32px;background:#fff6f4;border:1px solid #d1d5db;"></span>
  <span title="100 #ffe6e1" style="display:inline-block;width:32px;height:32px;background:#ffe6e1;border:1px solid #d1d5db;"></span>
  <span title="200 #ffd2cc" style="display:inline-block;width:32px;height:32px;background:#ffd2cc;border:1px solid #d1d5db;"></span>
  <span title="300 #ffb7b0" style="display:inline-block;width:32px;height:32px;background:#ffb7b0;border:1px solid #d1d5db;"></span>
  <span title="400 #ec978f" style="display:inline-block;width:32px;height:32px;background:#ec978f;border:1px solid #d1d5db;"></span>
  <span title="500 #d17169" style="display:inline-block;width:32px;height:32px;background:#d17169;border:1px solid #d1d5db;"></span>
  <span title="600 #b74b46" style="display:inline-block;width:32px;height:32px;background:#b74b46;border:1px solid #d1d5db;"></span>
  <span title="700 #971b1f" style="display:inline-block;width:32px;height:32px;background:#971b1f;border:1px solid #d1d5db;"></span>
  <span title="800 #761417" style="display:inline-block;width:32px;height:32px;background:#761417;border:1px solid #d1d5db;"></span>
  <span title="900 #520308" style="display:inline-block;width:32px;height:32px;background:#520308;border:1px solid #d1d5db;"></span>
  <span title="950 #340001" style="display:inline-block;width:32px;height:32px;background:#340001;border:1px solid #d1d5db;"></span>
</div>

### Family: bright_red

Source anchor: `600_source`

Swatch strip:

<div>
  <span title="50 #fff3f2" style="display:inline-block;width:32px;height:32px;background:#fff3f2;border:1px solid #d1d5db;"></span>
  <span title="100 #ffdfdc" style="display:inline-block;width:32px;height:32px;background:#ffdfdc;border:1px solid #d1d5db;"></span>
  <span title="200 #ffc7c3" style="display:inline-block;width:32px;height:32px;background:#ffc7c3;border:1px solid #d1d5db;"></span>
  <span title="300 #ffa7a5" style="display:inline-block;width:32px;height:32px;background:#ffa7a5;border:1px solid #d1d5db;"></span>
  <span title="400 #ff8181" style="display:inline-block;width:32px;height:32px;background:#ff8181;border:1px solid #d1d5db;"></span>
  <span title="500 #f15058" style="display:inline-block;width:32px;height:32px;background:#f15058;border:1px solid #d1d5db;"></span>
  <span title="600 #db0032" style="display:inline-block;width:32px;height:32px;background:#db0032;border:1px solid #d1d5db;"></span>
  <span title="700 #ab001f" style="display:inline-block;width:32px;height:32px;background:#ab001f;border:1px solid #d1d5db;"></span>
  <span title="800 #830010" style="display:inline-block;width:32px;height:32px;background:#830010;border:1px solid #d1d5db;"></span>
  <span title="900 #5d0002" style="display:inline-block;width:32px;height:32px;background:#5d0002;border:1px solid #d1d5db;"></span>
  <span title="950 #3d0000" style="display:inline-block;width:32px;height:32px;background:#3d0000;border:1px solid #d1d5db;"></span>
</div>

### Family: park_city_gray

Source anchors: `200_source = Pale Red`, `400_source = Cool Gray`, `800_source = Park City Gray`

Swatch strip:

<div>
  <span title="50 #fff7fd" style="display:inline-block;width:32px;height:32px;background:#fff7fd;border:1px solid #d1d5db;"></span>
  <span title="100 #f9ecf5" style="display:inline-block;width:32px;height:32px;background:#f9ecf5;border:1px solid #d1d5db;"></span>
  <span title="200 #f0d9ea" style="display:inline-block;width:32px;height:32px;background:#f0d9ea;border:1px solid #d1d5db;"></span>
  <span title="300 #d3c8d2" style="display:inline-block;width:32px;height:32px;background:#d3c8d2;border:1px solid #d1d5db;"></span>
  <span title="400 #b1b3b6" style="display:inline-block;width:32px;height:32px;background:#b1b3b6;border:1px solid #d1d5db;"></span>
  <span title="500 #8f9193" style="display:inline-block;width:32px;height:32px;background:#8f9193;border:1px solid #d1d5db;"></span>
  <span title="600 #727375" style="display:inline-block;width:32px;height:32px;background:#727375;border:1px solid #d1d5db;"></span>
  <span title="700 #58585a" style="display:inline-block;width:32px;height:32px;background:#58585a;border:1px solid #d1d5db;"></span>
  <span title="800 #414042" style="display:inline-block;width:32px;height:32px;background:#414042;border:1px solid #d1d5db;"></span>
  <span title="900 #29282a" style="display:inline-block;width:32px;height:32px;background:#29282a;border:1px solid #d1d5db;"></span>
  <span title="950 #161617" style="display:inline-block;width:32px;height:32px;background:#161617;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Park City stages one absorbed neutral family, `park_city_gray`, from the supplied pale pink wash through the cool gray mid-tone to the dark brand gray.
- `park_city_red` is the dominant expressive lane, while `bright_red` remains the supporting saturated lane.
- Exact white stays shared through `universal/white`.

## Proposed Semantic Mapping

- `surface/neutral/canvas`, `surface/neutral/subtle`, `surface/neutral/default`, `surface/neutral/strong`, `surface/neutral/emphasis` -> `park_city/park_city_gray/50`, `100`, `200`, `300`, `400`
- `on_surface/neutral/*`, `foreground/default`, `foreground/subtle` -> `park_city/park_city_gray/800` or `700`
- `border/default`, `border/subtle` -> `park_city/park_city_gray/400` and `300`
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `park_city/park_city_red/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `park_city/bright_red/*`
- `assets/logo` -> `Park City`

## Review Readiness

- Subject: `Park City neutral system`
  Channels: `web, email, ads`
  Rule: Keep the pale pink wash and the supplied grays in one governed neutral lane rather than inventing a separate third expressive family.
  Source basis: The palette and ratio image use these three swatches together as one background-to-contrast system.

- Subject: `Park City expressive lane order`
  Channels: `web, email, ads`
  Rule: Use Park City Red as the primary expressive lane and Bright Red as the secondary expressive lane.
  Source basis: The palette image presents Park City Red as the dominant brand swatch and Bright Red as the supporting vivid accent.
