# Mount Sunapee Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/mount_sunapee/brand.yml` and Figma.

## Original Source Roles

- Source role: `headline`
  Family: `Graphik`
  Style: `Bold`
  Weight label: `Bold`
  Usage scope: `primary_headers_h1`
  Case: `sentence_case`
  Tracking: `75`
  Leading: `not specified`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified`
  Sample copy: `We lift people up.`
  Notes: The typography sheet explicitly labels Graphik Bold for Primary Headers (H1). The source does not specify the tracking unit, so this artifact preserves the numeric label as shown.

- Source role: `secondary_header`
  Family: `Graphik`
  Style: `Regular`
  Weight label: `Regular`
  Usage scope: `secondary_headers_h2`
  Case: `sentence_case`
  Tracking: `75`
  Leading: `not specified`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified`
  Sample copy: `We elevate spirits by creating fun, invigorating mountain experiences for everyone.`
  Notes: The typography sheet explicitly labels Graphik Regular for Secondary Headers (H2).

- Source role: `body`
  Family: `Graphik`
  Style: `Light`
  Weight label: `Light`
  Usage scope: `body_copy`
  Case: `sentence_case`
  Tracking: `25`
  Leading: `not specified`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Memories and stories of which are the reason families continue to leave their homes, flock to the mountains, and enjoy the awe-inspiring outdoors to be uplifted again and again.`
  Notes: The typography sheet explicitly labels Graphik Light for Body Copy.

- Source role: `subheader`
  Family: `Neutraface Text`
  Style: `Bold Italic`
  Weight label: `Bold Italic`
  Usage scope: `subheaders_h3`
  Case: `sentence_case`
  Tracking: `0`
  Leading: `not specified`
  Size rule: `source names the role and tracking but does not define governed numeric sizes`
  Punctuation: `not specified`
  Sample copy: `Activities`
  Notes: The typography sheet explicitly labels Neutraface Text Bold Italic for Subheaders (H3). The application example confirms that this is a distinct utility lane rather than the default Graphik heading system.

## Primitive Recommendations

- Reuse:
  Source item: `Bold`
  Proposed token: `universal/weight/bold`
  Assumption status: `direct_match`
  Notes: Covers Graphik Bold in the H1 lane.

- Reuse:
  Source item: `Regular`
  Proposed token: `universal/weight/normal`
  Assumption status: `direct_match`
  Notes: Covers Graphik Regular in the H2 lane.

- Reuse:
  Source item: `Light`
  Proposed token: `universal/weight/light`
  Assumption status: `direct_match`
  Notes: Covers Graphik Light in the body lane.

- Proposed primitive:
  Token name: `mount_sunapee/family/primary`
  Source item: `Graphik`
  Fallback token: `universal/family/web_safe`
  Notes: Graphik is the repeated Mount Sunapee typography system across H1, H2, and body.

- Proposed primitive:
  Token name: `mount_sunapee/family/utility`
  Source item: `Neutraface Text Bold Italic`
  Fallback token: `universal/family/web_safe`
  Notes: Preserve the H3 subheader face as a raw utility family until the semantic typography schema gains a dedicated subhead lane.

## Semantic Mapping

- `family/heading` -> `mount_sunapee/family/primary`
- `family/body` -> `mount_sunapee/family/primary`
- `family/action` -> inherited from the base semantic typography collection in the first pass
- `family/heading_safe` -> `universal/family/web_safe`
- `family/body_safe` -> `universal/family/web_safe`
- `family/action_safe` -> inherited from the base semantic typography collection in the first pass
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/light`
- `weight/body/strong` -> `universal/weight/normal`
- `size/...` -> inherited from the current semantic typography ladder
- Inherited or deferred notes: action remains inherited because the source does not define a CTA recipe

## Role Recipes

### Role: headline

<div style="font-family: sans-serif; font-weight: 700; font-size: 32px; line-height: 1.2; letter-spacing: 0.075em; color:#253542;">
  We lift people up.
</div>

- Proposed family token: `mount_sunapee/family/primary`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: H1 remains on Graphik Bold.

### Role: secondary_header

<div style="font-family: sans-serif; font-weight: 400; font-size: 24px; line-height: 1.3; letter-spacing: 0.075em; color:#14b3c1;">
  We elevate spirits by creating fun, invigorating mountain experiences for everyone.
</div>

- Proposed family token: `mount_sunapee/family/primary`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `inherited current heading and body ladders`
- Notes: Approved live write. H2 stages through the Graphik family with the shared normal weight.

### Role: body

<div style="font-family: sans-serif; font-weight: 300; font-size: 18px; line-height: 1.6; letter-spacing: 0.025em; color:#6f898d;">
  Memories and stories of which are the reason families continue to leave their homes, flock to the mountains, and enjoy the awe-inspiring outdoors to be uplifted again and again.
</div>

- Proposed family token: `mount_sunapee/family/primary`
- Proposed weight token: `universal/weight/light`
- Proposed size token: `inherited current body ladder`
- Notes: Body copy remains on Graphik Light.

### Role: subheader

<div style="font-family: serif; font-style: italic; font-weight: 700; font-size: 24px; line-height: 1.2; letter-spacing: 0; color:#253542;">
  Activities
</div>

- Proposed family token: `mount_sunapee/family/utility`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `inherited current heading ladder`
- Notes: Raw-only utility recipe. It remains outside the live semantic extension until a subhead family lane exists.

## Review Notes

- Graphik stages cleanly as the shared heading and body family, with weight carrying the hierarchy between H1, H2, and body.
- Neutraface Text Bold Italic remains a raw utility recipe for H3 subheaders.
- The source does not define a CTA or action lane, so action remains inherited in the live semantic extension.

## Review Readiness

- Subject: `Mount Sunapee Graphik system`
  Channels: `web, email, ads`
  Rule: Keep H1 on Graphik Bold, H2 on Graphik Regular, and body copy on Graphik Light.
  Source basis: Mount Sunapee typography image.

- Subject: `Mount Sunapee H3 lane`
  Channels: `web, email, ads`
  Rule: Preserve Neutraface Text Bold Italic as a distinct raw subheader recipe rather than forcing it into the primary Graphik semantic family mapping.
  Source basis: Mount Sunapee typography image and application example.
