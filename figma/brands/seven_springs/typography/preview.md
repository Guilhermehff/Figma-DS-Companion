# Seven Springs Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/seven_springs/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Hoss Sharp`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary display headline`
  Tracking: `0px`
  Leading: `1:1`
  Notes: Left justified unless the layout calls for centering, with optical kerning.

- Source role: `subhead`
  Family: `Hoss Sharp`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting headline copy`
  Tracking: `0px`
  Leading: `1:1`
  Notes: The source says subheads follow the same alignment and leading rules as headlines.

- Source role: `body`
  Family: `Hoss Sharp`
  Style: `Medium`
  Weight label: `Medium`
  Usage scope: `reading copy`
  Tracking: `0px`
  Leading: `1:1.2`
  Notes: Left justified unless the layout calls for centering, with optical kerning.

- Source role: `cta`
  Family: `Hoss Sharp`
  Style: `Heavy`
  Weight label: `Heavy`
  Usage scope: `action or button copy`
  Tracking: `0px`
  Leading: `1:1`
  Notes: Left justified unless the layout calls for centering, with optical kerning.

## Primitive Recommendations

- Proposed primitive:
  Token name: `seven_springs/family/01`
  Source item: `Hoss Sharp`
  Fallback token: `universal/family/fallback`
  Notes: One-family Seven Springs system across headline, subhead, body, and CTA roles.

- Reuse:
  Source item: `Black`
  Proposed token: `universal/weight/black`
  Assumption status: `explicit`
  Notes: Headline treatment.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Subhead treatment.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: Body copy treatment.

- Reuse:
  Source item: `Heavy`
  Proposed token: `universal/weight/black`
  Assumption status: `approved default assumption`
  Notes: The shared raw ladder has no dedicated heavy primitive, so the first pass stages Heavy on Black.

## Approved Mapping

- `weight/heading/strong` -> `universal/weight/bold`
- Reason: The live write stages the Bold subhead treatment through the stronger heading slot because the current semantic theme typography schema has no dedicated subhead role.

## Semantic Mapping

- `family/heading` -> `seven_springs/family/01`
- `family/body` -> `seven_springs/family/01`
- `family/action` -> `seven_springs/family/01`
- `weight/heading/base` -> `universal/weight/black`
- `weight/heading/strong` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/medium`
- `weight/action/base` -> `universal/weight/black`
- `size/*` remain inherited

## Role Recipes

### Role: headline

<div style="font-family: 'Hoss Sharp', sans-serif; font-weight: 900; font-size: 36px; line-height: 1; letter-spacing: 0;">
  THESE SLOPES WON'T SKI THEMSELVES
</div>

- Proposed family token: `seven_springs/family/01`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `inherited current heading ladder`
- Notes: Left justified unless the layout calls for centering, with optical kerning.

### Role: subhead

<div style="font-family: 'Hoss Sharp', sans-serif; font-weight: 700; font-size: 24px; line-height: 1; letter-spacing: 0;">
  HEADLINES
</div>

- Proposed family token: `seven_springs/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: Proposed first pass routes the Bold subhead recipe through `weight/heading/strong`.

### Role: body

<div style="font-family: 'Hoss Sharp', sans-serif; font-weight: 500; font-size: 18px; line-height: 1.2; letter-spacing: 0;">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
</div>

- Proposed family token: `seven_springs/family/01`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `inherited current body ladder`
- Notes: Reading copy stays on Hoss Sharp Medium.

### Role: cta

<div style="font-family: 'Hoss Sharp', sans-serif; font-weight: 900; font-size: 20px; line-height: 1; letter-spacing: 0;">
  BOOK YOUR WINTER VACATION
</div>

- Proposed family token: `seven_springs/family/01`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `inherited current action ladder`
- Notes: Hoss Sharp Heavy stages on the strongest current raw weight.

## Review Notes

- Seven Springs fits the existing one-family semantic pattern cleanly.
- The live write stages the Bold subhead treatment through `weight/heading/strong`.
- Numeric size tokens remain inherited because the source defines relationships and behavior, not explicit governed sizes.

## Review Readiness

- Subject: `Seven Springs Hoss Sharp family`
  Channels: `web, email, ads`
  Rule: Keep headline, subhead, body, and CTA work on Hoss Sharp, with weight and layout behavior carrying the hierarchy.
  Source basis: Seven Springs typography guidance image.

- Subject: `Seven Springs subhead staging`
  Channels: `web, email, ads`
  Rule: Keep the Bold subhead treatment staged through `weight/heading/strong`.
  Source basis: User approval in chat plus the current semantic theme typography schema with no dedicated subhead role.
