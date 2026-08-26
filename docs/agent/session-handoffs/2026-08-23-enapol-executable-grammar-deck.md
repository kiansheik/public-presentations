# ENAPOL 2026 Executable Grammar Deck

## Goal

Create a 10-minute ENAPOL presentation about Kian Arad Sheik's project `Corpus Computacional e Gramática Executável do Tupi Antigo`, using the repo's native Slidev structure and emphasizing executable grammar as a testable layer of linguistic description rather than an NLP-first project.

## Files inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `/Users/kian/.codex/attachments/3db734b5-7284-4131-9674-0bdcd0fc9fb5/pasted-text.txt`
- `package.json`
- `scripts/build-all.mjs`
- `README.md`
- `decks/oficina-unb.md`
- `decks/components/DeckImage.vue`
- `decks/styles/index.css`
- `styles/oficina-unb.css`
- `docs/agent/log.md`

## Files changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `decks/components/EnapolImage.vue`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/*.svg`
- `decks/styles/index.css`
- `scripts/build-all.mjs`
- `package.json`
- `README.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-23-enapol-executable-grammar-deck.md`

## Commands run

- `sed -n ...` on the agent docs, pasted brief, README, package/build files, deck/component/style files, and log.
- `git status --short --branch`
- `find decks -maxdepth 2 -type f | sort`
- `find public/assets -maxdepth 2 -type f | sort | sed -n '1,220p'`
- `mkdir -p public/assets/enapol-2026-executable-grammar`
- `npm run build`
- `git diff --check`
- `rg -n '<pre|<code|`pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n 'enapol-2026-executable-grammar.md__slidev_[0-9]+' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n 'Corpus Computacional|O corpus obriga|Descrição linguística em 2026' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `npm run dev:enapol-2026 -- --host 127.0.0.1 --port 3035`
- `npm run dev:enapol-2026 -- --port 3035`
- `curl -I http://localhost:3035/`
- `git diff --stat`

## What worked

- `npm run build` succeeds for both built decks.
- `git diff --check` succeeds.
- The generated ENAPOL deck has nine slide modules.
- The generated Markdown slide modules contain no `<pre>`, `<code>`, or `` `pre` `` markers.
- Local Slidev review is running at `http://localhost:3035/`.
- `curl -I http://localhost:3035/` returns `HTTP/1.1 200 OK`.

## What failed

- `npm run dev:enapol-2026 -- --host 127.0.0.1 --port 3035` failed because this Slidev version does not accept `--host`.
- `npm run dev:enapol-2026 -- --port 3035` failed inside the sandbox with `listen EPERM: operation not permitted ::1:3035`.
- The same `--port 3035` command succeeded after approved escalation.
- One broad generated-bundle `rg` check was too noisy because Slidev framework files naturally contain internal `innerHTML`/code-related strings; the check was narrowed to generated `md-*.js` slide modules.

## Remaining questions

- Replace SVG placeholders with real source-page crops and screenshots before final export.
- Choose the one concrete Araújo or Bettendorff corpus line and ensure the formal expression and generated output screenshots all refer to the same line.
- Confirm whether the branch should be renamed from current `enapol-kian` to the requested `kian/enapol-2026-executable-grammar-talk`.

## Suggested next prompt

Replace the ENAPOL placeholder assets with the real source screenshots and polish slide 5 around one concrete corpus line.
