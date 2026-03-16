# Decision Log

- Date: 2026-03-13
- Title: Role-Based Semantic Color Model
- Status: accepted
- Scope: color governance
- Brand (if brand-specific):
- Figma file (if applicable): https://www.figma.com/design/70O01X6MWNKMpsLqIke99Q/Design-System?node-id=1-3&t=jagoUKe5gyKCbAbG-1
- Stakeholders: Design System Governance
- Supersedes:
  - figma/decisions/2026-03-11-initial-semantic-color-family-model.md
  - figma/decisions/2026-03-11-semantic-feedback-color-family-naming.md
- Superseded by:

## Context

The current color model is sufficient for the present ads and email exploration, but it risks becoming brittle when downstream channels need more explicit usage roles and state behavior.

The main pressure point is not raw color availability. The Design System file already supports brand-specific global ramps. The pressure point is how downstream channels consume those ramps safely and consistently.

Ads and email are the current drivers, and both can work well with a stable background and foreground role system. Future web work is expected to need richer interaction behavior, but those channel-specific states should not force semantic color naming to become component-specific or state-specific.

Reviewing other systems suggests a consistent pattern:

- Atlassian uses semantic color tokens named by property, role, emphasis, and state, which keeps channels from depending on raw palette positions.
- Material 3 uses explicit paired roles such as `primary` and `onPrimary`, plus structured surface roles.
- Fluent 2 and Carbon treat neutral as a structural surface system rather than as a muted branch of brand.
- Apple platform semantic colors rely on paired foreground and background intent rather than fixed shade references.

This decision is now active governance for semantic color.

## Decision

Downstream color model:

`Global -> Semantic -> Channel`

In this model, `Semantic: Color` becomes the shared role-based contract for downstream channels. No separate palette-semantic collection is proposed.

Rules in this proposed model:

1. `_Global: Color` remains the raw source for universal and brand-specific ramps.
2. `Semantic: Color` becomes role-based rather than palette-step-based.
3. Semantic color tokens must remain channel-agnostic and avoid direct state names such as `hover` and `pressed`.
4. Semantic color tokens should define explicit background and readable foreground pairings.
5. Channel collections should use usage-first naming for actual places of use and should be grouped by applied property such as background, text, icon, and border.
6. Web states should map to stronger semantic emphasis levels instead of introducing interaction state names into semantic.
7. If a role is only useful in one channel, keep it in that channel layer rather than promoting it to semantic.
8. The shared expressive brand lanes should be reduced from three to two: `brand` and `brand_secondary`.
9. The current live `brand_tertiary/*` lane should be treated as a migration concern, not as part of the future target model.
10. Shared status lanes should be available in semantic for positive, warning, and critical messaging.

### Proposed Semantic Groups

- `surface/*` for background-like fills
- `on_surface/*` for readable foregrounds paired to a surface role
- `foreground/*` for standalone foreground roles not tied to one paired surface
- `border/*` for standalone border roles

By default, `foreground/*` should cover both text and icons when they share the same visual hierarchy. If a future channel needs icon-specific divergence, that should be introduced later as an explicit addition rather than assumed now.

### Proposed Neutral Surface Scale

Neutral should behave as a structural surface system, not as a muted brand scale.

- `canvas`
- `subtle`
- `default`
- `strong`
- `emphasis`
- `inverse`

Working intent for each step:

- `canvas`: the lightest or base neutral surface
- `subtle`: a lightly separated neutral surface
- `default`: the standard neutral container or module surface
- `strong`: a stronger neutral separation level
- `emphasis`: the highest neutral emphasis level before inversion
- `inverse`: the dark or inverted neutral surface

### Proposed Brand Emphasis Scale

The working five-step brand emphasis scale is:

- `muted`
- `subtle`
- `default`
- `strong`
- `emphasis`

Working intent for each step:

- `muted`: the quietest branded wash
- `subtle`: a light but intentional brand emphasis surface
- `default`: the standard brand expression
- `strong`: elevated brand emphasis
- `emphasis`: the highest approved brand emphasis level in the shared semantic system

### Proposed Status Scale

Status roles should remain functional and shared across brands. The working scale is:

- `subtle`
- `default`
- `strong`
- `emphasis`

Working intent for each step:

- `subtle`: light status fill for informational or supportive messaging
- `default`: standard status surface
- `strong`: elevated status emphasis
- `emphasis`: highest shared status emphasis level

### Proposed Semantic Inventory

