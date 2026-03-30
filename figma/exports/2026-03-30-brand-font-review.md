# Brand Font Review

Date: 2026-03-30

Repo source: `figma/brands/*/typography/intake.yml`.

Guideline source: `Vail Resorts Guidelines - Google Sheets.pdf`. The conflict notes below use the same sheet content from the matching CSV export because this shell environment does not have a PDF text extractor installed.

Repo parsing note: the following intake files currently contain invalid YAML for standard parsers because `Global: Typography` is unquoted in a plain scalar line:

- `afton_alps`
- `boston_mills_brandywine`
- `crotched`
- `hidden_valley_mo`
- `mad_river_mountain`
- `paoli_peaks`
- `roundtop_mountain`
- `snow_creek`
- `whitetail_resort`
- `wildcat_mountain`

## Vail

- Repo file: `figma/brands/vail/typography/intake.yml`
- Repo typography: `eyebrow` -> `Avenir` | `Avenir Black` | `Black`
- Repo typography: `headline` -> `Termina` | `Termina Black` | `Black`
- Repo typography: `subhead` -> `Avenir` | `Avenir Black` | `Black`
- Repo typography: `body` -> `Avenir` | `Avenir Medium` | `Medium`
- Repo typography: `cta` -> `Avenir` | `Avenir Black` | `Black`
- Guideline row: Headline `Termina Black`; Sub headline `Avenir Black`; Body `Avenir Medium`
- Guideline notes: Accesible through adobe only (Termina) (Avenir)
- Review note: No direct font conflict identified against the guideline row.

## Breckenridge

- Repo file: `figma/brands/breckenridge/typography/intake.yml`
- Repo typography: `headline` -> `Poppins` | `Poppins Bold` | `Bold`
- Repo typography: `subhead` -> `Poppins` | `Poppins Bold` | `Bold`
- Repo typography: `body` -> `Avenir Next` | `Avenir Next` | `not specified`
- Repo typography: `cta` -> `Poppins` | `Poppins Bold` | `Bold`
- Guideline row: Headline `Poppins Bold (H1) All caps`; Sub headline `Poppins Bold (H1) Sentence case`; Body `Avenir Next`
- Guideline notes: Accesible through adobe only (Avenir Next)
- Review note: No direct font conflict identified against the guideline row.

## Crested Butte

- Repo file: `figma/brands/crested_butte/typography/intake.yml`
- Repo typography: `headline` -> `Gibson` | `Gibson Semibold` | `Semibold`
- Repo typography: `subhead` -> `Gibson` | `Gibson Semibold` | `Semibold`
- Repo typography: `body` -> `Gibson` | `Gibson Regular` | `Regular`
- Guideline row: Headline `Gibson semibold (lower case)`; Sub headline `Gibson semibold (all caps)`; Body `Gibson regular`
- Guideline notes: Accesible through adobe only
- Review note: No direct font conflict identified against the guideline row.

## Northstar

- Repo file: `figma/brands/northstar/typography/intake.yml`
- Repo typography: `headline` -> `New Order` | `New Order Medium` | `Medium`
- Repo typography: `subhead` -> `New Order` | `New Order Regular` | `Regular`
- Repo typography: `body` -> `New Order` | `New Order Regular` | `Regular`
- Guideline row: Headline `New Order Medium`; Sub headline `New Order Regular`; Body `New Order Regular`
- Guideline notes: Accesible through adobe only (New order)
- Review note: No direct font conflict identified against the guideline row.

## Heavenly

- Repo file: `figma/brands/heavenly/typography/intake.yml`
- Repo typography: `title` -> `Din Condensed` | `Din Condensed Bold` | `Bold`
- Repo typography: `headline` -> `Din Condensed` | `Din Condensed Light` | `Light`
- Repo typography: `subhead` -> `Brandon Grotesque` | `Brandon Grotesque Medium` | `Medium`
- Repo typography: `body` -> `Brandon Grotesque` | `Brandon Grotesque Regular` | `Regular`
- Guideline row: Headline `Din Condensed Bold (Titles) and Din Condensed Light (headlines)`; Sub headline `not listed`; Body `Brandon Grotesque Regular`
- Guideline notes: None
- Review note: No direct font conflict identified against the guideline row.

## Kirkwood

