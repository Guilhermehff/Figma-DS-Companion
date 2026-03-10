# Decision Log

- Date: 2026-03-10
- Title: Brand Color Preview Before Write
- Status: Accepted
- Stakeholders: Design System Governance

## Context

Brand-color intake artifacts define proposed reuse decisions and new color ramps, but those values still need a human-readable review step before the system writes new variables into Figma.

## Decision

Every brand-color proposal must generate a preview artifact before any Figma write is proposed or executed.

The preview must show:

- universal color reuse decisions
- each proposed family on the full 50 to 950 scale
- the documented source anchor for each family

## Consequences

Brand-color write workflows now have a hard review gate between intake and Figma mutation.

Templates and future intake artifacts must include the preview reference so the write status is explicit.
