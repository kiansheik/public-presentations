# Repo Map

## Root Decks

- `decks/oficina-unb.md` is the active Oficina UnB deck and is built by `scripts/build-all.mjs`.
- `oficina-tupi-antigo.md` is the original starter deck, renamed from `slides.md`.
- `lingua-geral-brasil.md` is a starter deck for a later presentation on Língua Geral.
- `anchieta-contexto.md` is a starter deck for a later presentation on Anchieta and colonial writing.

Each deck imports shared CSS with:

```html
<style src="./styles/custom.css"></style>
```

## Shared UI

- `AGENTS.md` is the repo-local instruction file for future agents. It points agents to the wiki and forbids Playwright screenshots unless the user explicitly requests them.
- `decks/components/DeckImage.vue` renders Oficina UnB image assets from `public/assets/oficina-unb/` through `import.meta.glob`. Use it inside `decks/oficina-unb.md` instead of raw `<img src="../public/...">` or `<img src="/assets/...">`.
- `decks/styles/index.css` imports `../../styles/oficina-unb.css` as the global CSS entry for decks under `decks/`.
- `components/QuoteSlide.vue` renders a quote slide with source and optional note.
- `components/PersonBio.vue` renders a speaker/person profile slide.
- `components/ContextTimeline.vue` renders a simple timeline slide.
- `styles/custom.css` defines shared layout classes used by the decks.
- `styles/oficina-unb.css` defines the Oficina UnB slide canvas, manuscript positioning, and quote typography.
- `styles/oficina-unb.css` also owns the half-split layout variables `--oficina-left-*` and `--oficina-right-*`.

## Assets

- `public/assets/oficina-unb/`
- `public/assets/oficina-tupi-antigo/`
- `public/assets/lingua-geral-brasil/`
- `public/assets/anchieta-contexto/`
- `public/assets/shared/`

Use deck-specific folders for presentation-only assets and `shared/` for reusable maps, manuscripts, or images.

## Build And Deploy

- `README.md` documents the expected workflow for commands, deck structure, styling, image handling, and adding new decks.
- `package.json` exposes one dev command per deck.
- `scripts/build-all.mjs` is the deck manifest and build loop. It currently builds `decks/oficina-unb.md`.
- The build output is `dist/index.html` plus one folder per deck.
- `.github/workflows/deploy.yml` installs with `npm ci`, runs `npm run build`, uploads `dist`, and deploys Pages from Actions.

To add a deck:

1. Add `decks/<slug>.md`.
2. Add an asset folder under `public/assets/<slug>/` if needed.
3. Add the deck to the `decks` array in `scripts/build-all.mjs`.
4. Add a `dev:<name>` and export script in `package.json` if useful.
5. Update `README.md` and this map.
