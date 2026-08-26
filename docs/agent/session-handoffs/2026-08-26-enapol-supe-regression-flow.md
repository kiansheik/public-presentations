# ENAPOL 2026 supé / regression-flow handoff

## Goal

Refine the 10-minute ENAPOL 2026 deck so it briefly states the overall project, then focuses on one concrete research problem: representing historical surface forms as executable grammatical analyses that are cumulatively tested against the corpus.

## Files inspected

- `AGENTS.md`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `decks/styles/index.css`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `scripts/build-all.mjs`
- `package.json`
- related source repositories:
  - `kiansheik/nhe-enga/pydicate/pydicate/lang/tupilang/pos/postposition.py`
  - `kiansheik/oldtupicorpus/historic/lexicon.tu.py`
  - `kiansheik/oldtupicorpus/historic/araujo_catecismo_1686.tu.py`

## Source findings

- Canonical executable dative definition: `nhe-enga/pydicate/pydicate/lang/tupilang/pos/postposition.py`.
- `Dative` initializes `supé` with definition `to, for, in favor of` and tag `[POSTPOSITION:DATIVE]`; the module exports `supé = Dative()`.
- `oldtupicorpus/historic/lexicon.tu.py` defines `orébe = (oré * supé).var(1)` and `orébo = (oré * supé).var(0)`.
- The Araújo Padre Nosso expression in `historic/araujo_catecismo_1686.tu.py` uses the surface-oriented `orébe` object.

## Files changed

- `decks/enapol-2026-executable-grammar.md`
  - Rewritten as a concise 10-slide narrative.
  - Removed vague/app-tour framing.
  - Added Anchieta/Gerardi/pydicate `supé` comparison.
  - Added layered `orébe` surface/function/deeper-analysis treatment.
  - Kept the Araújo source crop and executable tree.
  - Restored a central bootstrapping/regression-test flow after the worked example.
  - Restored all four final QR cards.
- `styles/enapol-2026-executable-grammar-refinement.css`
  - Added scoped styles for comparison panels, code rendering, layered analysis, executable example, and four-card QR layout.
- `decks/styles/index.css`
  - Imports the refinement stylesheet.
- `notes/enapol-2026-executable-grammar.md`
  - Updated rehearsal script to match the 10-slide deck.
- `public/assets/enapol-2026-executable-grammar/README.md`
  - Documents the now-used Anchieta/Gerardi/Araújo assets, `supé` source, `orébe` layering, and four QR assets.

## Commands / checks

The GitHub connector was used for repository reads/writes and branch creation. Local clone/build execution was not available from the working container, so final build validation is delegated to the repository's existing GitHub Actions build check after the PR is opened.

The build entry point is `npm run build`, which runs `scripts/build-all.mjs`; ENAPOL remains in the deck manifest and therefore remains linked from generated `dist/index.html`.

## What worked

- Branch created from exact latest `main` commit `c3586286f6d78c727ce51f8819519bb24e3db764`.
- Latest image commit was inspected and production images are referenced by their real logical names: `anchietaSupe`, `gerardiSupe`, `araujoPaiNosso`.
- The exact executable `supé` definition and `orébe` decomposition were grounded in source code rather than inferred.

## What failed / limitations

- A direct local `git clone` from the container failed, so local `npm run build` could not be executed there.
- The connector does not expose an append/patch operation for arbitrary text files, so the very large cumulative `docs/agent/current-state.md` and `docs/agent/log.md` were not safely rewritten just to append this session. This handoff records the state without truncating those files.

## Remaining questions

- Visual review of the comparison and four-QR layouts after CI/build is still useful before presenting.
- The existing `qr-presentation.svg` targets the GitHub Pages deck URL; the slide text points to `kiansheik.io/public-presentations`. Both can remain if the custom site redirects/serves the same material, but the QR target could be regenerated later if desired.

## Suggested next prompt

Review the ENAPOL PR visually after CI, especially slides 4, 6, 7, 8, and 10, and make only surgical spacing/text-size fixes if needed.
