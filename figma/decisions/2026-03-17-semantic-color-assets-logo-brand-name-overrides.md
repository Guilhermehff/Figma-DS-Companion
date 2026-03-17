# Decision Log

- Date: 2026-03-17
- Title: Semantic Color Assets Logo Uses Brand Name Overrides
- Status: accepted
- Scope: semantic color write workflow
- Brand (if brand-specific):
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance
- Supersedes:
- Superseded by:

## Context

`Semantic: Color` now includes a string variable named `assets/logo` with the default base value `Agnostic`.

Without an explicit workflow rule, brand extension writes can leave that variable inherited from the base collection even when the rest of the color extension has already been branded.

## Decision

When `assets/logo` exists in the base `Semantic: Color` collection, every brand extension must override it to the brand display name string.

This override is part of the normal semantic color write workflow, not an optional brand-specific extra.

## Scope

- Affected collections:
  - `Semantic: Color`
- Affected tokens or artifact paths:
  - `assets/logo`
  - `figma/docs/semantic-extension-write-workflow.md`
- Explicit exceptions:
  - none
- Inherited or deferred items:
  - The actual channel-side logo asset mapping remains deferred to downstream channel libraries or implementation layers.

## Consequences

Future brand extension writes must treat `assets/logo` as part of the minimal semantic color override set whenever the variable is present.

Brand manifests should capture the override in notes when it is relevant to the live write.

## Follow-up

- Update:
  - The rule is now added to `figma/docs/semantic-extension-write-workflow.md`.
- Link from:
  - future brand write decisions when relevant
- Verify:
  - new brand semantic color extensions resolve `assets/logo` to the brand display name rather than `Agnostic`
