# Breckenridge Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/breckenridge/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Poppins`
  Safe family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `h1 headline size not numerically specified`
  Punctuation: `not specified`
  Sample copy: `LOREM IPSUM DOLOR SIT.`
  Notes: Source labels this as H1 Headline.

- Source role: `subhead`
  Family: `Poppins`
  Safe family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `sentence_case`
  Tracking: `-15px`
  Leading: `not specified`
  Size rule: `h1 subhead size not numerically specified`
  Punctuation: `not specified`
  Sample copy: `Lorem ipsum dolor sit sed elit dolore magna aliqua.`
  Notes: Source labels this as H1 Subhead.

- Source role: `body`
  Family: `Avenir Next`
  Safe family: `Poppins`
  Style: `Avenir Next`
  Weight label: `not specified`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `body copy size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.`
  Notes: Source labels this as Body Copy.

- Source role: `cta`
  Family: `Poppins`
  Safe family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `action_or_button_copy`
  Case: `sentence_case`
  Tracking: `-15px`
  Leading: `not specified`
  Size rule: `cta size not numerically specified`
  Punctuation: `not specified`
  Sample copy: `Learn more`
  Notes: Source labels this as CTA.

## Role Recipes

### Role: headline

Proposed family token: `breckenridge/family/01`

Safe family token: `breckenridge/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/800`

Recipe notes:

- Case: `all_caps`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `h1 headline size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Proposed family mapping is ready for review and uses the shared raw bold weight in the global typography ladder.

### Role: subhead

Proposed family token: `breckenridge/family/01`

Safe family token: `breckenridge/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/600`

Recipe notes:

- Case: `sentence_case`
- Tracking: `-15px`
- Leading: `not specified in source`
- Size rule: `h1 subhead size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Uses the same family as the headline with a smaller assumed size and negative tracking.

### Role: body

Proposed family token: `breckenridge/family/02`

Safe family token: `breckenridge/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `not specified in source`
- Size rule: `body copy size not numerically specified`
- Punctuation: `sentence punctuation allowed`
- Notes: Body weight remains a provisional normal-weight assumption until the source provides a stricter raw mapping.

### Role: cta

Proposed family token: `breckenridge/family/01`

Safe family token: `breckenridge/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `-15px`
- Leading: `not specified in source`
- Size rule: `cta size not numerically specified`
- Punctuation: `not specified in source`
- Notes: CTA shares the brand family and tracking direction of the headline system.
