# Kirkwood Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/kirkwood/brand.yml` and Figma.

## Original Source Roles

- Source role: `title_or_small_type`
  Family: `Futura`
  Safe family: `Futura`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `title lines and small type elements`
  Case: `all_caps_or_title_case`
  Tracking: `not specified in source`
  Leading: `around_120_percent_of_font_height`
  Size rule: `title size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `Futura Bold`
  Notes: The source says to use Futura Bold in all caps as well as title case and to keep leading around 120 percent of font height.

- Source role: `headline`
  Family: `Trade Gothic Condensed No. 20`
  Safe family: `Futura`
  Style: `Trade Gothic Bold Condensed No. 20`
  Weight label: `Bold`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `not specified in source`
  Leading: `100_percent_of_font_height_or_less`
  Size rule: `headline size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `ABCDEFGHIJKLMNOP QRSTUVWXYZ`
  Notes: The source explicitly says headlines should use this family in all caps only and can be stacked to create a more square headline shape.

- Source role: `body`
  Family: `Avenir Next`
  Safe family: `Open Sans`
  Style: `Avenir Next Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `150_percent_of_font_height`
  Size rule: `max type size 16 pt`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSs TtUuVvWwXxYyZz`
  Notes: The source says to use Avenir Next Regular in sentence case only, with loose leading at 150 percent and a max size of 16 pt.

- Source role: `limited_space_emphasis`
  Family: `Trade Gothic Condensed No. 18`
  Safe family: `Futura`
  Style: `Trade Gothic Condensed No. 18`
  Weight label: `Regular`
  Usage scope: `limited-space emphasis or short supporting phrases`
  Case: `not specified in source`
  Tracking: `not specified in source`
  Leading: `150_percent_of_font_height`
  Size rule: `short emphasized copy only`
  Punctuation: `not specified in source`
  Sample copy: `AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSs`
  Notes: The source says to use this family when space is limited or when only a few words need emphasis, with loose leading at 150 percent.

## Role Recipes

### Role: title_or_small_type

Proposed family token: `kirkwood/family/03`

Safe family token: `kirkwood/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/400`

Recipe notes:

- Case: `all_caps_or_title_case`
- Tracking: `not specified in source`
- Leading: `around 120 percent of font height`
- Size rule: `title size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Best-fit semantic staging for the short title lane.

### Role: headline

Proposed family token: `kirkwood/family/01`

Safe family token: `kirkwood/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/800`

Recipe notes:

- Case: `all_caps`
- Tracking: `not specified in source`
- Leading: `100 percent of font height or less`
- Size rule: `headline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Primary condensed display treatment.

### Role: body

Proposed family token: `kirkwood/family/02`

Safe family token: `kirkwood/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `150 percent of font height`
- Size rule: `max 16 pt`
- Punctuation: `sentence punctuation allowed`
- Notes: Reading copy remains on the shared base body step.

### Role: limited_space_emphasis

Proposed family token: `kirkwood/family/04`

Safe family token: `kirkwood/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `150 percent of font height`
- Size rule: `short emphasized copy only`
- Punctuation: `not specified in source`
- Notes: Raw-only utility recipe pending a future semantic slot decision.
