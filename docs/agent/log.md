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
- Added Makefile targets for manual branch-based GitHub Pages deploy: `build`, `deploy-gh-pages`, and `push-gh-pages`.
- Documented the `.gh-pages` worktree deploy flow in `README.md`.
- Added `.gh-pages/` to `.gitignore`.
- Added `make help`, split no-push publishing into `make prepare-gh-pages`, and consolidated `make deploy-gh-pages` so it builds, commits, and pushes `gh-pages`.
- Updated the README Makefile docs to reflect the one-command branch deploy and deploy variable overrides.

## 2026-05-15

- Changed `.github/workflows/deploy.yml` from GitHub Pages artifact deployment to a build-only workflow, avoiding `actions/configure-pages@v5` when Pages is not configured for Actions.
- Kept branch publishing in `make deploy-gh-pages` and updated deploy docs to say GitHub Pages should serve from the `gh-pages` branch root.
- Appended five Anchieta grammar/use slides to `decks/oficina-unb.md` with right-side screenshot placeholders and speaker notes.
- Added Oficina CSS for the new grammar block, regional form lists, point labels, and placeholder text-shot frames.
- Verified with `npm run build`, a static generated-bundle title check, and `curl -I http://localhost:3032/`; started Slidev locally at `http://localhost:3032/`.

## 2026-05-16

- Inserted a fourteen-slide Tupi Antigo corpus-definition block into `decks/oficina-unb.md`, positioned after the Brasil convergence slide and before the Anchieta grammar slides.
- Defined Tupi Antigo as a finite corpus designation and added modular source fichas plus a central-corpus timeline.
- Added matching Oficina CSS for corpus definition, source-card, terminology-note, footer, and timeline layouts.
- Verified with `npm run build` and a static Slidev parser check showing 33 slides, with the corpus block on slides 15-28.
- Improved the opening quote-heavy source slides with scoped `source-quote-block` styling: warmer quote color, subtle dark backing, accent rule, tighter quote/source spacing, and softer citation color.
- Fixed the unclosed `<div>` in the Anchieta variation slide so the deck builds again with the new `apab.png` asset.
- Verified with `npm run build` and checked the user's existing `3030` Slidev server at `http://[::1]:3030/`; no Playwright screenshots were taken.
- Reworked the Quechua, Nahuatl, and Guarani case-study slides into clearer `language-case-block` layouts with dated source rows and separate takeaway/note styles.
- Verified the language case-slide readability pass with `npm run build` and `git diff --check`; no Playwright screenshots were taken.
