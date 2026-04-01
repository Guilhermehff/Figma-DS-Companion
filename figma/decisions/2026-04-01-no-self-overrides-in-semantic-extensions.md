# Decision Log

- Date: 2026-04-01
- Title: No self-overrides in semantic extensions
- Status: accepted
- Scope: Semantic extension write workflow and cleanup
- Brand (if brand-specific): N/A
- Figma file (if applicable): Foundations (`https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations`)
- Stakeholders: Design system governance
- Supersedes: None
- Superseded by:

## Context

A live audit of `Semantic: Theme` extensions found redundant override records that resolved to the same alias target as the base semantic token. Those entries changed extension state without changing the effective token mapping.

The issue came from prior extension writes that stored override entries even when the extension and base values were identical. That behavior makes the Foundations file harder to govern and obscures which tokens actually differ by brand.

## Decision

Semantic extensions must not keep self-overrides.

If an extension value resolves to the same alias target or the same literal value as the base semantic token, the token must inherit from the base collection instead of storing an override entry.

When redundant override entries are found in live Figma, they should be removed as cleanup rather than preserved.

## Scope

- Affected collections:
  - `Semantic: Theme`
  - All `Semantic: Theme` extension collections in Foundations
- Affected tokens or artifact paths:
  - Semantic color, typography, and asset overrides when the extension value matches the base value
  - `AGENTS.md`
  - `figma/config/variable-taxonomy.yml`
  - `figma/docs/semantic-extension-write-workflow.md`
- Explicit exceptions:
  - None
- Inherited or deferred items:
  - Genuine brand-specific overrides remain valid and should stay in place

## Consequences

Extension cleanup should reduce noisy override counts without changing resolved token behavior.

Future semantic extension writes must compare each proposed override against the base semantic value before finalizing the write. Verification must confirm that no same-target override entries remain.

## Follow-up

- Update:
  - Remove redundant same-target override entries from live `Semantic: Theme` extensions in Foundations
  - Keep the governed write workflow aligned with this rule
- Link from:
  - No brand manifest link required because this decision is system-wide rather than brand-specific
- Verify:
  - `variableOverrides` no longer contains entries whose extension value matches the base semantic value
