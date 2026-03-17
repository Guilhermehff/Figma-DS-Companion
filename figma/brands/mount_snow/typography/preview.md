# Mount Snow Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/mount_snow/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Vastago Grotesk`
  Style: `Heavy`
  Weight label: `Heavy`
  Usage scope: `primary display headline`
  Case: `lowercase`
  Tracking: `0%`
  Leading: `+10px`
  Size rule: `example 44px / 54px leading, not a governed token size`
  Punctuation: `not specified`
  Sample copy: `the quick brown fox jumps over the lazy dog`
  Notes: Use for bold, impactful type.

- Source role: `subheadline`
  Family: `Area Extended`
  Style: `Extra Bold`
  Weight label: `Extra Bold`
  Usage scope: `supporting headline copy`
  Case: `sentence case`
  Tracking: `0%`
  Leading: `+10px`
  Size rule: `example 36px / 46px leading, not a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: Source says to lean into Bold or Extra Bold for subheads.

- Source role: `body`
  Family: `Area Extended`
  Style: `Medium`
  Weight label: `Medium`
  Usage scope: `reading copy`
  Case: `sentence case`
  Tracking: `0%`
  Leading: `+10px`
  Size rule: `example 20px / 30px leading, not a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: Body copy should use Medium.

## Primitive Recommendations

- Proposed primitive:
  Token name: `mount_snow/family/primary`
  Source item: `Vastago Grotesk`
  Fallback token: `universal/family/web_safe`
  Notes: Primary display family.

- Proposed primitive:
  Token name: `mount_snow/family/secondary`
  Source item: `Area Extended`
  Fallback token: `universal/family/web_safe`
  Notes: Shared family for Mount Snow subheadline and body copy.

- Reuse:
  Source item: `Heavy`
  Proposed token: `universal/weight/black`
  Assumption status: `assumed`
  Notes: Mapped to the strongest current shared raw weight.

- Reuse:
  Source item: `Extra Bold`
  Proposed token: `universal/weight/black`
  Assumption status: `assumed`
  Notes: Mapped to the strongest current shared raw weight in the absence of a governed extra-bold primitive.

- Reuse:
  Source item: `Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `explicit`
  Notes: Direct match to the existing shared raw ladder.

## Hold For Review

- Item: `action typography`
  Reason: The source does not define CTA or button-specific typography behavior.

## Semantic Mapping

- `family/heading` -> `mount_snow/family/primary`
- `family/body` -> `mount_snow/family/secondary`
- `weight/heading/base` -> `universal/weight/black`
- `weight/body/base` -> `universal/weight/medium`
- `weight/body/strong` -> `universal/weight/black`
- `family/action`, `weight/action/*`, and `size/*` remain inherited in the live extension

## Role Recipes

### Role: headline

<div style="font-family: 'Vastago Grotesk', sans-serif; font-weight: 900; font-size: 36px; line-height: 1.3; letter-spacing: 0; text-transform: lowercase;">
  the quick brown fox jumps over the lazy dog
</div>

- Proposed family token: `mount_snow/family/primary`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `universal/size/700`
- Notes: Strong lowercase headline lane.

### Role: subheadline

<div style="font-family: 'Area Extended', sans-serif; font-weight: 900; font-size: 24px; line-height: 1.42; letter-spacing: 0;">
  The quick brown fox jumps over the lazy dog.
</div>

- Proposed family token: `mount_snow/family/secondary`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `universal/size/500`
- Notes: Supportive headline lane using the same family as body.

### Role: body

<div style="font-family: 'Area Extended', sans-serif; font-weight: 500; font-size: 16px; line-height: 1.625; letter-spacing: 0;">
  The quick brown fox jumps over the lazy dog.
</div>

- Proposed family token: `mount_snow/family/secondary`
- Proposed weight token: `universal/weight/medium`
- Proposed size token: `universal/size/200`
- Notes: Reading-copy lane on the shared secondary family.

## Review Notes

- Mount Snow can stage cleanly on two family primitives: one headline family and one text family.
- `Heavy` and `Extra Bold` are both approximated to the existing shared black raw weight in this first pass.
- The source’s numeric pairs are treated as illustrative leading examples, so the live extension keeps size semantics inherited from the shared baseline.

## Review Readiness

- Subject: `Mount Snow headline lane`
  Channels: `web, email, ads`
  Rule: Keep headlines on Vastago Grotesk Heavy in lowercase with 0 tracking and a 10px leading offset.
  Source basis: Mount Snow hierarchy guidance image.

- Subject: `Mount Snow supporting copy`
  Channels: `web, email, ads`
  Rule: Keep subheadlines on Area Extended Extra Bold and body on Area Extended Medium, both in sentence case with 0 tracking and a 10px leading offset.
  Source basis: Mount Snow hierarchy guidance image.
