# Liberty Mountain Typography Preview

Review state: written_in_figma preview artifact. Verify live write state in `figma/brands/liberty_mountain/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Brown`
  Safe family: `Semplicitapro`
  Style: `Brown Regular`
  Weight label: `Regular`
  Usage scope: `Headlines`
  Case: `not specified in source`
  Tracking: `-40`
  Leading: `90 percent minimum / 100 percent maximum`
  Size rule: `36 to 72 pt and above`
  Punctuation: `not specified in source`
  Sample copy: `Duis non, commodo luctus!`
  Notes: The source also lists Brown Light in the Headlines section, so Brown Light remains documented as a raw alternate headline treatment.

- Source role: `headline_alternate`
  Family: `Brown`
  Safe family: `Semplicitapro`
  Style: `Brown Light`
  Weight label: `Light`
  Usage scope: `Headlines`
  Case: `not specified in source`
  Tracking: `-40`
  Leading: `90 percent minimum / 100 percent maximum`
  Size rule: `36 to 72 pt and above`
  Punctuation: `not specified in source`
  Sample copy: `Maecenas diam eget.`
  Notes: Preserved in documentation as a raw alternate headline treatment rather than a separate semantic lane.

- Source role: `subheadline`
  Family: `Brown`
  Safe family: `Semplicitapro`
  Style: `Brown Light`
  Weight label: `Light`
  Usage scope: `Sub headline`
  Case: `not specified in source`
  Tracking: `-40`
  Leading: `110 percent minimum / 120 percent maximum`
  Size rule: `14 to 36 pt`
  Punctuation: `not specified in source`
  Sample copy: `Donec ullamcorper nulla non metus auctor fringilla.`
  Notes: The source lists Sentinel Book as an alternate subheadline family.

- Source role: `body`
  Family: `Brown`
  Safe family: `Open Sans`
  Style: `Brown Light`
  Weight label: `Light`
  Usage scope: `Body copy`
  Case: `sentence case`
  Tracking: `0`
  Leading: `110 percent minimum / 120 percent maximum`
  Size rule: `below 14 pt`
  Punctuation: `not specified in source`
  Sample copy: `Lorem ipsum dolor sit amet, consectetur adipiscing elit.`
  Notes: The source lists Sentinel Book as an alternate body family.

- Source role: `alternate`
  Family: `Sentinel Book`
  Safe family: `Open Sans`
  Style: `Sentinel Book`
  Weight label: `Book`
  Usage scope: `Alternate sub headline and body copy`
  Case: `sentence case`
  Tracking: `not specified in source`
  Leading: `follows the paired role`
  Size rule: `follows the paired role`
  Punctuation: `not specified in source`
  Sample copy: `Nullam id dolor! Nibh ultricies ut id elit.`
  Notes: Preserved as a raw alternate family because the current semantic theme typography schema has no dedicated alternate serif lane.

## Role Recipes

### Role: heading

Proposed family token: `liberty_mountain/family/01`

Safe family token: `liberty_mountain/family_safe/01`

Proposed weight token: `universal/weight/normal`

Proposed size token: `inherited`

Recipe notes:

- Case: `not specified in source`
- Tracking: `-40`
- Leading: `90 percent minimum / 100 percent maximum`
- Size rule: `36 to 72 pt and above`
- Punctuation: `not specified in source`
- Notes: Brown Light remains documented as a raw alternate headline treatment.

### Role: subheadline

Proposed family token: `liberty_mountain/family/01`

Safe family token: `liberty_mountain/family_safe/01`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited`

Recipe notes:

- Case: `not specified in source`
- Tracking: `-40`
- Leading: `110 percent minimum / 120 percent maximum`
- Size rule: `14 to 36 pt`
- Punctuation: `not specified in source`
- Notes: Sentinel Book remains a raw alternate rather than a live semantic family override.

### Role: body

Proposed family token: `liberty_mountain/family/01`

Safe family token: `liberty_mountain/family_safe/02`

Proposed weight token: `universal/weight/light`

Proposed size token: `inherited`

Recipe notes:

- Case: `sentence case`
- Tracking: `0`
- Leading: `110 percent minimum / 120 percent maximum`
- Size rule: `below 14 pt`
- Punctuation: `not specified in source`
- Notes: Sentinel Book remains a raw alternate rather than a live semantic family override.
