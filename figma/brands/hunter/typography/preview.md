# Hunter Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/hunter/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Galano Grotesque`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_headers_h1`
  Case: `sentence_case`
  Tracking: `not specified`
  Leading: `not specified`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `not specified`
  Sample copy: `You can't get these views in SOHO.`
  Notes: The typography sheet explicitly labels headlines as Galano Grotesque Bold.

- Source role: `subheadline`
  Family: `Galano Grotesque`
  Style: `Semibold`
  Weight label: `Semibold`
  Usage scope: `supporting_headers_h2`
  Case: `sentence_case`
  Tracking: `not specified`
  Leading: `not specified`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `not specified`
  Sample copy: `Experience Hunter Mountain in the Catskills.`
  Notes: The typography sheet explicitly labels sub-headlines as Galano Grotesque Semibold.

- Source role: `body`
  Family: `Galano Grotesque`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `not specified`
  Leading: `not specified`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: The typography sheet explicitly labels body copy as Galano Grotesque Regular.

- Source role: `body_contrasting`
  Family: `Galano Grotesque`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `contrasting_body_or_supporting_copy`
  Case: `sentence_case`
  Tracking: `not specified`
  Leading: `not specified`
  Size rule: `source names roles and weights but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This font should be used sparingly due to legibility.`
  Notes: The typography sheet explicitly labels the contrasting body lane as Galano Grotesque Light and says it should be used sparingly.

## Primitive Recommendations

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `direct_match`
  Notes: Covers Galano Grotesque Bold in the H1 lane.

- Reuse:
  Source item: `Semibold`
  Proposed token: `universal/weight/semibold`
  Assumption status: `direct_match`
  Notes: Covers Galano Grotesque Semibold in the H2 lane.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `direct_match`
  Notes: Covers Galano Grotesque Regular in the body lane.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `direct_match`
  Notes: Covers Galano Grotesque Light in the contrasting-body lane.

- Proposed primitive:
  Token name: `hunter/family/primary`
  Source item: `Galano Grotesque`
  Fallback token: `universal/family/web_safe`
  Notes: Hunter uses one Galano Grotesque family across headline, subheadline, body, and contrasting body roles.

## Semantic Mapping

- `family/heading` -> `hunter/family/primary`
- `family/body` -> `hunter/family/primary`
- `family/action` -> inherited from the base semantic theme mapping in the live pass
- `family/heading_safe` -> `universal/family/web_safe`
- `family/body_safe` -> `universal/family/web_safe`
- `family/action_safe` -> inherited from the base semantic theme mapping in the live pass
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/semibold`
- `size/...` -> published directly from `Global: Typography`
- Inherited or deferred notes: action remains inherited because the source does not define a CTA recipe

## Role Recipes

### Role: headline

<div style="font-family: sans-serif; font-weight: 700; font-size: 32px; line-height: 1.15; letter-spacing: 0; color:#222233;">
  You can't get these views in SOHO.
</div>

- Proposed family token: `hunter/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: H1 remains on Galano Grotesque Bold.

### Role: subheadline

<div style="font-family: sans-serif; font-weight: 600; font-size: 24px; line-height: 1.25; letter-spacing: 0; color:#222233;">
  Experience Hunter Mountain in the Catskills.
</div>

- Proposed family token: `hunter/family/primary`
- Proposed weight token: `universal/weight/semibold`
- Proposed size token: `inherited current heading and body ladders`
- Notes: Approved live write. H2 stages through the shared Galano Grotesque family with the semibold weight.

### Role: body

<div style="font-family: sans-serif; font-weight: 400; font-size: 18px; line-height: 1.6; letter-spacing: 0; color:#222233;">
  Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?
</div>

- Proposed family token: `hunter/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `inherited current body ladder`
- Notes: Body copy remains on Galano Grotesque Regular.

### Role: body_contrasting

<div style="font-family: sans-serif; font-weight: 300; font-size: 18px; line-height: 1.6; letter-spacing: 0; color:#808080;">
  This font should be used sparingly due to legibility.
</div>

- Proposed family token: `hunter/family/primary`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `inherited current body ladder`
- Notes: Contrasting type remains a documented raw option rather than a separate semantic lane in the first pass.

## Review Notes

- Hunter stages cleanly as a one-family system with Galano Grotesque carrying the full hierarchy through weight changes.
- `weight/body/strong` is the live semantic slot for the explicit Semibold subheadline treatment.
- The source does not define a CTA or action lane, so action remains inherited in the live semantic extension.

## Review Readiness

- Subject: `Hunter Galano hierarchy`
  Channels: `web, email, ads`
  Rule: Keep H1 on Galano Grotesque Bold, H2 on Galano Grotesque Semibold, and body copy on Galano Grotesque Regular.
  Source basis: Hunter typography image.

- Subject: `Hunter contrasting body lane`
  Channels: `web, email, ads`
  Rule: Preserve Galano Grotesque Light as a documented contrasting-body option rather than forcing it into the primary semantic weight mapping.
  Source basis: Hunter typography image.
