# Decision Log

- Date: 2026-04-06
- Title: Semantic theme Ads typography size recipes
- Status: accepted
- Scope: Typography token model, Ads brand switching, Foundations write behavior
- Brand (if brand-specific): n/a
- Figma file (if applicable): Foundations
- Stakeholders: Design system governance, Ads library authors
- Supersedes:
  - `2026-03-26-semantic-theme-and-published-global-typography.md`
- Superseded by:
  - `2026-04-06-semantic-theme-ad-brand-row-order-mappings.md`

## Context

The current token model kept typography size out of `Semantic: Theme` and required channels to bind size directly from `Global: Typography`.

That rule worked for the shared universal core size ladder and for current Email usage, but it created a mismatch for Ads. Ads already consumes color through `Semantic: Theme` brand extensions, while the approved ad heading system now uses five branded scale columns (`0.75x`, `0.875x`, `base`, `1.125x`, `1.375x`) that must switch with the same single brand context.

Keeping Ads heading size outside `Semantic: Theme` would force a second independent brand switch or duplicate channel structures. That would split brand-controlled color and typography decisions across different mechanisms in the Ads workflow.

## Decision

1. Keep raw ad heading size values in `Global: Typography`.
2. Approve a narrow semantic exception for Ads heading size recipes inside `Semantic: Theme`.
3. Use the raw global naming family `universal/size/ad/<scale>/<slot>` for the five approved Ads scale columns.
4. Use the semantic naming family `typography/size/ad/heading/<role>` for Ads heading size roles.
5. Keep the raw global names structural rather than role-based. Slot mapping is:
   - `01 -> xs`
   - `02 -> s`
   - `03 -> md`
   - `04 -> lg`
   - `05 -> xl`
6. Seed the base `Semantic: Theme` Ads heading roles from the `base` raw column.
7. Defer brand extension overrides until each brand-to-scale mapping is approved.
8. Email remains on the existing raw shared size ladder for now and does not move into semantic size recipes in this decision.

## Scope

- Affected collections:
  - `Global: Typography`
  - `Semantic: Theme`
- Affected tokens or artifact paths:
  - `universal/size/core/100` through `universal/size/core/800`
  - `universal/size/ad/0_75/01` through `universal/size/ad/1_375/05`
  - `typography/size/ad/heading/xs`
  - `typography/size/ad/heading/s`
  - `typography/size/ad/heading/md`
  - `typography/size/ad/heading/lg`
  - `typography/size/ad/heading/xl`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/AGENTS.md`
  - `/Users/guilhermefidelio/Documents/GitHub/Vail Resorts DS/figma/config/variable-taxonomy.yml`
- Explicit exceptions:
  - `Semantic: Theme` may carry Ads-only typography size recipe aliases.
  - The approved semantic size exception is scoped to `typography/size/ad/*` and does not authorize general semantic size ladders.
- Inherited or deferred items:
  - Email keeps binding size directly from `Global: Typography`.
  - Brand extension overrides for Ads size recipes are deferred.
  - Ad format mappings such as `970x250` and `320x50` stay in documentation and style recipes, not in token names.

## Consequences

Ads can keep one brand switch in `Semantic: Theme` for both color and heading size behavior.

`Global: Typography` now contains a second published raw size family for Ads in addition to the shared universal size ladder. `Semantic: Theme` is still not a general-purpose home for typography size aliases; it now carries one explicit channel-scoped exception for Ads heading recipes.

Future channel-specific typography size recipes require another accepted decision before they are written into Figma.

## Follow-up

- Update:
  - Align `AGENTS.md` and `figma/config/variable-taxonomy.yml` with the Ads semantic size exception.
- Link from:
  - Future Ads brand governance artifacts once brand-to-scale mappings are approved.
- Verify:
  - `Foundations` contains `universal/size/core/<step>` and `universal/size/ad/<scale>/<slot>` raw values.
  - `Semantic: Theme` contains `typography/size/ad/heading/<role>` aliases pointing to the `base` raw column until brand extensions are written.
