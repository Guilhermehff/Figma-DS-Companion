# Workspace Guide

This repository is organized so Codex can turn MCP output into durable design-system artifacts.

## Recommended Workflow

1. Start from a specific Figma link or node.
2. Check the standing repository references before making assumptions:
   - `figma/config/variable-taxonomy.yml` for token structure and naming rules
   - `figma/variables/registry.yml` for the current normalized token inventory
   - `figma/components/index.yml` for the current component inventory
3. Pull context with the MCP tool that matches the task.
4. Normalize the result into Markdown or YAML in this repo.
5. Update existing artifacts instead of creating parallel versions.
6. Record decisions when taxonomy or naming changes affect multiple files.

## Tool Selection

- Token and variable work: `mcp__figma_console__figma_get_variables` first, then `mcp__figma_console__figma_get_token_values` for focused lookups.
- Component documentation: `mcp__figma_console__figma_get_component` first, plus `mcp__figma_console__figma_get_component_image` or `mcp__figma_console__figma_capture_screenshot` for visual evidence.
- Broad file discovery: `mcp__figma_console__figma_get_design_system_summary` first.
- Current selection workflows: `mcp__figma_console__figma_get_selection`.
- Only use `mcp__figma_console__figma_get_component_for_development` when the task is explicitly implementation-oriented.

## Directory Use

- `figma/variables/`: token registries, naming proposals, mode maps, alias cleanup
- `figma/components/`: component specs, inventories, usage notes
- `figma/docs/`: stable reference docs for the system
- `figma/audits/`: dated audits and cleanup reports
- `figma/decisions/`: design-system governance decisions

## Good Task Examples

- Audit all color variables used in a frame and write the findings to `figma/audits/`
- Convert the variables in a library section into `figma/variables/registry.yml`
- Document a component family and its variants in `figma/components/`
- Propose a cleaner naming taxonomy and capture the decision in `figma/decisions/`

## Default Output Style

- concise
- explicit about unknowns
- grounded in the exact Figma scope provided
- easy to diff in Git
