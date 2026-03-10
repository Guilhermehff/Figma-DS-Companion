# Design System Companion Rules

This workspace is a Codex companion for Figma design-system work. It is not an application codebase by default. Favor analysis, organization, documentation, and system governance over code generation unless the user explicitly asks for implementation work.

## Primary Goals

- Keep design-system knowledge in versioned files that Codex can update safely.
- Use Figma MCP as the primary source for variables, components, screenshots, and structure.
- Normalize MCP output into concise Markdown or YAML artifacts in this repository.
- Help with variable audits, naming cleanup, documentation, taxonomy decisions, and component inventories.

## Persistent Workspace References

- Treat `figma/config/variable-taxonomy.yml` as the standing token taxonomy unless the user explicitly overrides it.
- Treat `figma/variables/registry.yml` as the canonical normalized variable inventory in this repository. Update it instead of creating duplicate registries.
- Treat `figma/components/index.yml` as the canonical component inventory for tracking documentation status and scope.
- Use `docs/workspace-guide.md` to decide where new artifacts belong before creating files.
- Use `figma/templates/variable-audit.md`, `figma/templates/component-spec.md`, and `figma/templates/decision-log.md` for repeatable output structure.
- When taxonomy or governance changes, preserve history and record the change in `figma/decisions/` instead of silently replacing prior decisions.

## Source of Truth Order

1. The current Figma node or file accessed through MCP
2. Existing files in this repository
3. User instructions in the current conversation
4. Prior assumptions

When MCP data conflicts with local notes, update the local notes unless the user says otherwise.

## Required Figma MCP Workflow

When MCP is available and the task references a Figma file, selection, or node:

1. Use `mcp__figma_console__figma_get_selection` first when the task depends on the current Figma selection. If the file context is missing, use `mcp__figma_console__figma_get_status`, `mcp__figma_console__figma_list_open_files`, or `mcp__figma_console__figma_navigate` as needed.
2. Use `mcp__figma_console__figma_get_variables` first for token and variable work. Use `mcp__figma_console__figma_get_token_values` for narrow value lookups, and prefer filtered or summary output before full dumps.
3. Use `mcp__figma_console__figma_get_component` first for component structure, metadata, variants, and documentation work. Use `mcp__figma_console__figma_get_component_for_development` only when the user explicitly wants implementation-oriented output.
4. Use `mcp__figma_console__figma_get_component_image`, `mcp__figma_console__figma_capture_screenshot`, or `mcp__figma_console__figma_take_screenshot` when documenting behavior, reviewing visual consistency, or comparing variants.
5. Use `mcp__figma_console__figma_get_design_system_summary` first for broad file discovery. Escalate to `mcp__figma_console__figma_get_design_system_kit` or `mcp__figma_console__figma_get_file_data` only when the task needs wider system context.
6. Prefer documentation and inventory tools over implementation-oriented tools unless the user explicitly asks for code.

If the user wants Figma analysis but does not provide a selection, URL, or node, ask for the exact Figma link or node.

## Repository Map

- `figma/inbox/`: raw task notes or pasted MCP outputs waiting to be normalized
- `figma/variables/`: structured token inventories, naming proposals, and cleanup work
- `figma/components/`: component inventories and component-level specs
- `figma/docs/`: polished documentation intended for ongoing reference
- `figma/audits/`: one-off audits, gap analyses, and cleanup reports
- `figma/decisions/`: ADR-style records for naming, taxonomy, and governance choices
- `figma/templates/`: reusable templates for Codex outputs
- `figma/config/`: naming systems and taxonomy rules

## File Conventions

- Prefer YAML for structured inventories that Codex may update repeatedly.
- Prefer Markdown for narrative documentation, audits, and decisions.
- Include the Figma URL or node ID in every artifact created from MCP data.
- Date new reports using ISO format (`YYYY-MM-DD`).
- Do not create duplicate artifacts for the same purpose; update the existing file when possible.

## Variable Work Rules

- Capture collection, mode, scope, variable name, resolved value, alias target, and usage notes when available.
- Distinguish primitive tokens from semantic tokens and component-scoped tokens.
- Flag hard-to-maintain names such as `color-1`, `gray-new`, `test`, or names that encode implementation instead of meaning.
- Prefer naming based on intent and usage, not raw appearance alone.
- Track deprecations explicitly rather than silently renaming or deleting variables in documentation.

## Documentation Rules

- Default outputs should be concise and operational.
- Call out open questions, missing modes, inconsistent aliases, and naming collisions explicitly.
- When documenting components, capture purpose, variants, states, dependencies on variables, and known gaps.
- When a recommendation is an inference from MCP output rather than a direct fact, label it as an inference.
- When a task touches taxonomy or naming, reference the current rules in `figma/config/variable-taxonomy.yml` instead of restating them from memory.

## Boundaries

- Do not invent variable values, modes, or component behavior that MCP did not return.
- Do not treat implementation-oriented output from `mcp__figma_console__figma_get_component_for_development` as the goal in this repository unless the user asks for code.
- Do not overwrite user-authored decisions without preserving the decision history.
