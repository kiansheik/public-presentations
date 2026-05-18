# 2026-05-18 Oficina Concept Slide Polish

## Goal

Improve the CSS for the slide `Língua geral: não uma língua, mas uma categoria`, keeping the existing Markdown/HTML content but making the layout read clearly.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/.codex/memories/MEMORY.md`

## Files Changed

- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-concept-slide-polish.md`

## Commands Run

- `rg -n "concept-slide|concept-block|concept-question|concept-answer|Língua geral: não uma língua" decks/oficina-unb.md styles/oficina-unb.css`
- `sed -n '300,330p' decks/oficina-unb.md`
- `sed -n '860,1030p' styles/oficina-unb.css`
- `npm run build`
- `git diff --check`
- `curl -I http://localhost:3034/11`
- `rg -n "Língua geral: não uma língua|concept-block|concept-question|concept-answer|<pre>|<code" dist/oficina-unb/assets/md-*.js`
- `rg -n "<pre[[:space:]>]|<code[[:space:]>]|TupiVocabularyLookup|vocab-lookup" dist/oficina-unb/assets/md-*.js`
- `node -e '...'` Playwright DOM attempt for route `/11`

## What Worked

- The concept slide now uses two balanced question panels:
  - the rejected question is muted on the left;
  - the preferred category question is accented on the right;
  - the working definition spans both columns at the bottom.
- The slide keeps the deck's dark Oficina visual system, gold accent rail, and no inline per-slide CSS.
- `npm run build` and `git diff --check` pass.
- The generated slide module contains the expected concept-slide content and no raw `<pre>/<code` rendering.
- The local server route `http://localhost:3034/11` returns `200 OK`.

## What Failed

- A headless DOM bounds check could not run because `require("playwright")` fails with `MODULE_NOT_FOUND`; this checkout does not currently have the `playwright` package installed.

## Remaining Questions

- The slide has not been visually reviewed by the user in the browser after this CSS pass.

## Suggested Next Prompt

Review `http://localhost:3034/11` and ask for any spacing, emphasis, or typography adjustment on the concept slide.
