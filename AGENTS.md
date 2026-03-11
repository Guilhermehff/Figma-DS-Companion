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
- Global collection names must use the `_Global: *` pattern so they are not published.
- Every `_Global: *` collection uses an initial mode named `values`.
- Variable names inside a collection must not repeat the collection category.
- Brand separation at the Global level is achieved through **groups** inside that shared collection.
- The first group is **universal**.
- Additional groups are **brand specific** and come from `figma/brands/registry.yml`.
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
- In `_Global: Color`, `_Global: Typography`, and `_Global: Dimensions`, the collection already defines the category, so variable names start at the child path (for example `universal/slate/50`, `universal/size/100`, `space/4`).

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

## Confirmed Semantic Extension Write Route

When creating or updating a Semantic extension collection in the Design System file, use this exact route first.

1. Confirm context
   - Use `mcp__figma_console__figma_get_status` and `mcp__figma_console__figma_list_open_files`.
   - Only proceed when the intended DS file is the sole confirmed write target.

2. Read the parent collection and source variables
   - Use `mcp__figma_console__figma_execute` with the native Variables API.
   - Resolve the parent collection with `await figma.variables.getVariableCollectionByIdAsync(...)`.
   - Resolve reusable source variables from the Global collection before writing aliases.

3. Create the extension natively
   - Do not create a parallel semantic collection by hand.
   - Call `parentCollection.extend("Brand Name")`.
   - Important: `extend()` requires the extension name string. Calling `extend()` without a name fails validation.

4. Write overrides on the base semantic variables
   - Use the extension mode ID from `extensionCollection.modes[0].modeId`.
   - Set overrides on the base semantic variables with:
     `baseVariable.setValueForMode(extensionModeId, figma.variables.createVariableAlias(sourceVariable))`
   - The override key is the base semantic variable ID, not a duplicate variable name inside a new collection.

5. Verify through the extension collection object
   - Inspect `extensionCollection.variableOverrides` to confirm which base variables are overridden.
   - Use `await baseVariable.valuesByModeForCollectionAsync(extensionCollection)` to verify the extension-specific alias target.
   - Important: `valuesByModeForCollectionAsync()` expects the collection object, not the collection ID string.
   - Immediately query local variable collections for duplicate brand extension collections in the same semantic category.
   - If more than one extension collection exists for the same brand and parent category, stop and remove the stray duplicate before syncing repo state.

6. Sync repo state immediately
   - Persist the extension collection ID and any approved non-obvious mapping notes back into `figma/brands/<brand>/brand.yml`.
   - Create `figma/variables/extensions/*.yml` only when a local audit or export is explicitly requested.
   - Create or rebuild `figma/variables/registry.yml` only when a local compatibility export is explicitly requested.

7. Treat cached inventory reads carefully
   - `figma_get_variables` may lag after a write.
   - If results look stale, verify with `figma_execute` against the plugin runtime before changing repo artifacts again.

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
- figma/brands/registry.yml is the governed source of truth for which brands currently exist in repo governance.
- figma/brands/<brand>/brand.yml is the canonical per-brand metadata record.
- figma/variables/index.yml is the optional export manifest for local collection snapshots and compatibility exports.
- figma/variables/registry.yml, when present, is an on-demand generated compatibility export and must not be hand-edited.
- figma/templates/variable-audit.md, figma/templates/component-spec.md, figma/templates/decision-log.md must be used for repeatable output.
- Preserve decision history. Record governance changes in figma/decisions rather than overwriting prior decisions silently.

## Repository map

- figma/config: taxonomies and governance rules
- figma/brands: brand registry, per-brand manifests, and staged brand artifacts
- figma/variables: optional local exports, collection snapshots, and naming proposals
- figma/history: migrated dated artifacts that are no longer current source files
- figma/components: inventories and component level specs
- figma/templates: reusable output templates
- docs: setup and onboarding guidance

## Output conventions

- Prefer YAML for structured inventories that will be updated repeatedly.
- Prefer Markdown for audits, decisions, and narrative documentation.
- Keep Figma provenance in canonical artifacts such as `figma/brands/<brand>/brand.yml`, intake YAML, and node-specific specs or audits.
- Preview Markdown may omit repeated Figma file links or node IDs when that provenance is already captured in the linked canonical artifact.
- When brand documentation contains contradictions, missing provenance, stale write status, broken cross-references, or other documentation defects, call them out explicitly and fix or log them as part of the governance task instead of leaving them implicit.
- Date new reports using ISO format (YYYY-MM-DD).

## Boundaries

- Do not invent variable values, modes, or component behavior that MCP did not return.
- Do not perform destructive writes without explicit user confirmation.
- Do not write to a channel file or DS file unless the target file is confirmed.
