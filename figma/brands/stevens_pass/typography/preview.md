# Stevens Pass Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/stevens_pass/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Gibson`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary display headline`
  Notes: The source explicitly labels headlines as `Gibson Bold`.

- Source role: `subhead`
  Family: `Gibson`
  Style: `Semi Bold`
  Weight label: `Semi Bold`
  Usage scope: `supporting headline copy`
  Notes: The source explicitly labels subheads as `Gibson Semi Bold`.

- Source role: `cta`
  Family: `Gibson`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `action or button copy`
  Notes: The source explicitly labels CTA as `Gibson Regular`.

- Source role: `body`
  Family: `Gibson`
  Style: `Medium`, `Regular`, `Light`, and italic variants
  Weight label: `Mixed`
  Usage scope: `reading copy`
  Notes: The source shows multiple approved body variants rather than a single semantic default.

## Primitive Recommendations

- Proposed primitive:
  Token name: `stevens_pass/family/primary`
  Source item: `Gibson`
  Fallback token: `universal/family/web_safe`
  Notes: One-family Stevens Pass system across headline, subhead, CTA, and body roles.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Headline lane.

- Reuse:
  Source item: `Semi Bold`
  Proposed token: `universal/weight/semibold`
  Assumption status: `explicit`
  Notes: Subhead lane.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: CTA lane and one allowed body variant.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: One allowed body variant and the recommended `body/base` candidate.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `explicit`
  Notes: Approved raw body variant.

## Proposed Semantic Mapping

- `family/heading` -> `stevens_pass/family/primary`
- `family/body` -> `stevens_pass/family/primary`
- `family/action` -> `stevens_pass/family/primary`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/light`
- `weight/body/strong` -> `universal/weight/medium`
- `weight/action/base` -> `universal/weight/medium`
- `size/*` remain inherited

## Review Notes

- Stevens Pass fits the existing one-family semantic pattern cleanly.
- User-approved exception: even though the source labels subheads as `Semi Bold` and CTA as `Regular`, the approved live mapping uses `body/base = Light`, `body/strong = Medium`, and `action/base = Medium`.
- Regular, Light, Medium, and italic variants remain documented raw Gibson options for downstream channel recipes.

## Approved Exception

- `weight/body/base` -> `universal/weight/light`
- `weight/body/strong` -> `universal/weight/medium`
- `weight/action/base` -> `universal/weight/medium`
- Reason: This is the approved exception in chat resolving the ambiguous body baseline and overriding the source CTA weight for the live semantic pass.
