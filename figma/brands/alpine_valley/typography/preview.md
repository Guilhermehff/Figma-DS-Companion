# Alpine Valley Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/alpine_valley/brand.yml` and Figma.

## Original Source Roles

- Source role: `primary_header`
  Family: `Prompt`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_header_h1`
  Case: `all_caps_in_example`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels H1 but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `PROMPT BOLD: PRIMARY HEADER (H1)`
  Notes: The source explicitly shows Prompt Bold for the primary header.

- Source role: `secondary_header`
  Family: `Prompt`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `secondary_header_h2`
  Case: `all_caps_in_example`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels H2 but does not define governed token sizes`
  Punctuation: `not specified in source`
  Sample copy: `PROMPT BOLD: SECONDARY HEADER (H2)`
  Notes: The source explicitly shows Prompt Bold for the secondary header.

- Source role: `body`
  Family: `Prompt`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `not specified in source`
  Leading: `not specified in source`
  Size rule: `source labels body copy but does not define governed token sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `PROMPT REGULAR: Alpine Valley is an easy getaway...`
  Notes: The source explicitly shows Prompt Regular for body copy.

## Primitive Recommendations

- Proposed primitive:
  Token name: `alpine_valley/family/01`
  Source item: `Prompt`
  Fallback token: `universal/family/fallback`
  Notes: One-family Alpine Valley digital campaign system across H1, H2, and body copy.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: H1 and H2 lane.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: Body lane.

## Live Semantic Mapping

- `family/heading` -> `alpine_valley/family/01`
- `family/body` -> `alpine_valley/family/01`
- `family/action` -> `alpine_valley/family/01`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/bold`
- `weight/action/base` -> `universal/weight/bold`
- `family/*_safe` -> inherit `universal/family/fallback`
- `size/*` -> inherit current semantic base

## Review Notes

- Alpine Valley can stage on one raw family, `Prompt`, because the reviewed system uses Bold and Regular variants of the same family.
- Extra Bold and italic variants remain documented raw Prompt options, but the current semantic pass does not need extra family or weight slots for them.
- User-approved follow-up: CTA also stages on Prompt, using Bold for the live semantic action pass.

## Review Readiness

- Subject: `Alpine Valley campaign typography`
  Channels: `web, email, ads`
  Rule: Keep H1 and H2 on Prompt Bold and body on Prompt Regular.
  Source basis: Alpine Valley campaign typography guide image.

- Subject: `Alpine Valley CTA typography`
  Channels: `web, email, ads`
  Rule: Use Prompt for CTA copy and stage the live semantic action pass on Bold.
  Source basis: User-approved follow-up in chat.
