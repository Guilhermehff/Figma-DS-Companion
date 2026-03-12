# Shared Semantic Collections With Brand Extensions

Date: 2026-03-11
Status: accepted
Historical naming note: References to `semantic_typography` describe the pre-rename display name. The current collection is `Semantic: Typography`.

## Context

The semantic layer needs to support multiple brands while keeping one stable schema for downstream web and email libraries.

## Decision

Use one shared semantic collection per category, with brand-specific extensions.

For typography:

1. The shared base collection is `semantic_typography`.
2. The base collection uses a mode named `values` and points to universal global primitives.
3. Brand-specific differences are applied only through the brand extension collection, using the brand name only, for example `vail`.
4. A brand extension overrides only the semantic tokens that differ from the universal baseline.
5. Tokens that remain universal should stay defined only in the base collection and should not be redundantly reassigned inside the brand extension.

## Rationale

- One shared semantic schema keeps channel libraries stable.
- Extensions let brand differences exist without forking the entire semantic ladder.
- Universal defaults remain visible and governable in one place.

## Consequences

- Semantic writes should start by building the shared universal baseline.
- Brand semantic work should touch only the override tokens inside the relevant extension collection.
- Registries and previews should distinguish between base semantic aliases and brand-specific overrides.
