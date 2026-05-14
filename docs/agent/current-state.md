# Current State

Last updated: 2026-05-14

This is a Slidev repository for public presentations. The active deck lives under `decks/`; older starter decks still live at the repository root.

Current decks:

- `decks/oficina-unb.md` is the active Oficina UnB deck and the only deck in the current build manifest.
- `oficina-tupi-antigo.md`
- `lingua-geral-brasil.md`
- `anchieta-contexto.md`

Shared presentation infrastructure:

- `AGENTS.md` is the repo-local instruction file for future agents. It explicitly says not to take Playwright screenshots unless the user requests screenshots.
- `decks/components/DeckImage.vue` renders Oficina UnB manuscript images as real `<img>` tags by importing files from `public/assets/oficina-unb/`. This avoids Slidev rewriting raw `/assets/...` or `../public/assets/...` paths in slide Markdown.
- `decks/styles/index.css` is the active global Slidev style entry for the `decks/` user root and imports `styles/oficina-unb.css`. Do not rely on a deck-level `<style>` tag for shared Oficina CSS; Slidev scopes slide `<style>` tags by default.
- `components/` contains reusable Vue slide components for the older root-level starter decks.
- `styles/custom.css` contains the shared visual language.
- `styles/oficina-unb.css` contains the Oficina UnB layout and positioning CSS.
- `public/assets/` is organized by deck slug plus `shared/`.
- `scripts/build-all.mjs` clears `dist/`, builds every deck into `dist/<slug>/`, and writes `dist/index.html`.
- `.github/workflows/deploy.yml` deploys the generated `dist` directory with GitHub Pages Actions.
- `README.md` is the project-facing guide for commands, adding decks, styling decks under `decks/`, and handling image assets.

Verified on 2026-05-13:

- `npm run build` succeeds for the current `oficina-unb` build manifest.
- `npm ci --dry-run` accepts the current `package.json` and `package-lock.json`.
- Generated deck assets use `/public-presentations/<deck>/` base paths by default.
- `dist/` and `node_modules/` are ignored by git.
- A local `oficina-tupi-antigo.md` dev server was started at `http://localhost:3030/` during the 2026-05-13 session.
- A fresh `oficina-unb` dev server was started at `http://localhost:3031/`.
- Browser verification on `http://localhost:3031/3` found zero escaped `<pre><code>` quote blocks, one rendered blockquote, and a loaded manuscript image with natural size `944x1432`.
- Oficina content slides now use a consistent half-split frame: left text column ends around x=609 and right manuscript column starts around x=666 on a 1280px viewport.

Verified on 2026-05-14:

- Added five Brasil witness slides to `decks/oficina-unb.md` after the question slide: Anchieta title page, Anchieta biography/quote, Cardim biography/quote, Gabriel Soares biography/quote, and a convergence slide.
- Added `styles/oficina-unb.css` layout classes for the Brasil source, witness, quote-panel, and convergence slide variants.
- `npm run build` succeeds after the Brasil slide block.
- A static generated-bundle check found the new slide modules/classes and the `DeckImage` import for `anchieta-arte-grammatica.png`.
- Browser screenshot verification was not run for the new slides; future agents should avoid Playwright screenshots unless explicitly requested.
