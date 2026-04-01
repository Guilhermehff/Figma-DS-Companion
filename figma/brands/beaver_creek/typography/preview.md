# Beaver Creek Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/beaver_creek/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `IvyPresto Display`
  Safe family: `Playfair Display`
  Style: `Thin`
  Weight label: `Thin`
  Usage scope: `primary_display_headline`
  Case: `not specified in source`
  Tracking: `90`
  Leading: `font_size_times_1_2`
  Size rule: `headline size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `Headlines`
  Notes: Headlines are center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `subhead_or_cta`
  Family: `Vinila Condensed`
  Safe family: `Playfair Display`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy_or_cta`
  Case: `not specified in source`
  Tracking: `80`
  Leading: `font_size_times_1_2`
  Size rule: `CTA and subheadline size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `CTA / Subheadlines`
  Notes: Sub-headlines and CTA are center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `body`
  Family: `Vinila`
  Safe family: `Open Sans`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `reading_copy`
  Case: `not specified in source`
  Tracking: `10`
  Leading: `font_size_times_1_7`
  Size rule: `body size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `All body copy should be in Light.`
  Notes: Body copy is center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `url`
  Family: `Vinila Condensed`
  Safe family: `Open Sans`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `non_clickable_url`
  Case: `mixed_case`
  Tracking: `120`
  Leading: `not specified in source`
  Size rule: `URL size not numerically specified`
  Punctuation: `Always include BeaverCreek.com when relevant to media is not clickable.`
  Sample copy: `BeaverCreek.com`
  Notes: Kerning is optical. The source treats this as a distinct utility recipe rather than a general CTA rule.

## Role Recipes

### Role: headline

Proposed family token: `beaver_creek/family/01`

Safe family token: `beaver_creek/family_safe/02`

Proposed weight token: `universal/weight/thin`

Proposed size token: `universal/size/700`

Recipe notes:

- Case: `not specified in source`
- Tracking: `90`
- Leading: `font size to leading ratio 1 to 1.2`
- Size rule: `headline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Center justified unless a specific layout calls for left justification.

### Role: subhead_or_cta

Proposed family token: `beaver_creek/family/03`

Safe family token: `beaver_creek/family_safe/02`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/400`

Recipe notes:

- Case: `not specified in source`
- Tracking: `80`
- Leading: `font size to leading ratio 1 to 1.2`
- Size rule: `CTA and subheadline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Center justified unless a specific layout calls for left justification.

### Role: body

Proposed family token: `beaver_creek/family/02`

Safe family token: `beaver_creek/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `universal/size/200`

Recipe notes:

- Case: `not specified in source`
- Tracking: `10`
- Leading: `font size to leading ratio 1 to 1.7`
- Size rule: `body size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Center justified unless a specific layout calls for left justification.

### Role: url

Proposed family token: `beaver_creek/family/03`

Safe family token: `beaver_creek/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `universal/size/100`

Recipe notes:

- Case: `mixed_case`
- Tracking: `120`
- Leading: `not specified in source`
- Size rule: `URL size not numerically specified`
- Punctuation: `Always include BeaverCreek.com when relevant to media is not clickable.`
- Notes: Raw-only utility recipe. It reuses the condensed family but does not alter the semantic action baseline.
