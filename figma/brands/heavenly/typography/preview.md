# Heavenly Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/heavenly/brand.yml` and Figma.

## Original Source Roles

- Source role: `title`
  Family: `Din Condensed`
  Style: `Din Condensed Bold`
  Weight label: `Bold`
  Usage scope: `section title or emphasized copy`
  Case: `All caps`
  Tracking: `0`
  Leading: `not specified`
  Size rule: `title size not numerically specified`
  Punctuation: `not specified`
  Sample copy: `SKI HEAVENLY`
  Notes: Use for titles and specific emphasized copy lines.

- Source role: `headline`
  Family: `Din Condensed`
  Style: `Din Condensed Light`
  Weight label: `Light`
  Usage scope: `primary display headline`
  Case: `All caps`
  Tracking: `0`
  Leading: `not specified`
  Size rule: `headline size not numerically specified`
  Punctuation: `only when paired with the campaign logo lockup`
  Sample copy: `IT'S A MOUNTAIN, AND A BEACH`
  Notes: The source allows Bold only in specific cases such as manifestos or social headlines.

- Source role: `subhead`
  Family: `Brandon Grotesque`
  Style: `Brandon Grotesque Medium`
  Weight label: `Medium`
  Usage scope: `supporting headline copy`
  Case: `All caps`
  Tracking: `0`
  Leading: `not specified`
  Size rule: `subhead size not numerically specified`
  Punctuation: `not specified`
  Sample copy: `YOUR PHONE WON'T DO IT JUSTICE`
  Notes: Brandon Grotesque Medium in all caps for all subheads.

- Source role: `body`
  Family: `Brandon Grotesque`
  Style: `Brandon Grotesque Regular`
  Weight label: `Regular`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `0`
  Leading: `not specified`
  Size rule: `body size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?`
  Notes: Default body copy treatment.

## Primitive Recommendations

- Proposed primitive:
  Token name: `heavenly/family/01`
  Source item: `Din Condensed`
  Fallback token: `universal/family/fallback`
  Notes: One condensed display family spans Heavenly titles and headlines.

- Proposed primitive:
  Token name: `heavenly/family/02`
  Source item: `Brandon Grotesque`
  Fallback token: `universal/family/fallback`
  Notes: Secondary family spans the supportive and reading-copy roles.

- Proposed primitive:
  Token name: `universal/weight/light`
  Source item: `Light`
  Notes: Staged as a shared raw weight because Heavenly's default display headline is explicitly Light.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Titles use Din Condensed Bold.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: Subheads use Brandon Grotesque Medium.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `explicit`
  Notes: Body copy uses Brandon Grotesque Regular.

## Hold For Review

- Item: `action typography family`
  Reason: The source defines CTA tracking but does not name a CTA family, weight, or size.

- Item: `digital fallback for Din Condensed`
  Reason: The source mentions URW Din Condensed Regular for digital use, but it does not define whether that should become the semantic family or remain a delivery fallback note.

## Semantic Mapping

- `family/heading` -> `heavenly/family/01`
- `family/body` -> `heavenly/family/02`
- `weight/heading/base` -> `universal/weight/light`
- `weight/heading/strong` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/medium`
- `family/action` and `weight/action/*` remain inherited until CTA family guidance is explicit

## Role Recipes

### Role: title

<div style="font-family: 'Din Condensed', sans-serif; font-weight: 700; font-size: 18px; line-height: 1.1; letter-spacing: 0; text-transform: uppercase;">
  SKI HEAVENLY
</div>

- Proposed family token: `heavenly/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/400`
- Notes: Compact uppercase title treatment.

### Role: headline

<div style="font-family: 'Din Condensed', sans-serif; font-weight: 300; font-size: 36px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  IT'S A MOUNTAIN, AND A BEACH
</div>

- Proposed family token: `heavenly/family/01`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `universal/size/800`
- Notes: Default all-caps display headline. Bold remains reserved for specific emphasized cases.

### Role: subhead

<div style="font-family: 'Brandon Grotesque', sans-serif; font-weight: 500; font-size: 20px; line-height: 1.2; letter-spacing: 0; text-transform: uppercase;">
  YOUR PHONE WON'T DO IT JUSTICE
</div>

- Proposed family token: `heavenly/family/02`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `universal/size/500`
- Notes: All-caps support line using the secondary family.

### Role: body

<div style="font-family: 'Brandon Grotesque', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.6; letter-spacing: 0; text-transform: none;">
  Nam velliqui beatur alit la volorpo rionsedi consecus ent quam sumquiam, occatur?
</div>

- Proposed family token: `heavenly/family/02`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Sentence-case body copy.

## Review Notes

- Heavenly stages on two clear family lanes: Din Condensed for display and Brandon Grotesque for support and body copy.
- The source is explicit enough to stage role, family, weight, case, and tracking, but not enough to stage CTA family or numeric type sizes.
- `universal/weight/light` is staged as the one new shared raw weight needed to represent the supplied Heavenly system faithfully.

## Review Readiness

- Subject: `Heavenly display hierarchy`
  Channels: `web, email, ads`
  Rule: Keep titles and headlines in Din Condensed, all caps, with 0 tracking; default headline weight is Light and title/emphasis weight is Bold.
  Source basis: Heavenly typography image and the typography-in-use example.

- Subject: `Heavenly supporting copy`
  Channels: `web, email, ads`
  Rule: Keep subheads on Brandon Grotesque Medium in all caps and body copy on Brandon Grotesque Regular in sentence case.
  Source basis: Heavenly typography guidance image.

- Subject: `Heavenly CTA treatment`
  Channels: `web, email, ads`
  Rule: Preserve CTA tracking of 50 after CTA family and size are explicitly approved.
  Source basis: Heavenly typography note specifying CTA tracking.
