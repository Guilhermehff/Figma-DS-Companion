# Park City Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/park_city/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Futura Std`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary display headline`
  Case: `all caps`
  Tracking: `0px`
  Leading: `equal to point size`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified`
  Sample copy: `THIS IS YOUR HEADLINE.`
  Notes: Usually center justified, with left alignment allowed in certain layouts.

- Source role: `subhead`
  Family: `Trade Gothic LT Std Bold Condensed No. 20`
  Style: `Bold Condensed No. 20`
  Weight label: `Bold`
  Usage scope: `supporting headline copy`
  Case: `all caps`
  Tracking: `100px`
  Leading: `+2 over point size`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified`
  Sample copy: `THIS IS YOUR SUBHEAD.`
  Notes: Distinct condensed subhead face in the Park City hierarchy.

- Source role: `body`
  Family: `Futura Std`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `reading copy`
  Case: `sentence case`
  Tracking: `0px`
  Leading: `1.6x`
  Size rule: `source gives no governed size token`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This is your body copy.`
  Notes: Body copy should be highly legible in every medium.

- Source role: `cta`
  Family: `Futura Std`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `action or button copy`
  Case: `all caps`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `source gives no governed size token`
  Punctuation: `not specified`
  Sample copy: `PLAN YOUR VISIT`
  Notes: CTA is explicitly Futura Std Bold.

## Primitive Recommendations

- Proposed primitive:
  Token name: `park_city/family/01`
  Source item: `Futura Std`
  Fallback token: `universal/family/fallback`
  Notes: Shared Park City family across headline, body, and CTA roles.

- Proposed primitive:
  Token name: `park_city/family/02`
  Source item: `Trade Gothic LT Std Bold Condensed No. 20`
  Fallback token: `universal/family/fallback`
  Notes: Raw utility family for the distinct Park City subhead treatment.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Headlines, CTA, and the condensed subhead lane all explicitly use bold treatments.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `explicit`
  Notes: Body copy explicitly uses Light.

## Hold For Review

- Item: `semantic subhead lane`
  Reason: The current semantic theme typography schema exposes only `heading`, `body`, and `action`, so the distinct condensed subhead face remains a raw utility recipe in this pass.

## Semantic Mapping

- `family/heading` -> `park_city/family/01`
- `family/body` -> `park_city/family/01`
- `family/action` -> `park_city/family/01`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/light`
- `weight/action/base` -> `universal/weight/bold`
- `size/*` remain inherited in the live extension
- `park_city/family/02` remains raw-only for the condensed subhead recipe

## Role Recipes

### Role: headline

<div style="font-family: 'Futura Std', sans-serif; font-weight: 700; font-size: 40px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  THIS IS YOUR HEADLINE.
</div>

- Proposed family token: `park_city/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: Park City display lane on Futura Std Bold.

### Role: subhead

<div style="font-family: 'Trade Gothic LT Std Bold Condensed No. 20', sans-serif; font-weight: 700; font-size: 24px; line-height: 1.08; letter-spacing: 0.1em; text-transform: uppercase;">
  THIS IS YOUR SUBHEAD.
</div>

- Proposed family token: `park_city/family/02`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: Raw-only condensed utility recipe pending a future semantic subhead lane.

### Role: body

<div style="font-family: 'Futura Std', sans-serif; font-weight: 300; font-size: 16px; line-height: 1.6; letter-spacing: 0;">
  This is your body copy.
</div>

- Proposed family token: `park_city/family/01`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `inherited current body ladder`
- Notes: Reading-copy lane stays on Futura Std Light.

### Role: cta

<div style="font-family: 'Futura Std', sans-serif; font-weight: 700; font-size: 18px; line-height: 1.1; letter-spacing: 0; text-transform: uppercase;">
  PLAN YOUR VISIT
</div>

- Proposed family token: `park_city/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current action ladder`
- Notes: CTA stays on Futura Std Bold rather than the condensed subhead face.

## Review Notes

- Park City uses one core family, `Futura Std`, across headline, body, and CTA roles.
- The condensed Trade Gothic face is preserved as a raw utility family because the current semantic schema has no separate subhead slot and the CTA guidance is explicitly Futura.
- Numeric size tokens remain inherited from the shared semantic baseline because the source provides hierarchy rules and leading guidance, not governed size tokens.

## Review Readiness

- Subject: `Park City headline and CTA lane`
  Channels: `web, email, ads`
  Rule: Keep headline and CTA work on Futura Std Bold in all caps with 0px tracking.
  Source basis: Park City typography guidance image.

- Subject: `Park City subhead lane`
  Channels: `web, email, ads`
  Rule: Preserve Trade Gothic LT Std Bold Condensed No. 20 for subheads with 100px tracking and leading plus 2.
  Source basis: Park City typography guidance image.

- Subject: `Park City body lane`
  Channels: `web, email, ads`
  Rule: Keep body copy on Futura Std Light with 0px tracking and 1.6x leading.
  Source basis: Park City typography guidance image.
