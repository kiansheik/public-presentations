# 2026-05-17 Oficina Finbow LGP/LGA Caution Slides

## Goal

Add the requested Finbow slides at the end of `decks/oficina-unb.md`, using the recommended two-slide structure: conceptual caution first, then the Paulista Maranhão-Pará evidence.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `/Users/kian/.codex/memories/MEMORY.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `package.json`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-maia-da-gama-lingua-geral-slides.md`
- Web sources: official Revista do GEL article page and PDF for Finbow, `The Nature and Emergence of the Língua Geral Amazônica according to Mufwene’s Language Ecology Model`.

## Files Changed

- `decks/oficina-unb.md`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-finbow-lgp-lga-caution-slides.md`

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,240p' docs/agent/current-state.md`
- `sed -n '1,260p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `rg -n "public-presentations|oficina-unb|finite corpus|source fichas|Finbow|Língua Geral" /Users/kian/.codex/memories/MEMORY.md`
- `tail -n 260 decks/oficina-unb.md`
- `rg -n "amazonia-slide|maia-|daniel-followup|takeaway-list|closing" styles/oficina-unb.css`
- `cat package.json`
- `git status --short`
- `npm run build`
- `git diff --check`
- `node -e '...'` generated-module check for slide count, titles, and raw HTML markers.
- `rg -n "LGP/LGA|Paulistas no Maranhão-Pará|variedades tupi-guarani|Isso seria estranho" decks/oficina-unb.md`

## What Worked

- Appended two slides after `Mudança não é invenção`:
  - `LGP/LGA: rótulos úteis, mas modernos`
  - `Paulistas no Maranhão-Pará`
- Reused existing `amazonia-*` layout classes, so no CSS change was needed.
- `npm run build` succeeds.
- Generated `md-*.js` slide modules include both new titles.
- Generated `md-*.js` slide modules contain no `<pre>`, `<code>`, or `` `pre` `` markers.

## What Failed

- The first generated-module check accidentally let a backtick pattern be interpreted by `zsh` command substitution. The check was rerun with `String.fromCharCode(96)` to avoid shell backtick parsing.

## Remaining Questions

- The visible new slide footers use the article citation as `Finbow, 2023`, matching the Revista do GEL article page's publication/citation metadata. Several existing deck notes use `Finbow, 2022`, matching the issue year printed in the PDF. Decide later whether to standardize those citations deck-wide.
- No browser screenshot verification was run, following repo instructions.

## Suggested Next Prompt

Review the last four slides as a sequence and decide whether `Mudança não é invenção` should stay before the LGP/LGA caution pair or move after them as the final synthesis slide.
