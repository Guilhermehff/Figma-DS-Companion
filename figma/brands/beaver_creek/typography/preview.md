# Beaver Creek Typography Preview

Review state: approved preview artifact aligned to the Beaver Creek source guidance. Verify live write state in `figma/brands/beaver_creek/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `IvyPresto Display`
  Style: `Thin`
  Weight label: `Thin`
  Usage scope: `primary display headline`
  Case: `not specified`
  Tracking: `90`
  Leading: `1:1.2`
  Size rule: `not numerically specified`
  Punctuation: `not specified`
  Sample copy: `Headlines`
  Notes: Center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `subhead_or_cta`
  Family: `Vinila Condensed`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting headline copy or CTA`
  Case: `not specified`
  Tracking: `80`
  Leading: `1:1.2`
  Size rule: `not numerically specified`
  Punctuation: `not specified`
  Sample copy: `CTA / Subheadlines`
  Notes: Center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `body`
  Family: `Vinila`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `reading copy`
  Case: `not specified`
  Tracking: `10`
  Leading: `1:1.7`
  Size rule: `not numerically specified`
  Punctuation: `not specified`
  Sample copy: `All body copy should be in Light.`
  Notes: Center justified unless a specific layout calls for left justification. Kerning is optical.

- Source role: `url`
  Family: `Vinila Condensed`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `non-clickable URL`
  Case: `mixed case`
  Tracking: `120`
  Leading: `not specified`
  Size rule: `not numerically specified`
  Punctuation: `Always include BeaverCreek.com when relevant to media is not clickable.`
  Sample copy: `BeaverCreek.com`
  Notes: Distinct utility recipe.

## Primitive Recommendations

- Proposed primitive:
  Token name: `beaver_creek/family/01`
  Source item: `IvyPresto Display`
  Fallback token: `universal/family/fallback`
  Notes: Primary display family.

- Proposed primitive:
  Token name: `beaver_creek/family/02`
  Source item: `Vinila`
  Fallback token: `universal/family/fallback`
  Notes: Reading family.

- Proposed primitive:
  Token name: `beaver_creek/family/03`
  Source item: `Vinila Condensed`
  Fallback token: `universal/family/fallback`
  Notes: Condensed family for CTA and subheadline work.

- Proposed primitive:
  Token name: `universal/weight/thin`
  Source item: `Thin`
  Notes: New shared raw weight needed to preserve Beaver Creek display typography faithfully.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `explicit`
  Notes: Used for Beaver Creek body copy and the non-clickable URL recipe.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Used for Beaver Creek CTA and subheadline work.

## Hold For Review

- Item: `semantic URL lane`
  Reason: Current semantic typography only exposes one action family and one action base weight, so the URL recipe remains raw guidance rather than a new semantic slot.

## Semantic Mapping

- `family/heading` -> `beaver_creek/family/01`
- `family/body` -> `beaver_creek/family/02`
- `family/action` -> `beaver_creek/family/03`
- `weight/heading/base` -> `universal/weight/thin`
- `weight/body/base` -> `universal/weight/light`
- `weight/action/base` -> `universal/weight/bold`
- Beaver Creek keeps `size/*` inherited from the shared baseline

## Role Recipes

### Role: headline

<div style="font-family: 'IvyPresto Display', serif; font-weight: 200; font-size: 36px; line-height: 1.2; letter-spacing: 0.09em;">
  Headlines
</div>

- Proposed family token: `beaver_creek/family/01`
- Proposed weight token: `universal/weight/thin`
- Proposed size token: `universal/size/700`
- Notes: Beaver Creek display lane with high tracking and optical kerning.

### Role: subhead_or_cta

<div style="font-family: 'Vinila Condensed', sans-serif; font-weight: 700; font-size: 20px; line-height: 1.2; letter-spacing: 0.08em;">
  CTA / Subheadlines
</div>

- Proposed family token: `beaver_creek/family/03`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/400`
- Notes: Shared supporting and action lane.

### Role: body

<div style="font-family: 'Vinila', sans-serif; font-weight: 300; font-size: 16px; line-height: 1.7; letter-spacing: 0.01em;">
  All body copy should be in Light.
</div>

- Proposed family token: `beaver_creek/family/02`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `universal/size/200`
- Notes: Reading lane with the loosest leading ratio in the system.

### Role: url

<div style="font-family: 'Vinila Condensed', sans-serif; font-weight: 300; font-size: 14px; line-height: 1.2; letter-spacing: 0.12em;">
  BeaverCreek.com
</div>

- Proposed family token: `beaver_creek/family/03`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `universal/size/100`
- Notes: Raw-only utility recipe for non-clickable media.

## Review Notes

- Beaver Creek can stay within the current three-lane semantic family model by using IvyPresto Display for heading, Vinila for body, and Vinila Condensed for action.
- The URL treatment reuses the condensed family with a lighter weight and higher tracking, so it remains a documented raw recipe instead of expanding the semantic schema.
- `universal/weight/thin` is the only new shared raw typography primitive required by this brand pass.

## Review Readiness

- Subject: `Beaver Creek headline lane`
  Channels: `web, email, ads`
  Rule: Keep headlines on IvyPresto Display Thin with tracking `90`, optical kerning, and a 1 to 1.2 size-to-leading ratio.
  Source basis: Beaver Creek typography guidance image.

- Subject: `Beaver Creek action lane`
  Channels: `web, email, ads`
  Rule: Keep CTA and subheadline work on Vinila Condensed Bold with tracking `80`.
  Source basis: Beaver Creek typography guidance image.

- Subject: `Beaver Creek reading and URL treatments`
  Channels: `web, email, ads`
  Rule: Keep body copy on Vinila Light with tracking `10` and the non-clickable URL recipe on Vinila Condensed Light with tracking `120`.
  Source basis: Beaver Creek typography guidance image.
