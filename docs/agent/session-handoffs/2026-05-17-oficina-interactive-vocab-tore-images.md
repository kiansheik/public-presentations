# Oficina UnB Interactive Vocabulary And Toré Images

## Goal

Make `O Tupi que o Brasil já fala` interactive by clicking the existing word list to show inline dictionary definitions, then use the two supplied PDFs to replace right-side retomadas images and add more contemporary revitalization context.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `package.json`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `decks/components/DeckImage.vue`
- `public/assets/oficina-unb/README.md`
- `https://kiansheik.io/nhe-enga/` app assets through `curl`
- `/Users/kian/Downloads/A Língua Tupinambá nas músicas do Toré (1).pptx.pdf`
- `/Users/kian/Downloads/A Computational Grammar of Old Tupi (6).pdf`

## Files Changed

- `decks/oficina-unb.md`
- `decks/components/DeckImage.vue`
- `decks/components/TupiVocabularyLookup.vue`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `public/assets/oficina-unb/tore-nada-sem-nos.jpg`
- `public/assets/oficina-unb/tore-potiguara-revitalizacao.jpg`
- `public/assets/oficina-unb/tore-rorypaba.jpg`
- `public/assets/oficina-unb/tore-tupinamba-olivenca.jpg`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-interactive-vocab-tore-images.md`

## Commands Run

- `curl -fsS https://kiansheik.io/nhe-enga/docs/dict-conjugated.json.gz -o /private/tmp/nhe-enga-dict-conjugated.json.gz`
- local Node/zlib inspection of `/private/tmp/nhe-enga-dict-conjugated.json.gz`
- `file '/Users/kian/Downloads/A Língua Tupinambá nas músicas do Toré (1).pptx.pdf'`
- `file '/Users/kian/Downloads/A Computational Grammar of Old Tupi (6).pdf'`
- custom PDF DCT image extraction script under `/private/tmp`
- `cp /private/tmp/tore_dct/image-*.jpg public/assets/oficina-unb/...`
- `npm run build`
- `git diff --check`
- generated-module `rg` checks for `TupiVocabularyLookup`, `Entrada selecionada`, `Araújo da Silva`, and `tore-*.jpg`
- generated `<pre>/<code` checks against `dist/oficina-unb/assets/md-*.js`
- `curl -I http://localhost:3033/72`
- `curl -I http://localhost:3033/74`
- `curl -I http://localhost:3033/75`
- headless Playwright DOM click/image-load check on `http://localhost:3033/72` and `/74`; no screenshots

## What Worked

- The dictionary app publishes `dict-conjugated.json.gz`; extracting it locally made it possible to summarize the displayed entries without scraping the live UI at runtime.
- `TupiVocabularyLookup.vue` renders the existing vocabulary set as clickable buttons and updates the right-side definition panel in-place.
- The Toré PDF contains embedded DCT/JPEG images; extracting those streams avoided needing unavailable PDF image tools.
- `DeckImage.vue` now imports PNG, JPG, and JPEG assets, so the extracted Toré slides build correctly.
- The retomadas overview, Potiguara, and Tupinambá slides now use Toré-derived visuals and cite Araújo da Silva plus the computational grammar PDF sections.
- `npm run build` and `git diff --check` pass.
- The DOM interaction check confirmed that clicking `jacaré` updates the panel to include `îakaré` and `Jacaré`; the Potiguara Toré image loads with natural size `923x744`.
- A local Slidev server is running at `http://localhost:3033/`.

## What Failed

- `pypdf` and `PyPDF2` are not installed.
- `strings` did not expose useful searchable text from `A Computational Grammar of Old Tupi (6).pdf`.
- `pdfimages`, `pdftotext`, `magick`, `convert`, `mutool`, `pdfinfo`, and `pdftohtml` were unavailable in this environment.
- A Swift/PDFKit extraction attempt failed because of sandbox/module-cache and SDK/compiler issues.
- Starting Slidev inside the sandbox failed with `listen EPERM`; rerunning with approved escalation succeeded.
- The first headless Chromium launch failed in the sandbox with macOS Mach port permission errors; rerunning with approved escalation worked.
- The first Playwright image selector matched multiple preloaded Slidev pages; targeting the specific Potiguara image alt text fixed it.

## Remaining Questions

- The Potiguara slide currently uses the Toré song/translation image because it shows living language use. The extracted `tore-potiguara-revitalizacao.jpg` is documented and bundled but not displayed; it may be worth swapping in if the presenter wants the right side to show the explicit “protagonismo Potiguara” text instead.
- The dictionary definitions are static summaries from the 2026-05-17 dictionary data rather than live fetches inside Slidev. That keeps the deck offline-safe, but future dictionary updates will need a manual refresh.

## Suggested Next Prompt

Review slides 72-75 at `http://localhost:3033/` and decide whether Potiguara should show the Toré lyrics image or the explicit “A revitalização do Tupi e o protagonismo Potiguara” source slide.
