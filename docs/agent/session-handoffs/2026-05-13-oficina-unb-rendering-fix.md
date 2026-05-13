# 2026-05-13 Oficina UnB Rendering Fix Handoff

## Goal

Fix `decks/oficina-unb.md` so slide 3 renders the quote as a real blockquote instead of escaped raw HTML, and so manuscript images load instead of pointing at broken paths.

## Files inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-13-multi-deck-slidev.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `package.json`
- `scripts/build-all.mjs`
- `README.md`
- `public/assets/oficina-unb/*`
- selected installed Slidev files under `node_modules/@slidev/cli` and `node_modules/@slidev/client`

## Files changed

- `decks/oficina-unb.md`
- `decks/components/DeckImage.vue`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-13-oficina-unb-rendering-fix.md`

## Commands run

- `sed -n ... docs/agent/*`
- `rg -n "A língua geral como requisito|Recopilación|recopilacion|doctrinas|oficina-unb" .`
- `find public -maxdepth 4 -type f`
- `rg -n "../public/assets|/public/assets|/assets/" ...`
- `sed -n ... decks/oficina-unb.md`
- `sed -n ... styles/oficina-unb.css`
- `sed -n ... package.json`
- `sed -n ... scripts/build-all.mjs`
- `npm run build`
- `curl -I http://localhost:3030/`
- `./node_modules/.bin/slidev decks/oficina-unb.md --port 3031`
- Headless Playwright check against `http://localhost:3031/3`

## What worked

- Removing blank lines between nested raw HTML blocks inside each `<section>` stopped Slidev/Markdown from treating the indented quote HTML as a code block.
- Raw `../public/assets/...`, `./assets/...`, and `/assets/...` image paths were not reliable in `decks/oficina-unb.md` because Slidev treats `decks/` as the user root and rewrites slide image URLs.
- `decks/components/DeckImage.vue` works: it imports files from `public/assets/oficina-unb/` with `import.meta.glob` and renders a real `<img>`.
- `npm run build` succeeds and emits hashed manuscript PNG assets.
- Browser verification on slide 3 found `preCount: 0`, `blockquoteCount: 1`, and the `recopilacion-1681-doctrinas.png` image loaded with natural size `944x1432`.

## What failed

- `./assets/...` paths failed build because Slidev tried to import them relative to the generated slide Markdown module.
- `/assets/...` paths failed build under the slide import guard.
- A deck-level `<script setup>` import made Vite emit images but did not expose variables inside the split per-slide components; dev rendered `src` as undefined.
- Starting Slidev inside the sandbox failed with `listen EPERM`; the dev server on port `3031` required escalation.
- Headless Chromium also required escalation because the sandbox blocked Chromium's macOS Mach port setup.

## Remaining questions

- Decide whether future decks under `decks/` should get a generic shared image component instead of the Oficina-specific `DeckImage.vue`.
- Consider cleaning up the stale server on `http://localhost:3030/` if it is no longer useful.

## Suggested next prompt

Continue polishing `decks/oficina-unb.md`; use `DeckImage` for manuscript PNGs and keep nested raw HTML blocks contiguous inside slide sections.
