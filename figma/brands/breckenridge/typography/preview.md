# Breckenridge Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/breckenridge/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `primary display headline`
  Case: `ALL CAPS`
  Tracking: `0px`
  Sample copy: `LOREM IPSUM DOLOR SIT.`

- Source role: `subhead`
  Family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `supporting headline copy`
  Case: `Sentence case`
  Tracking: `-15px`
  Sample copy: `Lorem ipsum dolor sit sed elit dolore magna aliqua.`

- Source role: `body`
  Family: `Avenir Next`
  Style: `Avenir Next`
  Weight label: `not specified`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `0px`
  Sample copy: `Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.`

- Source role: `cta`
  Family: `Poppins`
  Style: `Poppins Bold`
  Weight label: `Bold`
  Usage scope: `action copy`
  Case: `Sentence case`
  Tracking: `-15px`
  Sample copy: `Learn more`

## Primitive Recommendations

- Proposed primitive:
  Token name: `breckenridge/family/01`
  Source item: `Poppins`
  Fallback token: `universal/family/fallback`
  Notes: Shared brand family across headline, subhead, and CTA.

- Proposed primitive:
  Token name: `breckenridge/family/02`
  Source item: `Avenir Next`
  Fallback token: `universal/family/fallback`
  Notes: Secondary reading family for body copy.

- Reuse:
  Source item: `body copy default weight`
  Proposed token: `universal/weight/normal`
  Assumption status: `assumed`
  Notes: The source does not list a body weight beyond the family name, so the first review keeps body on the normal raw weight.

- Proposed primitive:
  Token name: `universal/weight/bold`
  Source item: `Bold`
  Notes: Shared raw bold weight used by headline, subhead, and CTA.

## Semantic Mapping

- `family/heading` -> `breckenridge/family/01`
- `family/body` -> `breckenridge/family/02`
- `family/action` -> `breckenridge/family/01`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/action/base` -> `universal/weight/bold`
- Safe aliases remain on `universal/family/fallback`

## Role Recipes

### Role: headline

<div style="font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 36px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  LOREM IPSUM DOLOR SIT.
</div>

- Proposed family token: `breckenridge/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/800`
- Notes: Weight token now exists as a shared raw typography token.

### Role: subhead

<div style="font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 24px; line-height: 1.2; letter-spacing: -0.15px; text-transform: none;">
  Lorem ipsum dolor sit sed elit dolore magna aliqua.
</div>

- Proposed family token: `breckenridge/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/600`
- Notes: Negative tracking comes directly from the source and should be preserved in downstream review.

### Role: body

<div style="font-family: 'Avenir Next', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; letter-spacing: 0; text-transform: none;">
  Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
</div>

- Proposed family token: `breckenridge/family/02`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Body weight remains an assumption because the source provides only the family name.

### Role: cta

<div style="font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 16px; line-height: 1.2; letter-spacing: -0.15px; text-transform: none;">
  Learn more
</div>

- Proposed family token: `breckenridge/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/300`
- Notes: CTA uses the shared raw bold weight and is now covered by the live Breckenridge semantic theme typography overrides.

## Review Readiness

- Subject: `headline`
  Channels: `web, email, ads`
  Rule: Keep the headline in all caps with 0px tracking.
  Source basis: Breckenridge type hierarchy image.

- Subject: `subhead and cta`
  Channels: `web, email, ads`
  Rule: Keep both in sentence case with negative tracking.
  Source basis: Breckenridge type hierarchy image.

- Subject: `safe typography aliases`
  Channels: `email`
  Rule: Use safe family aliases when Poppins or Avenir Next cannot be relied on in delivery.
  Source basis: Safe-family governance for constrained channels.
