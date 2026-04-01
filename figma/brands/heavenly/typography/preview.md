# Heavenly Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/heavenly/brand.yml` and Figma.

## Original Source Roles

- Source role: `title`
  Family: `Din Condensed`
  Safe family: `Open Sans`
  Style: `Din Condensed Bold`
  Weight label: `Bold`
  Usage scope: `section_title_or_emphasized_copy`
  Case: `all_caps`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `title size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `SKI HEAVENLY`
  Notes: Use Din Condensed Bold in all caps for titles and specific emphasized copy lines such as manifestos or headlines that are hard to read.

- Source role: `headline`
  Family: `Din Condensed`
  Safe family: `Open Sans`
  Style: `Din Condensed Light`
  Weight label: `Light`
  Usage scope: `primary_display_headline`
  Case: `all_caps`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `headline size not numerically specified`
  Punctuation: `punctuation only when paired with the campaign logo lockup`
  Sample copy: `IT'S A MOUNTAIN, AND A BEACH`
  Notes: Headlines should use Din Condensed Light in all caps except for specific instances where bold is needed, such as manifestos or social headlines.

- Source role: `subhead`
  Family: `Brandon Grotesque`
  Safe family: `Open Sans`
  Style: `Brandon Grotesque Medium`
  Weight label: `Medium`
  Usage scope: `supporting_headline_copy`
  Case: `all_caps`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `subhead size not numerically specified`
  Punctuation: `not specified in source`
  Sample copy: `YOUR PHONE WON'T DO IT JUSTICE`
  Notes: Subheads should use Brandon Grotesque Medium in all caps.

- Source role: `body`
  Family: `Brandon Grotesque`
  Safe family: `Open Sans`
  Style: `Brandon Grotesque Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `body size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: Body copy should use Brandon Grotesque Regular in sentence case.

## Role Recipes

### Role: title

Proposed family token: `heavenly/family/01`

Safe family token: `heavenly/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `universal/size/400`

Recipe notes:

- Case: `all_caps`
- Leading: `not specified in source`
- Size rule: `title size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Intended for titles and emphasized short copy lines.

### Role: headline

Proposed family token: `heavenly/family/01`

Safe family token: `heavenly/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `universal/size/800`

Recipe notes:

- Case: `all_caps`
- Leading: `not specified in source`
- Size rule: `headline size not numerically specified`
- Punctuation: `punctuation only when paired with the campaign logo lockup`
- Notes: Default Heavenly display treatment. Use Bold only for source-approved emphasis cases such as manifestos or social headlines.

### Role: subhead

Proposed family token: `heavenly/family/02`

Safe family token: `heavenly/family_safe/01`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/500`

Recipe notes:

- Case: `all_caps`
- Leading: `not specified in source`
- Size rule: `subhead size not numerically specified`
- Punctuation: `not specified in source`
- Notes: Use Brandon Grotesque Medium in all caps for all subheads.

### Role: body

Proposed family token: `heavenly/family/02`

Safe family token: `heavenly/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `universal/size/300`

Recipe notes:

- Case: `sentence_case`
- Leading: `not specified in source`
- Size rule: `body size not numerically specified`
- Punctuation: `sentence punctuation allowed`
- Notes: Default reading-copy treatment.
