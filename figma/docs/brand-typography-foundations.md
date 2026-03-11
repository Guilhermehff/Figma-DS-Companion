# Brand Typography Foundations

This document defines how to intake brand-provided typography guidance and turn it into governable design-system artifacts for the Vail Resorts Design System.

It applies before any Figma write. The output of this workflow is a reviewed brand-typography intake artifact plus a separate preview artifact, not immediate variable creation.

## Core Rules

1. Start with the source artifact.
   Use the official brand guide, typography page, or user-provided image. Prefer explicit family names and stated rules over visual guessing.

2. Preserve the original source typography in the artifacts.
   Copy every source role, family name, weight label, and relevant notes into the intake artifact and the preview artifact so future reviews do not depend on reopening the original image.

3. Separate raw primitives from role recipes.
   Family tokens and raw weight or size values are primitives. `eyebrow`, `headline`, `subhead`, `body`, and `cta` are role recipes and should not be written as `_global_typography` primitive names.

4. Reuse universal typography primitives first.
   If a source weight or size already exists as a universal raw value, reuse it instead of creating a brand-specific duplicate.

5. Add brand-specific family primitives only when the family is distinct.
   Distinct brand fonts become brand-group family primitives under `_global_typography`, for example `vail/family/display`.

6. Keep family token names structural.
   Prefer slots such as `display`, `primary`, `secondary`, `accent`, or `web_safe`. Do not use role names such as `headline` or `body` in the raw family token name.

7. Default missing raw sizes to the universal size ladder.
   If a guide gives only relational rules such as `half the size of headline`, preserve that relation in the role recipe and assign a provisional `universal/size/*` token until design validation refines it later.

8. Default missing fallback stacks to the universal web-safe family.
   If the source does not specify a fallback or web-safe family, document `universal/family/web_safe` as the fallback reference.

9. Use shared universal raw weights.
   At the global raw layer, keep weights universal. If a source specifies `Black`, default to `universal/weight/black` unless a later review proves a different numeric raw value is required.

10. Generate a preview before write.
   Every proposal that would add or change brand typography must produce a preview artifact for review before any Figma write is proposed or executed.

11. Keep the artifacts review-ready.
   Brand typography instructions must preserve the rules needed for later review of pages, emails, and ads. Capture semantic role mappings, safe fallback mappings, casing, punctuation, leading, and any source-imposed channel constraints.

## Intake Workflow

1. Record the brand and the source reference.
2. Capture the original source roles in the intake artifact.
3. Mirror the same original source roles in the preview artifact.
4. Split the review into two outputs:
   - raw primitive recommendations for `_global_typography`
   - role recipe specifications for later channel styles
5. Reuse universal weights and sizes where the raw values already exist.
6. If raw sizes are missing, map the roles to provisional universal size tokens and mark those mappings as assumptions.
7. If fallback stacks are missing, attach `universal/family/web_safe` as the default fallback reference.
8. Reuse `universal/weight/black` for source styles labeled `Black`, unless a later numeric exception is approved.
9. Propose new brand family tokens only where a distinct family is required.
10. Record the semantic family mapping for `heading`, `body`, and `action` plus the safe counterparts used by email or other constrained channels.
11. Add a review-readiness summary so later audits of pages, emails, and ads do not need to reconstruct the brand rules from scratch.
12. Generate a preview artifact that shows the original source roles, the primitive recommendations, the semantic mapping, and the role recipes.
13. Store the result before any Figma write is proposed.

## Primitive Rules

- Family token format: `<brand>/family/<slot>`
- Weight token format: `<group>/weight/<weight_key>`
- Raw size token format: `universal/size/<step>`
- Role names do not belong in raw primitive names.

Examples from the Vail typography image:

