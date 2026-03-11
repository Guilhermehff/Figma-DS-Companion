# Semantic Extension Write Workflow

Date: 2026-03-11
Status: active
Figma URL: https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1

## Purpose

Use this route whenever a brand needs a Semantic extension collection in the Design System file.

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

8. Verify the extension through:
   - `extensionCollection.variableOverrides`
   - `await baseVariable.valuesByModeForCollectionAsync(extensionCollection)`
9. Write the resulting collection IDs and override inventories back into repo artifacts.

## Why This Route

- Semantic extensions in this file are true Figma extension collections, not separate hand-built collections that merely reuse the same names.
- The extension override state is attached to the base semantic variables and keyed by the base variable IDs.
- This route matches the already-working Vail and Breckenridge collections.

## Confirmed API Behaviors

- `extend()` must receive the extension name string.
  - `parentCollection.extend("Breckenridge")` works.
  - `parentCollection.extend()` fails validation.
- `valuesByModeForCollectionAsync()` expects the collection object, not a collection ID string.
- `figma_get_variables` can temporarily return stale cached data after a write, so plugin-runtime verification through `figma_execute` is the reliable source immediately after mutation.

## Minimal Verification Checklist

- Parent collection ID is correct.
- Extension collection exists and `isExtension` is true.
- Extension mode ID is captured from `extensionCollection.modes[0].modeId`.
- `variableOverrides` contains the expected base semantic variable IDs.
- At least one representative base variable resolves to the expected brand raw token through `valuesByModeForCollectionAsync(extensionCollection)`.
- Repo manifests and extension snapshots are updated before ending the task.
