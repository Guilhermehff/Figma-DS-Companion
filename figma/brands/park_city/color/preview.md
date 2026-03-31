# Park City Color Preview

Review state: written in figma. Verify live write state in `figma/brands/park_city/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Park City Red`
  Provided value: `#971b1f`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 187 C, CMYK 25-100-100-25, and RGB 151-27-31.

- Source color: `Bright Red`
  Provided value: `#db0032`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 199 C, CMYK 0-98-71-0, and RGB 219-0-50.

- Source color: `Pale Red`
  Provided value: `#f0d9ea`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 7436 C, CMYK 4-16-0-0, and RGB 240-217-234.

- Source color: `Park City Gray`
  Provided value: `#414042`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS 447 C, CMYK 0-0-0-90, and RGB 65-64-66.

- Source color: `Cool Gray`
  Provided value: `#b1b3b6`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists PMS Cool Gray 5 C, CMYK 0-0-0-30, and RGB 177-179-182.

- Source color: `White`
  Provided value: `#ffffff`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Exact white swatch shown in the palette image.

## Universal Reuse

- Source color: `White`
  Proposed token: `universal/white`
  Notes: Exact match to the shared universal white primitive, so no duplicate Park City white token is created.

## Color Proportion Guidance

Source basis: Approximate ratios inferred from the Park City ratio diagram plus the accompanying text that Bright Red should be treated as an accent rather than a dominant field. The source does not publish exact percentages.

### Brand Touchpoints

- Intent: `Pale Red and Park City Red carry most of the brand field. Bright Red stays accent-sized even when it is fully saturated. Cool Gray, Park City Gray, and White remain supporting neutrals outside the ratio bar.`
- Proportions:
  `Pale Red` -> `park_city/pale_red/300` (`50%`) Largest field in the proportion graphic and the branded wash behind the expressive red bars.
  `Park City Red` -> `park_city/park_city_red/700` (`30%`) Dominant horizontal brand bar in the ratio graphic and the main expressive lane.
  `Bright Red` -> `park_city/bright_red/600` (`20%`) Narrowest field in the ratio graphic and explicitly called out as more of an accent color.
- Notes:
  These percentages are approximate documentation guidance inferred from the displayed ratio diagram rather than exact published values.
  The source text explicitly says Bright Red should be treated more like an accent color, like arrow trios.

## Proposed Families

### Family: park_city_red

Source anchor: `700_source`

<div>
  <span title="100 #fff6f4" style="display:inline-block;width:32px;height:32px;background:#fff6f4;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe6e1" style="display:inline-block;width:32px;height:32px;background:#ffe6e1;border:1px solid #d1d5db;"></span>
  <span title="300 #ffb7b0" style="display:inline-block;width:32px;height:32px;background:#ffb7b0;border:1px solid #d1d5db;"></span>
  <span title="400 #ec978f" style="display:inline-block;width:32px;height:32px;background:#ec978f;border:1px solid #d1d5db;"></span>
  <span title="500 #d17169" style="display:inline-block;width:32px;height:32px;background:#d17169;border:1px solid #d1d5db;"></span>
  <span title="600 #b74b46" style="display:inline-block;width:32px;height:32px;background:#b74b46;border:1px solid #d1d5db;"></span>
  <span title="700 #971b1f" style="display:inline-block;width:32px;height:32px;background:#971b1f;border:1px solid #d1d5db;"></span>
  <span title="800 #761417" style="display:inline-block;width:32px;height:32px;background:#761417;border:1px solid #d1d5db;"></span>
  <span title="900 #340001" style="display:inline-block;width:32px;height:32px;background:#340001;border:1px solid #d1d5db;"></span>
</div>

### Family: bright_red

Source anchor: `600_source`

<div>
  <span title="100 #fff3f2" style="display:inline-block;width:32px;height:32px;background:#fff3f2;border:1px solid #d1d5db;"></span>
  <span title="200 #ffdfdc" style="display:inline-block;width:32px;height:32px;background:#ffdfdc;border:1px solid #d1d5db;"></span>
  <span title="300 #ffa7a5" style="display:inline-block;width:32px;height:32px;background:#ffa7a5;border:1px solid #d1d5db;"></span>
  <span title="400 #ff8181" style="display:inline-block;width:32px;height:32px;background:#ff8181;border:1px solid #d1d5db;"></span>
  <span title="500 #f15058" style="display:inline-block;width:32px;height:32px;background:#f15058;border:1px solid #d1d5db;"></span>
  <span title="600 #db0032" style="display:inline-block;width:32px;height:32px;background:#db0032;border:1px solid #d1d5db;"></span>
  <span title="700 #ab001f" style="display:inline-block;width:32px;height:32px;background:#ab001f;border:1px solid #d1d5db;"></span>
  <span title="800 #830010" style="display:inline-block;width:32px;height:32px;background:#830010;border:1px solid #d1d5db;"></span>
  <span title="900 #3d0000" style="display:inline-block;width:32px;height:32px;background:#3d0000;border:1px solid #d1d5db;"></span>
