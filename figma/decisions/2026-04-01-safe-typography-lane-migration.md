# Decision Log

- Date: 2026-04-01
- Title: Replace Fallback Typography with Brand Safe Family Lanes
- Status: accepted
- Scope: system-wide typography governance
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations (`70O01X6MWNKMpsLqIke99Q`)
- Stakeholders: design system governance
- Supersedes: typography safe-family behavior that staged on `*/family/fallback`
- Superseded by:

## Context

The design system previously modeled constrained-channel typography through a single fallback-family token path, typically `universal/family/fallback`, with a few brand exceptions. That model was too coarse once governed web-safe families were approved for each brand. It also forced the semantic safe aliases to collapse into one generic family even when brand-safe guidance existed.

The approved source for the safe-family mappings is `Vail Resorts Guidelines.pdf`. The migration needs to preserve the current brand-family, weight, and size model while adding a real raw safe-family lane and repointing the semantic safe aliases to that lane.

## Decision

Replace the active fallback-family model with explicit raw safe-family primitives:

- Global brand-family primitives remain on `family/<slot>`.
- Global safe-family primitives now live on `family_safe/<slot>`.
- Base semantic typography tokens remain unchanged for non-safe roles.
- Base and brand semantic safe aliases use `family/heading_safe`, `family/body_safe`, and `family/action_safe` and now point to `family_safe/*` tokens.
- `universal/family_safe/01` becomes the base safe-family token in `Global: Typography`.
- Each brand receives `brand_id/family_safe/01..n` in first-use order from the approved PDF mapping.
- `*/family/fallback` is retired from the active live model after safe aliases are repointed and verified.

Documentation also changes:

- Each brand typography documentation frame shows two family sections: `Brand Families` and `Web Safe Families`.
- Typography documentation cards show family token label plus family name only.
- The typography font list distinguishes the `brand` and `safe` lanes instead of conflating them into one table.

## Scope

- Affected collections:
  - `Global: Typography`
  - `Semantic: Theme`
  - all brand `Semantic: Theme` extensions
- Affected tokens or artifact paths:
  - `universal/family_safe/01`
  - `brand_id/family_safe/*`
  - `family/heading_safe`
  - `family/body_safe`
  - `family/action_safe`
  - `figma/config/variable-taxonomy.yml`
  - `figma/docs/brand-typography-foundations.md`
  - `figma/templates/brand-typography-intake.yml`
  - `figma/templates/brand-typography-preview.md`
  - `figma/brands/*/typography/intake.yml`
  - `figma/brands/*/typography/preview.md`
  - `figma/brands/*/brand.yml`
  - `figma/brands/font-inventory.yml`
  - `figma/brands/font-directory.md`
- Explicit exceptions:
  - When one brand family maps to multiple approved safe families, the primitive-level `safe_family_token` may remain blank and defer to role-level semantic safe mappings.
  - This migration changes only the safe-family lane. It does not redesign brand-family primitives, raw weights, or raw sizes.
- Inherited or deferred items:
  - Non-safe typography aliases continue to inherit or override exactly as already governed.
  - Channel-level CSS or fallback stacks remain channel concerns and are not encoded as raw Figma family values in this pass.

## Consequences

Safe typography is now governed at the same raw-token level as brand typography instead of being hidden behind one generic fallback token. Brand semantic extensions can point constrained-channel roles to approved brand-safe families without reworking the non-safe typography system.

This also means:

- repository typography artifacts must track both `brand` and `safe` family lanes
- typography docs in Figma must show separate brand and safe sections
- helper outputs such as the font inventory and font directory must distinguish lanes explicitly

## Follow-up

- Update:
  - create and verify the `family_safe/*` variables in `Global: Typography`
  - repoint base and brand semantic safe aliases
  - rebuild typography documentation and font list in `Foundations`
- Link from:
  - each brand `artifacts.typography.decision_artifacts` list in `figma/brands/<brand>/brand.yml`
- Verify:
  - no active safe alias resolves to `*/family/fallback`
  - all brand-safe mappings match `Vail Resorts Guidelines.pdf`
  - helper outputs regenerate cleanly with `brand` and `safe` lanes
