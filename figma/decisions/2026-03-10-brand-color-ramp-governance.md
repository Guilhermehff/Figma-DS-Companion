# Decision Log

- Date: 2026-03-10
- Title: Brand Color Ramp Governance
- Status: Accepted
- Historical naming note: References to `_global_color` describe the pre-rename collection display name. The current collection is `_Global: Color`.
- Stakeholders: Design System Governance

## Context

The design system needs a repeatable way to intake brand-provided color swatches from guides or images, decide when a color should reuse universal primitives, and expand distinct brand hues into governable ramps without breaking the global token schema.

## Decision

Brand color intake will follow these rules:

- Review each source swatch against existing universal tokens before proposing new brand primitives.
- Reuse `universal/white` and `universal/black` for exact matches instead of duplicating them under a brand group.
- Add new raw color families under the brand group in `_global_color` using `<brand>/<family>/<step>`.
- Use a standard 11-step scale for every new family: `50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950`.
- Generate ramps in `OKLCH` so step lightness remains perceptually aligned across hues.
- Document the exact source-matched swatch with the suffix `<step>_source` in the intake artifact, while keeping the Figma primitive name on the clean numeric step.
- Validate that `900` and `950` support white foreground use and that light steps support dark foreground use.

## Consequences

Each new brand color request now requires a structured intake artifact before any Figma write is proposed.

The taxonomy can scale to multiple brands without introducing duplicate whites, duplicate blacks, or one-off ramp shapes per hue.

If a future request needs the source-anchor notation to exist as a token rather than documentation metadata, that change must be handled as a separate governance decision because it would introduce duplicate raw values into the global layer.
