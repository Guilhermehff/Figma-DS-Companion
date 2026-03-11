# Brand Color Foundations

This workflow governs how brand-provided colors become durable design-system artifacts before any Figma write.

## Core Rules

1. Start from the official source artifact and prefer provided RGB or HEX values over sampling.
2. Preserve all source swatches, labels, usage scopes, and channel restrictions in the intake and preview artifacts.
3. Reuse existing universal tokens first, especially `universal/white` and `universal/black`.
4. Add brand families only for materially distinct brand hues or contractually important neutrals.
5. Keep raw brand families in `_Global: Color` and keep them on the shared `50-950` scale.
6. Generate ramps in `OKLCH` and validate contrast before proposing a write.
7. Produce a preview artifact before any write is proposed or executed.
8. Register the approved artifact paths in `figma/brands/<brand>/brand.yml`.

## Brand-Centered Output

Every reviewed brand should have:

- a canonical brand record in `figma/brands/registry.yml`
- a per-brand manifest at `figma/brands/<brand>/brand.yml`
- color staging space at `figma/brands/<brand>/color/`
- approved intake and preview artifacts referenced from the brand manifest

During the staged migration phase, existing approved color artifacts may remain in `figma/variables/` if the brand manifest points to them explicitly.

## Intake Workflow

1. Confirm the brand record or create it if it does not exist.
2. Record the source reference and source swatches in the intake artifact.
3. Mark each source swatch as `reuse_universal`, `new_brand_family`, or `hold_for_review`.
4. Choose stable hue-based family names.
5. Assign the source anchor step and expand the family to the full scale.
6. Document semantic slot recommendations for `brand`, `brand_secondary`, and `brand_tertiary`.
7. Capture downstream review guidance for web, email, and ads.
8. Generate the preview artifact and link both artifacts from the brand manifest.

## Inventory Impact

- Global color writes belong in `_Global: Color`.
- Shared semantic color ladders belong in `Semantic: Color`.
- Brand semantic overrides live in Figma. Create `figma/variables/extensions/` exports only when an audit or compatibility export is explicitly requested.
- `figma/variables/registry.yml`, when present, is an on-demand compatibility export and should not be hand-edited.

## Templates

Use [brand-color-intake.yml](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-color-intake.yml) for intake work.
Use [brand-color-preview.md](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-color-preview.md) for the required pre-write preview.
