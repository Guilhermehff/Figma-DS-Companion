# Semantic Extension Write Workflow

Date: 2026-03-11
Status: active
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations?node-id=1-3

## Purpose

Use this route whenever a brand needs a Semantic extension collection in the Foundations file.

This is the confirmed native workflow for the current Figma Variables API and should be the default route before trying alternative approaches.

## Preferred Route

1. Confirm the DS file with `figma_get_status` and `figma_list_open_files`.
2. Use `figma_execute` to work against the native Variables API.
3. Resolve the parent semantic collection with `await figma.variables.getVariableCollectionByIdAsync(...)`.
4. Create the extension with `parentCollection.extend("Brand Name")`.
5. Resolve the raw source variables from the Global collection.
6. Resolve the base semantic variables from the parent semantic collection.
7. Apply each override on the base semantic variable with:

```js
baseVariable.setValueForMode(
  extensionCollection.modes[0].modeId,
  figma.variables.createVariableAlias(sourceVariable),
);
```

8. Before keeping an override, compare it to the base semantic value for the parent mode. If the extension resolves to the same alias target or the same literal value as the base token, remove the override and inherit from the base instead.
9. If `assets/logo` exists in the base `Semantic: Theme` collection, override it to the brand display name string on the extension mode. Do not leave the inherited base value `Agnostic`.
10. Verify the extension through:
   - `extensionCollection.variableOverrides`
   - `await baseVariable.valuesByModeForCollectionAsync(extensionCollection)`
   - `figma.variables.getLocalVariableCollectionsAsync()` to confirm there is only one extension collection for that brand in the target semantic category
11. Update the brand manifest with the resulting collection IDs and any approved non-obvious override notes. Create local extension or registry exports only when explicitly requested.

## Why This Route

- Semantic extensions in this file are true Figma extension collections, not separate hand-built collections that merely reuse the same names.
- The extension override state is attached to the base semantic variables and keyed by the base variable IDs.
- This route matches the current live extension collections in Foundations.

## Confirmed API Behaviors

- `extend()` must receive the extension name string.
  - `parentCollection.extend("Breckenridge")` works.
  - `parentCollection.extend()` fails validation.
- `valuesByModeForCollectionAsync()` expects the collection object, not a collection ID string.
- `figma_get_variables` can temporarily return stale cached data after a write, so plugin-runtime verification through `figma_execute` is the reliable source immediately after mutation.
- `extend(\"Brand\")` can create a duplicate brand extension if the write flow is retried mid-session, so duplicate checks must run before repo sync.
- `assets/logo`, when present in the base semantic theme collection, should be written as a direct string override such as `Mount Snow`, not as a variable alias.
- `extensionCollection.removeOverridesForVariable(baseVariable)` removes a redundant same-target override cleanly when the extension should inherit from the base value.
- Same-target overrides are invalid write state. Tokens must inherit from the base semantic value instead of overriding to the same alias or literal value.

## Minimal Verification Checklist

- Parent collection ID is correct.
- Extension collection exists and `isExtension` is true.
- Extension mode ID is captured from `extensionCollection.modes[0].modeId`.
- `variableOverrides` contains the expected base semantic variable IDs.
- At least one representative base variable resolves to the expected brand raw token through `valuesByModeForCollectionAsync(extensionCollection)`.
- No override entry remains when the extension value matches the base semantic value.
- If `assets/logo` exists, it resolves to the brand display name string rather than `Agnostic`.
- No duplicate extension collection exists for the same brand and semantic parent.
- The brand manifest is updated if live collection IDs changed, and any optional local exports requested for the task are regenerated before ending the task.
