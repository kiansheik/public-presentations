# ENAPOL Synthesis, Tree, And QR Revision

## Goal

Make the next ENAPOL revision directly on `main` by comparing the current focused rewrite with the previous PR version, recovering the useful bootstrapping/regression and QR material, keeping the Araújo example concise, adding a tree visualization, and preserving a 10-minute deck.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `git show 297405c:decks/enapol-2026-executable-grammar.md`
- `git show 297405c:notes/enapol-2026-executable-grammar.md`
- `git show 297405c:styles/enapol-2026-executable-grammar.css`
- `/Users/kian/code/nhe-enga/README.md`
- `/Users/kian/code/nhe-enga/test_pydicate.py`
- `/Users/kian/code/oldtupicorpus/AGENTS.md`
- `/Users/kian/code/oldtupicorpus/CLAUDE.md`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/araujo-line-tree.svg`
- `public/assets/enapol-2026-executable-grammar/qr-presentation.svg`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-26-enapol-synthesis-tree-qr.md`

## Commands Run

- `git log --oneline --decorate -n 10`
- `git status --short --branch`
- `git show 297405c:decks/enapol-2026-executable-grammar.md`
- `git show 297405c:notes/enapol-2026-executable-grammar.md`
- `git show 297405c:styles/enapol-2026-executable-grammar.css`
- `rg -n 'build_graphviz|Graphviz|graphviz' ...`
- `node -e "import('uqr')..."`
- `npm run build`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n 'ENAPOL 2026|enapol-2026-executable-grammar|Corpus Computacional' dist/index.html scripts/build-all.mjs README.md`
- `git diff --check`
- `npm run dev:enapol-2026 -- --port 3039`
- `curl -I http://localhost:3039/`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`

## What Worked

- The deck now has 10 generated ENAPOL slide modules and keeps the user-requested structure within the 9-10 slide bound.
- The explicit `zoom` language is gone from deck, notes, stylesheet, and generated modules.
- The old vertical-line background pattern is gone from the live ENAPOL CSS.
- The Araújo example remains central and now treats `orébe` as its own surface form with a deeper `oré + supé` analysis.
- The tree visualization appears as an SVG asset on its own slide.
- The bootstrapping/regression diagram appears after the example, with click states that expand into spell-out, validation, regression diff, branches, and the long-term correction point.
- The QR close is restored with a new presentation QR plus existing corpus, dictionary, and neologism QRs.
- `npm run build`, `git diff --check`, raw-marker checks, source stale-wording checks, `curl -I`, and both PDF exports passed.

## What Failed

- Starting Slidev inside the sandbox failed with `listen EPERM`; rerunning the same dev command with approved escalation succeeded at `http://localhost:3039/`.
- A no-screenshot DOM/browser check could not run because this checkout does not have the `playwright` package installed.
- A broad first `rg` over sibling repositories accidentally hit large bundled assets before being narrowed to source files.

## Remaining Questions

- Replace TODO SVG placeholders with real Anchieta/Gerardi/pydicate/Araújo screenshots or page crops before final publication.
- Decide whether to replace the hand-drawn Araújo tree with a generated Graphviz export once the exact corpus expression can be rendered cleanly.
- Confirm the final public URL for the presentation QR if the deck will be served somewhere other than GitHub Pages under `/public-presentations/enapol-2026-executable-grammar/`.

## Suggested Next Prompt

Review `http://localhost:3039/` slide by slide and tell the next agent which slide feels too dense, visually weak, or narratively out of order. If visual QA is needed, explicitly request screenshots so the repo instruction permits Playwright screenshot capture.
