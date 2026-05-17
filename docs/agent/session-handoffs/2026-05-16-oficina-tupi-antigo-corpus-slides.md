# Handoff: Oficina UnB Tupi Antigo Corpus Slides

## Goal

Add slides defining what this deck means by "Tupi Antigo": a finite corpus designation for known Jesuit, Indigenous, and European documents, followed by modular source fichas.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `package.json`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-16-oficina-tupi-antigo-corpus-slides.md`

## Commands Run

- `sed -n '1,180p' docs/agent/index.md`
- `sed -n '1,220p' docs/agent/current-state.md`
- `sed -n '1,220p' docs/agent/repo-map.md`
- `sed -n '1,180p' docs/agent/open-questions.md`
- `rg -n "^(---|## |# |<div class=|layout:|class:)" decks/oficina-unb.md`
- `sed -n '1,260p' styles/oficina-unb.css`
- `sed -n '1,220p' decks/oficina-unb.md`
- `sed -n '220,520p' decks/oficina-unb.md`
- `sed -n '520,700p' decks/oficina-unb.md`
- `sed -n '260,620p' styles/oficina-unb.css`
- `sed -n '1,220p' package.json`
- `git status --short`
- `rg -n "Jesu|corpus-card|corpus-definition|corpus-timeline|Tupi Antigo" decks/oficina-unb.md`
- `sed -n '330,760p' decks/oficina-unb.md`
- `npm run build`
- `node --input-type=module -e '...'` for a static Slidev parser check
- `rg -n "Jesu íta|corpus-card-title|definition-main|timeline-row" decks/oficina-unb.md styles/oficina-unb.css`
- `git diff --stat`
- `git diff -- decks/oficina-unb.md styles/oficina-unb.css`
- `tail -n 120 docs/agent/log.md`
- `find docs/agent/session-handoffs -maxdepth 1 -type f -print`

## What Worked

- Inserted the corpus block after the Brasil convergence slide and before the Anchieta grammar slides.
- Added one definition slide, twelve source fichas, and one central-corpus timeline.
- Added CSS for the new source ficha layout without requiring new image assets.
- `npm run build` succeeds.
- The parser reports 33 slides, with the corpus block spanning slides 15-28.

## What Failed

- The first parser-check command used JavaScript template syntax inside a double-quoted shell command and triggered `zsh: bad substitution`. It still printed the slide count, then was rerun with safer quoting and produced the expected slide titles.

## Remaining Questions

- The new source fichas use short references from the user's provided outline; final bibliographic details may need a later source pass.
- The slides intentionally do not include manuscript images yet. They are text-first fichas ready for later source screenshots or facsimiles.

## Suggested Next Prompt

Review slides 15-28 in the local Slidev deck and tell Codex which source fichas should receive images or which entries should be shortened for pacing.
