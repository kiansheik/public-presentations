# Current State

Last updated: 2026-05-13

This is a Slidev repository for public presentations. The active deck lives under `decks/`; older starter decks still live at the repository root.

Current decks:

- `decks/oficina-unb.md` is the active Oficina UnB deck and the only deck in the current build manifest.
- `oficina-tupi-antigo.md`
- `lingua-geral-brasil.md`
- `anchieta-contexto.md`

Shared presentation infrastructure:

- `decks/components/DeckImage.vue` renders Oficina UnB manuscript images as real `<img>` tags by importing files from `public/assets/oficina-unb/`. This avoids Slidev rewriting raw `/assets/...` or `../public/assets/...` paths in slide Markdown.
- `components/` contains reusable Vue slide components for the older root-level starter decks.
- `styles/custom.css` contains the shared visual language.
- `styles/oficina-unb.css` contains the Oficina UnB layout and positioning CSS.
- `public/assets/` is organized by deck slug plus `shared/`.
- `scripts/build-all.mjs` clears `dist/`, builds every deck into `dist/<slug>/`, and writes `dist/index.html`.
- `.github/workflows/deploy.yml` deploys the generated `dist` directory with GitHub Pages Actions.

Verified on 2026-05-13:

- `npm run build` succeeds for the current `oficina-unb` build manifest.
- `npm ci --dry-run` accepts the current `package.json` and `package-lock.json`.
- Generated deck assets use `/public-presentations/<deck>/` base paths by default.
- `dist/` and `node_modules/` are ignored by git.
- A local `oficina-tupi-antigo.md` dev server was started at `http://localhost:3030/` during the 2026-05-13 session.
- A fresh `oficina-unb` dev server was started at `http://localhost:3031/`.
- Browser verification on `http://localhost:3031/3` found zero escaped `<pre><code>` quote blocks, one rendered blockquote, and a loaded manuscript image with natural size `944x1432`.
