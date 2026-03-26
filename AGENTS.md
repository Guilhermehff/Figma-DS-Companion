# Vail Resorts Design System Companion Rules (Codex via Cursor)

This workspace governs the **Vail Resorts Design System** across multiple brands and multiple channels.

This companion is authorized to:

1. Manage and govern design system artifacts in this repository.
2. Read and write directly in Figma using **Figma Console MCP (local)**, including creating and updating variables, collections, modes, aliases, styles, and DS helper structures.

Do not treat this repository as an application codebase by default.
Do not treat this repository as the live source of truth for tokens, variables, styles, or components when those artifacts already exist in Figma.

## Companion model

- Figma is the live source of truth for current variables, collections, aliases, styles, components, and write state.
- This repository is a companion layer for brand governance, brand metadata, intake artifacts, decision history, and minimal operating guidance.
- Prefer updating a canonical existing file over creating a new parallel note, report, or duplicate process document.
- Keep repo artifacts lean. If a file mostly mirrors live Figma state and is not needed for an active audit, export, or decision record, it is a cleanup candidate.
- Do not create local component inventories or component specs unless the user explicitly asks for component governance work.

## Primary goals

- Establish and evolve a scalable design system for multiple Vail Resorts brands.
- Govern tokens and variables with a three-level token model: **Global**, **Semantic**, **Channel**.
- Use Figma Console MCP as the operational interface to Figma so the companion can perform write operations.
- Keep the DS governable: consistent naming, predictable ladders, controlled changes, and traceable decisions.
- Expand brand foundations over time (tones, fonts, typography systems, color ramps), without breaking the token schema.
- Keep the repository focused on companion value and avoid maintenance-heavy duplication of live Figma data.

## Mandatory MCP tooling

- Use **Figma Console MCP** for all Figma reads and writes.
- Do not rely on the official remote Figma MCP server for governance work because it may not expose native write operations.
- Keep `docs/mcp-setup.md` as the only standalone top-level setup and recovery note. Do not maintain a parallel workspace workflow guide outside `AGENTS.md` unless the user explicitly asks for it.

## Source of truth order

1. The current Figma file or node accessed through Figma Console MCP
2. Existing files in this repository
3. User instructions in the current conversation
4. Prior assumptions

When MCP data conflicts with local notes, update the local notes unless the user says otherwise.
When local documentation duplicates other local documentation, keep the clearest canonical version and remove or reduce the duplicate unless the user wants both preserved.

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
   - If the proposed write depends on an exception, a non-obvious interpretation, an unresolved contradiction, or any mapping that falls outside the currently established rules in `AGENTS.md`, `figma/config/variable-taxonomy.yml`, or accepted decision logs, stop and request explicit confirmation before writing into Figma.

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
- Additional groups are **brand specific** and should use the `brand_id` values governed in `figma/brands/registry.yml`.
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
   - Create dated files under `figma/exports/` only when a local audit or export is explicitly requested.
   - Treat any files under `figma/exports/` as manual dated snapshots, not as a maintained registry pipeline.

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

## Decision log rules

Create a decision log in `figma/decisions` when any of the following is true:

1. A governance rule changes the system shape.
   This includes naming, collection strategy, semantic slot admission, extension behavior, deprecation policy, or write workflow.
2. A brand staging pass introduces a non-obvious approved interpretation that should survive beyond the intake and preview artifacts.
3. A live Figma write includes an approved exception, sequencing defect, or non-obvious mapping choice that is not obvious from `figma/brands/<brand>/brand.yml` alone.
4. An accepted decision is being superseded, narrowed, or deprecated and the change needs durable historical traceability.

Do not create a decision log for:

- routine cleanup or copy edits
- straightforward repo maintenance already explained by the edited canonical file
- normal Figma writes when `figma/brands/<brand>/brand.yml` already captures the resulting state and there was no exception or special approval
- duplicate summaries of intake, preview, or manifest content when no actual governance choice was made

Decision log requirements:

- Use `figma/templates/decision-log.md` for new decision artifacts unless the user explicitly wants another format.
- Date filenames using ISO format and keep the title specific to the governance choice being recorded.
- If the decision is brand-specific, link it from the relevant `decision_artifacts` list in `figma/brands/<brand>/brand.yml`.
- If a newer decision supersedes an older one, mark that relationship explicitly in the newer file and update the older file when appropriate.

## Persistent workspace references

- figma/config/variable-taxonomy.yml is the governing taxonomy and must match this AGENTS.md.
- figma/brands/registry.yml is the governed source of truth for which brands currently exist in repo governance.
- figma/brands/<brand>/brand.yml is the canonical per-brand metadata record.
- The Figma file `Documentation Library` (`https://www.figma.com/design/x06pdECSS2rS2mHRvtt297/Docs%20Library`, file key `x06pdECSS2rS2mHRvtt297`) is the canonical source for documentation-only variables and text styles.
- figma/exports/index.yml is the optional manifest for dated manual exports and snapshot references.
- Exports under figma/exports may be out of date relative to live Figma and must use `YYYY-MM-DD-` filename prefixes.
- figma/templates/variable-audit.md and figma/templates/decision-log.md must be used for repeatable output when those artifact types are requested.
- Preserve decision history. Record governance changes in figma/decisions rather than overwriting prior decisions silently.

## Repository map

- figma/config: taxonomies and governance rules
- figma/brands: brand registry, per-brand manifests, and staged brand artifacts
- figma/exports: optional dated manual exports and snapshot references
- figma/history: migrated dated artifacts that are no longer current source files
- figma/templates: reusable output templates
- docs: minimal MCP setup and recovery guidance only

## Output conventions

- Prefer YAML for structured inventories that will be updated repeatedly.
- Prefer Markdown for audits, decisions, and narrative documentation.
- Keep Figma provenance in canonical artifacts such as `figma/brands/<brand>/brand.yml`, intake YAML, and node-specific specs or audits.
- When creating or updating documentation in Figma, use the variables and text styles from `Documentation Library` by default.
- Do not create ad hoc documentation styling in other files unless the user explicitly requests an exception.
- Do not import, create, or leave behind local `Docs/*` styles, variables, or duplicate documentation artifacts in non-documentation files unless the user explicitly approves that file-level import.
- If using `Documentation Library` assets in another file would require creating a local duplicate instead of a remote reference or variable binding, stop and ask for confirmation before writing.
- Preview Markdown may omit repeated Figma file links or node IDs when that provenance is already captured in the linked canonical artifact.
- Create local component inventories or specs only when the user explicitly requests component governance artifacts.
- Avoid duplicating process guidance across `AGENTS.md`, `docs/`, and `figma/docs/`. If the same rule appears in multiple places, consolidate toward one canonical location and simplify the rest.
- When brand documentation contains contradictions, missing provenance, stale write status, broken cross-references, or other documentation defects, call them out explicitly and fix or log them as part of the governance task instead of leaving them implicit.
- Date new reports using ISO format (YYYY-MM-DD).

## Boundaries

- Do not invent variable values, modes, or component behavior that MCP did not return.
- Do not perform destructive writes without explicit user confirmation.
- Do not write to a channel file or DS file unless the target file is confirmed.
