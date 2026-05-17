# 2026-05-17 Oficina Maia da Gama Slides

## Goal

Add a follow-up point after the João Daniel/Finbow slides explaining why non-Tupi/Tapuia aldeados learned Língua Geral instead of Portuguese.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/log.md`
- Web sources: Bessa Freire thesis PDF and Observatório da Língua Portuguesa article reproducing the João Maia da Gama argument.

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-maia-da-gama-lingua-geral-slides.md`

## Commands Run

- `sed -n '1,180p' docs/agent/index.md`
- `sed -n '1,220p' docs/agent/current-state.md`
- `sed -n '1,220p' docs/agent/repo-map.md`
- `sed -n '1,180p' docs/agent/open-questions.md`
- `sed -n '960,1085p' decks/oficina-unb.md`
- `sed -n '1085,1145p' decks/oficina-unb.md`
- `tail -n 220 styles/oficina-unb.css`
- `rg -n "maia-|daniel-two-column|amazonia-longquote|takeaway-list" styles/oficina-unb.css`
- `npm run build`
- `rg -n '<pre|<code|`pre`' dist/oficina-unb/assets/md-*.js`
- `rg -n 'maia-question|maia-answer|João Maia|contínuo tracto' dist/oficina-unb/assets/md-*.js`
- `node -e "const fs=require('fs'); console.log(fs.readdirSync('dist/oficina-unb/assets').filter(f=>/^md-.*\\.js$/.test(f)).length)"`
- `git diff --check`
- `git status --short`

## What Worked

- Added two slides after the Daniel follow-up:
  - `Por que não ensinar português diretamente?`
  - `A resposta estava no cotidiano`
- The slides frame the Tapuia/Língua Geral question through social exposure: short Portuguese instruction with a missionary versus daily interaction with other Indigenous people in the aldeamento.
- Added scoped `maia-*` CSS for a question setup slide and a structured answer slide.
- `npm run build` succeeds.
- Generated slide modules include the Maia slides as normal DOM.
- Generated slide modules contain no `<pre>`, `<code>`, or `` `pre` `` markers.

## What Failed

- A broad generated-asset grep for `<pre|<code|`pre`` matched Slidev runtime code in `useNav-*.js`; narrowing the check to generated `md-*.js` slide modules was the useful check.
- Raw `class: oficina-unb` counting overcounts because the source file contains a commented-out old slide frontmatter block. The built deck currently emits 44 `md-*.js` slide modules.

## Remaining Questions

- Whether to remove the commented-out old Anchieta duplicate slide block later, so simple frontmatter counts match generated slide counts.
- Whether to adjust the following Tapuia slide now that the Maia da Gama pair already answers the Tapuia learner question.

## Suggested Next Prompt

Review the transition from the Maia da Gama slides into the existing Tapuia slide and decide whether to merge, shorten, or retitle the Tapuia slide to avoid repeating the same point.
