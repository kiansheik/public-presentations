# ENAPOL Pydicate SVG And Morpheme Correction

## Goal

Apply the user's correction to the ENAPOL deck: stop treating `orébe` as an explicit/base morpheme, show the deeper pydicate/base-form analysis, make the executable code block more readable, add the main human-difficulty argument, and replace the hand-maintained tree asset with a generated SVG path.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `/Users/kian/code/oldtupicorpus/historic/araujo_catecismo_1686.tu.py`
- `/Users/kian/code/oldtupicorpus/historic/bettendorff_compendio.tu.py`
- `/Users/kian/code/oldtupicorpus/historic/lexicon.tu.py`
- `/Users/kian/code/nhe-enga/pydicate/pydicate/predicate.py`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `package.json`
- `scripts/generate-pydicate-tree-svg.py`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/araujo-line-tree.svg`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-26-enapol-pydicate-svg-correction.md`

## Commands Run

- `git status --short --branch`
- `rg -n "orébe|supé|Dificuldade principal|Não é automação" ...`
- `python3 -m py_compile scripts/generate-pydicate-tree-svg.py`
- `npm run generate:enapol-tree`
- `npm run build`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n "orebe-note|forma de superfície própria|orébe =|\+ orébe|supé \* oré|oré \* supé|Dificuldade principal|Não é automação" ...`
- `curl -I http://localhost:3039/`
- no-screenshot Chromium DOM checks on routes `/4`, `/5`, `/6`, and `/7`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`
- `git diff --check`

## What Worked

- Slide 4 now frames the main difficulty as human grammatical labor in Python/pydicate rather than NLP automation.
- Slide 5 no longer has the explicit standalone `orébe` note.
- Slide 6 now lists base morphemes, including `oré` and `supé`, and shows the formal structure with indentation and `(supé * oré).var(1)`.
- Slide 7 now describes the tree as preserving the base dative relation, with `supé * oré` generating the surface `orébe`.
- `scripts/generate-pydicate-tree-svg.py` imports the real `oldtupicorpus` Araújo module and emits the SVG tree from the pydicate object structure.
- Normal and click-expanded PDF exports were regenerated successfully.

## What Failed

- The first Chromium DOM pass only inspected the active root slide, so it did not see the later changed slides. Rerunning against routes `/4` through `/7` fixed the coverage issue.
- Chromium launch still needs escalation in this environment because the sandbox blocks macOS Chromium rendezvous permissions. No screenshots were taken.
- Both Slidev PDF export commands first failed inside the sandbox with `GetPortError`; rerunning them with approved escalation succeeded. The click-expanded export reported `Port 12445 is in use, trying another one...` and then completed.

## Remaining Questions

- Decide whether the generated SVG should later be moved upstream into `pydicate`/`nhe-enga` proper instead of living as a presentation helper script.
- Confirm whether the tree should follow `pydicate.to_forest_tree()` labels exactly or keep the current presentation-oriented surface/base labels.
- Replace remaining TODO visual placeholders with real archival screenshots/crops before final publication.

## Suggested Next Prompt

Review `http://localhost:3039/` and focus on slides 4-7: whether the difficulty slide sounds right aloud, whether the declarations/code/output grid is readable, and whether the generated tree uses the labels you want for the talk.
