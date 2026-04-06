# Seven Springs Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/seven_springs/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Hoss Sharp`
  Safe family: `Prompt`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary_display_headline`
  Case: `not specified in source`
  Tracking: `0px`
  Leading: `font_size_times_1`
  Size rule: `source gives family, weight, alignment, and relational leading only`
  Punctuation: `not specified in source`
  Sample copy: `THESE SLOPES WON'T SKI THEMSELVES`
  Notes: The source says all headlines are in Hoss Sharp Black, are left justified unless a layout calls for centering, use optical kerning, and use a 1:1 leading ratio.

- Source role: `subhead`
  Family: `Hoss Sharp`
  Safe family: `Prompt`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `not specified in source`
  Tracking: `0px`
  Leading: `font_size_times_1`
  Size rule: `source gives family, weight, alignment, and relational leading only`
  Punctuation: `not specified in source`
  Sample copy: `HEADLINES`
  Notes: The source says subheads are in Hoss Sharp Bold and follow the same alignment and leading rules as headlines.

- Source role: `body`
  Family: `Hoss Sharp`
  Safe family: `Prompt`
  Style: `Medium`
  Weight label: `Medium`
  Usage scope: `reading_copy`
  Case: `not specified in source`
  Tracking: `0px`
  Leading: `font_size_times_1_2`
  Size rule: `source gives family, weight, alignment, and relational leading only`
  Punctuation: `not specified in source`
  Sample copy: `Lorem ipsum dolor sit amet, consectetur adipiscing elit.`
  Notes: The source says all body copy is in Hoss Sharp Medium, left justified unless the layout calls for centering, with optical kerning and a 1:1.2 leading ratio.

- Source role: `cta`
  Family: `Hoss Sharp`
  Safe family: `Prompt`
  Style: `Heavy`
  Weight label: `Heavy`
  Usage scope: `action_or_button_copy`
  Case: `not specified in source`
  Tracking: `0px`
  Leading: `font_size_times_1`
  Size rule: `source gives family, weight, alignment, and relational leading only`
  Punctuation: `not specified in source`
  Sample copy: `BOOK YOUR WINTER VACATION`
  Notes: The source says all CTAs are in Hoss Sharp Heavy, left justified unless the layout calls for centering, with optical kerning and a 1:1 leading ratio.

## Role Recipes

### Role: headline

Proposed family token: `seven_springs/family/01`

Safe family token: `seven_springs/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `0px`
- Leading: `leading equals the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Left justified unless the layout calls for centering, with optical kerning.

### Role: subhead

Proposed family token: `seven_springs/family/01`

Safe family token: `seven_springs/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `0px`
- Leading: `leading equals the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: The live mapping routes the subhead recipe through `typography/weight/heading/strong` because the semantic theme typography model has no dedicated subhead slot.

### Role: body

Proposed family token: `seven_springs/family/01`

Safe family token: `seven_springs/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `0px`
- Leading: `1.2 times the font size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Reading copy remains on Hoss Sharp with Medium carrying the default body tone.

### Role: cta

Proposed family token: `seven_springs/family/01`

Safe family token: `seven_springs/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `inherited current action ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `0px`
- Leading: `leading equals the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Heavy stages on the strongest existing shared raw weight in the first pass.
