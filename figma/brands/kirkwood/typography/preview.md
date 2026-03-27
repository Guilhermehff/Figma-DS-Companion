# Kirkwood Typography Preview

Review state: retrospective review artifact documenting the pre-review write exception. Verify live write state in `figma/brands/kirkwood/brand.yml` and Figma.

## Original Source Roles

- Source role: `title_or_small_type`
  Family: `Futura`
  Style: `Futura Bold`
  Weight label: `Bold`
  Usage scope: `title lines and small type elements`
  Case: `All caps or Title Case`
  Tracking: `not specified`
  Leading: `around 120 percent`
  Size rule: `not numerically specified`
  Punctuation: `not specified`
  Sample copy: `Futura Bold`
  Notes: Compact short-form lane.

- Source role: `headline`
  Family: `Trade Gothic Bold Condensed No. 20`
  Style: `Trade Gothic Bold Condensed No. 20`
  Weight label: `Bold`
  Usage scope: `primary display headline`
  Case: `All caps`
  Tracking: `not specified`
  Leading: `100 percent or less`
  Size rule: `not numerically specified`
  Punctuation: `not specified`
  Sample copy: `ABCDEFGHIJKLMNOP QRSTUVWXYZ`
  Notes: Main display lane.

- Source role: `body`
  Family: `Avenir Next`
  Style: `Avenir Next Regular`
  Weight label: `Regular`
  Usage scope: `reading copy`
  Case: `Sentence case`
  Tracking: `not specified`
  Leading: `150 percent`
  Size rule: `max 16 pt`
  Punctuation: `sentence punctuation allowed`
  Sample copy: `Avenir Next Regular`
  Notes: Reading-copy lane.

- Source role: `limited_space_emphasis`
  Family: `Trade Gothic Condensed No. 18`
  Style: `Trade Gothic Condensed No. 18`
  Weight label: `Regular`
  Usage scope: `limited-space emphasis`
  Case: `not specified`
  Tracking: `not specified`
  Leading: `150 percent`
  Size rule: `short copy only`
  Punctuation: `not specified`
  Sample copy: `Trade Gothic Condensed No. 18`
  Notes: Preserved as a raw utility lane.

## Primitive Recommendations

- Proposed primitive:
  Token name: `kirkwood/family/01`
  Source item: `Trade Gothic Bold Condensed No. 20`
  Fallback token: `universal/family/fallback`
  Notes: Primary headline family.

- Proposed primitive:
  Token name: `kirkwood/family/02`
  Source item: `Avenir Next`
  Fallback token: `universal/family/fallback`
  Notes: Reading family.

- Proposed primitive:
  Token name: `kirkwood/family/03`
  Source item: `Futura Bold`
  Fallback token: `universal/family/fallback`
  Notes: Best semantic fit for short emphatic copy.

- Proposed primitive:
  Token name: `kirkwood/family/04`
  Source item: `Trade Gothic Condensed No. 18`
  Fallback token: `universal/family/fallback`
  Notes: Raw-only utility family retained outside the current semantic family lanes.

## Hold For Review

- Item: `semantic slot for Trade Gothic Condensed No. 18`
  Reason: Current semantic theme typography schema exposes only heading, body, and action families.

## Semantic Mapping

- `family/heading` -> `kirkwood/family/01`
- `family/body` -> `kirkwood/family/02`
- `family/action` -> `kirkwood/family/03`
- `weight/heading/base` -> `universal/weight/bold`
- `weight/body/base` -> `universal/weight/normal`
- `weight/action/base` -> `universal/weight/bold`
- `kirkwood/family/04` remains raw-only

## Role Recipes

### Role: title_or_small_type

<div style="font-family: 'Futura', sans-serif; font-weight: 700; font-size: 18px; line-height: 1.2; letter-spacing: 0; text-transform: uppercase;">
  FUTURA BOLD
</div>

- Proposed family token: `kirkwood/family/03`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/400`
- Notes: Best-fit semantic staging for compact title and small type use.

### Role: headline

<div style="font-family: 'Trade Gothic Bold Condensed No. 20', sans-serif; font-weight: 700; font-size: 36px; line-height: 1; letter-spacing: 0; text-transform: uppercase;">
  ABCDEFGHIJKLMNOP QRSTUVWXYZ
</div>

- Proposed family token: `kirkwood/family/01`
- Proposed weight token: `universal/weight/bold`
- Proposed size token: `universal/size/800`
- Notes: Condensed display lane for stacked all-caps headlines.

### Role: body

<div style="font-family: 'Avenir Next', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; letter-spacing: 0; text-transform: none;">
  Avenir Next Regular
</div>

- Proposed family token: `kirkwood/family/02`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Sentence-case reading lane aligned to the 16 pt cap from the source.

### Role: limited_space_emphasis

<div style="font-family: 'Trade Gothic Condensed No. 18', sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; letter-spacing: 0; text-transform: none;">
  Trade Gothic Condensed No. 18
</div>

- Proposed family token: `kirkwood/family/04`
- Proposed weight token: `universal/weight/normal`
- Proposed size token: `universal/size/300`
- Notes: Raw-only utility lane for limited-space emphasis.

## Review Notes

- Kirkwood exceeds the current three-lane semantic family model, so one family had to remain raw-only.
- Futura Bold is staged semantically because it maps more cleanly to action and short emphasis than Trade Gothic No. 18.
- The body lane is the least ambiguous part of the source and stays aligned to the shared 16 pt base size.
- Process exception: this preview artifact was reviewed after the live Figma write, not before it.

## Review Readiness

- Subject: `Kirkwood display hierarchy`
  Channels: `web, email, ads`
  Rule: Keep primary headlines on Trade Gothic Bold Condensed No. 20 in all caps, with tight leading.
  Source basis: Kirkwood typography image headline guidance.

- Subject: `Kirkwood reading lane`
  Channels: `web, email, ads`
  Rule: Keep Avenir Next Regular in sentence case, with loose leading at 150 percent and a max size of 16 pt.
  Source basis: Kirkwood typography image body guidance.

- Subject: `Kirkwood utility lane`
  Channels: `web, email, ads`
  Rule: Treat Trade Gothic Condensed No. 18 as a raw utility family until a fourth semantic family lane is explicitly approved.
  Source basis: Kirkwood typography image plus current semantic schema constraints.
