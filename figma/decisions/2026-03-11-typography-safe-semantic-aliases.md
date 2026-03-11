# Typography Safe Semantic Aliases

Date: 2026-03-11
Status: accepted

## Context

Typography now needs to support both web and email channel libraries. The semantic layer must express role intent while also preserving a safe-family option for constrained channels such as email.

## Decision

1. Global raw family names standardize on structural slots such as `primary`, `secondary`, `display`, and `web_safe`.
2. Semantic typography family aliases standardize on:
   - `family/heading`
   - `family/heading_safe`
   - `family/body`
   - `family/body_safe`
   - `family/action`
   - `family/action_safe`
3. The safe semantic aliases are the semantic substitutes used by email and other constrained channels when brand fonts cannot be relied on.
4. `universal/family/web_safe` holds a single safe-family placeholder for those constrained-channel aliases. The current baseline value is `Arial`.
5. The universal baseline raw family token formerly named `universal/family/sans` should be renamed to `universal/family/primary`.

## Rationale

- Raw families stay structural and brand-driven.
- Semantic families stay usage-driven.
- Safe aliases let web and email share one semantic schema without forcing the email library to consume brand fonts directly.

## Consequences

- Channel libraries can map `heading`, `body`, and `action` differently from `heading_safe`, `body_safe`, and `action_safe`.
- Review artifacts must include both the primary semantic mapping and the safe semantic mapping.
- The global typography baseline must align its family naming with the new structural model.