- Repo file: `figma/brands/kirkwood/typography/intake.yml`
- Repo typography: `title_or_small_type` -> `Futura` | `Futura Bold` | `Bold`
- Repo typography: `headline` -> `Trade Gothic Bold Condensed No. 20` | `Trade Gothic Bold Condensed No. 20` | `Bold`
- Repo typography: `body` -> `Avenir Next` | `Avenir Next Regular` | `Regular`
- Repo typography: `limited_space_emphasis` -> `Trade Gothic Condensed No. 18` | `Trade Gothic Condensed No. 18` | `Regular`
- Guideline row: Headline `Futura Bold`; Sub headline `not listed`; Body `Avenir Next Regular`
- Guideline notes: Accesible through adobe only (Futura) (Avenir Next)
- Review note: Conflict: the guideline row names Futura Bold as the headline family and Avenir Next Regular as the body family, while the repo makes Trade Gothic Bold Condensed No. 20 the main headline lane and moves Futura into a smaller support lane.

## Keystone

- Repo file: `figma/brands/keystone/typography/intake.yml`
- Repo typography: `headline` -> `Futura` | `Futura Bold` | `Bold`
- Repo typography: `subheadline` -> `Avenir` | `Avenir Medium` | `Medium`
- Repo typography: `body` -> `Avenir` | `Avenir Medium` | `Medium`
- Repo typography: `emphasized_body_copy` -> `Futura` | `Futura Bold` | `Bold`
- Repo typography: `cta` -> `Futura` | `Futura Bold` | `Bold`
- Guideline row: Headline `Futura Bold`; Sub headline `Avenir Medium`; Body `Avenir Medium`
- Guideline notes: Accesible through adobe only (Futura) (Avenir)
- Review note: No direct font conflict identified against the guideline row.

## Beaver Creek

- Repo file: `figma/brands/beaver_creek/typography/intake.yml`
- Repo typography: `headline` -> `IvyPresto Display` | `Thin` | `Thin`
- Repo typography: `subhead_or_cta` -> `Vinila Condensed` | `Bold` | `Bold`
- Repo typography: `body` -> `Vinila` | `Light` | `Light`
- Repo typography: `url` -> `Vinila Condensed` | `Light` | `Light`
- Guideline row: Headline `IvyPresto Display Thin`; Sub headline `Vinila Condensed Bold`; Body `Vinila Light`
- Guideline notes: Missing Font (Vinila)
- Review note: No direct font conflict identified against the guideline row.

## Mount Snow

- Repo file: `figma/brands/mount_snow/typography/intake.yml`
- Repo typography: `headline` -> `Vastago Grotesk` | `Heavy` | `Heavy`
- Repo typography: `subheadline` -> `Area Extended` | `Extra Bold` | `Extra Bold`
- Repo typography: `body` -> `Area Extended` | `Medium` | `Medium`
- Guideline row: Headline `Vastago Grotesk Heavy`; Sub headline `Area Extended Extra Bold`; Body `Area Extended Medium`
- Guideline notes: Accesible through adobe only (Area) Vastago Grotesk heavy (extensis)
- Review note: No direct font conflict identified against the guideline row.

## JFBB

- Repo file: `figma/brands/jfbb/typography/intake.yml`
- Repo typography: `headline` -> `Vista Sans NAR OTCE` | `Black` | `Black`
- Repo typography: `subheadline` -> `Vista Sans NAR OTCE` | `Bold` | `Bold`
- Repo typography: `body` -> `Vista Sans NAR OTCE` | `Book` | `Book`
- Guideline row: Headline `Vista Sans Nar Black`; Sub headline `Vista Sans Nar Bold`; Body `Vista Sans Nar Book`
- Guideline notes: Accesible through adobe only
- Review note: No direct font conflict identified against the guideline row.

## Park City

- Repo file: `figma/brands/park_city/typography/intake.yml`
- Repo typography: `headline` -> `Futura Std` | `Bold` | `Bold`
- Repo typography: `subhead` -> `Trade Gothic LT Std Bold Condensed No. 20` | `Bold Condensed No. 20` | `Bold`
- Repo typography: `body` -> `Futura Std` | `Light` | `Light`
- Repo typography: `cta` -> `Futura Std` | `Bold` | `Bold`
- Guideline row: Headline `Futura STD Bold`; Sub headline `Trade Gothic LT STD Bold Condensed NO.20`; Body `Futura STD Light`
- Guideline notes: Accesible through adobe only (Futura)
- Review note: No direct font conflict identified against the guideline row.

## Stevens Pass