- `headline | termina black` suggests a family candidate such as `vail/family/display`
- `eyebrow | avenir black`, `subhead | avenir black`, `body copy | avenir medium`, and `cta | avenir black` suggest one reusable text family token rather than separate `family/eyebrow` or `family/body` tokens
- `Avenir Medium` may reuse `universal/weight/medium` if the numeric weight aligns with the existing universal primitive
- `Avenir Black` and `Termina Black` should map to `universal/weight/black` unless a later review requires a different numeric raw value
- missing fallback stacks should default to `universal/family/web_safe`
- missing raw sizes should map to provisional `universal/size/*` tokens and remain open to later refinement
- `universal/family/primary` is the universal baseline text family key
- `universal/family/web_safe` should store a single safe-family placeholder suitable for email-safe semantics; the current baseline is `Arial`

## Role Recipe Rules

Role recipes are documentation for later channel typography styles. They can include:

- family token mapping
- weight token mapping
- case rules
- punctuation rules
- tracking
- leading rules
- relational size rules
- sample copy

Examples from the Vail typography image:

- `eyebrow`: all caps, `0px` tracking, section-header usage, half headline size
- `headline`: all caps, `0px` tracking, no end punctuation by default, leading equals font size
- `subhead`: sentence case, punctuation allowed, `0px` tracking, half headline size
- `body`: sentence case, `0px` tracking, leading `1.6x` type size
- `cta`: all caps, `0px` tracking, no end punctuation

## Semantic Mapping Recommendation

Use brand family primitives as raw ingredients, then alias them into semantic family roles before any channel naming is applied.

- Global raw families: `vail/family/display`, `vail/family/primary`, `universal/family/primary`, `universal/family/web_safe`
- Recommended semantic aliases: `family/heading`, `family/body`, `family/action`
- Recommended safe semantic aliases: `family/heading_safe`, `family/body_safe`, `family/action_safe`
- Typical channel outcome: `typography/heading/*`, `typography/body/*`, `typography/button/*`

Safe-alias rule:
Use the safe semantic aliases for email and any other constrained channel that cannot rely on the brand family being delivered. The safe aliases should point to `universal/family/web_safe`.

Collection strategy:

- Base collection: `semantic_typography`
- Base mode: `base`
- Brand extension collection format: `semantic_typography/<brand>`

Implementation rule:
The base semantic collection aliases universal typography primitives. A brand extension collection should override only the semantic tokens that actually differ for that brand. If a token still points to the universal baseline, it should remain untouched in the base collection rather than being redundantly reassigned in the brand extension.

Opinion:
Use `action` instead of `cta` at the semantic layer. `cta` is already channel language, while `action` still covers buttons, links, chips, navigation prompts, and promotional actions without tying the semantic ladder to one UI term.

## Review Readiness

Every brand typography artifact must preserve the information required for later design-review work across:

- web pages
- emails
- ads

At minimum, capture:

- source role intent
- raw family recommendation
- semantic family mapping and safe semantic mapping
- fallback behavior for constrained channels
- case, punctuation, tracking, and leading rules
- any usage restrictions or exceptions stated by the source
- which semantic tokens stay on the universal baseline and which ones are overridden by the brand extension

## Artifact Separation

When a brand submission includes both color and typography, create four separate artifacts:

- `YYYY-MM-DD-brand-brand-color-intake.yml`
- `YYYY-MM-DD-brand-brand-color-preview.md`
- `YYYY-MM-DD-brand-brand-typography-intake.yml`
- `YYYY-MM-DD-brand-brand-typography-preview.md`

Do not merge color and typography into a single intake or preview file.

## Output Per Brand

Each new brand-typography review should produce:

- the original source roles preserved in intake and preview
- a primitive reuse recommendation
- proposed family primitives
- semantic family mapping
- safe semantic family mapping
- proposed weight reuse or additions
- assumed size mappings when source sizes are missing
- a role recipe specification
- downstream review guidance for pages, emails, and ads
- a hold-for-review summary when data is incomplete
- a preview artifact generated before write
- any open naming or data questions

Use [brand-typography-intake.yml](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-typography-intake.yml) for the repeatable intake artifact.
Use [brand-typography-preview.md](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-typography-preview.md) for the required pre-write preview.
