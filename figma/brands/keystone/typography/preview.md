# Keystone Typography Preview

Status: approved and written to `_Global: Typography`, `Semantic: Typography`, and `Keystone` in `Design System` on 2026-03-12

## Original Source Roles

- Source role: `headline`
  Family: `Futura`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `primary display headline`
  Case: `Sentence case`
  Tracking: `0%`
  Leading: `4px difference`
  Size rule: `48px / 52px example`
  Punctuation: `not specified`
  Sample copy: `Headline`
  Notes: Explicit headline recipe from the source.

- Source role: `subheadline`
  Family: `Avenir`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `supporting headline copy`
  Case: `Sentence case`
  Tracking: `0%`
  Leading: `4px difference`
  Size rule: `36px / 40px example`
  Punctuation: `not specified`
  Sample copy: `Sub Headline`
  Notes: Explicit subheadline recipe from the source.

- Source role: `body`
  Family: `Avenir`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `0%`
  Leading: `4px difference`
  Size rule: `16px / 20px example`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Body Copy`
  Notes: Explicit body recipe from the source.

- Source role: `emphasized_body_copy`
  Family: `Futura`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `emphasized short body copy`
  Case: `Sentence case`
  Tracking: `0%`
  Leading: `4px difference`
  Size rule: `16px / 20px example`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Emphasized body copy`
  Notes: Explicit emphasized body recipe from the source.

- Source role: `cta`
  Family: `Futura`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `action or button copy`
  Case: `Title Case`
  Tracking: `not specified`
  Leading: `not specified`
  Size rule: `20px example`
  Punctuation: `not specified`
  Sample copy: `CTA`
  Notes: Final approved CTA mapping.

## Primitive Recommendations

- Proposed primitive:
  Token name: `keystone/family/primary`
  Source item: `Futura`
  Fallback token: `universal/family/web_safe`
  Notes: Primary Keystone display and emphasis family.

- Proposed primitive:
  Token name: `keystone/family/secondary`
  Source item: `Avenir`
  Fallback token: `universal/family/web_safe`
  Notes: Secondary Keystone reading family.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Headline, emphasized body copy, and CTA use Bold.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: Subheadline and body use Medium.

- Reuse:
  Source item: `20px CTA`
  Proposed token: `universal/size/500`
  Assumption status: `explicit`
  Notes: CTA size fits the existing shared ladder, so no new raw size token was introduced.

## Hold For Review

- Item: `none`
  Reason: Preview review is complete for this first Keystone write.

## Semantic Mapping

- `family/heading` -> `keystone/family/primary`
- `family/body` -> `keystone/family/secondary`
- `family/action` -> `keystone/family/primary`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/medium`
- `weight/action/base` -> `universal/weight/bold`
- `size/action/base` -> `universal/size/500`
- No new shared size step was added for the explicit 48px headline recipe

## Role Recipes

### Role: headline

<div style="font-family: 'Futura', sans-serif; font-weight: 700; font-size: 48px; line-height: 52px; letter-spacing: 0; text-transform: none;">
  Headline
</div>

- Proposed family token: `keystone/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `deferred`
- Notes: The explicit source recipe remains documented, but this live write did not add a new raw size token.

### Role: subheadline

<div style="font-family: 'Avenir', sans-serif; font-weight: 500; font-size: 36px; line-height: 40px; letter-spacing: 0; text-transform: none;">
  Sub Headline
</div>

- Proposed family token: `keystone/family/secondary`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `deferred`
- Notes: The explicit source size remains documented, but no new size override was introduced in this pass.

### Role: body

<div style="font-family: 'Avenir', sans-serif; font-weight: 500; font-size: 16px; line-height: 20px; letter-spacing: 0; text-transform: none;">
  Body Copy
</div>

- Proposed family token: `keystone/family/secondary`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `universal/size/300`
- Notes: Fully represented by the current shared body size step.

### Role: emphasized_body_copy

<div style="font-family: 'Futura', sans-serif; font-weight: 700; font-size: 16px; line-height: 20px; letter-spacing: 0; text-transform: none;">
  Emphasized body copy
</div>

- Proposed family token: `keystone/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/300`
- Notes: Small-size emphasis lane using the display family.

### Role: cta

<div style="font-family: 'Futura', sans-serif; font-weight: 700; font-size: 20px; line-height: 24px; letter-spacing: 0; text-transform: capitalize;">
  CTA
</div>

- Proposed family token: `keystone/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/500`
- Notes: Final approved CTA mapping for the live Keystone write.

## Review Notes

- CTA is now resolved to Futura Bold.
- No new shared size token was introduced in this pass.
- The explicit 48px headline recipe remains documented for a future size-ladder review rather than being silently collapsed into a new raw size.

## Review Readiness

- Subject: `Keystone CTA family`
  Channels: `web, email, ads`
  Rule: CTA uses Futura Bold in Title Case.
  Source basis: User-approved preview review after the source contradiction was surfaced.

- Subject: `Keystone size ladder scope`
  Channels: `web, email, ads`
  Rule: Keep the current shared size ladder unchanged in this pass.
  Source basis: User-approved preview review direction.
