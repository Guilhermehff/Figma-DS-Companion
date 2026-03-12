# Figma Console MCP Setup

This is the only standalone top-level setup and recovery note for the local Figma Console MCP bridge used by this repository.

Do not use the remote Figma MCP server as the primary governance path for this repository.

## Setup

1. Start the local Figma Console MCP server in your Codex environment.
2. Open the Figma Desktop app.
3. Open the **Figma Desktop Bridge** plugin inside the target file.
4. In Codex, confirm connectivity with `mcp__figma_console__figma_get_status`.
5. If multiple files are connected, use `mcp__figma_console__figma_list_open_files` before any write.

## Recovery

- If `mcp__figma_console__figma_get_status` reports that the Desktop Bridge plugin is not connected, reopen the plugin in Figma Desktop.
- If the server reports a fallback port or stale plugin connection, re-import the Desktop Bridge plugin from the local Figma Console MCP install and reopen it in the target file.
- If stale local MCP listeners have accumulated, run `python3 -m scripts.figma_governance reset-mcp` before restarting the server. By default it scans the broader fallback-safe range `9223-9235`. Add `--keep-port <port>` only when you intentionally need to preserve one active listener.
- If the active file is unclear, stop and confirm the target before any write.

## Scope

- Keep broader workflow, taxonomy, and repository governance rules in `AGENTS.md`.
- Keep stable Figma process details in `figma/docs/`.
