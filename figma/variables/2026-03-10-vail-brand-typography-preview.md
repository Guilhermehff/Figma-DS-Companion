# Brand Typography Preview

- Date: 2026-03-10
- Brand: vail
- Source reference: User-provided image in chat showing Vail typography guidance
- Intake artifact: [2026-03-10-vail-brand-typography-intake.yml](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/variables/2026-03-10-vail-brand-typography-intake.yml)
- Write status: approved and global family primitives written to `_global_typography` in `Design System` on 2026-03-11; semantic aliases remain documentation until semantic collection structure is finalized

## Original Source Roles

- Source role: `eyebrow`
  Family: `Avenir`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `section header or hierarchy breaker`
  Case: `ALL CAPS`
  Tracking: `0px`
  Leading: `Use text height to inform spacing between lines`
  Size rule: `0.5x headline size`
  Punctuation: `not specified`
  Sample copy: `SAMPLE EYEBROW`
  Notes: Use to break up the headline for stronger hierarchy or as a section title or header. Stroke width should be as thick as the text.

- Source role: `headline`
  Family: `Termina`
  Style: `Termina Black`
  Weight label: `Black`
  Usage scope: `primary display headline`
  Case: `ALL CAPS`
  Tracking: `0px`
  Leading: `Equal to font size`
  Size rule: `Base headline size not numerically specified`
  Punctuation: `No end punctuation by default; exceptions for question marks, exclamation points, and paired short thoughts`
  Sample copy: `HEADLINES SHOULD ALWAYS BE IN TERMINA`
  Notes: Headline style should be all caps.

- Source role: `subhead`
  Family: `Avenir`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `supporting headline copy`
  Case: `Sentence case`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `0.5x headline size`
  Punctuation: `allowed`
  Sample copy: `This is your subhead.`
  Notes: Subhead is half the size of headline type.

- Source role: `body`
  Family: `Avenir`
  Style: `Avenir Medium`
  Weight label: `Medium`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `0px`
  Leading: `1.6x type size`
  Size rule: `Base body size not numerically specified`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `This is your body copy. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sodales diam ut metus bibendum sodales. Curabitur congue ligula et leo scelerisque lacinia.`
  Notes: Avoid widows and orphans if possible.

- Source role: `cta`
  Family: `Avenir`
  Style: `Avenir Black`
  Weight label: `Black`
  Usage scope: `action or button copy`
  Case: `ALL CAPS`
  Tracking: `0px`
  Leading: `not specified`
  Size rule: `Base CTA size not numerically specified`
  Punctuation: `Do not use end punctuation`
  Sample copy: `PLAN YOUR VISIT`
  Notes: CTA styling is all caps.

## Primitive Recommendations

- Reuse:
  Source item: `Avenir Medium`
  Proposed token: `universal/weight/medium`
  Assumption status: `confirmed`
  Notes: Recommended reuse of the existing universal raw medium weight token.

- Proposed primitive:
  Token name: `vail/family/primary`
  Source item: `Avenir`
  Fallback token: `universal/family/web_safe`
  Notes: Shared text family for eyebrow, subhead, body, and cta. Because no fallback stack is provided, the review defaults to the universal web-safe family.

- Proposed primitive:
  Token name: `vail/family/display`
  Source item: `Termina`
  Fallback token: `universal/family/web_safe`
  Notes: Distinct display family for headline treatment. Because no fallback stack is provided, the review defaults to the universal web-safe family.

- Reuse:
  Source item: `Black`
  Proposed token: `universal/weight/black`
  Assumption status: `governed default`
  Notes: Brand typography reviews now reuse one shared universal raw black weight instead of opening a brand-specific weight question.

- Reuse:
  Source item: `headline default size`
  Proposed token: `universal/size/800`
  Assumption status: `assumed`
  Notes: The source does not provide a numeric headline size, so the initial review uses the current largest universal size.

- Reuse:
  Source item: `eyebrow at 0.5x headline`
  Proposed token: `universal/size/400`
  Assumption status: `assumed`
  Notes: Half of the provisional headline size preserves the source relationship without inventing a new raw size.

- Reuse:
  Source item: `subhead at 0.5x headline`
  Proposed token: `universal/size/400`
  Assumption status: `assumed`
  Notes: Half of the provisional headline size preserves the source relationship without inventing a new raw size.

- Reuse:
  Source item: `body default size`
  Proposed token: `universal/size/300`
  Assumption status: `assumed`
  Notes: The source does not provide a numeric body size, so the initial review uses the current universal base reading size.

- Reuse:
  Source item: `cta default size`
  Proposed token: `universal/size/300`
  Assumption status: `assumed`
  Notes: The source does not provide a numeric CTA size, so the initial review uses the current universal base action size.

## Hold For Review

- Item: `Semantic typography collection structure`
  Reason: The approved semantic tokens are clear, but the multi-brand collection shape in Figma still needs an explicit decision before aliases are written.

## Semantic Mapping

- Semantic token: `family/heading`
  Global token: `vail/family/display`
  Safe semantic token: `family/heading_safe`
  Safe global token: `universal/family/web_safe`
  Intended channels: `web, email, ads`
  Notes: Web and ad executions should use the brand display family. Email should use the safe alias when Termina delivery is not reliable.

