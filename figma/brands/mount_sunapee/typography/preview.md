# Mount Sunapee Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/mount_sunapee/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Graphik`
  Safe family: `Montserrat`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_headers_h1`
  Case: `sentence_case`
  Tracking: `75`
  Leading: `not specified in source`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified in source`
  Sample copy: `We lift people up.`
  Notes: The typography sheet explicitly labels Graphik Bold for Primary Headers (H1). The source does not specify the tracking unit, so the artifact preserves the numeric label as shown.

- Source role: `secondary_header`
  Family: `Graphik`
  Safe family: `Montserrat`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `secondary_headers_h2`
  Case: `sentence_case`
  Tracking: `75`
  Leading: `not specified in source`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified in source`
  Sample copy: `We elevate spirits by creating fun, invigorating mountain experiences for everyone.`
  Notes: The typography sheet explicitly labels Graphik Regular for Secondary Headers (H2).

- Source role: `body`
  Family: `Graphik`
  Safe family: `Open Sans`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `25`
  Leading: `not specified in source`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Memories and stories of which are the reason families continue to leave their homes, flock to the mountains, and enjoy the awe-inspiring outdoors to be uplifted again and again.`
  Notes: The typography sheet explicitly labels Graphik Light for Body Copy.

- Source role: `subheader`
  Family: `Neutraface Text`
  Safe family: `Montserrat`
  Style: `Bold Italic`
  Weight label: `Bold Italic`
  Usage scope: `subheaders_h3`
  Case: `sentence_case`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified in source`
  Sample copy: `Activities`
  Notes: The typography sheet explicitly labels Neutraface Text Bold Italic for Subheaders (H3). The example page confirms this as a distinct utility lane rather than the default Graphik heading system.

## Role Recipes

### Role: headline

Proposed family token: `mount_sunapee/family/01`

Safe family token: `mount_sunapee/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `75`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: H1 remains on Graphik Bold.

### Role: secondary_header

Proposed family token: `mount_sunapee/family/01`

Safe family token: `mount_sunapee/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited current heading and body ladders`

Recipe notes:

- Case: `sentence_case`
- Tracking: `75`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Approved live write. H2 stages through the Graphik family with the shared normal weight.

### Role: body

Proposed family token: `mount_sunapee/family/01`

Safe family token: `mount_sunapee/family_safe/02`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited current body ladder`

Recipe notes:

- Case: `sentence_case`
- Tracking: `25`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `sentence punctuation allowed`
- Notes: Body copy remains on Graphik Light.

### Role: subheader

Proposed family token: `mount_sunapee/family/02`

Safe family token: `mount_sunapee/family_safe/01`

Proposed weight token: `universal/weight/bold`

Proposed size token: `inherited current heading ladder`

Recipe notes:

- Case: `sentence_case`
- Leading: `not specified in source`
- Size rule: `no governed source size token`
- Punctuation: `not specified in source`
- Notes: Raw-only utility recipe. It remains outside the live semantic extension until a subhead family lane exists.
