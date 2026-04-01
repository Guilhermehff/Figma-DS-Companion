# Mount Snow Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/mount_snow/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Vastago Grotesk`
  Safe family: `Prompt`
  Style: `Heavy`
  Weight label: `Heavy`
  Usage scope: `primary_display_headline`
  Case: `lowercase`
  Tracking: `0%`
  Leading: `plus_10px_over_font_size`
  Size rule: `source gives example 44px / 54px leading but not a governed token size`
  Punctuation: `not specified in source`
  Sample copy: `the quick brown fox jumps over the lazy dog`
  Notes: Use for bold, impactful type.

- Source role: `subheadline`
  Family: `Area Extended`
  Safe family: `Prompt`
  Style: `Extra Bold`
  Weight label: `Extra Bold`
  Usage scope: `supporting_headline_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `plus_10px_over_font_size`
  Size rule: `source gives example 36px / 46px leading but not a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: Source says to lean into Bold or Extra Bold for subheads.

- Source role: `body`
  Family: `Area Extended`
  Safe family: `Poppins`
  Style: `Medium`
  Weight label: `Medium`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `plus_10px_over_font_size`
  Size rule: `source gives example 20px / 30px leading but not a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: Source explicitly says body copy should use Medium.

## Role Recipes

### Role: headline

Proposed family token: `mount_snow/family/01`

Safe family token: `mount_snow/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/700`

Recipe notes:

- Case: `lowercase`
- Tracking: `0%`
- Leading: `add 10px to the font size`
- Size rule: `example 44px / 54px leading, not a governed token size`
- Punctuation: `not specified in source`
- Notes: Impactful display headline treatment.

### Role: subheadline

Proposed family token: `mount_snow/family/02`

Safe family token: `mount_snow/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/500`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `add 10px to the font size`
- Size rule: `example 36px / 46px leading, not a governed token size`
- Punctuation: `sentence punctuation allowed`
- Notes: Strong supportive headline lane using the same family as body copy.

### Role: body

Proposed family token: `mount_snow/family/02`

Safe family token: `mount_snow/family_safe/02`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/200`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `add 10px to the font size`
- Size rule: `example 20px / 30px leading, not a governed token size`
- Punctuation: `sentence punctuation allowed`
- Notes: Reading-copy treatment in the shared secondary family.
