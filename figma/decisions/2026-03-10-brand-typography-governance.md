# Decision Log

- Date: 2026-03-10
- Title: Brand Typography Governance
- Status: Accepted
- Stakeholders: Design System Governance

## Context

Brand typography needs a review workflow parallel to brand color. The workflow must preserve original source guidance, separate raw typography primitives from role-based style guidance, and support brands that may send typography and color together in one intake round.

## Decision

Brand typography will follow these rules:

- preserve the original source roles in both intake and preview artifacts
- separate raw primitives from role recipes
- keep raw `_global_typography` family names structural rather than role-based
- reuse universal raw weights and sizes where possible
- generate a preview artifact before any Figma write is proposed or executed
- keep typography intake and preview artifacts separate from color artifacts even when a brand sends both at once

## Consequences

Brand typography can now be reviewed independently from color while still fitting the same pre-write approval workflow.

Future combined submissions should produce separate color and typography artifacts rather than a merged foundation report.
