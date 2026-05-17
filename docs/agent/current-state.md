# Current State

Last updated: 2026-05-16

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
- `.github/workflows/deploy.yml` is a build check only: it installs with `npm ci` and runs `npm run build`. It does not use `actions/configure-pages`, because that path requires the repository Pages source to be configured for GitHub Actions before it runs.
- `Makefile` exposes `make help`, `make build`, `make prepare-gh-pages`, `make deploy-gh-pages`, and `make push-gh-pages`. `deploy-gh-pages` builds, commits, and pushes the `.gh-pages` worktree to the configured Pages branch.
- `README.md` is the project-facing guide for commands, adding decks, styling decks under `decks/`, and handling image assets.

Verified on 2026-05-13:

- `npm run build` succeeds for the current `oficina-unb` build manifest.
- `npm ci --dry-run` accepts the current `package.json` and `package-lock.json`.
- Generated deck assets use `/public-presentations/<deck>/` base paths by default.
- `dist/`, `.gh-pages/`, and `node_modules/` are ignored by git.
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
- `make build` succeeds and wraps the same `npm run build` flow.
- `make help` prints the Makefile command index and deploy variables.

Verified on 2026-05-15:

- `.github/workflows/deploy.yml` was switched from Pages artifact deployment to a build-only workflow to avoid `actions/configure-pages@v5` failing when Pages is not already configured for GitHub Actions.
- Branch publishing remains available through `make deploy-gh-pages`; the repository Pages setting should publish from `gh-pages` branch root.
- Added a five-slide Anchieta grammar/use block to the end of `decks/oficina-unb.md`: title framing, regional variation, use as teacher, oral use/viva voz, and universal/local systematization.
- Added `styles/oficina-unb.css` classes for the Anchieta grammar block and right-side text screenshot placeholders.
- `npm run build` succeeds after the appended slides.
- A local Slidev server for review is running at `http://localhost:3032/` and returned `HTTP/1.1 200 OK`; no Playwright screenshots were taken.

Verified on 2026-05-16:

- Added a fourteen-slide Tupi Antigo corpus-definition block to `decks/oficina-unb.md` after the Brasil convergence slide and before the Anchieta grammar close-reading slides.
- The new block defines Tupi Antigo as a finite corpus designation and adds modular source fichas for Staden, Thevet, Léry, Gândavo, Gabriel Soares de Sousa, Cardim, Anchieta, Araújo, Figueira, the `Vocabulário na Língua Brasílica`, the Cartas dos Camarões, Bettendorff, and a central-corpus timeline.
- Added `styles/oficina-unb.css` classes for the corpus definition slide, two-column source fichas, terminology notes, footers, and timeline layout.
- `npm run build` succeeds after the corpus block.
- A static Slidev parser check reports 33 slides, with the new corpus block spanning slides 15-28; no Playwright screenshots were taken.
- Refined the first three content slides with a scoped `source-quote-block` style so source quotations have warmer color, a subtle dark backing, accent rule, and clearer spacing from source citations.
- `npm run build` succeeds after the opening quote contrast pass.
- The user's existing local Slidev server on port `3030` is reachable from this shell at `http://[::1]:3030/` and returns `HTTP/1.1 200 OK`; `127.0.0.1:3030` is not reachable because the process is listening on IPv6 loopback only. No Playwright screenshots were taken.
- Reworked the Quechua, Nahuatl, and Guarani case-study slides so source entries are no longer same-weight paragraphs: each now uses a `language-case-block` with a label, dated source rows, and a stronger takeaway/note style.
- `npm run build` succeeds after the language case-slide readability pass.
