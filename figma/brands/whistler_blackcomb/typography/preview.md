# Whistler Blackcomb Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/whistler_blackcomb/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Proxima Nova`
  Safe family: `Montserrat`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary_display_headline`
  Case: `uppercase`
  Tracking: `15`
  Leading: `90%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `HEADLINES`
  Notes: The source explicitly labels headlines as Proxima Nova Black.

- Source role: `eyebrow`
  Family: `Proxima Nova`
  Safe family: `Open Sans`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `supporting_label_or_eyebrow`
  Case: `uppercase`
  Tracking: `15`
  Leading: `100%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `EYEBROW`
  Notes: Eyebrow uses the same family and weight as the headline lane, with a smaller role recipe.

- Source role: `subhead`
  Family: `Proxima Nova`
  Safe family: `Montserrat`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `title_case_from_sample`
  Tracking: `0`
  Leading: `100%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Subheads`
  Notes: The source explicitly labels subheads as Proxima Nova Bold.

- Source role: `body`
  Family: `Proxima Nova`
  Safe family: `Open Sans`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case_from_sample`
  Tracking: `0`
  Leading: `140%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Body`
  Notes: The source explicitly labels body as Proxima Nova Regular.

- Source role: `action`
  Family: `Proxima Nova`
  Safe family: `Open Sans`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `button_or_action_copy`
  Case: `not specified in source`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `Button`
  Notes: The source explicitly labels button copy as Proxima Nova Bold.

## Role Recipes

### Role: headline

Proposed family token: `whistler_blackcomb/family/01`

Safe family token: `whistler_blackcomb/family_safe/02`

Proposed weight token: `universal/weight/black`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `uppercase`
- Tracking: `15`
- Leading: `90%`
- Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
- Punctuation: `not specified in source`
- Notes: Core display headline treatment.

### Role: eyebrow

Proposed family token: `whistler_blackcomb/family/01`

Safe family token: `whistler_blackcomb/family_safe/01`

Proposed weight token: `universal/weight/black`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `uppercase`
- Tracking: `15`
- Leading: `100%`
- Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
- Punctuation: `not specified in source`
- Notes: Eyebrow remains a role recipe under the heading family and weight rather than becoming a new semantic lane.

### Role: subhead

Proposed family token: `whistler_blackcomb/family/01`

Safe family token: `whistler_blackcomb/family_safe/02`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `title_case_from_sample`
- Leading: `100%`
- Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
- Punctuation: `sentence punctuation allowed`
- Notes: Subheads stage through the stronger body weight lane in the current semantic theme typography schema.

### Role: body

Proposed family token: `whistler_blackcomb/family/01`

Safe family token: `whistler_blackcomb/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case_from_sample`
- Leading: `140%`
- Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
- Punctuation: `sentence punctuation allowed`
- Notes: Reading-copy treatment.

### Role: action

Proposed family token: `whistler_blackcomb/family/01`

Safe family token: `whistler_blackcomb/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current action ladder`

Recipe notes:

- Case: `not specified in source`
- Leading: `not specified in source`
- Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
- Punctuation: `not specified in source`
- Notes: Button copy maps cleanly to the existing action lane.
