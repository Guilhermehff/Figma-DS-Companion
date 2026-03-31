# Keystone Color Preview

Review state: written in figma. Verify live write state in `figma/brands/keystone/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Valencia`
  Provided value: `#e03c31`
  Usage scope: `primary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists HEX `#E03C31`, CMYK `0, 73, 78, 12`, RGB `224, 60, 49`, and PMS `179c`.

- Source color: `Curious Blue`
  Provided value: `#0066cc`
  Usage scope: `secondary brand palette`
  Channel restrictions: `not specified in source`
  Notes: Source image lists HEX `#0066CC`, CMYK `100, 50, 0, 20`, RGB `0, 102, 204`, and PMS `285c`.

- Source color: `Cool Grey`
  Provided value: `#4c5151`
  Usage scope: `tertiary palette and long-form copy support`
  Channel restrictions: `not specified in source`
  Notes: Source image lists HEX `#4C5151`, CMYK `6, 0, 0, 68`, RGB `76, 81, 81`, and PMS `425c`.

## Universal Reuse

- No exact Keystone source swatch reuses an existing universal color primitive in this pass.

## Proposed Families

### Family: valencia

Source anchor: `500_source`

<div>
  <span title="100 #fff4f1" style="display:inline-block;width:32px;height:32px;background:#fff4f1;border:1px solid #d1d5db;"></span>
  <span title="200 #ffe3dc" style="display:inline-block;width:32px;height:32px;background:#ffe3dc;border:1px solid #d1d5db;"></span>
  <span title="300 #ffac9e" style="display:inline-block;width:32px;height:32px;background:#ffac9e;border:1px solid #d1d5db;"></span>
  <span title="400 #ff8272" style="display:inline-block;width:32px;height:32px;background:#ff8272;border:1px solid #d1d5db;"></span>
  <span title="500 #e03c31" style="display:inline-block;width:32px;height:32px;background:#e03c31;border:1px solid #d1d5db;"></span>
  <span title="600 #c4493d" style="display:inline-block;width:32px;height:32px;background:#c4493d;border:1px solid #d1d5db;"></span>
  <span title="700 #9d352c" style="display:inline-block;width:32px;height:32px;background:#9d352c;border:1px solid #d1d5db;"></span>
  <span title="800 #752820" style="display:inline-block;width:32px;height:32px;background:#752820;border:1px solid #d1d5db;"></span>
  <span title="900 #2e100d" style="display:inline-block;width:32px;height:32px;background:#2e100d;border:1px solid #d1d5db;"></span>
</div>

### Family: curious_blue

Source anchor: `600_source`

<div>
  <span title="100 #f2f9ff" style="display:inline-block;width:32px;height:32px;background:#f2f9ff;border:1px solid #d1d5db;"></span>
  <span title="200 #e0f0ff" style="display:inline-block;width:32px;height:32px;background:#e0f0ff;border:1px solid #d1d5db;"></span>
  <span title="300 #a4cdff" style="display:inline-block;width:32px;height:32px;background:#a4cdff;border:1px solid #d1d5db;"></span>
  <span title="400 #82b4f6" style="display:inline-block;width:32px;height:32px;background:#82b4f6;border:1px solid #d1d5db;"></span>
  <span title="500 #6297de" style="display:inline-block;width:32px;height:32px;background:#6297de;border:1px solid #d1d5db;"></span>
  <span title="600 #0066cc" style="display:inline-block;width:32px;height:32px;background:#0066cc;border:1px solid #d1d5db;"></span>
  <span title="700 #2d568c" style="display:inline-block;width:32px;height:32px;background:#2d568c;border:1px solid #d1d5db;"></span>
  <span title="800 #1e3e66" style="display:inline-block;width:32px;height:32px;background:#1e3e66;border:1px solid #d1d5db;"></span>
  <span title="900 #091628" style="display:inline-block;width:32px;height:32px;background:#091628;border:1px solid #d1d5db;"></span>
</div>

### Family: cool_grey

Source anchor: `800_source`

<div>
  <span title="100 #fafbfb" style="display:inline-block;width:32px;height:32px;background:#fafbfb;border:1px solid #d1d5db;"></span>
  <span title="200 #f1f4f4" style="display:inline-block;width:32px;height:32px;background:#f1f4f4;border:1px solid #d1d5db;"></span>
  <span title="300 #c3cccc" style="display:inline-block;width:32px;height:32px;background:#c3cccc;border:1px solid #d1d5db;"></span>
  <span title="400 #abb7b7" style="display:inline-block;width:32px;height:32px;background:#abb7b7;border:1px solid #d1d5db;"></span>
  <span title="500 #94a1a1" style="display:inline-block;width:32px;height:32px;background:#94a1a1;border:1px solid #d1d5db;"></span>
  <span title="600 #7c8a8a" style="display:inline-block;width:32px;height:32px;background:#7c8a8a;border:1px solid #d1d5db;"></span>
  <span title="700 #657272" style="display:inline-block;width:32px;height:32px;background:#657272;border:1px solid #d1d5db;"></span>
  <span title="800 #4c5151" style="display:inline-block;width:32px;height:32px;background:#4c5151;border:1px solid #d1d5db;"></span>
  <span title="900 #1b1d1d" style="display:inline-block;width:32px;height:32px;background:#1b1d1d;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Valencia lands at `500` because the supplied source behaves as a bright mid-tone brand primary rather than a dark accent.
- Curious Blue lands at `600` because the source describes it as the standout CTA and information lane, not a pale support tint.
- Cool Grey lands at `800` because the supplied swatch is already dark enough for copy and recessive module use.
- The approved role-based write maps Cool Grey to the branded neutral lane only and retains no third expressive semantic lane.

## Review Readiness

- Subject: `Keystone accent slot order`
  Channels: `web, email, ads`
  Rule: Use Valencia as the primary accent lane and Curious Blue as the secondary accent lane.
  Source basis: Keystone color palette image labels `Primary` and `Secondary`.

- Subject: `Keystone Cool Grey semantic treatment`
  Channels: `web, email, ads`
  Rule: Keep Cool Grey in `neutral/*` only and do not promote a third expressive semantic lane.
  Source basis: User-approved review decision after preview.