```yaml
Semantic: Color
  surface/neutral/canvas
  on_surface/neutral/canvas

  surface/neutral/subtle
  on_surface/neutral/subtle

  surface/neutral/default
  on_surface/neutral/default

  surface/neutral/strong
  on_surface/neutral/strong

  surface/neutral/emphasis
  on_surface/neutral/emphasis

  surface/neutral/inverse
  on_surface/neutral/inverse

  surface/brand/muted
  on_surface/brand/muted

  surface/brand/subtle
  on_surface/brand/subtle

  surface/brand/default
  on_surface/brand/default

  surface/brand/strong
  on_surface/brand/strong

  surface/brand/emphasis
  on_surface/brand/emphasis

  surface/brand_secondary/muted
  on_surface/brand_secondary/muted

  surface/brand_secondary/subtle
  on_surface/brand_secondary/subtle

  surface/brand_secondary/default
  on_surface/brand_secondary/default

  surface/brand_secondary/strong
  on_surface/brand_secondary/strong

  surface/brand_secondary/emphasis
  on_surface/brand_secondary/emphasis

  surface/positive/subtle
  on_surface/positive/subtle

  surface/positive/default
  on_surface/positive/default

  surface/positive/strong
  on_surface/positive/strong

  surface/positive/emphasis
  on_surface/positive/emphasis

  surface/warning/subtle
  on_surface/warning/subtle

  surface/warning/default
  on_surface/warning/default

  surface/warning/strong
  on_surface/warning/strong

  surface/warning/emphasis
  on_surface/warning/emphasis

  surface/critical/subtle
  on_surface/critical/subtle

  surface/critical/default
  on_surface/critical/default

  surface/critical/strong
  on_surface/critical/strong

  surface/critical/emphasis
  on_surface/critical/emphasis

  foreground/default
  foreground/subtle
  foreground/inverse
  foreground/brand
  foreground/brand_secondary
  foreground/positive
  foreground/warning
  foreground/critical

  border/default
  border/subtle
  border/brand
  border/brand_secondary
  border/positive
  border/warning
  border/critical
```

### Example Shared Status Mapping

These roles are intended to stay on the shared semantic base rather than vary by brand unless a later decision explicitly allows it.

```yaml
Semantic: Color / shared base
  surface/positive/subtle -> universal/green/50
  on_surface/positive/subtle -> universal/green/900
  surface/positive/default -> universal/green/100
  on_surface/positive/default -> universal/green/900
  surface/positive/strong -> universal/green/700
  on_surface/positive/strong -> universal/white
  surface/positive/emphasis -> universal/green/800
  on_surface/positive/emphasis -> universal/white

  surface/warning/subtle -> universal/yellow/50
  on_surface/warning/subtle -> universal/yellow/900
  surface/warning/default -> universal/yellow/100
  on_surface/warning/default -> universal/yellow/900
  surface/warning/strong -> universal/yellow/700
  on_surface/warning/strong -> universal/black
  surface/warning/emphasis -> universal/yellow/800
  on_surface/warning/emphasis -> universal/black

  surface/critical/subtle -> universal/red/50
  on_surface/critical/subtle -> universal/red/900
  surface/critical/default -> universal/red/100
  on_surface/critical/default -> universal/red/900
  surface/critical/strong -> universal/red/700
  on_surface/critical/strong -> universal/white
  surface/critical/emphasis -> universal/red/800
  on_surface/critical/emphasis -> universal/white

  foreground/positive -> universal/green/800
  foreground/warning -> universal/yellow/800
  foreground/critical -> universal/red/800

  border/positive -> universal/green/500
  border/warning -> universal/yellow/500
  border/critical -> universal/red/500
```

### Example Brand Mapping

These examples are illustrative only. They show structure, not approved final values.

Example: `Vail`

