# Whistler Blackcomb Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/whistler_blackcomb/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Proxima Nova`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary display headline`
  Case: `uppercase`
  Tracking: `15`
  Leading: `90%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `HEADLINES`
  Notes: The source explicitly labels headlines as `Proxima Nova Black`.

- Source role: `eyebrow`
  Family: `Proxima Nova`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `supporting label or eyebrow`
  Case: `uppercase`
  Tracking: `15`
  Leading: `100%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `EYEBROW`
  Notes: Eyebrow uses the same family and weight as the headline lane.

- Source role: `subhead`
  Family: `Proxima Nova`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting headline copy`
  Case: `title_case_from_sample`
  Tracking: `0`
  Leading: `100%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Subheads`
  Notes: The source explicitly labels subheads as `Proxima Nova Bold`.

- Source role: `body`
  Family: `Proxima Nova`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `reading copy`
  Case: `sentence_case_from_sample`
  Tracking: `0`
  Leading: `140%`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Body`
  Notes: The source explicitly labels body as `Proxima Nova Regular`.

- Source role: `action`
  Family: `Proxima Nova`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `button or action copy`
  Case: `not specified in source`
  Tracking: `0`
  Leading: `not specified in source`
  Size rule: `source demonstrates hierarchy behavior but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `Button`
  Notes: The source explicitly labels button copy as `Proxima Nova Bold`.

## Primitive Recommendations

- Proposed primitive:
  Token name: `whistler_blackcomb/family/primary`
  Source item: `Proxima Nova`
  Fallback token: `universal/family/web_safe`
  Notes: One-family Whistler Blackcomb system across headline, eyebrow, subhead, body, and button roles.

- Reuse:
  Source item: `Black`
  Proposed token: `universal/weight/black`
  Assumption status: `explicit`
  Notes: Headline and eyebrow lane.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Subhead and action lane.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: Body lane.

## Semantic Mapping

- `family/heading` -> `whistler_blackcomb/family/primary`
- `family/body` -> `whistler_blackcomb/family/primary`
- `family/action` -> `whistler_blackcomb/family/primary`
- `family/heading_safe` -> inherit `universal/family/web_safe`
- `family/body_safe` -> inherit `universal/family/web_safe`
- `family/action_safe` -> inherit `universal/family/web_safe`
- `weight/heading/base` -> `universal/weight/black`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/bold`
- `weight/action/base` -> `universal/weight/bold`
- `size/*` -> inherit current semantic base
- Inherited or deferred notes: Eyebrow remains a role recipe under the heading lane rather than a separate semantic token.

## Role Recipes

### Role: headline

<div style="font-family: sans-serif; font-weight: 900; font-size: 32px; line-height: 0.9; letter-spacing: 0.015em; text-transform: uppercase;">
  HEADLINES
</div>

- Proposed family token: `whistler_blackcomb/family/primary`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `inherited current heading ladder`
- Notes: Core display headline treatment with 15 tracking and 90 percent leading.

### Role: eyebrow

<div style="font-family: sans-serif; font-weight: 900; font-size: 20px; line-height: 1; letter-spacing: 0.015em; text-transform: uppercase;">
  EYEBROW
</div>

- Proposed family token: `whistler_blackcomb/family/primary`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `inherited current heading ladder`
- Notes: Eyebrow stays in the heading family and weight, with smaller size behavior defined downstream.

### Role: subhead

<div style="font-family: sans-serif; font-weight: 700; font-size: 24px; line-height: 1; letter-spacing: 0; text-transform: none;">
  Subheads
</div>

- Proposed family token: `whistler_blackcomb/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: Supporting headline lane mapped through the stronger body weight semantic.

### Role: body

<div style="font-family: sans-serif; font-weight: 400; font-size: 18px; line-height: 1.4; letter-spacing: 0; text-transform: none;">
  Body
</div>

- Proposed family token: `whistler_blackcomb/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `inherited current body ladder`
- Notes: Reading-copy treatment with 140 percent leading.

### Role: action

<div style="font-family: sans-serif; font-weight: 700; font-size: 18px; line-height: 1; letter-spacing: 0; text-transform: none;">
  Button
</div>

- Proposed family token: `whistler_blackcomb/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current action ladder`
- Notes: Action copy maps directly to the existing bold action lane.

## Review Notes

- Whistler Blackcomb fits the existing one-family semantic pattern cleanly.
- The hierarchy is carried by weight plus tracking and leading behavior, not by multiple semantic family lanes.
- Eyebrow remains documented as a role recipe rather than a new semantic token because the current typography schema has no eyebrow lane.

## Review Readiness

- Subject: `Whistler Blackcomb headline behavior`
  Channels: `web, email, ads`
  Rule: Keep headlines and eyebrows on Proxima Nova Black with 15 tracking; headlines use 90 percent leading and eyebrows use 100 percent leading.
  Source basis: Whistler Blackcomb hierarchy guidance image.

- Subject: `Whistler Blackcomb supporting copy`
  Channels: `web, email, ads`
  Rule: Keep subheads on Proxima Nova Bold, body on Proxima Nova Regular, and button copy on Proxima Nova Bold while staying inside the existing one-family semantic typography model.
  Source basis: Whistler Blackcomb hierarchy guidance image.