- Repo file: `figma/brands/stevens_pass/typography/intake.yml`
- Repo typography: `headline` -> `Gibson` | `Bold` | `Bold`
- Repo typography: `subhead` -> `Gibson` | `Semi Bold` | `Semi Bold`
- Repo typography: `cta` -> `Gibson` | `Regular` | `Regular`
- Repo typography: `body` -> `Gibson` | `Medium, Regular, Light, and italic variants` | `Mixed`
- Guideline row: Headline `Gibson Bold`; Sub headline `Gibson Semi Bold`; Body `Gibson Medium`
- Guideline notes: Accesible through adobe only (Gibson)
- Review note: Conflict: the guideline row names Gibson Medium for body, while the repo broadens the body role to mixed Gibson variants and adds a separate CTA role.

## Whistler Blackcomb

- Repo file: `figma/brands/whistler_blackcomb/typography/intake.yml`
- Repo typography: `headline` -> `Proxima Nova` | `Black` | `Black`
- Repo typography: `eyebrow` -> `Proxima Nova` | `Black` | `Black`
- Repo typography: `subhead` -> `Proxima Nova` | `Bold` | `Bold`
- Repo typography: `body` -> `Proxima Nova` | `Regular` | `Regular`
- Repo typography: `action` -> `Proxima Nova` | `Bold` | `Bold`
- Guideline row: Headline `Proxima Nova Black`; Sub headline `Proxima Nova Bold`; Body `Proxima Nova Regular`
- Guideline notes: Accesible through adobe only (Proxima Nova)
- Review note: No direct font conflict identified against the guideline row.

## Afton Alps

- Repo file: `figma/brands/afton_alps/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Dela Gothic One Regular`; Sub headline `Chivo Bold`; Body `Chivo Regular`
- Guideline notes: Accesible through adobe only (both fonts)
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Dela Gothic One Regular, Chivo Bold, and Chivo Regular.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Alpine Valley

- Repo file: `figma/brands/alpine_valley/typography/intake.yml`
- Repo typography: `primary_header` -> `Prompt` | `Bold` | `Bold`
- Repo typography: `secondary_header` -> `Prompt` | `Bold` | `Bold`
- Repo typography: `body` -> `Prompt` | `Regular` | `Regular`
- Guideline row: Headline `Prompt Bold (H1)`; Sub headline `Prompt Bold (H2)`; Body `Prompt regular`
- Guideline notes: None
- Review note: No direct font conflict identified against the guideline row.

## Crotched

- Repo file: `figma/brands/crotched/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `not listed`; Sub headline `not listed`; Body `not listed`
- Guideline notes: Missing font guidelines
- Review note: No direct conflict. The guideline sheet also does not provide brand font guidance for this brand.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Hidden Valley MO

- Repo file: `figma/brands/hidden_valley_mo/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Altero Regular (all caps)`; Sub headline `Altero Outline (all caps)`; Body `Prompt Regular`
- Guideline notes: Found in extensis
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Altero Regular / Altero Outline / Prompt Regular.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Wildcat Mountain

- Repo file: `figma/brands/wildcat_mountain/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `not listed`; Sub headline `not listed`; Body `not listed`
- Guideline notes: Missing font guidelines
- Review note: No direct conflict. The guideline sheet also does not provide brand font guidance for this brand.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Whitetail Resort

- Repo file: `figma/brands/whitetail_resort/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Andes`; Sub headline `Andes`; Body `Andes`
- Guideline notes: Found in extensis
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Andes for headline, subheadline, and body.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Snow Creek

- Repo file: `figma/brands/snow_creek/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Prompt`; Sub headline `Prompt`; Body `Prompt`
- Guideline notes: None
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Prompt for headline, subheadline, and body.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Roundtop Mountain

- Repo file: `figma/brands/roundtop_mountain/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Rhode Semibold Normal`; Sub headline `Rhode Semibold Normal`; Body `Antique Olive`
- Guideline notes: Rhode: Found in Extensis Antique Olive: Accesible through adobe
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Rhode Semibold Normal / Rhode Semibold Normal / Antique Olive.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Paoli Peaks

- Repo file: `figma/brands/paoli_peaks/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Rockwell Nova Extra bold`; Sub headline `Rockwell Nova`; Body `not listed`
- Guideline notes: Rockwell.Found in Extensis
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Rockwell Nova Extra Bold and Rockwell Nova.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Mad River Mountain

