# Decision Log

- Date: 2026-03-27
- Title: Neutral Global Typography Family Slots
- Status: Accepted
- Scope: System-wide typography primitive naming in Foundations and companion governance artifacts
- Brand (if brand-specific): N/A
- Figma file (if applicable): Foundations
- Stakeholders: Design System Governance
- Supersedes: figma/decisions/2026-03-10-typography-default-assumptions.md (fallback token naming clause only)
- Superseded by:

## Context

`Global: Typography` raw family primitives had accumulated role-shaped and descriptive labels such as `primary`, `secondary`, `display`, `utility`, `action`, `alternate`, and `web_safe`. Those names leaked semantic meaning into the global layer even though family meaning is governed later in `Semantic: Theme`.

The design system needed one stable raw naming model that keeps typography primitives structural, preserves existing live variable IDs where possible, and makes future semantic mapping decisions explicit instead of implicit in the raw token names.

## Decision

Adopt neutral numeric slots for raw typography family primitives in `Global: Typography`.

- Use `01`, `02`, `03`, and `04` as the governed raw family slot names.
- Rename `web_safe` to `fallback` as the only approved named technical exception.
- Preserve the current live family order within each brand group when assigning numeric slots so the rename does not also introduce a second structural reordering.
- Keep semantic meaning in `Semantic: Theme`, where role aliases such as `family/heading`, `family/body`, and `family/action` continue to define usage.
- Update live Figma documentation in the `Global: Typography` section to describe neutral family slots and fallback families rather than role-shaped primitive names.

## Scope

- Affected collections:
  - `Global: Typography`
  - `Semantic: Theme`
- Affected tokens or artifact paths:
  - All live `*/family/*` raw typography primitives in Foundations
  - `AGENTS.md`
  - `figma/config/variable-taxonomy.yml`
  - `figma/templates/brand-typography-intake.yml`
  - Active `figma/brands/*` typography intake, preview, and manifest artifacts that reference raw family primitives
  - Figma documentation under `Foundations > Global Tokens > Global: Typography`
- Explicit exceptions:
  - `fallback` remains a named technical primitive because constrained channels still need a stable safe-family reference.
- Inherited or deferred items:
  - Semantic family aliases remain role-based and unchanged in principle.
  - Channel text styles continue to bind family and weight from `Semantic: Theme` and size from `Global: Typography`.

## Consequences

Global typography families no longer imply heading, body, action, or display behavior through their primitive names. Brand-specific meaning must now be expressed only through semantic alias mapping and downstream channel styles.

Existing repo artifacts and live Figma documentation must use neutral slot names consistently so future intake, review, and write work does not regress to the earlier descriptive primitive naming model.

## Follow-up

- Update: Governance files, active brand artifacts, and live Figma typography documentation
- Link from: System-wide governance references as needed
- Verify: Live Foundations variable inventory returns only `01`, `02`, `03`, `04`, and `fallback` as raw family descriptor names
