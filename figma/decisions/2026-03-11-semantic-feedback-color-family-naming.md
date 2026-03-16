# Decision Log

- Date: 2026-03-11
- Title: Semantic Feedback Color Family Naming
- Status: Accepted
- Stakeholders: Design System Governance
- Superseded by: figma/decisions/2026-03-13-proposed-semantic-role-channel-color-model.md

## Context

The shared `Semantic: Color` baseline currently governs `neutral`, `brand`, `brand_secondary`, and `brand_tertiary`.

Additional cross-channel feedback families are needed for web and other channel libraries, and the raw universal inputs for those families are being added separately under `_Global: Color`.

## Decision

When the shared feedback ladders are added to `Semantic: Color`, their family names will be:

- `positive/*`
- `warning/*`
- `negative/*`

These semantic families will alias the following universal raw families:

- `positive/*` -> `universal/green/*`
- `warning/*` -> `universal/yellow/*`
- `negative/*` -> `universal/red/*`

These ladders belong in the base shared `Semantic: Color` collection, not in a brand extension and not in `_Global: Color`.

Do not use `success`, `caution`, `danger`, or hue-based names as the shared semantic family names for this layer.

## Consequences

After the raw global ramps exist in Figma, the next semantic color expansion should add `positive/50-950`, `warning/50-950`, and `negative/50-950` to the base `Semantic: Color` collection.

Channel libraries should alias from these semantic ladders instead of pointing directly to `green`, `yellow`, or `red` raw values.

Brand extensions should override these feedback ladders only if a later approved decision establishes a brand-specific reason to do so.
