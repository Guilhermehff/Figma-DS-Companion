# Decision Log

- Date: 2026-03-26
- Title: Brand color documentation requires proportion guidance when available
- Status: accepted
- Scope: repo governance
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations
- Stakeholders: design_system_governance
- Supersedes:
- Superseded by:

## Context

Brand color artifacts already captured source swatches, reuse decisions, token ramps, and validation data, but they did not consistently capture how brand colors should be proportioned in documentation and downstream composition guidance.

Vail now has approved digital color proportion guidance, and the user requested that this become a standing requirement for future brand documentation rather than an isolated note.

## Decision

Brand color intake and preview artifacts must include approved color proportion guidance whenever a brand provides that information.

If a brand does not provide color proportion guidance, the artifact must say that explicitly instead of inferring proportions from palette structure or token ramps.

The first application of this rule is Vail, where digital interface guidance is now documented as:

- `Vail White`: `50%`
- `Vail Digital Blue`: `20%`
- `Vail Navy`: `20%`
- `Vail Yellow`: `10%`

## Scope

- Affected collections:
  none
- Affected tokens or artifact paths:
  `AGENTS.md`
  `figma/brands/<brand>/color/intake.yml`
  `figma/brands/<brand>/color/preview.md`
  `figma/brands/vail/color/intake.yml`
  `figma/brands/vail/color/preview.md`
- Explicit exceptions:
  Brands that do not have approved proportion guidance may omit percentages, but must state that the guidance is unavailable.
- Inherited or deferred items:
  This rule does not require inventing print, legacy, or primary-brand-color proportions when the source material does not provide or approve them.

## Consequences

Future brand intake passes need a proportion-guidance check alongside source swatches, reuse decisions, and ramp generation.

Brand documentation is now expected to answer both:

- what the colors are
- how they are intended to be composed when guidance exists

## Follow-up

- Update:
  future brand color artifacts as the user provides guidance
- Link from:
  `AGENTS.md`
- Verify:
  Vail color intake and preview stay aligned with the approved documentation guidance
