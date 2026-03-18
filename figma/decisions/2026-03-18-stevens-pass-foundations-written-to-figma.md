# Decision Log

- Date: 2026-03-18
- Title: Stevens Pass Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Stevens Pass
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Stevens Pass introduces a blue-led palette with exact black and white neutrals, one primary brand blue, one darker supporting blue, and one moss green that the source explicitly frames as a secondary or special-case color.

The typography guidance uses one family, `Gibson`, across all roles, but the source labels `Headline = Bold`, `Subheads = Semi Bold`, `CTA = Regular`, and presents multiple allowed body weights and italics rather than one canonical body baseline. That made the live semantic typography mapping an exception-driven decision that required confirmation before mutation.

## Decision

1. Reuse `universal/black` and `universal/white` for the supplied Stevens Pass exact neutrals instead of duplicating them under the brand group.
2. Add three Stevens Pass raw color families in `_Global: Color`:
   - `stevens_pass/stevens_blue/*`
   - `stevens_pass/secondary_blue/*`
   - `stevens_pass/mossy_green/*`
3. Create a Stevens Pass semantic color extension that:
   - leaves the neutral and status roles inherited from the shared base
   - maps `brand/*` to `stevens_pass/stevens_blue/*`
   - maps `brand_secondary/*` to `stevens_pass/secondary_blue/*`
   - overrides `assets/logo` to the string `Stevens Pass`
4. Keep `stevens_pass/mossy_green/*` as a governed global-only family for special-case use rather than promoting it into the first semantic pass.
5. Add one Stevens Pass raw typography family primitive in `_Global: Typography`:
   - `stevens_pass/family/primary` -> `Gibson`
6. Create a Stevens Pass semantic typography extension that maps `family/heading`, `family/body`, and `family/action` to `stevens_pass/family/primary`.
7. Apply the user-approved typography exception for the live semantic pass:
   - `weight/heading/base` -> `universal/weight/bold`
   - `weight/body/base` -> `universal/weight/light`
   - `weight/body/strong` -> `universal/weight/medium`
   - `weight/action/base` -> `universal/weight/medium`

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `stevens_pass/stevens_blue/*`
  - `stevens_pass/secondary_blue/*`
  - `stevens_pass/mossy_green/*`
  - `stevens_pass/family/primary`
  - `figma/brands/stevens_pass/brand.yml`
  - `figma/brands/stevens_pass/color/intake.yml`
  - `figma/brands/stevens_pass/color/preview.md`
  - `figma/brands/stevens_pass/typography/intake.yml`
  - `figma/brands/stevens_pass/typography/preview.md`
- Explicit exceptions:
  - `mossy_green` remains global-only after the first semantic pass even though it is an approved secondary brand color.
  - User-approved exception: the live typography extension stages `body/base` on Light, `body/strong` on Medium, and `action/base` on Medium even though the source labels subheads as Semi Bold and CTA as Regular.
- Inherited or deferred items:
  - Neutral and status color roles remain inherited from the shared semantic base because the supplied exact black and white already match the governed universal primitives.
  - Safe family aliases and all size semantics remain inherited from the shared semantic typography base.
  - Raw italic body variants remain documented in local artifacts and are not promoted into semantic.

## Consequences

Stevens Pass can now consume the current role-based semantic color and typography contracts in the active Foundations file without adding duplicate exact neutrals or expanding the semantic schema.

The approved typography exception is durable in governance rather than hidden only in chat context or in live Figma overrides. Future downstream work can use the manifest and decision log to understand why the live action and body weights differ from the literal source labels.

## Follow-up

- Update:
  - Stevens Pass global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/stevens_pass/brand.yml`.
- Link from:
  - `figma/brands/stevens_pass/brand.yml`
- Verify:
  - `Stevens Pass` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `stevens_pass/stevens_blue/700`, `stevens_pass/secondary_blue/800`, `stevens_pass/family/primary`, `universal/weight/light`, and `universal/weight/medium` as intended.
