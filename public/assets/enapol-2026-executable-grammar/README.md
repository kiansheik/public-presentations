# ENAPOL 2026 Asset Checklist

The deck uses logical asset names through `decks/components/EnapolImage.vue`.
Real `.png`, `.jpg`, or `.jpeg` assets take precedence over SVG placeholders.

## Current production visuals

- `anchietaSupe.png` — Anchieta passage used in the `çupê / supe / supé` comparison.
- `gerardiSupe.png` — Gerardi passage used in the same comparison.
- `araujoPaiNosso.png` — Araújo Padre Nosso crop used for the worked corpus line.
- `araujo-line-tree.svg` — generated pydicate tree for the worked Araújo line. Generate with `npm run generate:enapol-tree`; do not edit by hand.

The worked normalized line is:

`oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe`

The layered datative analysis used in the presentation is:

- surface: `orébe`
- grammatical analysis: `oré + supé`
- executable corpus definition: `orébe = (oré * supé).var(1)`

The canonical `supé` implementation lives in the `nhe-enga` pydicate package at:

`pydicate/pydicate/lang/tupilang/pos/postposition.py`

where `Dative` initializes the form `supé` with the definition `to, for, in favor of` and the tag `[POSTPOSITION:DATIVE]`.

## QR assets

Only the dictionary and neologism QR codes are shown on the final materials
slide. The presentation and corpus QR codes remain available here if the slide
is expanded again later.

- `qr-presentation.svg`: `https://kiansheik.github.io/public-presentations/enapol-2026-executable-grammar/`
- `qr-corpus.svg`: `https://github.com/kiansheik/oldtupicorpus`
- `qr-dictionary.svg`: `https://kiansheik.io/nhe-enga/`
- `qr-neo.svg`: `https://neo.academiatupi.com`

## Verification workflow

1. Run `npm run dev:enapol-2026 -- --port 3038` for local review.
2. Inspect the `supé` comparison, Araújo example, executable-analysis slide, regression flow, and final QR slide.
3. Run `npm run build`.
4. Optionally run `npm run export:enapol-2026:pdf` and `npm run export:enapol-2026:pdf:clicks`.
