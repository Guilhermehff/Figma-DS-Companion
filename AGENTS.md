# Vail Resorts Design System Companion Rules (Codex via Cursor)

This workspace governs the **Vail Resorts Design System** across multiple brands and multiple channels.

This companion is authorized to:

1. Manage and govern design system artifacts in this repository.
2. Read and write directly in Figma using **Figma Console MCP (local)**, including creating and updating variables, collections, modes, aliases, styles, and DS helper structures.

Do not treat this repository as an application codebase by default.

## Primary goals

- Establish and evolve a scalable design system for multiple Vail Resorts brands.
- Govern tokens and variables with a three-level token model: **Global**, **Semantic**, **Channel**.
- Use Figma Console MCP as the operational interface to Figma so the companion can perform write operations.
- Keep the DS governable: consistent naming, predictable ladders, controlled changes, and traceable decisions.
- Expand brand foundations over time (tones, fonts, typography systems, color ramps), without breaking the token schema.

## Mandatory MCP tooling

- Use **Figma Console MCP** for all Figma reads and writes.
- Do not rely on the official remote Figma MCP server for governance work because it may not expose native write operations.

## Source of truth order

1. The current Figma file or node accessed through Figma Console MCP
2. Existing files in this repository
3. User instructions in the current conversation
4. Prior assumptions

When MCP data conflicts with local notes, update the local notes unless the user says otherwise.

## Pre flight checklist (required before any Figma write)

Before performing any write operation in Figma:

1. Confirm the target file
   - Channel libraries are separate files from the DS file.
   - If the user did not provide a file link, ask for it.
   - If multiple candidate files are open, stop and ask which file to modify.

2. Confirm the scope
   - If the task depends on selection, confirm selection details through MCP.

3. Confirm write intent
   - If the task is destructive (delete, merge, bulk rename, remove modes), stop and request explicit confirmation.

## Token model

This DS uses three token levels.

### Level 1: Global

Global tokens are raw values.

Rules:

- Each global token category lives in its **own dedicated collection**.
- Global collection names must always start with `_` so they are not published.
- Every `_global_*` collection uses an initial mode named `values`.
- Variable names inside a collection must not repeat the collection category.
- Brand separation at the Global level is achieved through **groups** inside that shared collection.
- The first group is **universal**.
- Additional groups are **brand specific** (e.g., vail, beaver_creek, breckenridge, park_city).
- Global tokens do not carry UI meaning.

### Level 2: Semantic

Semantic tokens are an abstraction ladder but **still do not carry final meaning**.

They exist to bridge raw values toward meaning, while remaining interchangeable.

Example ladder for color:

- global color -> semantic category scale -> channel meaning
- slate/50 -> neutral/50 -> bg/surface

Rules:

- Semantic tokens alias Global tokens.
- Each semantic token category lives in its **own dedicated collection**.
- **Extended collections happen at the Semantic level** to support brand differences while keeping one semantic schema.
- Semantic tokens should be structured so they can be mapped into channel meaning cleanly.

Naming note:

- Figma variable names use slash-delimited paths, not dot-delimited names.
- In `_global_color`, `_global_typography`, and `_global_dimensions`, the collection already defines the category, so variable names start at the child path (for example `universal/slate/50`, `universal/size/100`, `space/4`).

### Level 3: Channel

Channel tokens are where meaning is defined and applied.

Rules:

- Channel libraries are separate Figma files from the DS file.
- Channel tokens alias Semantic tokens.
- Channel specific constraints are allowed and expected (e.g., Email limitations).
- Channel typography is typically handled as **styles** in the channel library.

### Exception: Dimensions

Dimensions group all sizing related aspects and remain global first across channels.

## Multi brand scope

- This DS supports multiple Vail Resorts brands.
- The companion must help expand tones, fonts, and foundational systems per brand.
- The companion must keep the token schema stable while adding brand coverage.

## Required Figma MCP workflow

When MCP is available and the task references a Figma file, selection, or node:

1. Context and file safety
   - Use mcp**figma_console**figma_get_status and mcp**figma_console**figma_list_open_files to confirm file context.
   - If unsure whether the active file is the DS file or a channel file, stop and ask.

2. Variables and tokens
   - Use mcp**figma_console**figma_get_variables for inventory, collections, modes, aliases, and naming.
   - Use mcp**figma_console**figma_get_token_values only for narrow checks.

3. Components and styles
   - Use mcp**figma_console**figma_get_component for component structure, metadata, variants, and documentation.
   - Use screenshots or component images when visual verification is required.

4. Write operations
   - Use native figma-console write tools when available.
   - Do not switch to capture based generation paths unless explicitly requested.

If the user wants Figma analysis or writes but does not provide a selection, URL, or node, ask for the exact Figma link.

## Naming dispute protocol (mandatory when ambiguous)

When a new token does not clearly fit the taxonomy or the ladder:

1. Stop and describe the ambiguity in one sentence.
2. Propose 2 to 3 compliant naming options.
3. Explain tradeoffs.
4. Ask which option to proceed with before writing into Figma.

Do not invent new conventions silently.

## Persistent workspace references

- figma/config/variable-taxonomy.yml is the governing taxonomy and must match this AGENTS.md.
- figma/templates/variable-audit.md, figma/templates/component-spec.md, figma/templates/decision-log.md must be used for repeatable output.
- Preserve decision history. Record governance changes in figma/decisions rather than overwriting prior decisions silently.

## Repository map

- figma/config: taxonomies and governance rules
- figma/variables: structured inventories, registries, and naming proposals
- figma/components: inventories and component level specs
- figma/templates: reusable output templates
- docs: setup and onboarding guidance

## Output conventions

- Prefer YAML for structured inventories that will be updated repeatedly.
- Prefer Markdown for audits, decisions, and narrative documentation.
- Include the Figma file link or node ID in every artifact created from MCP data.
- Date new reports using ISO format (YYYY-MM-DD).

## Boundaries

- Do not invent variable values, modes, or component behavior that MCP did not return.
- Do not perform destructive writes without explicit user confirmation.
- Do not write to a channel file or DS file unless the target file is confirmed.
