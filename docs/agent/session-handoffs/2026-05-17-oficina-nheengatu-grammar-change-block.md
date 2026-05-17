# Handoff: Nheengatu Grammar Change Block

## Goal

Add the user's workshop-sized block after the Pai Nosso slide, framing Nheengatu as historical continuity through grammatical restructuring rather than a simple rupture from Tupi Antigo.

## Files Inspected

- `AGENTS.md`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `package.json`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-nheengatu-grammar-change-block.md`

## Commands Run

- `rg` and `sed` targeted reads over the deck, CSS, wiki, and memory registry.
- `npm run build`
- `git diff --check`
- `rg -n '<pre>' dist/oficina-unb/assets -g 'md-*.js'`
- `rg -n '<code>' dist/oficina-unb/assets -g 'md-*.js'`
- `node -e ...` generated-module count and title-presence check.
- `curl -I http://localhost:3033/`
- Headless Playwright DOM bounds check for slides 57-64.

## What Worked

- Appended eight new slides after the Pai Nosso comparison slide:
  - `Continuidade não significa imobilidade`
  - `Nem tudo desaparece: os estativos continuam`
  - `Subordinação antiga: perda do gerúndio`
  - `De n(a)-...-i para ti`
  - `De ne / -xûé para kurí`
  - `Menos fusão, mais palavras separadas`
  - `Indicativo II: perdido, mas fossilizado`
  - `O que mudou? O que ficou?`
- Added reusable `change-*` CSS for cards, example comparisons, key points, and the closing two-column synthesis.
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated-module checks find all eight new titles and no `<pre>` / `<code>` raw-HTML markers.
- Existing local review server responds at `http://localhost:3033/`.
- Corrected headless DOM bounds check reports slides 57-64 as `ok`.

## What Failed

- The first headless Chromium launch failed inside the sandbox because macOS process services were blocked; rerunning with approval outside the sandbox worked.
- The first DOM check outside the sandbox timed out because the selector expected one visible `.oficina-canvas`, while Slidev keeps all slide canvases in the DOM. A corrected indexed check passed.

## Remaining Questions

- The user may want some of the reserve slides from the longer 18-slide draft added later, especially prefix simplification, `ti` grammaticalization, nominal tense, reflexive/reciprocal reduction, and vowel-system reduction.
- The exact source formatting for examples can still be tightened if the bibliography style is standardized later.

## Suggested Next Prompt

Review slides 57-64 at `http://localhost:3033/` and tell Codex which reserve topics, if any, should be expanded into optional appendix slides.
