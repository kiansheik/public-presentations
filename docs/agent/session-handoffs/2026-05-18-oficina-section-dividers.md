# Oficina UnB Section Dividers

## Goal

Summarize the major sections of `decks/oficina-unb.md` and add division/transition slides to improve pacing through the long workshop deck.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/.codex/memories/MEMORY.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-section-dividers.md`

## Commands Run

- `nl -ba /Users/kian/.codex/memories/MEMORY.md | sed -n '1,110p'`
- `cat docs/agent/index.md`
- `cat docs/agent/current-state.md`
- `cat docs/agent/repo-map.md`
- `cat docs/agent/open-questions.md`
- `rg -n "^---$|<h1|class=\"oficina-canvas|section-label|change-section-label|retomada-section-label|ms1089-section-label" decks/oficina-unb.md`
- `git diff --check`
- `npm run build`
- `rg --files dist/oficina-unb/assets | rg '/md-.*\\.js$' | wc -l`
- generated-module `rg` checks for roadmap/divider titles
- generated `<pre>/<code` checks against `dist/oficina-unb/assets/md-*.js`
- `curl -I http://localhost:3033/2`
- headless Playwright DOM overflow check on slides 2, 3, 12, 32, 38, 61, 69, and 79; no screenshots

## What Worked

- Added one seven-part roadmap slide after the title slide: `Roteiro da oficina`.
- Added seven divider slides at the major conceptual turns:
  - Parte 1: `Línguas gerais como categoria colonial`
  - Parte 2: `Da costa do Brasil ao corpus de Tupi Antigo`
  - Parte 3: `Anchieta entre regra, uso e variação`
  - Parte 4: `Quando a língua muda de ecologia`
  - Parte 5: `Nomear a continuidade: Língua Geral e Nheengatu`
  - Parte 6: `Continuidade gramatical não é imobilidade`
  - Parte 7: `Patrimônio, ensino e retomadas atuais`
- Added reusable `section-map-*` and `section-divider-*` CSS in `styles/oficina-unb.css`.
- `npm run build` succeeds and emits 86 slide modules.
- Generated-output checks found all new section slides and no raw `<pre>/<code` leakage.
- DOM overflow checks passed for all new roadmap/divider slides.

## What Failed

- No implementation failures in this pass.

## Remaining Questions

- None from this pass.

## Suggested Next Prompt

Review the new pacing slides at `http://localhost:3033/2`, `/3`, `/12`, `/32`, `/38`, `/61`, `/69`, and `/79`, then tune any divider titles that feel too long in presentation mode.
