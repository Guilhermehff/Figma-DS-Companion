# Decision Log

- Date: 2026-03-31
- Title: Park City neutral lane correction
- Status: accepted
- Scope: brand color foundations
- Brand (if brand-specific): park_city
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Foundations
- Stakeholders: design_system_governance, user-requested review pass
- Supersedes: figma/decisions/2026-03-18-park-city-foundations-written-to-figma.md (color neutral interpretation only)
- Superseded by:

## Context

Park City's original write absorbed `Pale Red`, `Cool Gray`, and `Park City Gray` into one neutral family, `park_city/park_city_gray/*`. In practice that made the semantic neutral lane pink at its lighter steps, because `surface/neutral/default` resolved to a value anchored on the supplied `Pale Red` swatch instead of a true neutral gray.

## Decision

Keep `park_city_gray` as the semantic neutral family, but correct the raw color model behind it.

- Redesign `park_city/park_city_gray/*` as a true gray ladder.
- Preserve `Cool Gray` exactly at `park_city/park_city_gray/400`.
- Preserve `Park City Gray` exactly at `park_city/park_city_gray/800`.
- Create a separate raw family, `park_city/pale_red/*`, and preserve `Pale Red` exactly at `park_city/pale_red/200`.
- Keep `pale_red/*` global-only in this pass; do not promote it into the semantic neutral role set.
- Leave `park_city_red/*` and `bright_red/*` as the primary and secondary expressive semantic lanes.

## Scope

- Affected collections:
  `_Global: Color`, `Semantic: Theme` extension `Park City`
- Affected tokens or artifact paths:
  `park_city/park_city_gray/*`
  `park_city/pale_red/*`
  `figma/brands/park_city/color/intake.yml`
  `figma/brands/park_city/color/preview.md`
  `figma/brands/park_city/brand.yml`
- Explicit exceptions:
  `pale_red/*` remains raw-only until a later accepted decision justifies semantic promotion.
- Inherited or deferred items:
  `park_city_red/*` and `bright_red/*` remain unchanged.
  Park City typography decisions from the superseded artifact remain in force.

## Consequences

Park City now has four raw color families instead of three. The semantic neutral role set still aliases `park_city_gray/*`, but those neutral tokens now resolve to a coherent gray ladder instead of a pink-to-gray composite. `Pale Red` remains available as a governed raw family for branded wash and proportion guidance usage without polluting neutral surfaces.

## Follow-up

- Update:
  Keep future Park City neutral changes on `park_city/park_city_gray/*` and preserve the `400` and `800` source anchors unless a newer decision explicitly changes them.
- Link from:
  `figma/brands/park_city/brand.yml`
- Verify:
  Confirm the Global Tokens documentation frame shows `4 ramps`, `44` tokens, `Pale Red -> park_city/pale_red/200`, and a separate `Pale Red` tokenized ramp.
