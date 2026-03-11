# Typography Default Assumptions

Date: 2026-03-10
Status: accepted

## Context

Brand typography source images often define families, role behavior, and relational sizing without listing complete raw numeric metadata. The design system still needs a consistent intake and preview workflow before typography is written into Figma.

## Decision

For brand typography reviews:

1. If a source style is labeled `Black` and no separate numeric exception is supplied, reuse `universal/weight/black` as the shared raw black weight.
2. If raw font sizes are missing, map the role to the existing universal size ladder for the current review and mark that mapping as assumed.
3. If a fallback or web-safe family is missing, default the fallback reference to `universal/family/web_safe`.
4. Treat semantic family aliases as role-light mappings from raw families. Prefer `family/heading`, `family/body`, and `family/action` over channel-shaped names such as `family/cta`.

## Rationale

- Global raw typography should stay mostly about reusable families, shared weights, and a stable size ladder.
- Missing source metadata should not block intake and preview work when the unresolved values can safely inherit universal defaults.
- `action` is broader than `cta`, so it supports a more stable semantic ladder across buttons, links, navigation prompts, and promotional actions.

## Consequences

- Typography previews can move forward without waiting for every numeric size decision.
- Review artifacts must clearly label assumed size mappings so later refinement is traceable.
- The design system can add one shared `universal/weight/black` raw token and reuse it across brands.
