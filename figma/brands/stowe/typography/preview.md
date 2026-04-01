# Stowe Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/stowe/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Athena`
  Safe family: `Italiana`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `primary_display_headline`
  Case: `uppercase`
  Tracking: `0px`
  Leading: `font_size_times_1`
  Size rule: `source defines case, weight language, and relational leading but no governed numeric size`
  Punctuation: `not specified in source`
  Sample copy: `STEP INTO THE ALLURE`
  Notes: The source explicitly labels the headline family as Athena Regular, and the user approved the live write to treat the supporting prose word `bold` as a copy mistake.

- Source role: `subhead`
  Family: `Raleway`
  Safe family: `Italiana`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `title_case`
  Tracking: `0px`
  Leading: `font_size_times_1_5`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified in source`
  Sample copy: `Experience The Luxury of Stowe In The Heart of Vermont.`
  Notes: The source explicitly labels subheads as Raleway Bold and says they remain left justified unless a layout calls for centering.

- Source role: `body`
  Family: `Raleway`
  Safe family: `Raleway`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `font_size_times_1_8`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified in source`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: Body copy is explicitly labeled Raleway Regular and should be left justified unless a layout calls for centering.

- Source role: `body_contrasting`
  Family: `Raleway`
  Safe family: `Raleway`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `contrast_body_or_supporting_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `font_size_times_1_8`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified in source`
  Sample copy: `This font should be used sparingly due to legibility and only when large enough to be read.`
  Notes: The source explicitly labels body and contrasting type as Raleway Light and says it should be used sparingly.

## Role Recipes

### Role: headline

Proposed family token: `stowe/family/01`

Safe family token: `stowe/family_safe/02`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `uppercase`
- Tracking: `0px`
- Leading: `leading equals the point size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: User-approved live write. The heading baseline follows the explicit Athena Regular label.

### Role: subhead

Proposed family token: `stowe/family/02`

Safe family token: `stowe/family_safe/02`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading and body ladders`

Recipe notes:

- Case: `title_case`
- Tracking: `0px`
- Leading: `1.5 times the font size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Subheads stay on Raleway Bold and remain left justified unless a layout calls for centering.

### Role: body

Proposed family token: `stowe/family/02`

Safe family token: `stowe/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `1.8 times the font size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Body copy explicitly uses Raleway Regular.

### Role: body_contrasting

Proposed family token: `stowe/family/02`

Safe family token: `stowe/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `0px`
- Leading: `1.8 times the font size`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Contrasting type remains a documented raw option rather than a separate semantic lane in the first pass.