```yaml
Semantic: Color / Vail
  surface/neutral/canvas -> universal/white
  on_surface/neutral/canvas -> universal/slate/900

  surface/neutral/subtle -> universal/slate/50
  on_surface/neutral/subtle -> universal/slate/900

  surface/neutral/default -> universal/slate/100
  on_surface/neutral/default -> universal/slate/900

  surface/neutral/strong -> universal/slate/200
  on_surface/neutral/strong -> universal/slate/900

  surface/neutral/emphasis -> universal/slate/300
  on_surface/neutral/emphasis -> universal/slate/900

  surface/neutral/inverse -> universal/slate/900
  on_surface/neutral/inverse -> universal/white

  surface/brand/muted -> vail/digital_blue/50
  on_surface/brand/muted -> universal/black

  surface/brand/subtle -> vail/digital_blue/100
  on_surface/brand/subtle -> universal/black

  surface/brand/default -> vail/digital_blue/800
  on_surface/brand/default -> universal/white

  surface/brand/strong -> vail/digital_blue/900
  on_surface/brand/strong -> universal/white

  surface/brand/emphasis -> vail/navy/900
  on_surface/brand/emphasis -> universal/white

  surface/brand_secondary/muted -> vail/navy/50
  on_surface/brand_secondary/muted -> universal/black

  surface/brand_secondary/subtle -> vail/navy/100
  on_surface/brand_secondary/subtle -> universal/black

  surface/brand_secondary/default -> vail/navy/700
  on_surface/brand_secondary/default -> universal/white

  surface/brand_secondary/strong -> vail/navy/800
  on_surface/brand_secondary/strong -> universal/white

  surface/brand_secondary/emphasis -> vail/navy/900
  on_surface/brand_secondary/emphasis -> universal/white

  foreground/default -> universal/slate/900
  foreground/subtle -> universal/slate/700
  foreground/inverse -> universal/white
  foreground/brand -> vail/digital_blue/800
  foreground/brand_secondary -> vail/navy/800

  border/default -> universal/slate/300
  border/subtle -> universal/slate/200
  border/brand -> vail/digital_blue/500
  border/brand_secondary -> vail/navy/500

  # Status roles inherit from the shared base semantic mapping in this proposal.
```

Example: `Keystone`

```yaml
Semantic: Color / Keystone
  surface/neutral/canvas -> universal/white
  on_surface/neutral/canvas -> keystone/cool_grey/900

  surface/neutral/subtle -> keystone/cool_grey/50
  on_surface/neutral/subtle -> keystone/cool_grey/900

  surface/neutral/default -> keystone/cool_grey/100
  on_surface/neutral/default -> keystone/cool_grey/900

  surface/neutral/strong -> keystone/cool_grey/200
  on_surface/neutral/strong -> keystone/cool_grey/900

  surface/neutral/emphasis -> keystone/cool_grey/300
  on_surface/neutral/emphasis -> keystone/cool_grey/900

  surface/neutral/inverse -> keystone/cool_grey/900
  on_surface/neutral/inverse -> universal/white

  surface/brand/muted -> keystone/valencia/50
  on_surface/brand/muted -> universal/black

  surface/brand/subtle -> keystone/valencia/100
  on_surface/brand/subtle -> universal/black

  surface/brand/default -> keystone/valencia/500
  on_surface/brand/default -> universal/black

  surface/brand/strong -> keystone/valencia/600
  on_surface/brand/strong -> universal/black

  surface/brand/emphasis -> keystone/valencia/700
  on_surface/brand/emphasis -> universal/white

  surface/brand_secondary/muted -> keystone/curious_blue/50
  on_surface/brand_secondary/muted -> universal/black

  surface/brand_secondary/subtle -> keystone/curious_blue/100
  on_surface/brand_secondary/subtle -> universal/black

  surface/brand_secondary/default -> keystone/curious_blue/600
  on_surface/brand_secondary/default -> universal/white

  surface/brand_secondary/strong -> keystone/curious_blue/700
  on_surface/brand_secondary/strong -> universal/white

  surface/brand_secondary/emphasis -> keystone/curious_blue/800
  on_surface/brand_secondary/emphasis -> universal/white

  foreground/default -> keystone/cool_grey/900
  foreground/subtle -> keystone/cool_grey/700
  foreground/inverse -> universal/white
  foreground/brand -> keystone/valencia/600
  foreground/brand_secondary -> keystone/curious_blue/700

  border/default -> keystone/cool_grey/300
  border/subtle -> keystone/cool_grey/200
  border/brand -> keystone/valencia/500
  border/brand_secondary -> keystone/curious_blue/500

  # Status roles inherit from the shared base semantic mapping in this proposal.
```

### Example Channel Mapping

In the proposed channel model, tokens are split by applied property:

- `background/*`
- `text/*`
- `icon/*`
- `border/*`

This keeps the semantic layer abstract while making the channel layer read like actual usage.

Ads:

```yaml
Channel: Ads Color
  background/action/default -> surface/brand/default
  text/action/default -> on_surface/brand/default
  icon/action/default -> on_surface/brand/default

  background/promo/default -> surface/brand_secondary/default
  text/promo/default -> on_surface/brand_secondary/default
  icon/promo/default -> on_surface/brand_secondary/default

  background/panel/default -> surface/neutral/default
  text/panel/default -> on_surface/neutral/default
  icon/panel/default -> on_surface/neutral/default

  background/status/positive -> surface/positive/subtle
  text/status/positive -> on_surface/positive/subtle
  icon/status/positive -> on_surface/positive/subtle

  text/body/default -> foreground/default
  text/body/subtle -> foreground/subtle
  text/accent/default -> foreground/brand_secondary
  text/status/critical -> foreground/critical
  icon/body/default -> foreground/default
  icon/body/subtle -> foreground/subtle

  border/panel/default -> border/default
  border/status/critical -> border/critical
```

