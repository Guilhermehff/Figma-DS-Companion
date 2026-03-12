# Northstar Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/northstar/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `New Order`
  Style: `New Order Medium`
  Weight label: `Medium`
  Usage scope: `primary display headline`
  Case: `Sentence case`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `headline size not numerically specified`
  Punctuation: `required`
  Sample copy: `Headlines will be in New Order Medium in sentence case, left justified.`
  Notes: The source explicitly calls for left justification and 0px tracking.

- Source role: `subhead`
  Family: `New Order`
  Style: `New Order Regular`
  Weight label: `Regular`
  Usage scope: `supporting headline copy`
  Case: `Sentence case`
  Tracking: `0px`
  Leading: `equal to font size`
  Size rule: `sub-headline size not numerically specified`
  Punctuation: `required`
  Sample copy: `Sub-Headlines will be in New Order Regular in sentence case, left justified.`
  Notes: The source explicitly defines line-height as equal to the font size.

- Source role: `body`
  Family: `New Order`
  Style: `New Order Regular`
  Weight label: `Regular`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `0px`
  Leading: `1.8x type size`
  Size rule: `body size not numerically specified`
  Punctuation: `required`
  Sample copy: `Body Copy will be in New Order Regular in sentence case, left justified.`
  Notes: The source explicitly defines line-height as `1.8` times type size.

## Primitive Recommendations

- Proposed primitive:
  Token name: `northstar/family/primary`
  Source item: `New Order`
  Fallback token: `universal/family/web_safe`
  Notes: One brand family covers all reviewed Northstar typography roles.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: The source directly names New Order Medium for headlines.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: The source directly names New Order Regular for sub-headline and body roles.

## Hold For Review

- Item: `Adobe Fonts delivery link`
  Reason: The source references Adobe Fonts but the URL is not visible in the provided image.

- Item: `action typography`
  Reason: The source does not define CTA or action-specific typography behavior.

## Semantic Mapping

- `family/heading` -> `northstar/family/primary`
- `family/body` -> `northstar/family/primary`
- `weight/heading/base` -> `universal/weight/medium`
- `weight/body/base` -> `universal/weight/normal`
- `family/action`, `weight/action/*`, and safe aliases remain inherited until a delivery-specific Northstar rule exists

## Role Recipes

### Role: headline

<div style="font-family: 'New Order', sans-serif; font-weight: 500; font-size: 36px; line-height: 1.1; letter-spacing: 0; text-transform: none;">
  Headlines will be in New Order Medium in sentence case.
</div>

- Proposed family token: `northstar/family/primary`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `universal/size/800`
- Notes: Left justified, sentence case, 0px tracking, punctuation retained.

### Role: subhead

<div style="font-family: 'New Order', sans-serif; font-weight: 400; font-size: 20px; line-height: 1; letter-spacing: 0; text-transform: none;">
  Sub-Headlines will be in New Order Regular in sentence case.
</div>

- Proposed family token: `northstar/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/500`
- Notes: Left justified, sentence case, leading equal to the font size.

### Role: body

<div style="font-family: 'New Order', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.8; letter-spacing: 0; text-transform: none;">
  Body Copy will be in New Order Regular in sentence case.
</div>

- Proposed family token: `northstar/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Left justified, sentence case, with 1.8x leading.

## Review Notes

- The source is strong on behavior and typographic voice, but it does not give numeric sizes, so all size mappings remain staged assumptions.
- Northstar can stage on one family token and existing shared weight tokens without expanding the raw typography ladder.
- No action role was supplied, so action aliases remain inherited rather than guessed.

## Review Readiness

- Subject: `Northstar headline and sub-headline`
  Channels: `web, email, ads`
  Rule: Keep the sentence-case New Order system, with Medium reserved for headlines and Regular for supporting copy.
  Source basis: Northstar typography and typography-in-use images.

- Subject: `Northstar body copy`
  Channels: `web, email, ads`
  Rule: Keep body copy on New Order Regular with 1.8x line-height and punctuation.
  Source basis: Northstar typography-in-use image.
