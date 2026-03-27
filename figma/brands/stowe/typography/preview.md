# Stowe Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/stowe/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Athena`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `primary_display_headline`
  Case: `uppercase`
  Tracking: `0px`
  Leading: `font size x 1`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified`
  Sample copy: `STEP INTO THE ALLURE`
  Notes: The source explicitly labels the headline family as Athena Regular. The user approved the live write to treat the contradictory prose word `bold` as a source copy mistake.

- Source role: `subhead`
  Family: `Raleway`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting_headline_copy`
  Case: `title_case`
  Tracking: `0px`
  Leading: `font size x 1.5`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified`
  Sample copy: `Experience The Luxury of Stowe In The Heart of Vermont.`
  Notes: The source explicitly labels subheads as Raleway Bold.

- Source role: `body`
  Family: `Raleway`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `reading_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `font size x 1.8`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: Body copy is explicitly labeled Raleway Regular.

- Source role: `body_contrasting`
  Family: `Raleway`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `contrast_body_or_supporting_copy`
  Case: `sentence_case`
  Tracking: `0px`
  Leading: `font size x 1.8`
  Size rule: `source defines relational leading but no governed numeric size`
  Punctuation: `not specified`
  Sample copy: `This font should be used sparingly due to legibility and only when large enough to be read.`
  Notes: The source explicitly labels body and contrasting type as Raleway Light and says it should be used sparingly.

## Primitive Recommendations

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `direct_match`
  Notes: Covers Athena Regular and the default Raleway body baseline.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `direct_match`
  Notes: Covers Raleway Bold in the subhead role.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `direct_match`
  Notes: Covers the contrasting Raleway Light role.

- Proposed primitive:
  Token name: `stowe/family/01`
  Source item: `Athena`
  Fallback token: `universal/family/fallback`
  Notes: Athena is isolated to the headline display lane in the first-pass staging.

- Proposed primitive:
  Token name: `stowe/family/02`
  Source item: `Raleway`
  Fallback token: `universal/family/fallback`
  Notes: Raleway carries subhead, body, and contrasting body roles in the first-pass staging.

## Approved Exceptions

- Item: `headline weight resolution`
  Decision: The live write follows `Athena Regular` and treats the contradictory prose word `bold` as a source copy mistake.

- Item: `action baseline`
  Decision: The live write maps action to the same family and weight as heading.

## Semantic Mapping

- `family/heading` -> `stowe/family/01`
- `family/body` -> `stowe/family/02`
- `family/action` -> `stowe/family/01`
- `family/heading_safe` -> `universal/family/fallback`
- `family/body_safe` -> `universal/family/fallback`
- `family/action_safe` -> `universal/family/fallback`
- `weight/heading/base` -> `universal/weight/normal`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/bold`
- `weight/action/base` -> `universal/weight/normal`
- `size/...` -> published directly from `Global: Typography`
- Inherited or deferred notes: no governed numeric size changes are proposed in the first pass

## Role Recipes

### Role: headline

<div style="font-family: serif; font-weight: 400; font-size: 32px; line-height: 1; letter-spacing: 0; text-transform: uppercase; color:#384851;">
  STEP INTO THE ALLURE
</div>

- Proposed family token: `stowe/family/01`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `inherited current heading ladder`
- Notes: User-approved live write. The heading baseline follows the explicit Athena Regular label.

### Role: subhead

<div style="font-family: sans-serif; font-weight: 700; font-size: 24px; line-height: 1.5; letter-spacing: 0; color:#384851;">
  Experience The Luxury of Stowe In The Heart of Vermont.
</div>

- Proposed family token: `stowe/family/02`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading and body ladders`
- Notes: Raleway Bold is explicit in the source.

### Role: body

<div style="font-family: sans-serif; font-weight: 400; font-size: 18px; line-height: 1.8; letter-spacing: 0; color:#384851;">
  Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?
</div>

- Proposed family token: `stowe/family/02`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `inherited current body ladder`
- Notes: Raleway Regular is explicit in the source.

### Role: body_contrasting

<div style="font-family: sans-serif; font-weight: 300; font-size: 18px; line-height: 1.8; letter-spacing: 0; color:#74838e;">
  This font should be used sparingly due to legibility and only when large enough to be read.
</div>

- Proposed family token: `stowe/family/02`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `inherited current body ladder`
- Notes: Contrasting type remains documented as a raw option rather than a separate semantic lane.

## Review Notes

- Stowe stages as a two-family system with Athena in the display lane and Raleway across the reading hierarchy.
- The live write treats the contradictory headline prose word `bold` as a source copy mistake and follows the explicit Athena Regular label.
- The live write maps action to the same family and weight as heading.
- `weight/body/strong` now stages the explicit Raleway Bold subhead treatment through the current semantic theme typography ladder.

## Review Readiness

- Subject: `Stowe display-family split`
  Channels: `web, email, ads`
  Rule: Keep Athena isolated to the headline display lane and keep Raleway on subhead and reading work.
  Source basis: The source explicitly names Athena only for headlines and Raleway for the supporting hierarchy.

- Subject: `Stowe headline weight contradiction`
  Channels: `web, email, ads`
  Rule: Follow the explicit `Athena Regular` label and treat the contradictory prose word `bold` as a source copy mistake.
  Source basis: User-approved live write decision in chat.
