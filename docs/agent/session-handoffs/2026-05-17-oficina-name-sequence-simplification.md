# 2026-05-17 Oficina Name Sequence Simplification

## Goal

Simplify the dense names/glotonyms timeline slide so it only shows the requested Brazil/Amazônia labels: `lingva mais vsada na costa do Brasil`, `lingoa brasílica`, `língua geral`, and `Nheengatu`, with where each appears and when.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-proportional-names-timeline.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-name-sequence-simplification.md`

## Commands Run

- `sed -n '1466,1564p' decks/oficina-unb.md`
- `sed -n '744,910p' styles/oficina-unb.css`
- `git status --short`
- `tail -n 80 docs/agent/log.md`
- `find docs/agent/session-handoffs -maxdepth 1 -type f`
- `sed -n '1564,1668p' decks/oficina-unb.md`
- `git diff -- decks/oficina-unb.md styles/oficina-unb.css docs/agent/current-state.md docs/agent/log.md docs/agent/session-handoffs/2026-05-17-oficina-proportional-names-timeline.md`
- `npm run build`
- `git diff --check`
- `rg -n "Quatro nomes|name-sequence-card|língua geral dos Tupynambás|lengua mexicana|Santo Tomás / Quechua|Olmos / Nahuatl" decks/oficina-unb.md styles/oficina-unb.css dist/oficina-unb/assets/md-*.js`
- `rg -n '<pre>|<code>|\\`pre\\`' dist/oficina-unb/assets/md-*.js`
- `rg -n "Quatro nomes|slidev_50|slidev_54|Quando aparece o nome" dist/oficina-unb/assets/md-*.js`
- `rg -n "lengua mexicana|Nahuatl|Quechua|Guarani|rótulos modernos|Tupi Antigo ·" dist/oficina-unb/assets/md-DmwkdhvX2.js`

## What Worked

- Replaced the proportional multi-lane timeline with a four-card slide titled `Quatro nomes na documentação`.
- Moved the simplified synthesis before the Nheengatu detail slides; the generated module identifies it as `oficina-unb.md__slidev_50`.
- Removed the comparative-language examples and modern analytical-label box from that slide.
- Kept each card focused on one label, date, source, and short interpretive note:
  - Anchieta, 1595: `lingva mais vsada na costa do Brasil`
  - Araújo, 1618: `lingoa brasílica`
  - Manoel Gomes, 1616: `língua geral dos Tupynambás`
  - Seixas, 1853: `Nheengatu`
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated module checks confirm the simplified slide is built, has no comparative-language labels inside that slide module, and generated slide modules contain no raw `<pre>/<code>` markers.

## What Failed

- One raw-marker `rg` command was initially quoted with double quotes, so the shell tried to execute the backticked `pre` fragment. The check was rerun with single quotes and passed.
- No Playwright screenshot was taken, following repo instructions to avoid screenshots unless explicitly requested.

## Remaining Questions

- Confirm whether the four-card order should remain chronological by first-attested date. The requested conceptual order puts `língua geral` before `Nheengatu`, but its current card date, 1616, precedes `lingoa brasílica` 1618.
- The worktree already contained untracked image assets for the later Nheengatu slides before this simplification: `public/assets/oficina-unb/SEU_ARQUIVO_VLB_NHEENGATU.png` and `public/assets/oficina-unb/boafala.png`.

## Suggested Next Prompt

Open the simplified names slide in the browser and check whether the four cards should be ordered conceptually (`língua mais usada` → `língua brasílica` → `língua geral` → `Nheengatu`) or strictly chronologically (`1595` → `1616` → `1618` → `1853`).
