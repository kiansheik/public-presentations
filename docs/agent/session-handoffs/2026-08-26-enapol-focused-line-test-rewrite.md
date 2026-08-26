# 2026-08-26 ENAPOL Focused Line-Test Rewrite

## Goal

Work directly on `main`, revise the ENAPOL presentation around Prof. Dr. Thomas Daniel Finbow's guidance, ensure the public presentations homepage discovers the ENAPOL deck after deploy, validate locally, export PDFs, and commit.

## Files Inspected

- `/Users/kian/.codex/attachments/7e21754d-7622-4e0d-a0ba-ead19a77bfcd/pasted-text.txt`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `scripts/build-all.mjs`
- `package.json`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `/Users/kian/code/oldtupicorpus/historic/araujo_catecismo_1686.tu.py`
- `/Users/kian/code/oldtupicorpus/ground_truth/records/historic/araujo_catecismo_1686.jsonl`
- `/Users/kian/code/oldtupicorpus/historic/bettendorff_compendio.tu.py`
- `/Users/kian/code/oldtupicorpus/ground_truth/records/historic/bettendorff_compendio.jsonl`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `scripts/build-all.mjs`
- `README.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/TODO_anchieta_grammar_page_same_topic.svg`
- `public/assets/enapol-2026-executable-grammar/TODO_gerardi_tupinamba_page_same_topic.svg`
- `public/assets/enapol-2026-executable-grammar/TODO_pydicate_executable_grammar_screenshot.svg`
- `public/assets/enapol-2026-executable-grammar/TODO_araujo_or_bettendorff_short_line.svg`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-26-enapol-focused-line-test-rewrite.md`

## Commands Run

- `sed -n '1,260p' /Users/kian/.codex/attachments/7e21754d-7622-4e0d-a0ba-ead19a77bfcd/pasted-text.txt`
- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,260p' docs/agent/current-state.md`
- `sed -n '1,220p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `git status --short --branch`
- `sed -n '1,460p' decks/enapol-2026-executable-grammar.md`
- `sed -n '1,760p' styles/enapol-2026-executable-grammar.css`
- `sed -n '1,220p' scripts/build-all.mjs`
- `sed -n '1,180p' package.json`
- `sed -n '1,240p' public/assets/enapol-2026-executable-grammar/README.md`
- `rg --files public/assets/enapol-2026-executable-grammar`
- `find /Users/kian/code -maxdepth 2 -iname '*tupi*corpus*' -o -iname '*oldtupi*'`
- `find /Users/kian/code -maxdepth 3 -path '*oldtupicorpus*' -type f | head -n 80`
- `sed -n '1,220p' /Users/kian/code/oldtupicorpus/historic/araujo_catecismo_1686.tu.py`
- `sed -n '1,220p' /Users/kian/code/oldtupicorpus/historic/bettendorff_compendio.tu.py`
- `find /Users/kian/code/oldtupicorpus/ground_truth -maxdepth 3 -type f | sort | head -n 80`
- `sed -n '1,120p' /Users/kian/code/oldtupicorpus/ground_truth/records/historic/bettendorff_compendio.jsonl`
- `sed -n '1,120p' /Users/kian/code/oldtupicorpus/ground_truth/records/historic/araujo_catecismo_1686.jsonl`
- `npm run build`
- `git diff --check`
- `rg -n "ENAPOL 2026|29º ENAPOL|enapol-2026-executable-grammar|Corpus Computacional" dist/index.html dist/enapol-2026-executable-grammar/index.html`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `npm run dev:enapol-2026 -- --port 3038`
- `node -e ...` no-screenshot Playwright/Chromium layout and image-load check for slides 1-8
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`

## What Worked

- The ENAPOL deck is now 8 slides and clearly follows the requested arc: general objective, zoom into one question, concrete corpus line, encoding, difficulty/response loop, and contribution.
- The worked line is grounded in local `oldtupicorpus` source and records: `araujo_catecismo_1686:0007`, Araújo 1686, Livro I, Padre Nosso, p. 2, lines 1-2.
- The generated homepage now includes the ENAPOL link with the requested title and context.
- The fresh local route `http://localhost:3038/` served the edited deck and passed a no-screenshot browser layout/image-load check for all 8 slides.
- `npm run build`, `git diff --check`, generated raw-marker checks, normal PDF export, and click-expanded PDF export passed.

## What Failed

- The existing `http://localhost:3037/` server was stale and still served the older deck, so a fresh server was started on port `3038`.
- Some broad exploratory `rg` commands against sibling repos produced very large output; future checks for corpus examples should use targeted file reads and generated JSONL records.

## Remaining Questions

- Replace the TODO SVG fallbacks with real PNG crops/screenshots before the final presentation.
- Confirm the exact Anchieta and Gerardi/modern grammar passages for slide 3 so the comparison uses the same grammatical phenomenon as the Araújo line.

## Suggested Next Prompt

Review `http://localhost:3038/`, then replace the four TODO visuals with real PNG crops for the same line/topic and run `npm run build` plus the two PDF exports.
