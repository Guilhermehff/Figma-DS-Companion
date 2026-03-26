# Role-Scoped Semantic Typography Ladders

Date: 2026-03-11
Status: superseded in part
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
Supersedes: `2026-03-11-semantic-typography-weight-and-size-aliases.md`
Superseded in part by: `2026-03-26-semantic-theme-and-published-global-typography.md`
Historical naming note: References to `semantic_typography` describe the pre-rename display name. The current collection is `Semantic: Typography`.

## Context

Flat semantic aliases such as `weight/medium` and `size/300` are too close to the raw layer. They do not preserve enough role intent to serve as a stable bridge between global typography primitives and downstream channel styles.

## Decision

1. Keep semantic family aliases role-based:
   - `family/heading`
   - `family/body`
   - `family/action`
   - their safe counterparts where constrained channels require them
2. Make semantic weight aliases role-scoped using the format `weight/<role>/<emphasis_step>`.
3. Standardize semantic weight emphasis steps on:
   - `subtle`
   - `base`
   - `strong`
4. Make semantic size aliases role-scoped using the format `size/<role>/<tshirt_step>`.
5. Start semantic size steps with t-shirt labels such as:
   - `sm`
   - `base`
   - `lg`
   - `xl`
   Larger steps such as `2xl` or `3xl` may be added when justified by approved role recipes.
6. Allow heading to start with a broader size ladder than body or action in the shared baseline, because heading systems typically need more reusable semantic range at the start.
7. Do not force every role to use every weight or size step. Only create the semantic aliases actually needed by the approved shared baseline or reviewed brand recipes.
8. Keep safe-alias behavior family-only. Do not create safe weight or size aliases.
9. Keep role-scoped semantic weight and size ladders in the shared `semantic_typography` base collection unless a brand-specific semantic override is explicitly approved.

## Consequences

- The semantic typography layer stays meaning-light without collapsing back to raw keys.
- Channel libraries can consume semantic family, weight, and size tokens without guessing role intent from raw numeric or raw font-weight labels.
- Heading can start with a wider semantic size ladder than body or action without forcing the same number of options across every role.
- Before any Figma write, the exact role-scoped weight and size inventory still needs to be derived from the approved shared baseline and current brand-reviewed typography recipes.
