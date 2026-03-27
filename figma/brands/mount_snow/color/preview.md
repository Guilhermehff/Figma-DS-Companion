# Mount Snow Color Preview

Review state: approved preview artifact. Verify live write state in `figma/brands/mount_snow/brand.yml` and Figma.

## Original Source Swatches

- Source color: `Bluebird Express`
  Provided value: `#0068ff`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `0 104 255`.

- Source color: `Somerset Blue`
  Provided value: `#0098ff`
  Usage scope: `secondary brand palette`
  Notes: Source image lists RGB `0 152 255`.

- Source color: `Whipped Cream`
  Provided value: `#fbf7f3`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `251 247 243`.

- Source color: `Rosy Cheeks`
  Provided value: `#ff79df`
  Usage scope: `secondary brand palette`
  Notes: Source image lists RGB `255 121 223`.

- Source color: `Heart Red`
  Provided value: `#ff0000`
  Usage scope: `primary brand palette`
  Notes: Source image lists RGB `255 0 0`.

- Source color: `Carinthia Rail`
  Provided value: `#000000`
  Usage scope: `secondary brand palette`
  Notes: Exact shared black.

## Universal Reuse

- `Carinthia Rail` reuses `universal/black`.

## Color Proportion Guidance

### Mount Snow Brand Work

- Intent: The primary Mount Snow palette must always be present. Secondary colors can support it but may never appear without the primary palette.
- Dominant palette:
  `Bluebird Express` -> `mount_snow/bluebird_express/600`
  `Whipped Cream` -> `mount_snow/whipped_cream/100`
  `Heart Red` -> `mount_snow/heart_red/500`
- Supporting palette:
  `Somerset Blue` -> `mount_snow/somerset_blue/500`
  `Rosy Cheeks` -> `mount_snow/rosy_cheeks/400`
  `Carinthia Rail` -> `universal/black`
- Notes: The usage page explicitly says secondary colors should never appear within work without the presence of the primary palette.

### Carinthia-Specific Work

- Intent: Carinthia-specific work uses a restricted three-color subset rather than the full Mount Snow palette.
- Dominant palette:
  `Carinthia Rail` -> `universal/black`
  `Whipped Cream` -> `mount_snow/whipped_cream/100`
  `Heart Red` -> `mount_snow/heart_red/500`
- Notes: The usage page explicitly says Carinthia work should use only `Carinthia Rail`, `Whipped Cream`, and `Heart Red`.

## Proposed Families

### Family: bluebird_express

Source anchor: `600_source`

Swatch strip:

<div>
  <span title="50 #edf6ff" style="display:inline-block;width:32px;height:32px;background:#edf6ff;border:1px solid #d1d5db;"></span>
  <span title="100 #daeaff" style="display:inline-block;width:32px;height:32px;background:#daeaff;border:1px solid #d1d5db;"></span>
  <span title="200 #b3d3ff" style="display:inline-block;width:32px;height:32px;background:#b3d3ff;border:1px solid #d1d5db;"></span>
  <span title="300 #8dbaff" style="display:inline-block;width:32px;height:32px;background:#8dbaff;border:1px solid #d1d5db;"></span>
  <span title="400 #66a1ff" style="display:inline-block;width:32px;height:32px;background:#66a1ff;border:1px solid #d1d5db;"></span>
  <span title="500 #3d86ff" style="display:inline-block;width:32px;height:32px;background:#3d86ff;border:1px solid #d1d5db;"></span>
  <span title="600 #0068ff" style="display:inline-block;width:32px;height:32px;background:#0068ff;border:1px solid #d1d5db;"></span>
  <span title="700 #004fbf" style="display:inline-block;width:32px;height:32px;background:#004fbf;border:1px solid #d1d5db;"></span>
  <span title="800 #003782" style="display:inline-block;width:32px;height:32px;background:#003782;border:1px solid #d1d5db;"></span>
  <span title="900 #00204b" style="display:inline-block;width:32px;height:32px;background:#00204b;border:1px solid #d1d5db;"></span>
  <span title="950 #001531" style="display:inline-block;width:32px;height:32px;background:#001531;border:1px solid #d1d5db;"></span>
</div>

### Family: heart_red

Source anchor: `500_source`

Swatch strip:

