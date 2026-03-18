# Decision Log

- Date: 2026-03-18
- Title: Confirm Out-Of-Rule Figma Writes Before Mutation
- Status: accepted
- Scope: Figma write workflow
- Brand (if brand-specific):
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3
- Stakeholders: Design System Governance, user approval in chat
- Supersedes:
- Superseded by:

## Context

The existing pre-flight checklist already requires target-file confirmation before any Figma write and explicit confirmation for destructive operations.

That was not strict enough for governance cases where a write is non-destructive but still depends on an exception, a non-obvious interpretation, a contradiction in source material, or a mapping that falls outside the established taxonomy and accepted decisions.

## Decision

Before any Figma mutation, if the proposed write depends on:

1. an exception to the established workflow or taxonomy,
2. a non-obvious interpretation that is not already approved in the governing artifacts,
3. an unresolved contradiction in the source material, or
4. any mapping that falls outside the currently established rules in `AGENTS.md`, `figma/config/variable-taxonomy.yml`, or accepted decision logs,

the companion must stop and request explicit confirmation before writing into Figma.

This confirmation requirement applies even when the write is non-destructive.

## Scope

- Affected collections:
  - all future Figma write targets
- Affected tokens or artifact paths:
  - `AGENTS.md`
  - future brand manifests and decision logs when exception-driven writes are proposed
- Explicit exceptions:
  - none
- Inherited or deferred items:
  - destructive writes still require explicit confirmation under the pre-existing rule
  - ordinary writes that stay fully inside the established governance rules do not require extra confirmation beyond normal target-file confirmation

## Consequences

The write workflow is now stricter for governance interpretation work. A write can no longer proceed just because it is non-destructive if it still requires a rule exception or a non-obvious mapping judgment.

This makes the approval boundary clearer for future brand staging and extension work, especially when source material does not map cleanly into the current token model.

## Follow-up

- Update:
  - Add the explicit confirmation rule to the Figma pre-flight checklist in `AGENTS.md`.
- Link from:
  - future decision logs that rely on approved exceptions or non-obvious mappings
- Verify:
  - future out-of-rule or exception-based Figma writes stop for confirmation before mutation
