# Stevens Pass Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/stevens_pass/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Gibson`
  Safe family: `Montserrat`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_display_headline`
  Case: `not specified in source`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source shows family and weight only`
  Punctuation: `not specified in source`
  Sample copy: `GIBSON BOLD`
  Notes: The typography sheet explicitly labels headlines as Gibson Bold.

- Source role: `subhead`
  Family: `Gibson`
  Safe family: `Montserrat`
  Style: `Semi Bold`
  Weight label: `Semi Bold`
  Usage scope: `supporting_headline_copy`
  Case: `not specified in source`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source shows family and weight only`
  Punctuation: `not specified in source`
  Sample copy: `GIBSON SEMI BOLD`
  Notes: The typography sheet explicitly labels subheads as Gibson Semi Bold.

- Source role: `cta`
  Family: `Gibson`
  Safe family: `Montserrat`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `action_or_button_copy`
  Case: `not specified in source`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source shows family and weight only`
  Punctuation: `not specified in source`
  Sample copy: `GIBSON REGULAR`
  Notes: The typography sheet explicitly labels CTA as Gibson Regular.

- Source role: `body`
  Family: `Gibson`
  Safe family: `Open Sans`
  Style: `Medium, Regular, Light, and italic variants`
  Weight label: `Mixed`
  Usage scope: `reading_copy`
  Case: `not specified in source`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source shows approved family variants rather than a single governed body recipe`
  Punctuation: `not specified in source`
  Sample copy: `GIBSON MEDIUM / REGULAR / LIGHT`
  Notes: The source lists multiple acceptable body weights and italics without stating which one is the semantic default.

## Role Recipes

### Role: headline

Proposed family token: `stevens_pass/family/01`

Safe family token: `stevens_pass/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source shows family and weight only`
- Punctuation: `not specified in source`
- Notes: Straightforward headline mapping.

### Role: subhead

Proposed family token: `stevens_pass/family/01`

Safe family token: `stevens_pass/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source shows family and weight only`
- Punctuation: `not specified in source`
- Notes: User-approved exception. Subheads stage through `typography/weight/body/strong = medium` rather than a separate semantic family or the source-labeled semibold.

### Role: cta

Proposed family token: `stevens_pass/family/01`

Safe family token: `stevens_pass/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `inherited current action ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source shows family and weight only`
- Punctuation: `not specified in source`
- Notes: User-approved exception. The live semantic action baseline will use Medium rather than the source-labeled Regular treatment.

### Role: body

Proposed family token: `stevens_pass/family/01`

Safe family token: `stevens_pass/family_safe/02`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `not specified in source`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source shows approved variants rather than a single default recipe`
- Punctuation: `not specified in source`
- Notes: User-approved exception. Light becomes the semantic body baseline, while Medium becomes the stronger body or subhead emphasis weight. Regular and italic variants remain documented raw options.
