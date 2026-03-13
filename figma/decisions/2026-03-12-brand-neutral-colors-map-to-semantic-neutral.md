# Decision Log

- Date: 2026-03-12
- Title: Brand Neutral Colors Map To Semantic Neutral
- Status: accepted
- Scope: color governance
- Brand (if brand-specific):
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Stakeholders: Design System Governance
- Supersedes:
- Superseded by:

## Context

Brand color reviews already allow materially distinct brand neutrals to exist in `_Global: Color`, and several reviewed brands use branded neutral families for backgrounds, surfaces, or system color roles.

That interpretation exists in approved examples, but it was not stated as an explicit semantic-color rule in the governing docs. Future reviews should not have to infer from precedent whether a branded neutral should map to `neutral/*` or be forced into a brand accent slot.

## Decision

When a brand family functions primarily as a neutral system color, especially for backgrounds, surfaces, or other system-neutral usage, it should map to semantic `neutral/*`.

Do not map those families to `brand/*`, `brand_secondary/*`, or `brand_tertiary/*` unless a separate approved decision establishes that the family is serving an accent role instead of a neutral role.

## Scope

- Affected collections: `Semantic: Color`, `_Global: Color`
- Affected tokens or artifact paths: `neutral/*`, brand color intake artifacts, brand color preview artifacts, `figma/docs/brand-color-foundations.md`, `figma/config/variable-taxonomy.yml`
- Explicit exceptions: none
- Inherited or deferred items: shared feedback families such as `positive/*`, `warning/*`, and `negative/*` remain governed by the base semantic collection and are unaffected

## Consequences

Brand color intake and preview work must now treat branded background or system neutrals as semantic neutral candidates first.

Future brand reviews should explicitly record when a branded family feeds `neutral/*`, rather than leaving that mapping implicit in narrative notes or relying on prior examples.

## Follow-up

- Update: `figma/docs/brand-color-foundations.md` and `figma/config/variable-taxonomy.yml`
- Link from: future brand manifests only when a brand-specific neutral mapping needs durable provenance
- Verify: color intake and preview artifacts keep `neutral/*` available for branded background and system ladders
