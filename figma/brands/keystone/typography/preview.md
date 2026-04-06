# Keystone Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/keystone/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Futura`
  Safe family: `Open Sans`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `primary_display_headline`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `4px_difference`
  Size rule: `explicit 48px with 52px leading example`
  Punctuation: `not specified in source`
  Sample copy: `Headline`
  Notes: The source explicitly says `Futura Bold / Sentence case`, `Leading: 4px difference (Ex: 48px / 52px leading)`, and `Kerning: 0%`.

- Source role: `subheadline`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `supporting_headline_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `4px_difference`
  Size rule: `explicit 36px with 40px leading example`
  Punctuation: `not specified in source`
  Sample copy: `Sub Headline`
  Notes: The source explicitly says `Avenir Medium / Sentence case`, `Leading: 4px difference (Ex: 36px / 40px leading)`, and `Kerning: 0%`.

- Source role: `body`
  Family: `Avenir`
  Safe family: `Open Sans`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `4px_difference`
  Size rule: `explicit 16px with 20px leading example`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Body Copy`
  Notes: The source explicitly says `Avenir Medium / Sentence case`, `Leading: 4px difference (Ex: 16px / 20px leading)`, and `Kerning: 0%`.

- Source role: `emphasized_body_copy`
  Family: `Futura`
  Safe family: `Open Sans`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `emphasized_short_body_copy`
  Case: `sentence_case`
  Tracking: `0%`
  Leading: `4px_difference`
  Size rule: `explicit 16px with 20px leading example`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Emphasized body copy`
  Notes: The source explicitly says `Futura Bold / Sentence case`, `Leading: 4px difference (Ex: 16px / 20px leading)`, and `Kerning: 0%`.

- Source role: `cta`
  Family: `Futura`
  Safe family: `Open Sans`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `action_or_button_copy`
  Case: `title_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `explicit 20px in CTA example`
  Punctuation: `not specified in source`
  Sample copy: `CTA`
  Notes: User-approved review decision resolves the source contradiction in favor of the CTA example: Futura Bold in Title Case at 20px.

## Role Recipes

### Role: headline

Proposed family token: `keystone/family/01`

Safe family token: `keystone/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `4px difference`
- Size rule: `48px / 52px example`
- Punctuation: `not specified in source`
- Notes: The source is explicit, but no new shared size step was added in this pass, so the 48px headline recipe remains documented for later follow-up.

### Role: subheadline

Proposed family token: `keystone/family/02`

Safe family token: `keystone/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `4px difference`
- Size rule: `36px / 40px example`
- Punctuation: `not specified in source`
- Notes: The explicit source size remains documented, but no new size override was written in this pass.

### Role: body

Proposed family token: `keystone/family/02`

Safe family token: `keystone/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/core/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `4px difference`
- Size rule: `16px / 20px example`
- Punctuation: `sentence punctuation allowed`
- Notes: Source is explicit and fits the current shared body size step.

### Role: emphasized_body_copy

Proposed family token: `keystone/family/01`

Safe family token: `keystone/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/core/300`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0%`
- Leading: `4px difference`
- Size rule: `16px / 20px example`
- Punctuation: `sentence punctuation allowed`
- Notes: Uses the headline family in a small-size emphasis role.

### Role: cta

Proposed family token: `keystone/family/01`

Safe family token: `keystone/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/core/500`

Recipe notes:

- Case: `title_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `20px example`
- Punctuation: `not specified in source`
- Notes: Final approved CTA mapping for the live Keystone write.
