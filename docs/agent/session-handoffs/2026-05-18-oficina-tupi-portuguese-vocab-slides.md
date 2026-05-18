# 2026-05-18 Oficina Tupi Portuguese Vocabulary Slides

## Goal

Replace the end vocabulary section with the user's more accurate three-slide `O Tupi que o português já fala` sequence, using Portuguese word, Old Tupi form, historical meaning, and source example columns.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `decks/components/TupiVocabularyLookup.vue`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `decks/components/TupiVocabularyLookup.vue`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-tupi-portuguese-vocab-slides.md`

## Commands Run

- `rg -n "TupiVocabularyLookup|vocab-|retomada-vocab-grid|retomada-word-cloud|retomada-word-panel|O Tupi que o Brasil já fala|O Tupi que o português já fala" decks styles docs`
- `sed -n '2440,2595p' decks/oficina-unb.md`
- `sed -n '2595,2685p' decks/oficina-unb.md`
- `rg -n "tupi-word-table|vocab-|retomada-vocab|retomada-word" styles/oficina-unb.css`
- `git diff --check`
- `npm run build`
- `rg -n "O Tupi que o português já fala: ações|Do pilão à gíria|Crianças, capivaras e Potiguaras|mutirão|potyrõ|kunhataĩ|Potiguara" dist/oficina-unb/assets/md-*.js`
- `rg -n "TupiVocabularyLookup|O Tupi que o Brasil já fala|vocab-definition|Entrada selecionada" dist/oficina-unb/assets/md-*.js`
- `rg -n "<pre[[:space:]>]|<code[[:space:]>]" dist/oficina-unb/assets/md-*.js`
- `rg --files dist/oficina-unb/assets | rg '/md-.*\\.js$' | wc -l`
- `curl -I http://localhost:3033/80`
- Headless Playwright DOM bounds check for routes 80, 81, and 82; no screenshots were taken.

## What Worked

- The old single vocabulary slide was replaced by three table slides:
  - `O Tupi que o português já fala: ações`
  - `Do pilão à gíria`
  - `Crianças, capivaras e Potiguaras`
- The obsolete interactive component was removed.
- The generated deck now emits 88 slide modules.
- The new routes are 80-82, followed by the modern retomadas block starting on route 83.
- Final checks pass: build, diff whitespace check, generated content checks, raw HTML marker checks, stale interactive vocabulary checks, `curl -I`, and DOM overflow checks.

## What Failed

- The first headless browser run failed under the macOS sandbox with Chromium Mach port permission errors; rerunning with approved escalation worked.
- The first DOM layout pass found horizontal table overflow on routes 80-82. The fix was to allow table cell/source wrapping and constrain table max width.

## Remaining Questions

- None for this pass. The slides are source-backed from the user-provided content, but they have not been visually reviewed by the user in the browser.

## Suggested Next Prompt

Review `http://localhost:3033/80`, `/81`, and `/82` and ask for any wording, density, or visual hierarchy changes to the vocabulary tables.
