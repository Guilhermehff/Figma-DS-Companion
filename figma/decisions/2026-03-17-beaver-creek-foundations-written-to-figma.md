# Decision Log

- Date: 2026-03-17
- Title: Beaver Creek Foundations Written To Figma
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Beaver Creek
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

Beaver Creek introduces a silver-led brand system that does not separate cleanly into the usual neutral and expressive color families. The supplied color guidance is one continuous silver-to-near-black palette, and the user explicitly approved the option to let that same family drive both the neutral and expressive semantic lanes.

The typography guidance also introduces a distinct `Thin` display weight for IvyPresto Display while keeping the rest of the system on Vinila and Vinila Condensed.

## Decision

1. Add one Beaver Creek raw color family, `beaver_creek/silver/*`, in `_Global: Color`.
2. Reuse `universal/white` for the supplied Beaver Creek white swatch instead of duplicating it under the brand group.
3. Treat `beaver_creek/silver/*` as an approved Beaver Creek-specific exception that drives semantic `neutral/*`, `brand/*`, and `brand_secondary/*`.
4. Add Beaver Creek raw typography families in `_Global: Typography`:
   - `beaver_creek/family/primary` -> `IvyPresto Display`
   - `beaver_creek/family/secondary` -> `Vinila`
   - `beaver_creek/family/action` -> `Vinila Condensed`
5. Add the shared raw weight `universal/weight/thin` to `_Global: Typography`.
6. Create Beaver Creek semantic extension collections for both `Semantic: Color` and `Semantic: Typography`.

## Scope

- Affected collections:
  - `_Global: Color`
  - `_Global: Typography`
  - `Semantic: Color`
  - `Semantic: Typography`
- Affected tokens or artifact paths:
  - `beaver_creek/silver/*`
  - `beaver_creek/family/primary`
  - `beaver_creek/family/secondary`
  - `beaver_creek/family/action`
  - `universal/weight/thin`
  - `figma/brands/beaver_creek/brand.yml`
  - `figma/brands/beaver_creek/color/intake.yml`
  - `figma/brands/beaver_creek/color/preview.md`
  - `figma/brands/beaver_creek/typography/intake.yml`
  - `figma/brands/beaver_creek/typography/preview.md`
- Explicit exceptions:
  - Beaver Creek is approved to use the same silver family for `neutral/*`, `brand/*`, and `brand_secondary/*`.
- Inherited or deferred items:
  - `foreground/inverse` and all shared status color lanes remain inherited from the semantic base.
  - Beaver Creek size semantics remain inherited from the shared typography base.
  - The non-clickable URL treatment remains a raw documented recipe rather than a separate semantic typography lane.

## Consequences

Beaver Creek can now be consumed through the current role-based semantic color and typography contracts without adding new shared semantic slots.

The approved color exception is durable and traceable in repo governance rather than being hidden only inside live Figma overrides or chat context.

## Follow-up

- Update:
  - Beaver Creek global variables and semantic overrides are now written in Figma.
  - The resulting semantic extension collection IDs are synced into `figma/brands/beaver_creek/brand.yml`.
- Link from:
  - `figma/brands/beaver_creek/brand.yml`
- Verify:
  - `Beaver Creek` exists as exactly one semantic color extension and one semantic typography extension in the active Foundations file.
  - Representative semantic variables resolve to `beaver_creek/silver/*`, Beaver Creek family tokens, and `universal/weight/thin` as intended.
