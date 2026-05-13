# Agent Log

## 2026-05-13

- Converted the single-deck starter into a root-level multi-deck Slidev repo.
- Renamed `slides.md` to `oficina-tupi-antigo.md`.
- Added starter decks for `lingua-geral-brasil.md` and `anchieta-contexto.md`.
- Added `scripts/build-all.mjs` to clean `dist/` and build each deck into `dist/<slug>/` with per-deck base paths.
- Added GitHub Pages Actions deployment for generated `dist`.
- Added `.gitignore` for `node_modules/`, `dist/`, `.slidev/`, and logs.
- Added deck-specific and shared asset folders.
- Verified `npm run build`.
- Fixed `decks/oficina-unb.md` rendering so nested raw HTML blockquotes are not parsed as escaped code blocks.
- Added `decks/components/DeckImage.vue` and switched Oficina UnB manuscript images to it so local/dev/build URLs resolve from `public/assets/oficina-unb/`.
- Verified `npm run build` and browser-checked slide 3 at `http://localhost:3031/3`.
