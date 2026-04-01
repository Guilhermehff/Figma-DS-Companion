# Park City Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/park_city/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Futura Std`
  Safe family: `Futura Bold`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `equal_to_point_size`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified in source`
  Sample copy: `THIS IS YOUR HEADLINE.`
  Notes: The source says headlines are all caps with 0px tracking, leading equal to the point size, and should usually be center justified.

- Source role: `subhead`
  Family: `Trade Gothic LT Std Bold Condensed No. 20`
  Safe family: `Futura Bold`
  Style: `Bold Condensed No. 20`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `all_caps`
  Tracking: `100px`
  Leading: `plus_2_over_point_size`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified in source`
  Sample copy: `THIS IS YOUR SUBHEAD.`
  Notes: The source explicitly uses the condensed Trade Gothic face for subheads with 100px tracking.

- Source role: `body`
  Family: `Futura Std`
  Safe family: `Open Sans`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `font_size_times_1_6`
  Size rule: `source gives no governed size token`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This is your body copy.`
  Notes: The source explicitly says body copy should be highly legible and use Futura Std Light with 0px tracking and 1.6x leading.

- Source role: `cta`
  Family: `Futura Std`
  Safe family: `Open Sans`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `action_or_button_copy`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `not specified in source`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified in source`
  Sample copy: `PLAN YOUR VISIT`
  Notes: The source explicitly names CTA as Futura Std Bold in all caps with 0px tracking.

## Role Recipes

### Role: headline

Proposed family token: `park_city/family/01`

Safe family token: `park_city/family_safe/02`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `leading equals the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Usually center justified, with left alignment allowed in certain layouts.

### Role: subhead

Proposed family token: `park_city/family/02`

Safe family token: `park_city/family_safe/02`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `all_caps`
- Tracking: `100px`
- Leading: `add 2 to the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Raw-only utility recipe. It remains outside the live semantic extension until a subhead lane exists.

### Role: body

Proposed family token: `park_city/family/01`

Safe family token: `park_city/family_safe/03`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `1.6 times the font size`
- Size rule: `no governed source size token`
- Punctuation: `sentence punctuation allowed`
- Notes: Reading copy remains on the primary family with weight carrying the distinction.

### Role: cta

Proposed family token: `park_city/family/01`

Safe family token: `park_city/family_safe/03`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current action ladder`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: The CTA lane stays on Futura Std Bold in all caps.