- Semantic token: `family/body`
  Global token: `vail/family/primary`
  Safe semantic token: `family/body_safe`
  Safe global token: `universal/family/web_safe`
  Intended channels: `web, email, ads`
  Notes: Primary reading family across channels, with the safe alias reserved for constrained rendering environments.

- Semantic token: `family/action`
  Global token: `vail/family/primary`
  Safe semantic token: `family/action_safe`
  Safe global token: `universal/family/web_safe`
  Intended channels: `web, email, ads`
  Notes: Action-oriented copy stays on the primary family, with a safe counterpart for email-safe use.

## Role Recipes

### Role: eyebrow

Proposed family token: `vail/family/primary`

Fallback token: `universal/family/web_safe`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/400`

Size assumption: `assumed from the universal size ladder`

Sample block:

<div style="font-family: 'Avenir', sans-serif; font-weight: 900; font-size: 18px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  SAMPLE EYEBROW
</div>

Recipe notes:

- Case: `ALL CAPS`
- Tracking: `0px`
- Leading: `Use text height to inform spacing between lines`
- Size rule: `0.5x headline size`
- Punctuation: `not specified`
- Notes: Intended as section-header or hierarchy-breaking text.

### Role: headline

Proposed family token: `vail/family/display`

Fallback token: `universal/family/web_safe`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/800`

Size assumption: `assumed from the universal size ladder`

Sample block:

<div style="font-family: 'Termina', sans-serif; font-weight: 900; font-size: 36px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  HEADLINES SHOULD ALWAYS BE IN TERMINA
</div>

Recipe notes:

- Case: `ALL CAPS`
- Tracking: `0px`
- Leading: `Equal to font size`
- Size rule: `Base headline size not numerically specified`
- Punctuation: `No end punctuation by default; limited exceptions allowed`
- Notes: Primary display style.

### Role: subhead

Proposed family token: `vail/family/primary`

Fallback token: `universal/family/web_safe`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/400`

Size assumption: `assumed from the universal size ladder`

Sample block:

<div style="font-family: 'Avenir', sans-serif; font-weight: 900; font-size: 18px; line-height: 1.2; letter-spacing: 0; text-transform: none;">
  This is your subhead.
</div>

Recipe notes:

- Case: `Sentence case`
- Tracking: `0px`
- Leading: `not specified`
- Size rule: `0.5x headline size`
- Punctuation: `allowed`
- Notes: Supporting headline copy.

### Role: body

Proposed family token: `vail/family/primary`

Fallback token: `universal/family/web_safe`

Proposed weight token: `universal/weight/medium`

Proposed size token: `universal/size/300`

Size assumption: `assumed from the universal size ladder`

Sample block:

<div style="font-family: 'Avenir', sans-serif; font-weight: 500; font-size: 16px; line-height: 1.6; letter-spacing: 0; text-transform: none;">
  This is your body copy. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
</div>

Recipe notes:

- Case: `Sentence case`
- Tracking: `0px`
- Leading: `1.6x type size`
- Size rule: `Base body size not numerically specified`
- Punctuation: `sentence punctuation allowed`
- Notes: Avoid widows and orphans when possible.

### Role: cta

Proposed family token: `vail/family/primary`

Fallback token: `universal/family/web_safe`

Proposed weight token: `universal/weight/black`

Proposed size token: `universal/size/300`

Size assumption: `assumed from the universal size ladder`

Sample block:

<div style="font-family: 'Avenir', sans-serif; font-weight: 900; font-size: 16px; line-height: 1.2; letter-spacing: 0; text-transform: uppercase;">
  PLAN YOUR VISIT
</div>

Recipe notes:

- Case: `ALL CAPS`
- Tracking: `0px`
- Leading: `not specified`
- Size rule: `Base CTA size not numerically specified`
- Punctuation: `Do not use end punctuation`
- Notes: Action-oriented interface copy.

## Review Notes

- This preview is for governance review only. The rendered font in Markdown depends on local font availability and is not a guaranteed visual match.
- Missing fallback stacks default to `universal/family/web_safe`.
- Missing numeric sizes are mapped provisionally to the universal size ladder and should be revisited after design experimentation.
- Global family naming is now approved as `primary`, `display`, and `web_safe`.

## Review Readiness

- Subject: `family/heading_safe`
  Channels: `email`
  Rule: Use the safe semantic alias when the channel cannot reliably deliver the brand display font.
  Source basis: Safe-semantic governance for constrained channels.

- Subject: `family/body_safe`
  Channels: `email`
  Rule: Use the safe semantic alias when the channel cannot reliably deliver Avenir.
  Source basis: Safe-semantic governance for constrained channels.

- Subject: `headline`
  Channels: `web, email, ads`
  Rule: Headlines stay all caps with 0px tracking and avoid end punctuation except the source-approved exceptions.
  Source basis: Vail typography guide headline rule.

- Subject: `body`
  Channels: `web, email, ads`
  Rule: Body copy stays sentence case with 0px tracking and 1.6x leading.
  Source basis: Vail typography guide body rule.

- Subject: `cta`
  Channels: `web, email, ads`
  Rule: CTA copy stays all caps and does not use end punctuation.
  Source basis: Vail typography guide CTA rule.
