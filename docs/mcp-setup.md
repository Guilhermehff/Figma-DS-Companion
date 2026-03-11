# Figma Console MCP Setup

This workspace uses **Figma Console MCP** for governance reads and writes.

Do not use the remote Figma MCP server as the primary governance path for this repository.

## Required Setup

1. Start the local Figma Console MCP server in your Codex environment.
2. Open the Figma Desktop app.
3. Open the **Figma Desktop Bridge** plugin inside the target file.
4. In Codex, confirm connectivity with `mcp__figma_console__figma_get_status`.
5. If multiple files are connected, use `mcp__figma_console__figma_list_open_files` before any write.

## Recovery Steps

- If `figma_get_status` reports that the Desktop Bridge plugin is not connected, reopen the plugin in Figma Desktop.
- If the server reports a fallback port or stale plugin connection, re-import the Desktop Bridge plugin from the local Figma Console MCP install and reopen it in the target file.
- If the active file is unclear, stop and confirm the target before any write.

## Validation Tasks

After setup, the minimum governance validation loop is:

1. `mcp__figma_console__figma_get_status`
2. `mcp__figma_console__figma_list_open_files`
3. `mcp__figma_console__figma_get_variables`
4. Refresh the relevant brand manifest or split inventory in this repo
5. Run `python -m scripts.figma_governance validate`

## Repository Outputs

- Update `figma/brands/<brand>/brand.yml` when live brand context changes.
- Update `figma/variables/collections/` or `figma/variables/extensions/` after governed reads or writes.
- Regenerate `figma/variables/registry.yml` after inventory changes.
