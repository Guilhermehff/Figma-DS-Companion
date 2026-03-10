# Decision Log

- Date: 2026-03-10
- Title: Preserve Original Source Swatches In Intake And Preview
- Status: Accepted
- Stakeholders: Design System Governance

## Context

Brand-color reviews may happen well after the initial intake. If the original source swatches only live in the user-provided image, later reviewers would need to find the image again to understand what the approved ramps were derived from.

## Decision

Every brand-color workflow must preserve the original source swatches in both the intake artifact and the preview artifact.

The preserved source data must include:

- the source swatch name
- the provided digital value
- any relevant source notes needed to interpret the swatch later

## Consequences

Future reviews can compare the approved ramp against the original brand inputs without reopening the original image or asking for it again.

Preview templates and existing preview artifacts should expose the source swatches explicitly rather than relying only on reuse mappings or family scales.
