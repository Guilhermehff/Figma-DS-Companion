# Crotched Typography Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/crotched/brand.yml` and Figma.

## Original Source Roles

- Source role: `shared_brand_typography`
  Family: `universal/family/primary`
  Style: `primary`
  Weight label: `inherit`
  Usage scope: `heading_body_action`
  Case: `inherit_base`
  Tracking: `inherit_base`
  Leading: `inherit_base`
  Size rule: `inherit_base`
  Punctuation: `inherit_base`
  Sample copy: `Crotched`
  Notes: The user instructed Crotched to use the universal typography baseline because no brand-specific font guidance was supplied.

## Primitive Recommendations

- Proposed primitive:
  Token name: `crotched/family/primary`
  Source item: `Inter`
  Fallback token: `universal/family/web_safe`
  Notes: Raw brand family token created for governance parity while intentionally keeping the same value as `universal/family/primary`.

- Reuse:
  Source item: `universal weight and size baseline`
  Proposed token: `inherit semantic base`
  Assumption status: `explicit`
  Notes: No brand-specific typography guidance was supplied, so Crotched keeps the universal effective typography behavior.

## Live Semantic Mapping

- `family/heading` -> `crotched/family/primary`
- `family/body` -> `crotched/family/primary`
- `family/action` -> `crotched/family/primary`
- `family/heading_safe` -> inherit `universal/family/web_safe`
- `family/body_safe` -> inherit `universal/family/web_safe`
- `family/action_safe` -> inherit `universal/family/web_safe`
- `weight/*` -> inherit current semantic base
- `size/*` -> inherit current semantic base
- Inherited or deferred notes: Crotched adds a raw brand family token only; the effective typography values stay identical to the universal baseline.

## Role Recipes

### Role: heading

<div style="font-family: sans-serif; font-weight: 700; font-size: 32px; line-height: 1.1; letter-spacing: 0;">
  Crotched
</div>

- Proposed family token: `crotched/family/primary`
- Proposed weight token: `inherited current heading weights`
- Proposed size token: `inherited current heading ladder`
- Notes: Same effective values as universal, but through the Crotched raw family alias.

### Role: body

<div style="font-family: sans-serif; font-weight: 500; font-size: 18px; line-height: 1.4; letter-spacing: 0;">
  Crotched
</div>

- Proposed family token: `crotched/family/primary`
- Proposed weight token: `inherited current body weights`
- Proposed size token: `inherited current body ladder`
- Notes: Body remains semantically identical to the universal baseline.

### Role: action

<div style="font-family: sans-serif; font-weight: 900; font-size: 18px; line-height: 1; letter-spacing: 0;">
  Crotched
</div>

- Proposed family token: `crotched/family/primary`
- Proposed weight token: `inherited current action weights`
- Proposed size token: `inherited current action ladder`
- Notes: Action remains semantically identical to the universal baseline.

## Review Notes

- Crotched adds a governed raw family token for brand parity, but the live typography behavior remains unchanged from the universal baseline.
- Weight, safe-family, and size semantics stay inherited because the user explicitly asked to use the universal typography system.

## Review Readiness

- Subject: `Crotched mirrored typography baseline`
  Channels: `web, email, ads`
  Rule: Create a raw Crotched family token, but keep its effective typography values identical to the universal baseline.
  Source basis: User instruction in chat.
