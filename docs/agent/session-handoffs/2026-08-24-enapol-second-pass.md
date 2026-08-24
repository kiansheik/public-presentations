# ENAPOL Second-Pass Handoff

## Goal

Improve the existing ENAPOL PR/branch deck without starting over, keeping it near nine slides and a 10-minute delivery. The requested emphasis was linguistic description using computational methods, not an NLP/product pitch.

## Files Inspected

- `/Users/kian/.codex/attachments/807fefd2-4721-4be6-ad9d-1d16826cdf6b/pasted-text.txt`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `decks/components/EnapolImage.vue`
- `public/assets/enapol-2026-executable-grammar/`
- GitHub PR #1 metadata for `enapol-kian`

## Files Changed

- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `decks/components/EnapolImage.vue`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/*.svg`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-24-enapol-second-pass.md`

## Commands Run

- `git status --short --branch`
- `npm run build`
- `git diff --check`
- `rg -n -F '<pre' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `rg -n -F '<code' dist/enapol-2026-executable-grammar/assets/md-*.js`
- `npm run dev:enapol-2026 -- --port 3036`
- Playwright/Chromium screenshot and DOM checks against `http://localhost:3036/`
- `npm run export:enapol-2026:pdf`
- `file enapol-2026-executable-grammar-export.pdf`
- `qlmanage -t -s 1280 -o /private/tmp enapol-2026-executable-grammar-export.pdf`

## What Worked

- The deck remains nine slides and now follows the requested argument: source problem, worked corpus example, programming as metalanguage, historical/modern/executable comparison, bootstrapping loop, current outputs versus doctorate direction, significance, and close.
- Visual QA caught and fixed title/panel collisions, slide 3 overlap, slide 6 loop crowding, and slide 7 raw HTML/clipping.
- `EnapolImage.vue` now supports extensionless logical names, so real PNG/JPG/JPEG replacements can override SVG placeholders without deck edits.
- `npm run build`, `git diff --check`, generated raw-marker checks, and `npm run export:enapol-2026:pdf` passed.

## What Failed

- The stale dev server on port 3035 could not be stopped from the old session, so a fresh server was started on port 3036.
- The first PDF export attempt inside the sandbox failed with `GetPortError`; the approved escalated rerun succeeded.
- All-page PDF raster QA could not be completed with local tools: `pdfinfo`/`pdftoppm` are unavailable, and `gs` cannot find `gs_init.ps`. A macOS thumbnail check confirmed the exported first page.

## Remaining Questions

- Exact corpus line, page reference, transcription, segmentation, gloss, and translation for slide 3.
- Exact Anchieta and modern-source passages for the slide 5 phenomenon comparison.
- One concrete empirical result for slide 7.
- Final bibliography entries and page references for all captured sources.
- Real screenshots/page crops for the ten assets listed in the ENAPOL asset README.

## Suggested Next Prompt

Replace the ENAPOL placeholders with these real screenshots and citation details, then rerun build/export and do one final slide-by-slide QA pass.
