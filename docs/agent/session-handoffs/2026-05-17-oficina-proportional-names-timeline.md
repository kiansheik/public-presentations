# 2026-05-17 Oficina Proportional Names Timeline

## Goal

Add a chronological, proportionally scaled timeline that synthesizes the different historical names, descriptions, and modern labels used across the deck, from Iberian `lengua general` framing through present-day Nheengatu.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `/Users/kian/.codex/memories/MEMORY.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-proportional-names-timeline.md`

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,260p' docs/agent/current-state.md`
- `sed -n '1,240p' docs/agent/repo-map.md`
- `sed -n '1,180p' docs/agent/open-questions.md`
- `rg -n "public-presentations|oficina-unb|timeline|glotônimo|Nheengatu|VLB|Seixas" /Users/kian/.codex/memories/MEMORY.md`
- `tail -n 110 decks/oficina-unb.md`
- `rg -n "corpus-timeline|timeline-row|timeline" styles/oficina-unb.css decks/oficina-unb.md`
- `sed -n '560,740p' styles/oficina-unb.css`
- `npm run build`
- `git diff --check`
- `node -e '...'` generated-module check for slide count, new timeline content, and raw HTML code modules.
- `git status --short`

## What Worked

- Inserted `Nomes, descrições e glotônimos ao longo do tempo` after the Finbow `Mudança não é invenção` closeout and before `Quando aparece o nome “Nheengatu”?`.
- Used a 1547-2026 proportional horizontal rail with staggered cards so early dense dates remain readable.
- Split event cards into:
  - comparative Iberian/missionary labels
  - Brazil/Amazônia labels
  - modern analytical labels
- Included `Tupi Antigo`, `LGP`, and `LGA` as modern analytical labels rather than colonial names.
- `npm run build` succeeds.
- Generated `md-*.js` modules include the timeline slide and contain no rendered `<pre>/<code>` slide modules.

## What Failed

- The first CSS patch target missed the exact existing `.timeline-note` block shape; the patch was reapplied against the current CSS around the corpus timeline styles.

## Remaining Questions

- The deck references two untracked image assets: `public/assets/oficina-unb/SEU_ARQUIVO_VLB_NHEENGATU.png` and `public/assets/oficina-unb/boafala.png`. They existed before this timeline change in the current worktree state and are required by the later Nheengatu slides.
- No Playwright screenshots were run, following repo instructions.

## Suggested Next Prompt

Review the new timeline slide in the browser and decide whether any dense early labels should be split into a second zoomed-in timeline slide for 1547-1681.
