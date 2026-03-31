# Decision Log

- Date: 2026-03-31
- Title: Vail Primary Brand Colors Added To Global
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Vail
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=277-54
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

The existing Vail foundations pass only governed the neutral references plus the digital-only accent palette: `digital_blue`, `navy`, and `yellow`.

The user then supplied the primary Vail brand palette and pointed out that `Vail Vintage Blue` and `Vail Dark Blue` were missing from the Vail documentation and raw token inventory. Those two colors do not match the existing governed Vail families, and the primary-brand source image does not provide approved semantic role mapping or proportion guidance for them.

## Decision

1. Add two new Vail raw color families in `_Global: Color`:
   - `vail/vintage_blue/*`
   - `vail/dark_blue/*`
2. Preserve the exact source swatches at:
   - `vail/vintage_blue/600` = `#3968B1`
   - `vail/dark_blue/500` = `#009ADA`
3. Update the Vail Global Tokens documentation frame so the original palette includes both new source swatches and the tokenized section includes both new ramps.
4. Keep the live Vail `Semantic: Theme` extension unchanged in this pass:
   - `brand/*` stays on `vail/digital_blue/*`
   - `brand_secondary/*` stays on `vail/navy/*`
   - `yellow` remains global-only
5. Keep the existing digital color proportion guidance unchanged. The new primary-brand families are preserved as governed raw tokens, not as new semantic or composition rules.

## Scope

- Affected collections:
  - `_Global: Color`
- Affected tokens or artifact paths:
  - `vail/vintage_blue/*`
  - `vail/dark_blue/*`
  - `figma/brands/vail/brand.yml`
  - `figma/brands/vail/color/intake.yml`
  - `figma/brands/vail/color/preview.md`
- Explicit exceptions:
  - The source image provides no explicit HEX for `Vail Dark Blue`, so the governed HEX is derived from the provided RGB `0 154 218`.
  - The semantic override model remains intentionally unchanged even after the new raw families are added.

## Consequences

Vail now carries five raw color families in `_Global: Color` while its semantic brand mapping remains aligned to the digital accent palette. The Vail documentation now distinguishes between the primary brand palette source colors and the currently active semantic/digital families instead of conflating them.

This preserves the full source palette in governed artifacts without forcing a semantic remap that has not been approved.

## Follow-up

- Update:
  - The Vail Global Tokens frame should show `5 ramps`, `55` tokens, `Vail Vintage Blue`, and `Vail Dark Blue`.
  - Repo artifacts should record both new families and the unchanged semantic mapping.
- Link from:
  - `figma/brands/vail/brand.yml`
- Verify:
  - `_Global: Color` contains `vail/vintage_blue/*` and `vail/dark_blue/*`
  - The Vail original palette documentation points to `vail/vintage_blue/600` and `vail/dark_blue/500`
  - No Vail semantic override aliases resolve to `vail/vintage_blue/*` or `vail/dark_blue/*`