<div>
  <span title="50 #fff1ef" style="display:inline-block;width:32px;height:32px;background:#fff1ef;border:1px solid #d1d5db;"></span>
  <span title="100 #ffded8" style="display:inline-block;width:32px;height:32px;background:#ffded8;border:1px solid #d1d5db;"></span>
  <span title="200 #ffb8ab" style="display:inline-block;width:32px;height:32px;background:#ffb8ab;border:1px solid #d1d5db;"></span>
  <span title="300 #ff8f7e" style="display:inline-block;width:32px;height:32px;background:#ff8f7e;border:1px solid #d1d5db;"></span>
  <span title="400 #ff604e" style="display:inline-block;width:32px;height:32px;background:#ff604e;border:1px solid #d1d5db;"></span>
  <span title="500 #ff0000" style="display:inline-block;width:32px;height:32px;background:#ff0000;border:1px solid #d1d5db;"></span>
  <span title="600 #cc0000" style="display:inline-block;width:32px;height:32px;background:#cc0000;border:1px solid #d1d5db;"></span>
  <span title="700 #9c0000" style="display:inline-block;width:32px;height:32px;background:#9c0000;border:1px solid #d1d5db;"></span>
  <span title="800 #6e0000" style="display:inline-block;width:32px;height:32px;background:#6e0000;border:1px solid #d1d5db;"></span>
  <span title="900 #440000" style="display:inline-block;width:32px;height:32px;background:#440000;border:1px solid #d1d5db;"></span>
  <span title="950 #300000" style="display:inline-block;width:32px;height:32px;background:#300000;border:1px solid #d1d5db;"></span>
</div>

### Family: whipped_cream

Source anchor: `100_source`

Swatch strip:

<div>
  <span title="50 #fffdfa" style="display:inline-block;width:32px;height:32px;background:#fffdfa;border:1px solid #d1d5db;"></span>
  <span title="100 #fbf7f3" style="display:inline-block;width:32px;height:32px;background:#fbf7f3;border:1px solid #d1d5db;"></span>
  <span title="200 #ddd9d5" style="display:inline-block;width:32px;height:32px;background:#ddd9d5;border:1px solid #d1d5db;"></span>
  <span title="300 #c0bbb8" style="display:inline-block;width:32px;height:32px;background:#c0bbb8;border:1px solid #d1d5db;"></span>
  <span title="400 #a39f9b" style="display:inline-block;width:32px;height:32px;background:#a39f9b;border:1px solid #d1d5db;"></span>
  <span title="500 #888380" style="display:inline-block;width:32px;height:32px;background:#888380;border:1px solid #d1d5db;"></span>
  <span title="600 #6d6965" style="display:inline-block;width:32px;height:32px;background:#6d6965;border:1px solid #d1d5db;"></span>
  <span title="700 #544f4c" style="display:inline-block;width:32px;height:32px;background:#544f4c;border:1px solid #d1d5db;"></span>
  <span title="800 #3b3734" style="display:inline-block;width:32px;height:32px;background:#3b3734;border:1px solid #d1d5db;"></span>
  <span title="900 #25211d" style="display:inline-block;width:32px;height:32px;background:#25211d;border:1px solid #d1d5db;"></span>
  <span title="950 #1a1613" style="display:inline-block;width:32px;height:32px;background:#1a1613;border:1px solid #d1d5db;"></span>
</div>

### Family: somerset_blue

Source anchor: `500_source`

Swatch strip:

<div>
  <span title="50 #eef9ff" style="display:inline-block;width:32px;height:32px;background:#eef9ff;border:1px solid #d1d5db;"></span>
  <span title="100 #d9efff" style="display:inline-block;width:32px;height:32px;background:#d9efff;border:1px solid #d1d5db;"></span>
  <span title="200 #b0daff" style="display:inline-block;width:32px;height:32px;background:#b0daff;border:1px solid #d1d5db;"></span>
  <span title="300 #85c5ff" style="display:inline-block;width:32px;height:32px;background:#85c5ff;border:1px solid #d1d5db;"></span>
  <span title="400 #56afff" style="display:inline-block;width:32px;height:32px;background:#56afff;border:1px solid #d1d5db;"></span>
  <span title="500 #0098ff" style="display:inline-block;width:32px;height:32px;background:#0098ff;border:1px solid #d1d5db;"></span>
  <span title="600 #0079cb" style="display:inline-block;width:32px;height:32px;background:#0079cb;border:1px solid #d1d5db;"></span>
  <span title="700 #005b99" style="display:inline-block;width:32px;height:32px;background:#005b99;border:1px solid #d1d5db;"></span>
  <span title="800 #003f6b" style="display:inline-block;width:32px;height:32px;background:#003f6b;border:1px solid #d1d5db;"></span>
  <span title="900 #00253f" style="display:inline-block;width:32px;height:32px;background:#00253f;border:1px solid #d1d5db;"></span>
  <span title="950 #00192b" style="display:inline-block;width:32px;height:32px;background:#00192b;border:1px solid #d1d5db;"></span>
