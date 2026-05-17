# Handoff: Language Case Slide Readability

## Goal

Make the Quechua, Nahuatl, and Guarani case-study slides easier to read by separating labels, source entries, dates, and takeaways instead of using one repeated paragraph style.

## Files Inspected

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-16-language-case-slide-readability.md`

## Commands Run

- `nl -ba decks/oficina-unb.md | sed -n '115,180p'`
- `nl -ba styles/oficina-unb.css | sed -n '105,250p'`
- `git status --short`
- `npm run build`
- `git diff -- decks/oficina-unb.md styles/oficina-unb.css`
- `git diff --check`

## What Worked

- Added `language-case-block` to the Quechua, Nahuatl, and Guarani slides.
- Replaced flat paragraph runs with `language-case-label`, `language-source-list`, `language-source`, `language-case-point`, and `language-case-note`.
- Added CSS for dated source rows, visible source-title emphasis, and a stronger takeaway block.
- `npm run build` succeeds.
- `git diff --check` succeeds.

## What Failed

- No browser screenshot review was run, per repo instructions.

## Remaining Questions

- The user should visually review slides 5-7 and decide whether the date/source-row style is strong enough or should become even more compact.

## Suggested Next Prompt

Review slides 5-7 at the running local deck and tell Codex whether to make the source rows denser, larger, or more manuscript-like.