- Repo file: `figma/brands/mad_river_mountain/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Prompt`; Sub headline `Prompt`; Body `Prompt`
- Guideline notes: None
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Prompt for headline, subheadline, and body.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Boston Mills / Brandywine

- Repo file: `figma/brands/boston_mills_brandywine/typography/intake.yml`
- Repo typography: inherits universal baseline; no brand-specific `source_roles` are recorded.
- Guideline row: Headline `Interstate Black (H1)`; Sub headline `Insterstate H2`; Body `Interstate Medium`
- Guideline notes: Accesible through adobe only
- Review note: Conflict: repo inherits the universal typography baseline, but the guideline row specifies Interstate Black / Interstate H2 / Interstate Medium.
- Repo file note: this intake currently fails a standard YAML parse and should be quoted/fixed before any automated typography audit relies on it.

## Seven Springs

- Repo file: `figma/brands/seven_springs/typography/intake.yml`
- Repo typography: `headline` -> `Hoss Sharp` | `Black` | `Black`
- Repo typography: `subhead` -> `Hoss Sharp` | `Bold` | `Bold`
- Repo typography: `body` -> `Hoss Sharp` | `Medium` | `Medium`
- Repo typography: `cta` -> `Hoss Sharp` | `Heavy` | `Heavy`
- Guideline row: Headline `Hoss Sharp Black`; Sub headline `Hoss Sharp Bold`; Body `Hoss Sharp Medium`
- Guideline notes: Accesible through adobe only (Hoss Sharp)
- Review note: Extension: core Hoss Sharp headline / subhead / body align, but the repo also adds a Heavy CTA lane beyond the three-font guideline row.

## Stowe

- Repo file: `figma/brands/stowe/typography/intake.yml`
- Repo typography: `headline` -> `Athena` | `Regular` | `Regular`
- Repo typography: `subhead` -> `Raleway` | `Bold` | `Bold`
- Repo typography: `body` -> `Raleway` | `Regular` | `Regular`
- Repo typography: `body_contrasting` -> `Raleway` | `Light` | `Light`
- Guideline row: Headline `Athena`; Sub headline `Raleway Bold`; Body `Raleway Bold`
- Guideline notes: Found in extensis (Athena) Raleway (google)
- Review note: Conflict: the guideline row lists Raleway Bold for both subheadline and body, while the repo uses Raleway Regular for body plus an extra light contrast lane.

## Mount Sunapee

- Repo file: `figma/brands/mount_sunapee/typography/intake.yml`
- Repo typography: `headline` -> `Graphik` | `Bold` | `Bold`
- Repo typography: `secondary_header` -> `Graphik` | `Regular` | `Regular`
- Repo typography: `body` -> `Graphik` | `Light` | `Light`
- Repo typography: `subheader` -> `Neutraface Text` | `Bold Italic` | `Bold Italic`
- Guideline row: Headline `Graphik Bold`; Sub headline `Graphik Regular`; Body `Graphik Light`
- Guideline notes: Found in extensis
- Review note: Extension: core Graphik roles align, but the repo also adds Neutraface Text Bold Italic as a subheader family that is not listed in the guideline row.

## Hunter

- Repo file: `figma/brands/hunter/typography/intake.yml`
- Repo typography: `headline` -> `Galano Grotesque` | `Bold` | `Bold`
- Repo typography: `subheadline` -> `Galano Grotesque` | `Semibold` | `Semibold`
- Repo typography: `body` -> `Galano Grotesque` | `Regular` | `Regular`
- Repo typography: `body_contrasting` -> `Galano Grotesque` | `Light` | `Light`
- Guideline row: Headline `Galano Grotesque Bold`; Sub headline `Galano Grotesque Semibold`; Body `Galano Grotesque Regular`
- Guideline notes: Missing font
- Review note: Extension: repo adds a Galano Grotesque Light contrast role beyond the Bold / Semibold / Regular trio in the guideline row.

## Liberty Mountain

- Repo file: `figma/brands/liberty_mountain/typography/intake.yml`
- Repo typography: `headline` -> `Brown` | `Brown Regular` | `Regular`
- Repo typography: `headline_alternate` -> `Brown` | `Brown Light` | `Light`
- Repo typography: `subheadline` -> `Brown` | `Brown Light` | `Light`
- Repo typography: `body` -> `Brown` | `Brown Light` | `Light`
- Repo typography: `alternate` -> `Sentinel Book` | `Sentinel Book` | `Book`
- Guideline row: Headline `Brown Regular`; Sub headline `Brown Light`; Body `Brown Regular`
- Guideline notes: Found name Brown LL (asking the client to confirm)
- Review note: Conflict: the guideline row uses Brown Regular / Brown Light / Brown Regular, while the repo stages body on Brown Light and adds Sentinel Book as an alternate family.

