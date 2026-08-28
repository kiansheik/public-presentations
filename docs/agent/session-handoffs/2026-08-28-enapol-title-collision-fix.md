# ENAPOL Title Advisor Collision Fix

## Goal

Fix the title-slide collision reported from the user's screenshot: the advisor line ran beneath the FFLCH logo after adding `Orientador: Prof. Dr. Thomas Daniel Finbow`.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `styles/enapol-2026-executable-grammar-refinement.css`
- `decks/styles/index.css`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar-refinement.css`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-28-enapol-title-collision-fix.md`

## Commands Run

- `git status --short --branch`
- `rg -n "fflch-logo|presenter-block|title-slide|title-block" ...`
- `sed -n ... styles/enapol-2026-executable-grammar-refinement.css`
- `npm run build`
- no-screenshot Chromium geometry check on `http://localhost:3039/1`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `git diff --check`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`

## What Worked

- Added `class="advisor-line"` to the advisor span.
- In the active refinement stylesheet, moved `.fflch-logo` from `calc(4.8rem + 19.5rem)` to `calc(4.8rem + 26rem)`.
- Narrowed `.presenter-block` to `min(25rem, 48%)`.
- Shrank and balanced `.advisor-line` so it stays in the reserved text column.
- No-screenshot Chromium geometry check reported no overlap:
  - presenter/logo overlap: `false`
  - advisor/logo overlap: `false`
  - presenter-to-logo gap: `25.24px`
  - advisor-to-logo gap: `54.35px`

## What Failed

- No code-level failure. Chromium and Slidev export still require sandbox escalation in this environment.
- The click-expanded PDF export reported `Port 12445 is in use, trying another one...` and completed.

## Remaining Questions

- If the advisor label needs to be more prominent, consider moving it to a separate small line under the talk title instead of enlarging it in the footer.
- If the FFLCH logo is not required on the title slide, removing it would give the footer more room.

## Suggested Next Prompt

Review `http://localhost:3039/1` and confirm whether the title footer balance looks right now, especially in the exported PDF.
