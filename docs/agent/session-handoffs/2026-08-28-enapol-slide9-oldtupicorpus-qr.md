# 2026-08-28 ENAPOL Slide 9 Old Tupi Corpus QR

## Goal

Add a click-through QR code and visible hyperlink label for `https://kiansheik.io/oldtupicorpus/` to the second-to-last ENAPOL slide, without changing the final slide.

## Files Inspected

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `notes/enapol-2026-executable-grammar.md`
- `package.json`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `notes/enapol-2026-executable-grammar.md`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/qr-oldtupicorpus.svg`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-28-enapol-slide9-oldtupicorpus-qr.md`

## Commands Run

- `curl -I https://kiansheik.io/oldtupicorpus/`
- `node -e "import('uqr').then(...)"` to generate `qr-oldtupicorpus.svg`
- `npm run build`
- `find dist/enapol-2026-executable-grammar/assets -name 'md-*.js' | wc -l`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets`
- `git diff --check`
- `curl -I http://localhost:3037`
- Headless Chromium DOM check on `http://localhost:3037/9` and `/10`
- `npm run export:enapol-2026:pdf`
- `npm run export:enapol-2026:pdf:clicks`
- `strings enapol-2026-executable-grammar-export.pdf | rg -n "oldtupicorpus|kiansheik.io"`
- `strings enapol-2026-executable-grammar-clicks-export.pdf | rg -n "oldtupicorpus|kiansheik.io"`

## What Worked

- The live URL returned `HTTP/2 200`.
- Slide 9 now has a right-side QR card beside the existing output grid.
- Both slide 9 anchors point to `https://kiansheik.io/oldtupicorpus/`.
- DOM geometry reported no overlap between `.outputs-grid` and `.corpus-qr-card`.
- Slide 10 still has `.neo-only-slide` and no visible `Dicionário` label.
- Normal and click-expanded PDF exports succeeded.

## What Failed

- The first Chromium launch failed inside the sandbox with macOS `MachPortRendezvousServer` permission denial; rerunning with approved escalation succeeded.
- `strings` did not expose the URL inside either exported PDF, likely because the PDFs are compressed. Link-target verification came from the live Slidev DOM before export.

## Remaining Questions

- None for the scoped slide 9 QR request.

## Suggested Next Prompt

Review slide 9 at `http://localhost:3037/9` and confirm whether the QR card size and placement should stay as-is before any further deck-wide edits.