## Attitash

- Repo file: `figma/brands/attitash/typography/intake.yml`
- Repo typography: `headline` -> `Buenos Aires` | `Bold` | `Bold`
- Repo typography: `body` -> `Buenos Aires` | `Light` | `Light`
- Repo typography: `action` -> `Buenos Aires` | `Bold` | `Bold`
- Repo typography: `subhead` -> `Coordinates` | `Medium` | `Medium`
- Guideline row: Headline `Buenos Aires Bold`; Sub headline `not listed`; Body `Buenos Aires Light`
- Guideline notes: Found in extensis
- Review note: Extension: repo adds Coordinates Medium as a subhead family, but the guideline row only specifies Buenos Aires.

## Hidden Valley PA

- Repo file: `figma/brands/hidden_valley_pa/typography/intake.yml`
- Repo typography: `headline` -> `Roboto` | `Black` | `Black`
- Repo typography: `subhead` -> `Roboto` | `Black` | `Black`
- Repo typography: `body` -> `Roboto` | `Regular` | `Regular`
- Repo typography: `display` -> `Mrs Eaves XL Regular` | `Regular` | `Regular`
- Guideline row: Headline `Roboto Black (all caps)`; Sub headline `Roboto Black (all caps)`; Body `Roboto Regular`
- Guideline notes: None
- Review note: Extension: repo adds Mrs Eaves XL Regular as a display family, but the guideline row only lists the Roboto hierarchy.

## Laurel Mountain

- Repo file: `figma/brands/laurel_mountain/typography/intake.yml`
- Repo typography: `display_headline` -> `Niagara` | `Regular` | `Display`
- Repo typography: `digital_headline_alt` -> `Roboto` | `Black` | `Black`
- Repo typography: `subhead` -> `Roboto` | `Black` | `Black`
- Repo typography: `body` -> `Roboto` | `Regular` | `Regular`
- Guideline row: Headline `Roboto Black (all caps)`; Sub headline `Roboto Black (all caps)`; Body `Roboto Regular`
- Guideline notes: None
- Review note: Extension: repo adds Niagara as a display headline family, while the guideline row only lists the Roboto hierarchy.

## Mt. Brighton

- Repo file: `figma/brands/mt_brighton/typography/intake.yml`
- Repo typography: `headline` -> `Museo Slab` | `900` | `Black`
- Repo typography: `action` -> `Museo Slab` | `900` | `Black`
- Repo typography: `subhead` -> `Museo Sans` | `700` | `Bold`
- Repo typography: `utility` -> `Prompt` | `fallback` | `Utility`
- Guideline row: Headline `Museo Slab 900 (all caps)`; Sub headline `Museo Sans 700 (all caps)`; Body `not listed`
- Guideline notes: Found in extensis
- Review note: Extension: core roles align to Museo Slab 900 and Museo Sans 700, but the repo also adds Prompt as a utility family that is not listed in the guideline row.

## Wilmot

- Repo file: `figma/brands/wilmot/typography/intake.yml`
- Repo typography: `headline` -> `Museo Slab` | `700` | `Bold`
- Repo typography: `action` -> `Museo Slab` | `700` | `Bold`
- Repo typography: `subhead` -> `Museo Sans` | `700` | `Bold`
- Repo typography: `body` -> `Museo Sans` | `500` | `Medium`
- Repo typography: `utility` -> `Prompt` | `Bold / Regular` | `Utility`
- Guideline row: Headline `Museo Slab 900 (all caps)`; Sub headline `Museo Sans 700 (all caps)`; Body `not listed`
- Guideline notes: Found in extensis
- Review note: Conflict: the guideline row names Museo Slab 900 for headline, while the repo uses Museo Slab 700, adds Museo Sans 500 body, and adds a Prompt utility family.

## Guideline Rows Not Represented In The Repo

- `okemo`: the guideline sheet includes an `Okemo` row marked `Rebrand ongoing`, but there is no `okemo` brand in `figma/brands/registry.yml`.
