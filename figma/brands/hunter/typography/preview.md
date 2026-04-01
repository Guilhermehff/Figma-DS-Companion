# Hunter Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/hunter/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Galano Grotesque`
  Safe family: `Poppins`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_headers_h1`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `not specified in source`
  Sample copy: `You can't get these views in SOHO.`
  Notes: The typography sheet explicitly labels headlines as Galano Grotesque Bold.

- Source role: `subheadline`
  Family: `Galano Grotesque`
  Safe family: `Poppins`
  Style: `Semibold`
  Weight label: `Semibold`
  Usage scope: `supporting_headers_h2`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `not specified in source`
  Sample copy: `Experience Hunter Mountain in the Catskills.`
  Notes: The typography sheet explicitly labels sub-headlines as Galano Grotesque Semibold.

- Source role: `body`
  Family: `Galano Grotesque`
  Safe family: `Poppins`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: The typography sheet explicitly labels body copy as Galano Grotesque Regular.

- Source role: `body_contrasting`
  Family: `Galano Grotesque`
  Safe family: `Poppins`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `contrasting_body_or_supporting_copy`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This font should be used sparingly due to legibility.`
  Notes: The typography sheet explicitly labels the contrasting body lane as Galano Grotesque Light and says it should be used sparingly.

## Role Recipes

### Role: headline

Proposed family token: `hunter/family/01`

Safe family token: `hunter/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: H1 remains on Galano Grotesque Bold.

### Role: subheadline

Proposed family token: `hunter/family/01`

Safe family token: `hunter/family_safe/01`

Proposed weight token: `universal/weight/semibold`

Proposed size token: `inherited current heading and body ladders`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Approved live write. H2 stages through the shared Galano Grotesque family with the semibold weight.

### Role: body

Proposed family token: `hunter/family/01`

Safe family token: `hunter/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `sentence punctuation allowed`
- Notes: Body copy remains on Galano Grotesque Regular.

### Role: body_contrasting

Proposed family token: `hunter/family/01`

Safe family token: `hunter/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `not specified in source`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `sentence punctuation allowed`
- Notes: Contrasting type remains a documented raw option rather than a separate semantic lane in the first pass.
