# ENAPOL 2026 Asset Checklist

The deck uses logical asset names through `decks/components/EnapolImage.vue`.
Save replacement screenshots or page crops in this folder with the same basename
as the SVG placeholder, preferably as `.png`. The component checks `.png`,
`.jpg`, `.jpeg`, and then `.svg`, so a file like
`TODO_araujo_or_bettendorff_short_line.png` automatically replaces the SVG
fallback without editing the deck.

Recommended capture rules:

- Crop to the useful page, passage, or app/code panel.
- Keep page numbers, headers, or titles visible when they help citation.
- Prefer legible page crops and syntax-highlighted code screenshots.
- Do not delete SVG placeholders until real assets are checked in.

## Current Required Visuals

### `TODO_anchieta_grammar_page_same_topic.png`

- Logical name: `TODO_anchieta_grammar_page_same_topic`
- Used on slide 3.
- Purpose: show the historical grammar side of the same phenomenon used in the talk.
- What to capture: an Anchieta 1595 page or passage on the selected grammatical topic.
- Status: TODO, SVG fallback present.

### `TODO_gerardi_tupinamba_page_same_topic.png`

- Logical name: `TODO_gerardi_tupinamba_page_same_topic`
- Used on slide 3.
- Purpose: show the modern descriptive grammar side of the same phenomenon.
- What to capture: Gerardi or another current Tupinambá/Tupi descriptive page on the same topic.
- Status: TODO, SVG fallback present.

### `TODO_pydicate_executable_grammar_screenshot.png`

- Logical name: `TODO_pydicate_executable_grammar_screenshot`
- Used on slide 3.
- Purpose: show the executable grammar as a third descriptive layer.
- What to capture: a clear pydicate/editor screenshot for the same topic.
- Status: TODO, SVG fallback present.

### `TODO_araujo_or_bettendorff_short_line.png`

- Logical name: `TODO_araujo_or_bettendorff_short_line`
- Used on slide 5.
- Purpose: anchor the talk in one concrete corpus line.
- Current worked line: `araujo_catecismo_1686:0007`, Araújo 1686, Livro I, Padre Nosso, p. 2, lines 1-2.
- Normalized current target: `oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe`.
- What to capture: the manuscript/scan crop for that line, or a comparable Araújo/Bettendorff line if the worked example changes.
- Status: TODO, SVG fallback present.

## Existing QR Assets

These are no longer part of the focused 8-slide deck, but remain available if a
later version adds a compact resources slide.

- `qr-dictionary.svg`: `https://kiansheik.io/nhe-enga/`
- `qr-corpus.svg`: `https://github.com/kiansheik/oldtupicorpus`
- `qr-neo.svg`: `https://neo.academiatupi.com`

## Replacement Workflow

1. Save the real crop/screenshot using the exact `.png` basename listed above.
2. Keep the SVG fallback in place.
3. Run `npm run dev:enapol-2026 -- --port 3037` and inspect slides 3 and 5.
4. Run `npm run build`.
5. Run `npm run export:enapol-2026:pdf` and, if using click exports, `npm run export:enapol-2026:pdf:clicks`.
