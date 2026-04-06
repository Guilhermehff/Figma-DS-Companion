# JFBB Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/jfbb/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Vista Sans NAR OTCE`
  Safe family: `Futura`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `0%`
  Leading: `plus_10px_over_font_size`
  Size rule: `source gives example 44px / 54px leading but not a governed token size`
  Punctuation: `not specified in source`
  Sample copy: `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG`
  Notes: Use for headlines and bold impactful type.

- Source role: `subheadline`
  Family: `Vista Sans NAR OTCE`
  Safe family: `Futura`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `all_caps`
  Tracking: `0%`
  Leading: `plus_10px_over_font_size`
  Size rule: `source gives example 36px / 46px leading but not a governed token size`
  Punctuation: `punctuation allowed`
  Sample copy: `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.`
  Notes: The hierarchy sheet says subheads should lean into Bold.

- Source role: `body`
  Family: `Vista Sans NAR OTCE`
  Safe family: `Open Sans`
  Style: `Book`
  Weight label: `Book`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `source lists 100px difference and 24px / 124px example; treated as inconsistent`
  Size rule: `source body example is internally inconsistent and not treated as a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: The source explicitly says body should use Book.

## Role Recipes

### Role: headline

Proposed family token: `jfbb/family/01`

Safe family token: `jfbb/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/core/700`

Recipe notes:

- Case: `all_caps`
- Tracking: `0%`
- Leading: `add 10px to the font size`
- Size rule: `example 44px / 54px leading, not a governed token size`
- Punctuation: `not specified in source`
- Notes: Strong all-caps headline lane.

### Role: subheadline

Proposed family token: `jfbb/family/01`

Safe family token: `jfbb/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/core/500`

Recipe notes:

- Case: `all_caps`
- Tracking: `0%`
- Leading: `add 10px to the font size`
- Size rule: `example 36px / 46px leading, not a governed token size`
- Punctuation: `punctuation allowed`
- Notes: Supportive all-caps headline lane.

### Role: body

Proposed family token: `jfbb/family/01`

Safe family token: `jfbb/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/core/200`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `source body example is internally inconsistent; do not create a size override from it`
- Size rule: `source lists 100px difference and 24px / 124px leading, so the live extension keeps shared size semantics`
- Punctuation: `sentence punctuation allowed`
- Notes: Reading-copy treatment on the shared JFBB family.
