# 2026-08-28 ENAPOL Final Slide Neologisms Links

## Goal

Make the final-slide neologisms QR image and visible label clickable, matching the slide 9 QR/link behavior.

## Files Inspected

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar-refinement.css`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `docs/agent/current-state.md`
- `docs/agent/log.md`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar-refinement.css`
- `notes/enapol-2026-executable-grammar.md`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-28-enapol-final-slide-neo-links.md`

## Commands Run

- `npm run build`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets`
- `git diff --check`
- `curl -I http://localhost:3037`
- Headless Chromium DOM check on `http://localhost:3037/10`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`

## What Worked

- The final slide now has two anchors to `https://neo.academiatupi.com/`: one wrapping the QR image and one wrapping the visible `neo.academiatupi.com` label.
- The QR image still loads and reports natural size `150x150`.
- DOM geometry reported the QR card inside the viewport and no overlap with the stats card.
- Normal and click-expanded PDF exports succeeded.

## What Failed

- Nothing blocked the scoped change. Chromium still requires the approved unsandboxed run for local DOM checks on this macOS setup.

## Remaining Questions

- None for this scoped final-slide link fix.

## Suggested Next Prompt

Review `http://localhost:3037/10` and confirm whether the final-slide label styling should remain underlined or be visually closer to the original plain heading.
