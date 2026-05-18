# Handoff: Retomada Overview Layout

## Goal

Improve the `Tupi Antigo hoje: sem falantes nativos, mas em retomada` slide after the user reported visible overlap in the title/cards/keypoint/source layout, and correct the variety labels from English-order names to Portuguese-order names.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-retomada-overview-layout.md`

## Commands Run

- `rg -n "retomada-slide|retomada-left-stack|retomada-statement-card|retomada-pill-grid|retomada-keypoint|retomada-source|Potiguara Tupi|Tupinambá Tupi|Tupinakyîa Tupi|Tupi potiguara" decks/oficina-unb.md styles/oficina-unb.css docs/agent`
- `sed -n '2678,2730p' decks/oficina-unb.md`
- `sed -n '2790,2970p' styles/oficina-unb.css`
- `rg -n "Potiguara Tupi|Tupinambá Tupi|Tupinakyîa Tupi|Tupi Potiguara|Tupi Tupinambá|Tupi Tupinakyîa" decks/oficina-unb.md styles/oficina-unb.css`
- `npm run build`
- `git diff --check`
- `rg -n "Tupi potiguara|Tupi tupinambá|Tupi tupinakyîa|retomada-overview-slide" dist/oficina-unb/assets/md-*.js dist/oficina-unb/assets/index-*.css`
- `rg -n "Potiguara Tupi|Tupinambá Tupi|Tupinakyîa Tupi|Tupi Tupinambá|Tupi Tupinakyîa" decks/oficina-unb.md dist/oficina-unb/assets/md-*.js`
- `./node_modules/.bin/slidev decks/oficina-unb.md --port 3034`
- `curl -I http://localhost:3034/83`

## What Worked

- Added `retomada-overview-slide` to the dense overview slide.
- Consolidated the slide-specific CSS into one scoped block in `styles/oficina-unb.css`.
- Reduced the title size, moved the left stack down, made the cards and pills more compact, positioned the keypoint inside the left stack, and constrained the source line to the right column below the image.
- Updated visible labels to `Tupi potiguara`, `Tupi tupinambá`, and `Tupi tupinakyîa`.
- Left exact source titles such as `Tupi Potiguara Kuapa` unchanged.
- `npm run build`, `git diff --check`, generated-module checks, and `curl -I http://localhost:3034/83` passed.

## What Failed

- Starting Slidev in the sandbox failed with `EPERM` on `::1:3034`.
- Rerunning the same Slidev command with approved escalation succeeded.
- No Playwright screenshots were taken, following repo instructions.

## Remaining Questions

- Confirm visually whether the smaller title and three-column pill grid are the preferred density for this overview slide.
- If the user wants the official titles normalized in visible citation text too, decide whether exact bibliographic titles should remain capitalized as published.

## Suggested Next Prompt

Review `http://localhost:3034/83` and tell me whether the overview should feel more like a dense summary panel or more like a large thesis slide with fewer cards.
