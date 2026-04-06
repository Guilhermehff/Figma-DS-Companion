# Decision Log

- Date: 2026-04-06
- Title: Grouped semantic theme namespaces
- Status: accepted
- Scope: Semantic token naming, repo artifact alignment, Foundations namespace migration
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations
- Stakeholders: Design system governance, Foundations maintainers, channel library authors
- Supersedes:
- Superseded by:

## Context

`Semantic: Theme` had become harder to read as more token families were added. Color roles, typography aliases, Ads size recipes, and asset tokens all lived in one collection but not under one consistent top-level grouping pattern.

That made the live collection harder to scan and increased the chance of mixing color, typography, and asset concerns in downstream governance notes. The Foundations file was renamed live to group semantic tokens by foundation family first.

## Decision

1. Group `Semantic: Theme` token paths by top-level foundation family.
2. Use `color/*` for semantic color roles.
3. Use `typography/*` for semantic typography roles, including family, weight, and approved size recipes.
4. Use `variables/*` for governed semantic string variables such as the logo label token.
5. Preserve the existing collection boundary and brand-extension model. This is a path migration, not a collection split.
6. Align canonical repo artifacts to the grouped namespace after the live Figma rename.

## Scope

- Affected collections:
  - `Semantic: Theme`
- Affected tokens or artifact paths:
  - `surface/* -> color/surface/*`
  - `on_surface/* -> color/on_surface/*`
  - `foreground/* -> color/foreground/*`
  - `border/* -> color/border/*`
  - `family/* -> typography/family/*`
  - `weight/* -> typography/weight/*`
  - `typography/size/ad/heading/*`
  - `assets/logo -> variables/assets/logo`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/AGENTS.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/config/variable-taxonomy.yml`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/brands/*`
- Explicit exceptions:
  - Historical decision logs may retain legacy token names when they are describing the state that existed at the time of the decision.
- Inherited or deferred items:
  - Raw global token naming remains unchanged.
  - Brand extension collection IDs remain unchanged because only token paths moved.

## Consequences

The live semantic collection is easier to scan and now presents color, typography, and variables as clear top-level groups.

Canonical repo artifacts must now use grouped semantic paths when they describe active Foundations state or future governance work. Historical decisions can remain as historical records, but active manifests, intake artifacts, previews, and taxonomy docs must use the live grouped namespace.

## Follow-up

- Update:
  - Keep active brand manifests and intake artifacts aligned with grouped semantic paths.
- Link from:
  - Future decisions that extend `Semantic: Theme`.
- Verify:
  - `Foundations` contains only grouped semantic paths for active variables.
  - Canonical repo docs no longer describe the active semantic namespace with legacy top-level paths.
