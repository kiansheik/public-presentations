# 2026-05-18 Oficina Finbow Footnotes

## Goal

Make Finbow-cited slides more academic by adding visible footnotes with the cited work title and year, rather than leaving bare `Finbow, 2022` or `Finbow, 2025` references.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/Downloads/oficina_source_images/full_pages/finbow2022_page_01.png`
- `/Users/kian/Downloads/oficina_source_images/full_pages/finbow2025_page_02.png`
- `/Users/kian/.codex/memories/MEMORY.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-finbow-footnotes.md`

## Commands Run

- `rg -n "Finbow|finbow" decks/oficina-unb.md styles/oficina-unb.css public/assets/oficina-unb docs/agent`
- `nl -ba decks/oficina-unb.md | sed -n '1080,1325p'`
- `nl -ba decks/oficina-unb.md | sed -n '1360,1610p'`
- `nl -ba decks/oficina-unb.md | sed -n '1820,2015p'`
- `rg --pcre2 -n "class=\"source[^\"]*\"[^\n]*Finbow(?!, Thomas)|Finbow, 20[0-9]{2}, p\.|Finbow \(2025\)|Fonte visual: Finbow, 20" decks/oficina-unb.md`
- `git diff --check`
- `npm run build`
- `rg -n "The Nature and Emergence of the Língua Geral Amazônica according to Mufwene|A sociophilological account of the formation and evolution|SciELO Preprints|finbow-source" dist/oficina-unb/assets/md-*.js`
- `rg --pcre2 -n "Finbow, 20[0-9]{2}, p\.|Finbow \(2025\)|class=\"source[^\"]*\"[^\n]*Finbow(?!, Thomas)|Fonte visual: Finbow, 20" decks/oficina-unb.md dist/oficina-unb/assets/md-*.js`
- `rg -n "<pre[[:space:]>]|<code[[:space:]>]" dist/oficina-unb/assets/md-*.js`
- `curl -I http://localhost:3033/40`
- Headless Playwright DOM overflow check for routes 40-45, 48-54, and 62; no screenshots were taken.

## What Worked

- Replaced bare visible Finbow citations with full footnotes for the 2022 article:
  - Thomas Finbow, `The Nature and Emergence of the Língua Geral Amazônica according to Mufwene’s Language Ecology Model`, `Revista do GEL`, 19(2), 2022.
- Replaced bare visible Finbow citations with full footnotes for the 2025 preprint:
  - Thomas Finbow, `A sociophilological account of the formation and evolution of the term Língua Geral, with emphasis on Amazonia`, SciELO Preprints, 2025.
- Added visible `source finbow-source` lines to Finbow-derived argument slides that previously only had source information in speaker notes.
- Added compact `finbow-source` CSS so the longer citations fit.
- Final build and generated checks pass, and DOM checks report no overflow on all affected routes.

## What Failed

- A first `rg` check used look-ahead without `--pcre2`; rerunning the same check with `--pcre2` worked.

## Remaining Questions

- The deck currently cites the `Revista do GEL` issue year as 2022 because that is what the local PDF footer shows. A previous handoff notes that an official article page may expose publication metadata differently; standardize later only if you want the deck to follow article-page metadata rather than the PDF issue year.

## Suggested Next Prompt

Review the Finbow footnote density on routes 40-45 and 48-54, then ask for any shortening strategy if the citations feel visually too heavy in presenter mode.
