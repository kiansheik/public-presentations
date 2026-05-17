# 2026-05-17 Oficina Pombal Bridge

## Goal

Add a concise historical bridge between the Língua Geral/Amazônia sequence and the Nheengatu naming section, marking the Pombaline state intervention without overbuilding the history section.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `/Users/kian/.codex/memories/MEMORY.md`
- `decks/oficina-unb.md`
- `docs/agent/log.md`

## Files Changed

- `decks/oficina-unb.md`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-pombal-bridge.md`

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,240p' docs/agent/current-state.md`
- `sed -n '1,220p' docs/agent/repo-map.md`
- `sed -n '1,180p' docs/agent/open-questions.md`
- `rg -n "public-presentations|oficina-unb|Pombal|Diretório|Nheengatu|Finbow" /Users/kian/.codex/memories/MEMORY.md`
- Web search/open for Diretório dos Índios date and language-policy framing.
- `sed -n '1458,1555p' decks/oficina-unb.md`
- `sed -n '1555,1608p' decks/oficina-unb.md`
- `git status --short`
- `tail -n 16 docs/agent/log.md`
- `npm run build`
- `git diff --check`
- `sed -n '1495,1575p' decks/oficina-unb.md`
- `git diff -- decks/oficina-unb.md`
- `rg -n "Quando o Estado tenta substituir|Depois da repressão|Diretório dos Índios|slidev_51|slidev_52" dist/oficina-unb/assets/md-*.js`
- `rg -n '<pre>|<code>|\\`pre\\`' dist/oficina-unb/assets/md-*.js`

## What Worked

- Added one bridge slide, `Quando o Estado tenta substituir a Língua Geral`, immediately after the names/descriptions synthesis.
- The bridge says `Diretório dos Índios: 1757, confirmado por alvará régio em 1758` to preserve the user's 1757 framing while avoiding date ambiguity.
- The slide keeps the argument compact: Pombaline policy tries to impose Portuguese and restrict Indigenous languages/Língua Geral in schools and settlements.
- Added the key interpretive line: `Uma língua irrelevante não precisaria ser combatida com tanta força.`
- Retitled the next transition slide to `Depois da repressão, o nome Nheengatu` and reframed it as a post-Diretório naming question.
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated module checks find the new bridge as `slidev_51`, the transition as `slidev_52`, and no raw `<pre>/<code>` markers.

## What Failed

- No Playwright screenshot was taken, following repo instructions to avoid screenshots unless explicitly requested.

## Remaining Questions

- The deck still needs the later promised accessible language-example block and short modern continuity/retomada block.
- The Pombal bridge currently uses only text, not a manuscript image or primary-source screenshot.

## Suggested Next Prompt

Add a small interactive language-example section after the historical block: vocabulary of Tupi origin in Brazilian Portuguese plus one or two transparent structure examples.
