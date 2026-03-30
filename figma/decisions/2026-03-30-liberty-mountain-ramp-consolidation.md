# Decision Log

- Date: 2026-03-30
- Title: Liberty Mountain Ramp Consolidation
- Status: accepted
- Scope: brand foundations
- Brand (if brand-specific): Liberty Mountain
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=348-32141
- Stakeholders: Design System Governance, user approval in chat
- Supersedes: Raw color family inventory and documentation model in `figma/decisions/2026-03-19-liberty-mountain-foundations-written-to-figma.md`
- Superseded by:

## Context

The first Liberty Mountain write preserved every source swatch as its own raw family and also added `warm_neutral` for the warm neutral lane. That kept source provenance, but it made the documentation redundant because the original palette and the tokenized section both repeated the same colors as separate ramps.

On 2026-03-30, the user clarified that the earlier documentation image was wrong for Tundra: `Summit = #748693`, `Twilight = #3F5364`, and `Tundra = #3A4959`. The user also approved a cleaner model: keep original palette swatches visible in documentation, let multiple source values alias into one governed ramp, and name the grouped families generically as `warm_neutral` and `cool_neutral` inside the Liberty Mountain brand namespace.

## Decision

1. Remove the standalone raw families `twilight`, `summit`, `tundra`, `sand`, `mineral`, and `limestone` from `_Global: Color`.
2. Keep `warm_neutral/*` as the warm structural neutral ramp that preserves `Limestone`, `Mineral`, and `Sand` as documented alias anchors at `100`, `200`, and `400`.
3. Add `cool_neutral/*` as a grouped raw-only cool neutral ramp that preserves `Summit`, `Twilight`, and corrected `Tundra` as documented alias anchors at `400`, `500`, and `600`.
4. Keep the semantic Liberty Mountain extension unchanged in structure: `warm_neutral` remains the live neutral semantic source, while `cool_neutral` remains raw-only in this pass.
5. Update the Liberty Mountain documentation frame so the original palette shows source swatches with alias callouts, the tokenized section shows only the grouped ramps, and the frame summary reflects `9 ramps` and `99 tokens`.

## Scope

- Affected collections:
  - `_Global: Color`
- Affected tokens or artifact paths:
  - `liberty_mountain/cool_neutral/*`
  - `liberty_mountain/warm_neutral/*`
  - `figma/brands/liberty_mountain/brand.yml`
  - `figma/brands/liberty_mountain/color/intake.yml`
  - `figma/brands/liberty_mountain/color/preview.md`
  - `figma/decisions/2026-03-19-liberty-mountain-foundations-written-to-figma.md`
- Explicit exceptions:
  - `cool_neutral` is intentionally raw-only. It documents a governed grouped ramp, but it does not become a semantic neutral override in this pass.
  - The original Liberty Mountain palette swatches remain visible in documentation even when their standalone raw families are removed.
  - The corrected `Tundra` source value comes from user clarification in chat on 2026-03-30 and supersedes the earlier duplicated documentation image.
- Inherited or deferred items:
  - Semantic brand, brand-secondary, positive, warning, and critical color roles remain unchanged.
  - Typography primitives and typography semantic overrides are unaffected by this decision.

## Consequences

Liberty Mountain keeps source provenance without duplicating six standalone ramp families that no longer add governance value. The live global color inventory is reduced to nine Liberty Mountain families while the documentation becomes clearer about which source swatches are original palette anchors versus governed token ramps.

The Liberty Mountain semantic neutral lane remains warm-only through `warm_neutral`. If a future channel needs a semantic cool neutral lane, that would require a separate naming and slot decision rather than silently promoting `cool_neutral`.

## Follow-up

- Update:
  - `_Global: Color` and the Liberty Mountain documentation frame are now updated live in Figma.
  - The Liberty Mountain companion artifacts are synced to the grouped-ramp model and corrected Tundra provenance.
- Link from:
  - `figma/brands/liberty_mountain/brand.yml`
- Verify:
  - `liberty_mountain/cool_neutral/400 = #748693`
  - `liberty_mountain/cool_neutral/500 = #3f5364`
  - `liberty_mountain/cool_neutral/600 = #3a4959`
  - Liberty Mountain documentation frame `348:32141` shows `9 ramps` and `99 tokens`
