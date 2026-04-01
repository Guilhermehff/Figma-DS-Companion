# Northstar Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/northstar/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `New Order`
  Safe family: `Afacad Flux`
  Style: `New Order Medium`
  Weight label: `Medium`
  Usage scope: `primary_display_headline`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `not specified in source`
  Size rule: `headline size not numerically specified`
  Punctuation: `punctuation required`
  Sample copy: `Headlines will be in New Order Medium in sentence case, left justified.`
  Notes: The source explicitly says headlines use New Order Medium, sentence case, left justified, and 0px tracking.

- Source role: `subhead`
  Family: `New Order`
  Safe family: `Afacad Flux`
  Style: `New Order Regular`
  Weight label: `Regular`
  Usage scope: `supporting_headline_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `equal_to_font_size`
  Size rule: `sub-headline size not numerically specified`
  Punctuation: `punctuation required`
  Sample copy: `Sub-Headlines will be in New Order Regular in sentence case, left justified.`
  Notes: The source explicitly says sub-headlines use New Order Regular and leading equal to type size.

- Source role: `body`
  Family: `New Order`
  Safe family: `Open Sans`
  Style: `New Order Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `1.8x type size`
  Size rule: `body size not numerically specified`
  Punctuation: `punctuation required`
  Sample copy: `Body Copy will be in New Order Regular in sentence case, left justified.`
  Notes: The source explicitly says body copy uses New Order Regular with leading set to 1.8 type size.

## Role Recipes

### Role: headline

Proposed family token: `northstar/family/01`

Safe family token: `northstar/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/800`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `headline size not numerically specified`
- Punctuation: `punctuation required`
- Notes: Left justified. The source explicitly requires punctuation on all reviewed copy types.

### Role: subhead

Proposed family token: `northstar/family/01`

Safe family token: `northstar/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/500`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `line-height equals font size`
- Size rule: `sub-headline size not numerically specified`
- Punctuation: `punctuation required`
- Notes: Left justified, with leading set to the same value as the font size.

### Role: body

Proposed family token: `northstar/family/01`

Safe family token: `northstar/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `1.8x type size`
- Size rule: `body size not numerically specified`
- Punctuation: `punctuation required`
- Notes: Left justified, with generous leading defined relative to the type size.
