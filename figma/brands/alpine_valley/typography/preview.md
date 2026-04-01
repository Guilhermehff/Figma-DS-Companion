# Alpine Valley Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/alpine_valley/brand.yml` and Figma.

## Original Source Roles

- Source role: `primary_header`
  Family: `Prompt`
  Safe family: `Prompt`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_header_h1`
  Case: `all_caps_in_example`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels H1 but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `PROMPT BOLD: PRIMARY HEADER (H1)`
  Notes: The source explicitly shows Prompt Bold for the primary header.

- Source role: `secondary_header`
  Family: `Prompt`
  Safe family: `Prompt`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `secondary_header_h2`
  Case: `all_caps_in_example`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels H2 but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `PROMPT BOLD: SECONDARY HEADER (H2)`
  Notes: The source explicitly shows Prompt Bold for the secondary header.

- Source role: `body`
  Family: `Prompt`
  Safe family: `Open Sans`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels body copy but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `PROMPT REGULAR: Alpine Valley is an easy getaway...`
  Notes: The source explicitly shows Prompt Regular for body copy.

## Role Recipes

### Role: primary_header

Proposed family token: `alpine_valley/family/01`

Safe family token: `alpine_valley/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `all_caps_in_example`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source labels H1 but does not define governed token sizes`
- Punctuation: `not specified in source`
- Notes: The source explicitly shows H1 on Prompt Bold.

### Role: secondary_header

Proposed family token: `alpine_valley/family/01`

Safe family token: `alpine_valley/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `all_caps_in_example`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source labels H2 but does not define governed token sizes`
- Punctuation: `not specified in source`
- Notes: The source explicitly shows H2 on Prompt Bold.

### Role: body

Proposed family token: `alpine_valley/family/01`

Safe family token: `alpine_valley/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source labels body copy but does not define governed token sizes`
- Punctuation: `sentence punctuation allowed`
- Notes: The source explicitly shows body copy on Prompt Regular.

### Role: action

Proposed family token: `alpine_valley/family/01`

Safe family token: `alpine_valley/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current action ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source does not define CTA behavior`
- Punctuation: `not specified in source`
- Notes: User-approved follow-up. CTA uses Prompt and stages on Bold even though the source image does not explicitly define a CTA recipe.
