# Figma MCP Setup For Codex

This workspace is ready for Figma MCP-driven work, but the MCP connection itself must be enabled in Codex.

## Recommended Setup

Use the Figma remote MCP server unless you specifically need desktop-only selection workflows inside the Figma desktop app.

- Remote server endpoint: `https://mcp.figma.com/mcp`
- Desktop server endpoint: `http://127.0.0.1:3845/mcp`

## Codex App Setup

Based on Figma's official documentation current on March 10, 2026:

1. Open the Codex app.
2. Open `Skills` and install the Figma skill.
3. Open `Settings` -> `MCP servers`.
4. In recommended servers, install and authenticate the Figma server.
5. After authentication, start a new session in this workspace.

## When To Use Remote Vs Desktop

Use the remote server when:

- you want the simplest setup
- you are working from shared Figma links
- you want Codex to access Figma without the desktop app

Use the desktop server when:

- you want selection-based prompting from the Figma desktop app
- you want to inspect the currently selected layer directly in Dev Mode
- you have a paid Figma plan with a Dev or Full seat

## Figma Access Notes

- The remote MCP server is available on all Figma seats and plans.
- The desktop MCP server requires a Dev or Full seat on a paid Figma plan.
- Figma documents daily and per-minute rate limits; if MCP calls start failing unexpectedly, check seat type and rate limits first.

## How To Confirm It Worked

After setup, a Codex session should expose Figma MCP tools such as:

- `mcp__figma_console__figma_get_variables`
- `mcp__figma_console__figma_get_component`
- `mcp__figma_console__figma_get_component_image`
- `mcp__figma_console__figma_get_selection`
- `mcp__figma_console__figma_get_design_system_summary`

In this workspace, the fastest validation task is:

`Use mcp__figma_console__figma_get_variables for this Figma scope and normalize the result into figma/variables/registry.yml.`

## Current Workspace State

Connection state is session-specific. Confirm the active session with `mcp__figma_console__figma_get_status` or `mcp__figma_console__figma_get_selection` before assuming Figma context is available.

## Sources

- [Figma MCP guide](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)
- [Figma remote MCP installation](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Figma MCP tools and prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
- [Figma plans, access, and permissions](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/)
