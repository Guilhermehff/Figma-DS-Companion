# Boston Mills / Brandywine Color Preview

Review state: written in figma. Verify live write state in `figma/brands/boston_mills_brandywine/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Black`
  Provided value: `#000000`

## Universal Reuse

- Source color: `Black`
  Proposed token: `universal/black`
  Notes: Exact match.

## Live Semantic Mapping

- Scope: `neutral` -> `inherited_base`
  Exact black and white remain inherited from the shared neutral baseline.
- Scope: `brand` -> `universal/black`
  The supplied brand palette is monochrome, so the expressive lane aliases the shared universal black primitive.
- Scope: `brand_secondary` -> `universal/black`
  The supplied brand palette is monochrome, so the second expressive lane aliases the shared universal black primitive as well.
- `assets/logo` -> `Boston Mills / Brandywine`

## Review Readiness

- Subject: `Boston Mills / Brandywine monochrome mapping`
  Rule: Use `universal/black` for both expressive semantic lanes because the source only supplies exact black.