</div>

### Family: rosy_cheeks

Source anchor: `400_source`

Swatch strip:

<div>
  <span title="50 #fff3fc" style="display:inline-block;width:32px;height:32px;background:#fff3fc;border:1px solid #d1d5db;"></span>
  <span title="100 #ffe3f8" style="display:inline-block;width:32px;height:32px;background:#ffe3f8;border:1px solid #d1d5db;"></span>
  <span title="200 #ffc1f0" style="display:inline-block;width:32px;height:32px;background:#ffc1f0;border:1px solid #d1d5db;"></span>
  <span title="300 #ff9fe8" style="display:inline-block;width:32px;height:32px;background:#ff9fe8;border:1px solid #d1d5db;"></span>
  <span title="400 #ff79df" style="display:inline-block;width:32px;height:32px;background:#ff79df;border:1px solid #d1d5db;"></span>
  <span title="500 #d462b8" style="display:inline-block;width:32px;height:32px;background:#d462b8;border:1px solid #d1d5db;"></span>
  <span title="600 #ab4b93" style="display:inline-block;width:32px;height:32px;background:#ab4b93;border:1px solid #d1d5db;"></span>
  <span title="700 #84366f" style="display:inline-block;width:32px;height:32px;background:#84366f;border:1px solid #d1d5db;"></span>
  <span title="800 #5e214d" style="display:inline-block;width:32px;height:32px;background:#5e214d;border:1px solid #d1d5db;"></span>
  <span title="900 #3b0e2e" style="display:inline-block;width:32px;height:32px;background:#3b0e2e;border:1px solid #d1d5db;"></span>
  <span title="950 #2b061f" style="display:inline-block;width:32px;height:32px;background:#2b061f;border:1px solid #d1d5db;"></span>
</div>

## Review Notes

- Mount Snow stages on two semantic expressive lanes: `bluebird_express` and `heart_red`.
- `whipped_cream` drives the neutral surface system, while exact black is reused from `universal/black` rather than duplicated under the Mount Snow group.
- `somerset_blue` and `rosy_cheeks` remain governed global-only extra families after the first semantic pass.

## Proposed Semantic Mapping

- `surface/neutral/subtle`, `surface/neutral/default`, `surface/neutral/strong`, `surface/neutral/emphasis`, `border/default`, `border/subtle` -> `mount_snow/whipped_cream/*`
- `on_surface/neutral/*`, `foreground/default`, `assets/logo` -> `universal/black` or `Mount Snow` for the string logo variable
- `foreground/subtle` -> `mount_snow/whipped_cream/800`
- `surface/brand/*`, `on_surface/brand/*`, `foreground/brand`, `border/brand` -> `mount_snow/bluebird_express/*`
- `surface/brand_secondary/*`, `on_surface/brand_secondary/*`, `foreground/brand_secondary`, `border/brand_secondary` -> `mount_snow/heart_red/*`
- Global-only extra families: `mount_snow/somerset_blue/*`, `mount_snow/rosy_cheeks/*`

## Review Readiness

- Subject: `Mount Snow expressive lane order`
  Channels: `web, email, ads`
  Rule: Use Bluebird Express as the first expressive semantic lane and Heart Red as the second.
  Source basis: Source image marks both as `PRIMARY` brand colors.

- Subject: `Mount Snow neutral system`
  Channels: `web, email, ads`
  Rule: Use Whipped Cream for neutral surfaces and reuse exact shared black where the source calls for Carinthia Rail.
  Source basis: Source image explicitly supplies Whipped Cream and exact black.

- Subject: `Mount Snow secondary extras`
  Channels: `web, email, ads`
  Rule: Keep Somerset Blue and Rosy Cheeks global-only until a later review promotes another shared semantic lane.
  Source basis: Source image marks both as `SECONDARY`.
