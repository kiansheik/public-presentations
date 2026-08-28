# ENAPOL Advisor And Two-QR Revision

## Goal

Add the user's advisor, Prof. Dr. Thomas Daniel Finbow, to the ENAPOL title slide; keep the generated tree centered/unclipped; and simplify the final resource slide to dictionary and neologism QR codes only.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `scripts/generate-pydicate-tree-svg.py`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-28-enapol-advisor-two-qr.md`

## Commands Run

- `git status --short --branch`
- `git log --oneline --decorate -n 4`
- `rg -n "title-meta|title-block|speaker|orientador|advisor|Finbow" ...`
- `rg -n "neo-only|stats-grid|stats-note|qr-dictionary|qr-neo|qr-corpus|qr-presentation|Thomas Daniel Finbow" ...`
- `npm run build`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `curl -I http://localhost:3039/`
- no-screenshot Chromium DOM check on routes `/1`, `/7`, and `/10`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`
- `git diff --check`

## What Worked

- The title slide now shows `Orientador: Prof. Dr. Thomas Daniel Finbow` below the presenter/program line.
- The opening rehearsal script and embedded title-slide note now mention the advisor.
- The final resource slide now has exactly two QR cards: `Dicionário` and `Neologismos`.
- The final slide no longer shows presentation or corpus QR cards.
- The existing generated tree layout was verified centered and unclipped in the slide 7 frame.
- Normal and click-expanded PDFs were regenerated.

## What Failed

- No code-level failure. The click-expanded PDF export reported `Port 12445 is in use, trying another one...` and then completed.
- Chromium DOM verification still requires sandbox escalation in this environment; no screenshots were taken.

## Remaining Questions

- Confirm whether the final resource slide should keep the generic two-output framing or restore any neologism usage statistics later.
- Confirm whether `Orientador` should be shown as `Orientador`, `Orientação`, or a bilingual/English label for the ENAPOL audience.

## Suggested Next Prompt

Review `http://localhost:3039/` slides 1, 7, and 10 and say whether the advisor/footer spacing, tree size, and two QR cards look right for the final export.
