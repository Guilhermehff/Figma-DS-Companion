# Decision Log

- Date: 2026-03-10
- Title: Brand Color Source Anchor Flexibility
- Status: Accepted
- Stakeholders: Design System Governance

## Context

The first Vail brand-color intake validated the ramp rules against official source swatches. That validation showed the source colors do not all land near the middle of the shared lightness ladder: Vail Digital Blue aligns to `600`, Vail Navy aligns to `800`, and Vail Yellow aligns closest to `300`.

## Decision

Treat the source anchor step as the scale step whose lightness band best matches the official swatch.

`500` remains the default starting assumption for middle-value accents, but it is no longer treated as the expected anchor for every family. Source anchors may land anywhere on the shared scale when needed to preserve the official swatch and maintain a coherent 50 to 950 ramp.

## Consequences

Brand-color intake artifacts must explicitly record the source anchor per family.

Future ramp proposals should not force dark navies or bright yellows into `500`-centered scales when doing so would distort the source color or break cross-family lightness consistency.
