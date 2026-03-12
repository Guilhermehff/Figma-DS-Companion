# Brand Typography Foundations

This workflow governs how brand typography guidance becomes durable design-system artifacts before any Figma write.

## Core Rules

1. Start from the official source artifact and preserve the original roles, family names, weights, and notes.
2. Separate raw primitives from usage-bearing role recipes.
3. Reuse existing universal families, weights, and sizes before proposing new raw primitives.
4. Keep raw family tokens structural, not role-based.
5. Default missing fallback stacks to `universal/family/web_safe`.
6. Default missing raw sizes to the governed universal size ladder and mark them as assumptions.
7. Keep semantic typography role-based and use safe family aliases only where constrained channels need them.
8. Generate a preview artifact before any write is proposed or executed.
9. Register approved artifact paths and override status in `figma/brands/<brand>/brand.yml`.

## Brand-Centered Output

Every reviewed brand should have:

- a canonical brand record in `figma/brands/registry.yml`
- a per-brand manifest at `figma/brands/<brand>/brand.yml`
- typography staging space at `figma/brands/<brand>/typography/`
- approved intake and preview artifacts referenced from the brand manifest
- Figma provenance captured in the manifest and intake artifact; preview Markdown should stay focused on review content unless a node-specific reference materially helps

When a local export is explicitly requested, store the dated snapshot under `figma/exports/` and treat it as potentially stale relative to live Figma.

## Intake Workflow

1. Confirm the brand record or create it if it does not exist.
2. Capture the original source roles in the intake artifact.
3. Split the review into primitive recommendations and role recipes.
4. Record semantic family, semantic weight, semantic size, and safe-family mappings.
5. Capture downstream review guidance for web, email, and ads.
6. Generate the preview artifact and link both artifacts from the brand manifest.

## Inventory Impact

- Raw family, weight, and size primitives belong in `_Global: Typography`.
- Shared semantic ladders belong in `Semantic: Typography`.
- Brand semantic overrides live in Figma. Create dated exports under `figma/exports/` only when an audit or compatibility export is explicitly requested.
- Compatibility exports under `figma/exports/` are on-demand snapshots and should not be hand-edited.

## Templates

Use [brand-typography-intake.yml](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-typography-intake.yml) for intake work.
Use [brand-typography-preview.md](/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/templates/brand-typography-preview.md) for the required pre-write preview.
