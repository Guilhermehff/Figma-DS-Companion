# Vail Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/vail/brand.yml` and Figma.

## Original Source Roles

- Source role: `eyebrow`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `section_header_or_hierarchy_breaker`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `use_text_height_to_inform_spacing_between_lines`
  Size rule: `0.5x headline size`
  Punctuation: `not specified`
  Sample copy: `SAMPLE EYEBROW`
  Notes: Use to break up the headline for stronger hierarchy or as a section title or header. Stroke width should be as thick as the text.

- Source role: `headline`
  Family: `Termina`
  Safe family: `Open Sans`
  Style: `Termina Black`
  Weight label: `Black`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `equal_to_font_size`
  Size rule: `base headline size not numerically specified`
  Punctuation: `No end punctuation by default. Exceptions allowed for exclamation points, question marks, and two short thoughts in one headline.`
  Sample copy: `HEADLINES SHOULD ALWAYS BE IN TERMINA`
  Notes: Headline style should be all caps.

- Source role: `subhead`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `supporting_headline_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `0.5x headline size`
  Punctuation: `punctuation allowed`
  Sample copy: `This is your subhead.`
  Notes: Subhead is half the size of headline type.

- Source role: `body`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `1.6x type size`
  Size rule: `base body size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This is your body copy. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sodales diam ut metus bibendum sodales. Curabitur congue ligula et leo scelerisque lacinia.`
  Notes: Avoid widows and orphans if possible.

- Source role: `cta`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `action_or_button_copy`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `base CTA size not numerically specified`
  Punctuation: `do not use end punctuation`
  Sample copy: `PLAN YOUR VISIT`
  Notes: CTA styling is all caps.

## Role Recipes

### Role: eyebrow

Proposed family token: `vail/family/02`

Safe family token: `vail/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/core/400`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `Use text height to inform spacing between lines`
- Size rule: `0.5x headline size`
- Punctuation: `not specified in source`
- Notes: Use as a section title or header and to break up headline hierarchy. Stroke width should be as thick as the text.

### Role: headline

Proposed family token: `vail/family/01`

Safe family token: `vail/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/core/800`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `line-height equals font size`
- Size rule: `headline base size not numerically specified`
- Punctuation: `No end punctuation by default. Exceptions allowed for question marks, exclamation points, and paired short thoughts.`
- Notes: Primary display treatment.

### Role: subhead

Proposed family token: `vail/family/02`

Safe family token: `vail/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/core/400`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `0.5x headline size`
- Punctuation: `punctuation allowed`
- Notes: Intended as secondary supporting headline copy.

### Role: body

Proposed family token: `vail/family/02`

Safe family token: `vail/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/core/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `1.6x type size`
- Size rule: `body base size not numerically specified`
- Punctuation: `sentence punctuation allowed`
- Notes: Avoid widows and orphans when setting copy.

### Role: cta

Proposed family token: `vail/family/02`

Safe family token: `vail/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/core/300`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `CTA base size not numerically specified`
- Punctuation: `do not use end punctuation`
- Notes: Intended for action-oriented interface copy.
