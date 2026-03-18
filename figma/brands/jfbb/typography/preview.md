# JFBB Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/jfbb/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Vista Sans NAR OTCE`
  Style: `Black`
  Weight label: `Black`
  Usage scope: `primary display headline`
  Case: `all caps`
  Tracking: `0%`
  Leading: `+10px`
  Size rule: `example 44px / 54px leading, not a governed token size`
  Punctuation: `not specified`
  Sample copy: `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG`
  Notes: Use for headlines and bold impactful type.

- Source role: `subheadline`
  Family: `Vista Sans NAR OTCE`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `supporting headline copy`
  Case: `all caps`
  Tracking: `0%`
  Leading: `+10px`
  Size rule: `example 36px / 46px leading, not a governed token size`
  Punctuation: `punctuation allowed`
  Sample copy: `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.`
  Notes: The source says subheads should lean into Bold.

- Source role: `body`
  Family: `Vista Sans NAR OTCE`
  Style: `Book`
  Weight label: `Book`
  Usage scope: `reading copy`
  Case: `sentence case`
  Tracking: `0%`
  Leading: `source lists 100px difference and 24px / 124px example`
  Size rule: `body example is internally inconsistent and not treated as a governed token size`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `The quick brown fox jumps over the lazy dog.`
  Notes: Body copy should use Book.

## Primitive Recommendations

- Proposed primitive:
  Token name: `jfbb/family/primary`
  Source item: `Vista Sans NAR OTCE`
  Fallback token: `universal/family/web_safe`
  Notes: Shared family for the full JFBB hierarchy.

- Reuse:
  Source item: `Black`
  Proposed token: `universal/weight/black`
  Assumption status: `explicit`
  Notes: Direct shared raw match.

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `explicit`
  Notes: Direct shared raw match.

- Reuse:
  Source item: `Book`
  Proposed token: `universal/weight/normal`
  Assumption status: `assumed`
  Notes: No separate shared book primitive exists in the current raw ladder.

## Hold For Review

- Item: `action typography`
  Reason: The source does not define CTA or button-specific typography behavior.

## Semantic Mapping

- `family/heading` -> `jfbb/family/primary`
- `family/body` -> `jfbb/family/primary`
- `weight/heading/base` -> `universal/weight/black`
- `weight/body/base` -> `universal/weight/normal`
- `weight/body/strong` -> `universal/weight/bold`
- `family/action`, `weight/action/*`, and `size/*` remain inherited in the live extension

## Role Recipes

### Role: headline

<div style="font-family: 'Vista Sans NAR OTCE', sans-serif; font-weight: 900; font-size: 36px; line-height: 1.3; letter-spacing: 0; text-transform: uppercase;">
  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
</div>

- Proposed family token: `jfbb/family/primary`
- Proposed weight token: `universal/weight/black`
- Proposed size token: `universal/size/700`
- Notes: Strong all-caps headline lane.

### Role: subheadline

<div style="font-family: 'Vista Sans NAR OTCE', sans-serif; font-weight: 700; font-size: 24px; line-height: 1.42; letter-spacing: 0; text-transform: uppercase;">
  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
</div>

- Proposed family token: `jfbb/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/500`
- Notes: Supportive all-caps headline lane.

### Role: body

<div style="font-family: 'Vista Sans NAR OTCE', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.6; letter-spacing: 0;">
  The quick brown fox jumps over the lazy dog.
</div>

- Proposed family token: `jfbb/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/200`
- Notes: The source body-leading example is internally inconsistent, so the live extension keeps shared size semantics.

## Review Notes

- JFBB can stage cleanly on one family primitive, with weight carrying the hierarchy.
- `Book` is approximated to the shared `normal` raw weight because no distinct governed book primitive exists today.
- The body-leading note in the source appears defective, so the live extension intentionally keeps size semantics inherited.

## Review Readiness

- Subject: `JFBB headline lane`
  Channels: `web, email, ads`
  Rule: Keep headlines on Vista Sans NAR OTCE Black in all caps with 0 tracking and a 10px leading offset.
  Source basis: JFBB hierarchy guidance image.

- Subject: `JFBB supporting and body copy`
  Channels: `web, email, ads`
  Rule: Keep subheadlines on Vista Sans NAR OTCE Bold in all caps and body on Vista Sans NAR OTCE Book in sentence case; do not create a size override from the inconsistent body-leading example.
  Source basis: JFBB hierarchy guidance image.
