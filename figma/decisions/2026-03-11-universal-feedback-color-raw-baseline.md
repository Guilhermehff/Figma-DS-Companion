# Decision Log

- Date: 2026-03-11
- Title: Universal Feedback Color Raw Baseline
- Status: Accepted
- Stakeholders: Design System Governance

## Context

The Design System file at `https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1` currently governs universal raw color ramps for `slate` and `cyan`, plus exact `white` and `black`, and the reviewed Vail brand families.

Upcoming web and cross-channel work needs additional shared raw color families so future semantic `positive`, `warning`, and `negative` ladders can be added without forcing meaning into the global layer or borrowing from brand-specific ramps.

## Decision

Add these universal raw families to `_Global: Color`:

- `universal/green/50` through `universal/green/950`
- `universal/yellow/50` through `universal/yellow/950`
- `universal/red/50` through `universal/red/950`

Use the Tailwind palette values for each family, aligned with the same Tailwind baseline already used for the governed `universal/slate/*` and `universal/cyan/*` ramps.

Keep the global layer raw and meaning-free. Do not create `positive`, `warning`, or `negative` tokens in `_Global: Color`.

Treat these raw families as inputs for the shared semantic feedback families defined in `figma/decisions/2026-03-11-semantic-feedback-color-family-naming.md`.

## Consequences

`_Global: Color` will gain 33 additional universal raw variables.

These families become approved raw inputs for future shared semantic `positive`, `warning`, and `negative` aliases used by web and other channel libraries.

Any dated compatibility export under `figma/exports/` must only be generated after the Figma write is completed and verified through Figma Console MCP.

The Figma write for these raw families was completed on 2026-03-11 in the `Design System` file. The registry and proposal artifact should mirror the live `_Global: Color` count of 90 variables.