</div>

### Family: pale_red

Source anchor: `300_source`

<div>
  <span title="100 #fff8fc" style="display:inline-block;width:32px;height:32px;background:#fff8fc;border:1px solid #d1d5db;"></span>
  <span title="200 #f8e8f2" style="display:inline-block;width:32px;height:32px;background:#f8e8f2;border:1px solid #d1d5db;"></span>
  <span title="300 #f0d9ea" style="display:inline-block;width:32px;height:32px;background:#f0d9ea;border:1px solid #d1d5db;"></span>
  <span title="400 #d6a5be" style="display:inline-block;width:32px;height:32px;background:#d6a5be;border:1px solid #d1d5db;"></span>
  <span title="500 #c286a4" style="display:inline-block;width:32px;height:32px;background:#c286a4;border:1px solid #d1d5db;"></span>
  <span title="600 #a76886" style="display:inline-block;width:32px;height:32px;background:#a76886;border:1px solid #d1d5db;"></span>
  <span title="700 #8b4c68" style="display:inline-block;width:32px;height:32px;background:#8b4c68;border:1px solid #d1d5db;"></span>
  <span title="800 #6f334d" style="display:inline-block;width:32px;height:32px;background:#6f334d;border:1px solid #d1d5db;"></span>
  <span title="900 #331020" style="display:inline-block;width:32px;height:32px;background:#331020;border:1px solid #d1d5db;"></span>
</div>

### Family: park_city_gray

Source anchor: `800_source`

<div>
  <span title="100 #fafafb" style="display:inline-block;width:32px;height:32px;background:#fafafb;border:1px solid #d1d5db;"></span>
  <span title="200 #f0f1f2" style="display:inline-block;width:32px;height:32px;background:#f0f1f2;border:1px solid #d1d5db;"></span>
  <span title="300 #cacdcf" style="display:inline-block;width:32px;height:32px;background:#cacdcf;border:1px solid #d1d5db;"></span>
  <span title="400 #b1b3b6" style="display:inline-block;width:32px;height:32px;background:#b1b3b6;border:1px solid #d1d5db;"></span>
  <span title="500 #95979a" style="display:inline-block;width:32px;height:32px;background:#95979a;border:1px solid #d1d5db;"></span>
  <span title="600 #7a7c7f" style="display:inline-block;width:32px;height:32px;background:#7a7c7f;border:1px solid #d1d5db;"></span>
  <span title="700 #5f6164" style="display:inline-block;width:32px;height:32px;background:#5f6164;border:1px solid #d1d5db;"></span>
  <span title="800 #414042" style="display:inline-block;width:32px;height:32px;background:#414042;border:1px solid #d1d5db;"></span>
  <span title="900 #18181a" style="display:inline-block;width:32px;height:32px;background:#18181a;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Park City Red lands at `700` because the supplied swatch is already a dark, high-contrast brand red rather than a mid-tone accent.
- Bright Red lands at `600` because the supplied swatch sits cleanly in the governed mid-dark expressive band while still supporting lighter and darker steps above and below it.
- Pale Red is preserved as a dedicated raw tint family so the brand wash remains available without tinting the semantic neutral lane pink.
- Park City keeps `park_city_gray` as the semantic neutral family, but the reviewed ladder now stays genuinely gray while preserving `Cool Gray` at `400` and `Park City Gray` at `800`.
- Exact white is reused from `universal/white` rather than duplicated under the Park City group.

## Review Readiness

- Subject: `Park City neutral correction`
  Channels: `web, email, ads`
  Rule: Keep `park_city_gray` as a true gray neutral family for semantic neutral roles, and preserve `pale_red` as a separate raw family for branded wash usage.
  Source basis: The supplied palette includes a branded pale red wash, but semantic neutral surfaces need a coherent gray ladder anchored by Cool Gray and Park City Gray.

- Subject: `Park City expressive lane order`
  Channels: `web, email, ads`
  Rule: Keep `park_city_red` as the primary expressive lane and `bright_red` as the secondary expressive lane.
  Source basis: The palette image presents Park City Red as the dominant signature swatch and Bright Red as the supporting saturated accent.
