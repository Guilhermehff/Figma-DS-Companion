# Decision Log

- Date: 2026-03-26
- Title: Figma grid write route for documentation and component builds
- Status: accepted
- Scope: Figma write workflow
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations and future documentation/component files
- Stakeholders: Design system companion, documentation authors
- Supersedes:
- Superseded by:

## Context

Recent documentation work on `_Global: Typography - Font List` exposed a repeatable Figma MCP pitfall: grid children in a `GRID` parent keep explicit row and column anchors, so cloning and moving them by surface coordinates does not reliably create new rows. That behavior makes it easy to break documentation tables or silently convert a grid layout into a row/column fallback.

The workspace needs a durable write rule so grid can be used intentionally for future documentation frames and component construction without repeating that failure mode.

## Decision

The accepted write route for Figma `GRID` containers is:

1. Inspect the existing grid child pattern before writing.
2. Preserve the confirmed `GRID` parent instead of swapping it to another layout model.
3. Duplicate the intended source cells or row pattern.
4. Place every duplicated grid child with `setGridChildPosition(row, col)` instead of relying on `x` and `y`.
5. Resize cells and the parent frame to the real content bounds when text length changes row height.
6. Verify both screenshot output and grid child anchors before closing the task.

This route applies to documentation tables and to future component-building tasks that use grid as a structural layout tool.

## Scope

- Affected collections:
  - n/a
- Affected tokens or artifact paths:
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/AGENTS.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/decisions/2026-03-26-figma-grid-write-route-for-documentation-and-component-builds.md`
- Explicit exceptions:
  - A confirmed `GRID` parent may only be replaced with another layout model when the user explicitly approves that structural change.
- Inherited or deferred items:
  - Existing documentation and component files can continue using any current layout model; this decision governs future writes and edits.

## Consequences

Grid becomes a supported construction method for documentation and components, but only through explicit grid-child placement rather than coordinate-based movement.

Future Figma MCP writes should be more predictable, especially for repeated rows, generated tables, and component patterns with variable content length.

## Follow-up

- Update:
  - Keep the grid workflow bullets in `AGENTS.md` current if future Figma MCP behavior changes.
- Link from:
  - n/a
- Verify:
  - Apply this route on future grid-based Figma writes instead of reverting to row-layout fallbacks.
