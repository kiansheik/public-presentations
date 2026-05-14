# 2026-05-13 README Project Guide Handoff

## Goal

Make `README.md` clear enough for future presentation projects: how to run commands, add decks, style decks, handle images, and understand the current Oficina UnB pattern.

## Files inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `README.md`
- `Makefile`
- `package.json`
- `scripts/build-all.mjs`

## Files changed

- `README.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-13-readme-project-guide.md`

## Commands run

- `sed -n ... docs/agent/index.md`
- `sed -n ... docs/agent/current-state.md`
- `sed -n ... docs/agent/repo-map.md`
- `sed -n ... docs/agent/open-questions.md`
- `sed -n ... README.md`
- `sed -n ... Makefile`
- `sed -n ... package.json`
- `sed -n ... scripts/build-all.mjs`
- `rg -n "DeckImage|decks/styles|styles/index|Adicionar decks|Imagens|Layout da Oficina" README.md docs/agent`
- `git diff -- README.md`

## What worked

- `README.md` now documents the command surface, current repo structure, deck/style conventions, image asset pitfalls, `DeckImage` usage, Oficina half-split layout conventions, and the checklist for adding future decks.
- The docs call out that shared deck CSS belongs in `decks/styles/index.css`, not in a deck-level scoped `<style>` tag.

## What failed

- Nothing failed. No build was run because this pass changed documentation only.

## Remaining questions

- Decide later whether `DeckImage.vue` should become a generic shared component for all future decks.
- Confirm whether root-level starter decks should stay documented once the repo fully standardizes on `decks/<slug>.md`.

## Suggested next prompt

Add a second real deck under `decks/<slug>.md` using the README checklist, then update `scripts/build-all.mjs` and verify the generated `dist/<slug>/` route.
