# Crested Butte Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/crested_butte/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Gibson`
  Style: `Gibson Semibold`
  Weight label: `Semibold`
  Usage scope: `primary display headline`
  Case: `lowercase`
  Tracking: `regular`
  Sample copy: `gibson semibold`

- Source role: `subhead`
  Family: `Gibson`
  Style: `Gibson Semibold`
  Weight label: `Semibold`
  Usage scope: `supporting headline copy`
  Case: `ALL CAPS`
  Tracking: `regular`
  Sample copy: `GIBSON SEMIBOLD`

- Source role: `body`
  Family: `Gibson`
  Style: `Gibson Regular`
  Weight label: `Regular`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `regular`
  Sample copy: `Gibson Regular is our default body copy font, and should primarily be used in black on white backgrounds in layout.`

## Primitive Recommendations

- Proposed primitive:
  Token name: `crested_butte/family/01`
  Source item: `Gibson`
  Fallback token: `universal/family/fallback`
  Notes: A single family covers headline, sub-headline, and body.

- Reuse:
  Source item: `Gibson Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: Body copy is defined as Regular in the source.

- Proposed primitive:
  Token name: `universal/weight/semibold`
  Source item: `Gibson Semibold`
  Notes: Shared raw weight needed so Crested Butte does not have to collapse Semibold into Bold.

## Semantic Mapping

- `family/heading` -> `crested_butte/family/01`
- `family/body` -> `crested_butte/family/01`
- `family/action` -> `crested_butte/family/01`
- `weight/heading/base` -> `universal/weight/semibold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/action/base` -> `universal/weight/semibold`
- Safe aliases remain on `universal/family/fallback`

## Role Recipes

### Role: headline

<div style="font-family: 'Gibson', sans-serif; font-weight: 600; font-size: 36px; line-height: 0.86; letter-spacing: 0; text-transform: none;">
  gibson<br/>semibold
</div>

- Proposed family token: `crested_butte/family/01`
- Proposed weight token: `universal/weight/semibold`
- Proposed size token: `universal/size/800`
- Notes: Preserve the lowercase lockup, 86% leading, and intentional line indentation in downstream layout work.

### Role: subhead

<div style="font-family: 'Gibson', sans-serif; font-weight: 600; font-size: 20px; line-height: 1.1; letter-spacing: 0; text-transform: uppercase;">
  GIBSON SEMIBOLD
</div>

- Proposed family token: `crested_butte/family/01`
- Proposed weight token: `universal/weight/semibold`
- Proposed size token: `universal/size/500`
- Notes: Keep the sub-headline to one line and limit it to black or white application.

### Role: body

<div style="font-family: 'Gibson', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; letter-spacing: 0; text-transform: none;">
  Gibson Regular is our default body copy font, and should primarily be used in black on white backgrounds in layout.
</div>

- Proposed family token: `crested_butte/family/01`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Body guidance is explicit about dark-on-light and light-on-dark use, so that behavior should carry downstream.

## Review Notes

- The first Crested Butte typography pass uses one family token because the source differentiates roles by weight, case, and layout behavior rather than by introducing a second family.
- `Semibold` is now written as the shared raw token `universal/weight/semibold` and is used by the Crested Butte semantic theme typography overrides.
- Numeric sizes are not provided in the source, so all size mappings remain provisional review defaults.

## Review Readiness

- Subject: `headline`
  Channels: `web, email, ads`
  Rule: Keep the headline lowercase with 86% leading and use the lockup indentation only where the layout can preserve the intended shape.
  Source basis: Crested Butte typography guidance image.

- Subject: `sub-headline`
  Channels: `web, email, ads`
  Rule: Keep the sub-headline all caps, single line, and black or white only.
  Source basis: Crested Butte typography guidance image.

- Subject: `body`
  Channels: `web, email, ads`
  Rule: Use Gibson Regular primarily in black on white layouts or white on dark backgrounds.
  Source basis: Crested Butte typography guidance image.
