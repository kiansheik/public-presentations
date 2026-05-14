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
- Moved Oficina CSS loading into `decks/styles/index.css` so Slidev applies it globally across split slide components.
- Normalized Oficina content slides to a half-split left text/right manuscript layout and fixed Seriph theme overrides on titles, blockquotes, and custom bullets.
- Re-verified with `npm run build`, browser measurements across slides 2-8, and screenshots for slides 3, 5, and 8.
- Expanded `README.md` into a project guide covering commands, repo structure, new deck setup, global style loading, image component conventions, and Oficina layout notes.

## 2026-05-14

- Added five Brasil witness slides to `decks/oficina-unb.md`: Anchieta title page, Anchieta, Cardim, Gabriel Soares de Sousa, and a convergence slide.
- Added Oficina CSS classes for Brasil source/witness/quote-panel/convergence layouts.
- Verified the deck with `npm run build` and static generated-bundle checks.
- Added root `AGENTS.md` and recorded that future agents should not take Playwright screenshots unless the user explicitly requests screenshots.