Email:

```yaml
Channel: Email Color
  background/action/default -> surface/brand/default
  text/action/default -> on_surface/brand/default
  icon/action/default -> on_surface/brand/default

  background/highlight/default -> surface/brand_secondary/subtle
  text/highlight/default -> on_surface/brand_secondary/subtle
  icon/highlight/default -> on_surface/brand_secondary/subtle

  background/canvas/default -> surface/neutral/canvas

  background/module/default -> surface/neutral/default
  text/module/default -> on_surface/neutral/default
  icon/module/default -> on_surface/neutral/default

  background/notice/warning -> surface/warning/subtle
  text/notice/warning -> on_surface/warning/subtle
  icon/notice/warning -> on_surface/warning/subtle

  text/body/default -> foreground/default
  text/body/subtle -> foreground/subtle
  text/link/default -> foreground/brand
  text/status/positive -> foreground/positive
  icon/body/default -> foreground/default

  border/module/default -> border/subtle
  border/notice/warning -> border/warning
```

Web:

```yaml
Channel: Web Color
  background/action/default -> surface/brand/default
  background/action/hover -> surface/brand/strong
  background/action/pressed -> surface/brand/emphasis

  text/action/default -> on_surface/brand/default
  text/action/hover -> on_surface/brand/strong
  text/action/pressed -> on_surface/brand/emphasis
  icon/action/default -> on_surface/brand/default
  icon/action/hover -> on_surface/brand/strong
  icon/action/pressed -> on_surface/brand/emphasis

  background/panel/brand -> surface/brand/subtle
  text/panel/brand -> on_surface/brand/subtle
  icon/panel/brand -> on_surface/brand/subtle

  background/badge/promo -> surface/brand_secondary/default
  text/badge/promo -> on_surface/brand_secondary/default
  icon/badge/promo -> on_surface/brand_secondary/default

  background/alert/critical -> surface/critical/subtle
  text/alert/critical -> on_surface/critical/subtle
  icon/alert/critical -> on_surface/critical/subtle

  text/body/default -> foreground/default
  text/body/subtle -> foreground/subtle
  text/link/default -> foreground/brand
  text/link/promo -> foreground/brand_secondary
  text/status/positive -> foreground/positive
  icon/body/default -> foreground/default
  icon/body/subtle -> foreground/subtle

  border/input/default -> border/default
  border/panel/subtle -> border/subtle
  border/accent/default -> border/brand
  border/alert/critical -> border/critical
```

## Scope

- Affected collections: `_Global: Color`, proposed role-based `Semantic: Color`, future `Channel: Ads Color`, future `Channel: Email Color`, future `Channel: Web Color`
- Affected tokens or artifact paths: proposed semantic tokens under `surface/*`, `on_surface/*`, `foreground/*`, and `border/*`; future taxonomy updates in `figma/config/variable-taxonomy.yml`
- Explicit exceptions: none in this proposal
- Inherited or deferred items: typography and dimensions are out of scope; web-only specialty tokens remain deferred until channel needs are reviewed

## Consequences

If adopted, the shared downstream color contract becomes role-first rather than palette-step-first.

Neutral becomes a structural surface system, starting from the lightest surface roles and moving toward stronger and inverse neutral surfaces.

Ads and email can consume the simpler `canvas`, `subtle`, and `default` neutral roles plus the lower-emphasis brand and status roles first, while web can later map `default`, `strong`, and `emphasis` brand roles to interaction states without naming those states in semantic.

Brand-specific differences such as contrast pairing, ramp placement, whether brand and brand-secondary land on different raw families, and whether the highest emphasis stays in the same family or shifts to another approved family are resolved once in semantic mapping instead of being guessed separately by each channel.

The proposal keeps reusable cross-channel visual meaning in semantic while letting the channel layer read like actual applied UI properties: background, text, icon, and border.

Trimming the expressive color lanes from three to two should reduce redundancy, but it also means the current live `brand_tertiary/*` lane will need an explicit migration and deprecation plan if this proposal is accepted.

## Follow-up

- Update: review this proposal; if accepted, update `figma/config/variable-taxonomy.yml` and create a concrete implementation plan before any Figma write
- Link from: none until the proposal is accepted
- Verify: test the proposed role inventory against at least two brands and real examples for ads, email, and planned web interactions before implementation
