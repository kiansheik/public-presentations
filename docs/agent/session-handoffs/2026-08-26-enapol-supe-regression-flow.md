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
- `styles/enapol-2026-executable-grammar-refinement.css`
- `decks/styles/index.css`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `scripts/build-all.mjs`
- `package.json`
- related source repositories:
  - `kiansheik/nhe-enga/pydicate/pydicate/lang/tupilang/pos/postposition.py`
  - `kiansheik/oldtupicorpus/historic/lexicon.tu.py`
  - `kiansheik/oldtupicorpus/historic/araujo_catecismo_1686.tu.py`
  - `kiansheik/neologismotupi` commit history

## Source findings

- Canonical executable dative definition: `nhe-enga/pydicate/pydicate/lang/tupilang/pos/postposition.py`.
- `Dative` initializes `supé` with definition `to, for, in favor of` and tag `[POSTPOSITION:DATIVE]`; the module exports `supé = Dative()`.
- `oldtupicorpus/historic/lexicon.tu.py` defines `orébe = (oré * supé).var(1)` and `orébo = (oré * supé).var(0)`.
- The Araújo Padre Nosso expression in `historic/araujo_catecismo_1686.tu.py` uses the surface-oriented `orébe` object.
- `kiansheik/neologismotupi` has its initial commit on 2026-03-13, so the final slide can accurately describe it as an experiment open since March 2026.

## Files changed

- `decks/enapol-2026-executable-grammar.md`
  - Rewritten as a concise 10-slide narrative.
  - Removed vague/app-tour framing.
  - Added Anchieta/Gerardi/pydicate `supé` comparison.
  - Added layered `orébe` surface/function/deeper-analysis treatment.
  - Kept the Araújo source crop and executable tree.
  - Restored a central bootstrapping/regression-test flow after the worked example.
  - Added a fourth click on slide 8 with a synthesis box before the final accountability callout.
  - Added the FFLCH USP logo to the title slide using the Linguística FFLCH transparent PNG URL supplied by the user.
  - Expanded slide 10 into a public-output showcase with four QR codes plus selected live community statistics for the neologism dictionary.
- `styles/enapol-2026-executable-grammar-refinement.css`
  - Replaced overly bright comparison/code panels with dark, high-contrast panels.
  - Changed Anchieta/Gerardi image handling to contained aspect-ratio-aware frames.
  - Reduced and tightened the `supé` code font/padding.
  - Added title-logo positioning, slide-8 synthesis styling, compact QR cards, and the final-slide statistics grid.
- `decks/styles/index.css`
  - Imports the refinement stylesheet.
- `notes/enapol-2026-executable-grammar.md`
  - Updated rehearsal script to match the four-click methodology slide and public-output close.
- `public/assets/enapol-2026-executable-grammar/README.md`
  - Documents the now-used Anchieta/Gerardi/Araújo assets, `supé` source, `orébe` layering, and four QR assets.

## Commands / checks

The GitHub connector was used for repository reads/writes and PR updates.

A local clone/build was attempted again after the visual-feedback pass with:

`git clone --branch kian/enapol-supe-regression-flow --single-branch https://github.com/kiansheik/public-presentations.git`

but the execution container cannot resolve `github.com`, so `npm ci` / `npm run build` could not be run there.

The repository workflow was checked directly. `.github/workflows/deploy.yml` runs `npm ci` and `npm run build`, but only on pushes to `main` or manual `workflow_dispatch`; it does not currently run automatically for PR pushes. ENAPOL remains in `scripts/build-all.mjs`, so it remains linked from generated `dist/index.html` once built.

## What worked

- Branch created from exact latest `main` commit `c3586286f6d78c727ce51f8819519bb24e3db764`.
- Latest image commit was inspected and production images are referenced by their real logical names: `anchietaSupe`, `gerardiSupe`, `araujoPaiNosso`.
- The exact executable `supé` definition and `orébe` decomposition were grounded in source code rather than inferred.
- PR #2 remains open and mergeable after the follow-up visual-feedback commits.

## What failed / limitations

- Direct local `git clone` from the execution container fails because DNS/network access to GitHub is unavailable, so local `npm run build` cannot be executed there.
- The existing build workflow does not have a `pull_request` trigger, so no automatic Actions build is expected for this PR head.
- The FFLCH logo is currently referenced by its official remote PNG URL rather than vendored into the repository because the connector text-write path does not directly upload the supplied remote binary asset.
- The connector does not expose an append/patch operation for arbitrary text files, so the very large cumulative `docs/agent/current-state.md` and `docs/agent/log.md` were not safely rewritten just to append this session. This handoff records the state without truncating those files.

## Remaining questions

- Visual review of slides 1, 3, 4, 8, and 10 is useful before presenting, especially the remote FFLCH logo and the denser final statistics panel.
- The existing `qr-presentation.svg` targets the GitHub Pages deck URL; the slide text points to `kiansheik.io/public-presentations`. Both can remain if the custom site redirects/serves the same material, but the QR target could be regenerated later if desired.

## Suggested next prompt

Review the updated PR visually slide by slide, especially slides 1, 3, 4, 8, and 10, and make only surgical spacing/text-size fixes after seeing the rendered deck.
