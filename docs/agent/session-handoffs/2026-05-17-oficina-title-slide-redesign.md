# Oficina UnB Title Slide Redesign

## Goal

Make the title slide more aesthetic and clarify that `Kian Sheik` is presenter metadata, not part of the workshop title.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/anchieta-arte-grammatica.png`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-title-slide-redesign.md`

## Commands Run

- `rg -n "title|cover|oficina|nome|Kian|Sheik|Universidade|UnB" /Users/kian/.codex/memories/MEMORY.md`
- `cat docs/agent/index.md`
- `cat docs/agent/current-state.md`
- `cat docs/agent/repo-map.md`
- `cat docs/agent/open-questions.md`
- `nl -ba decks/oficina-unb.md | sed -n '1,90p'`
- `rg -n "title-slide|opening|cover|oficina-canvas|slide-title|oficina-title" styles/oficina-unb.css decks/oficina-unb.md`
- `nl -ba styles/oficina-unb.css | sed -n '1,180p'`
- `ls public/assets/oficina-unb | sort | sed -n '1,120p'`
- `npm run build`
- `git diff --check`
- generated-module checks for the redesigned title slide
- generated `<pre>/<code` checks against `dist/oficina-unb/assets/md-*.js`
- `curl -I http://localhost:3033/1`
- headless Playwright DOM bounds/image-load check for slide 1; no screenshots

## What Worked

- The cover now separates title hierarchy into `Oficina UnB`, `Tupi Antigo`, the subtitle, topic chips, and a presenter block labeled `com`.
- `Kian Sheik` is no longer in the title/subtitle block.
- The right side uses `DeckImage` with `anchieta-arte-grammatica.png` and a small `Anchieta, 1595` caption.
- `npm run build` and `git diff --check` pass.
- The DOM check at 1280x720 found no overflow for the title hero, title text, subtitle, presenter block, or source panel; the title image loaded with natural size `952x814`.

## What Failed

- No failures after the markup/CSS pass.

## Remaining Questions

- The title slide now uses Anchieta as the visual source anchor. If the workshop should foreground contemporary retomadas from the first slide instead, a later pass could swap the right-side image.

## Suggested Next Prompt

Review slide 1 at `http://localhost:3033/1` and tell me whether the title image should stay Anchieta or use a more contemporary source visual.
