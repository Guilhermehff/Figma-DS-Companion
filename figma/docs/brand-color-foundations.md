# Brand Color Foundations

This document defines how to intake brand-provided colors and turn them into governable global primitives for the Vail Resorts Design System.

It applies before any Figma write. The output of this workflow is a reviewed brand-color intake artifact, not immediate variable creation.

## Core Rules

1. Start with the source artifact.
   Use the official brand guide, asset sheet, or user-provided image. Prefer explicit RGB or HEX values over visually sampled approximations.

2. Reuse universal tokens first.
   If a source color is an exact match to `universal/white` or `universal/black`, reuse the universal token and do not create a brand duplicate.

3. Only add brand families for distinct brand hues.
   Signature accents and materially distinct neutrals become new families under the brand group. Commodity neutrals can stay universal.

4. Keep brand groups inside `_global_color`.
   New raw color families live under the brand name, for example `vail/digital_blue/500`.

5. Build every new family on the shared 50 to 950 ladder.
   The required steps are `50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950`.

6. Use perceptual lightness, not a fixed HSL recipe.
   Generate ramps in `OKLCH` so a `950` yellow and a `950` navy land in a comparable darkness band.

7. Document the source-matched swatch explicitly.
   Use the documentation suffix `<step>_source` in the intake artifact, such as `500_source`, to show which scale step matches the original brand swatch.

8. Keep Figma primitive names clean.
   The global variable in Figma remains the numeric step, for example `vail/navy/500`. The `_source` suffix is documentation metadata, not a duplicate primitive.

9. Generate a preview before write.
   Every proposal that would add or change brand colors must produce a preview artifact for review before any Figma write is proposed or executed.

## Intake Workflow

1. Record the brand and the source reference.
2. List every source swatch with its provided name and digital value.
3. Mark each source swatch as one of:
   - `reuse_universal`
   - `new_brand_family`
   - `hold_for_review`
4. For each new family, choose a hue-based family name that is stable across channels.
5. Set the source anchor step.
   Match the official source swatch to the scale step whose lightness band fits best. `500` is only the default starting assumption, not a requirement.
6. Expand the family to the full 50 to 950 scale.
7. Validate contrast and perceptual consistency.
8. Generate a preview artifact that shows universal reuse and every proposed family scale.
9. Store the result in the intake artifact before any Figma write is proposed.

## Naming Rules

- Use slash-delimited paths.
- Use the brand as the first path segment.
- Use hue-based family names, not usage names.
- Use lowercase names.
- Use underscores only inside a term when the source name has multiple words.

Examples:

- `vail/digital_blue/500`
- `vail/navy/600`
- `beaver_creek/gold/500`

## Scale Rules

- Working color space: `OKLCH`
- Default source anchor step: `500` when the source swatch sits near the center of the ladder
- Common source anchor range: `300` through `800`
- Dark steps may reduce chroma to preserve contrast and family coherence.
- Do not force the same saturation behavior across all hues.

Target lightness bands:

- `50`: `0.98-0.99`
- `100`: `0.95-0.96`
- `200`: `0.90-0.92`
- `300`: `0.83-0.86`
- `400`: `0.74-0.78`
- `500`: `0.63-0.68`
- `600`: `0.53-0.58`
- `700`: `0.44-0.48`
- `800`: `0.35-0.39`
- `900`: `0.26-0.30`
- `950`: `0.18-0.22`

Contrast gates:

- `50` and `100` must support black at `7:1` or better.
- `200` must support black at `4.5:1` or better.
- `800` should support white at `4.5:1` or better.
- `900` and `950` must support white at `7:1` or better.

## Output Per Brand

Each new brand-color intake should produce:

- a universal reuse recommendation
- a list of new brand families
- a documented source anchor step for each family
- a full 50 to 950 scale proposal for each family
- contrast validation notes
- a preview artifact generated before write
- any open naming or taxonomy questions

Use [brand-color-intake.yml](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-color-intake.yml) for the repeatable artifact.
Use [brand-color-preview.md](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-color-preview.md) for the required pre-write preview.
