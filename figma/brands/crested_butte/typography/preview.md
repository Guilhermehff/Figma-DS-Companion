# Crested Butte Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/crested_butte/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Gibson`
  Safe family: `Montserrat`
  Style: `Gibson Semibold`
  Weight label: `Semibold`
  Usage scope: `primary_display_headline`
  Case: `lowercase`
  Tracking: `regular`
  Leading: `86% of type size`
  Size rule: `headline size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `gibson semibold`
  Notes: Left aligned. Use varied indentation per line to create an intentional, fluid, and tight lockup. No more than four lines stacked, best in two or three lines. May use any brand color.

- Source role: `subhead`
  Family: `Gibson`
  Safe family: `Montserrat`
  Style: `Gibson Semibold`
  Weight label: `Semibold`
  Usage scope: `supporting_headline_copy`
  Case: `all_caps`
  Tracking: `regular`
  Leading: `not specified in source`
  Size rule: `sub-headline size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `GIBSON SEMIBOLD`
  Notes: Left aligned. Single line of copy. Black or white only.

- Source role: `body`
  Family: `Gibson`
  Safe family: `Open Sans`
  Style: `Gibson Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `regular`
  Leading: `not specified in source`
  Size rule: `body size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Gibson Regular is our default body copy font, and should primarily be used in black on white backgrounds in layout. Or in White, against darker backgrounds.`
  Notes: Source explicitly describes Gibson Regular as the default body copy font.

## Role Recipes

### Role: headline

Proposed family token: `crested_butte/family/01`

Safe family token: `crested_butte/family_safe/01`

Proposed weight token: `universal/weight/semibold`

Proposed size token: `universal/size/800`

Recipe notes:

- Case: `lowercase`
- Tracking: `regular`
- Leading: `86% of type size`
- Size rule: `headline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Left aligned. Use varied indentation per line and keep the lockup to four lines or fewer.

### Role: subhead

Proposed family token: `crested_butte/family/01`

Safe family token: `crested_butte/family_safe/01`

Proposed weight token: `universal/weight/semibold`

Proposed size token: `universal/size/500`

Recipe notes:

- Case: `all_caps`
- Tracking: `regular`
- Leading: `not specified in source`
- Size rule: `sub-headline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Intended as a single-line supporting headline and limited to black or white application.

### Role: body

Proposed family token: `crested_butte/family/01`

Safe family token: `crested_butte/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `regular`
- Leading: `not specified in source`
- Size rule: `body size not numerically specified`
- Punctuation: `sentence punctuation allowed`
- Notes: Source explicitly positions Gibson Regular as the default body treatment.
