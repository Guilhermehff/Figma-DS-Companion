# Liberty Mountain Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/liberty_mountain/brand.yml` and Figma.

## Original Source Roles

- Headline
  Family: `Brown`
  Styles: `Brown Regular`, `Brown Light`
  Tracking: `-40`
  Leading: `90 percent minimum / 100 percent maximum`
  Size rule: `36 to 72 pt and above`
- Sub headline
  Family: `Brown Light`
  Alternate: `Sentinel Book`
  Tracking: `-40`
  Leading: `110 percent minimum / 120 percent maximum`
  Size rule: `14 to 36 pt`
- Body copy
  Family: `Brown Light`
  Alternate: `Sentinel Book`
  Tracking: `0`
  Leading: `110 percent minimum / 120 percent maximum`
  Size rule: `below 14 pt`

## Primitive Recommendations

- Proposed raw primary family: `liberty_mountain/family/primary` -> `Brown`
- Proposed raw alternate family: `liberty_mountain/family/alternate` -> `Sentinel Book`
- Shared weights:
  - `Regular` -> `universal/weight/normal`
  - `Light` -> `universal/weight/light`

## Semantic Mapping

- `family/heading` -> `liberty_mountain/family/primary`
- `family/body` -> `liberty_mountain/family/primary`
- `family/action` -> `liberty_mountain/family/primary`
- `family/heading_safe` -> inherited `universal/family/web_safe`
- `family/body_safe` -> inherited `universal/family/web_safe`
- `family/action_safe` -> inherited `universal/family/web_safe`
- `weight/heading/base` -> `universal/weight/normal`
- `weight/heading/strong` -> `universal/weight/normal`
- `weight/body/base` -> `universal/weight/light`
- `weight/body/strong` -> `universal/weight/normal`
- `weight/action/base` -> `universal/weight/normal`
- `size/*` -> inherited from the shared semantic base

## Role Recipes

- Heading
  Sample copy: `Duis non, commodo luctus!`
  Proposed family token: `liberty_mountain/family/primary`
  Proposed weight token: `universal/weight/normal`
  Notes: Brown Light remains documented as a raw alternate headline treatment rather than a separate semantic slot.
- Subheadline
  Sample copy: `Donec ullamcorper nulla non metus auctor fringilla.`
  Proposed family token: `liberty_mountain/family/primary`
  Proposed weight token: `universal/weight/light`
  Notes: Sentinel Book remains raw-only in the first pass.
- Body
  Sample copy: `Lorem ipsum dolor sit amet, consectetur adipiscing elit.`
  Proposed family token: `liberty_mountain/family/primary`
  Proposed weight token: `universal/weight/light`
  Notes: Sentinel Book remains raw-only in the first pass.

## Review Notes

- Brown is the live family across the semantic hierarchy because the source explicitly defines it as the primary Liberty Mountain font for print and web.
- Sentinel Book is preserved as a governed raw family only; the current shared semantic typography ladder has no alternate serif slot.
- The live write overrides `weight/heading/strong` and `weight/action/base` away from the shared black default so Liberty Mountain does not inherit an unsupported heavy treatment.

## Review Readiness

- Subject: `Liberty Mountain Brown-led semantic family`
  Channels: `web`, `email`, `ads`
  Rule: Brown should drive heading, body, and action families.
  Source basis: Source typography page
- Subject: `Liberty Mountain Sentinel containment`
  Channels: `web`, `email`, `ads`
  Rule: Sentinel Book remains raw-only in the first pass.
  Source basis: Source typography page
