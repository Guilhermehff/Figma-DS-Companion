# Decision Log

- Date: 2026-03-10
- Title: Initial Global Values Baseline
- Status: Accepted
- Stakeholders: Design System Governance

## Context

The Design System file at `https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1` had no variable collections or variables. The first global primitives needed to establish a usable baseline for color, typography, and dimensions.

## Decision

Create three `_global_*` collections in Figma with an initial mode named `values`:

- `_global_color`
- `_global_typography`
- `_global_dimensions`

Use slash-delimited variable names in Figma because dot-delimited names are rejected by the Variables API.

Seed the first universal primitives as follows:

- Color: `color/universal/slate/50` through `color/universal/slate/950` using Tailwind Slate values
- Dimensions: `dimensions/space/*` only, using the Tailwind base spacing ladder
- Typography:
  - `typography/universal/family/sans`
  - `typography/universal/family/serif`
  - `typography/universal/weight/normal`
  - `typography/universal/weight/medium`
  - `typography/universal/size/100` through `typography/universal/size/800`

Typography size names use a numeric ladder at the global level. T-shirt naming is reserved for semantic tokens.

## Consequences

The repository taxonomy must describe slash-delimited Figma variable paths and the `_global_*` mode naming rule.

The next token work should build semantic collections on top of this baseline instead of introducing alternate raw scales.
