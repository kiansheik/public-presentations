# Session Handoff: Oficina Amazônia LGA Ecology Block

## Goal

Add a new block after the Anchieta closeout that transitions from Tupi Antigo / Língua Brasílica as a classical corpus to Língua Geral Amazônica as a living language of aldeamento, contact, and change. The block should avoid the thesis that “the Jesuits simplified the language” and instead foreground linguistic ecology: multiethnic aldeamentos, descimentos, epidemics, non-Tupi-speaking learners, everyday immersion, and the tension between written missionary norms and vernacular use.

## Files Inspected

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/maisuniversal.png`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- Finbow, Thomas. “The Nature and Emergence of the Língua Geral Amazônica according to Mufwene’s Language Ecology Model.” `Revista do GEL`, 19(2), 75-112, 2022.

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-16-oficina-amazonia-lga-ecology-block.md`

## Commands Run

- `tail -n 170 styles/oficina-unb.css`
- `tail -n 80 decks/oficina-unb.md`
- `file public/assets/oficina-unb/maisuniversal.png`
- `rg -n "Diretório|Pombal|Nheengatu|Amazônia|Língua Geral Amazônica|João Daniel|Finbow" decks/oficina-unb.md styles/oficina-unb.css public/assets/oficina-unb docs/agent/current-state.md docs/agent/log.md`
- `npm run build`
- `rg -n "Da costa à Amazônia|João Daniel|verdadeiros topinambares|Aldeamentos multiétnicos|Duas normas|Mudança não é invenção|ecologia colonial" decks/oficina-unb.md styles/oficina-unb.css`
- `rg -n "^class: oficina-unb$" decks/oficina-unb.md | wc -l`
- `git diff --check`
- `git status --short`
- `git diff --stat`
- `nl -ba decks/oficina-unb.md | sed -n '832,1072p'`
- `nl -ba styles/oficina-unb.css | sed -n '900,1125p'`

## What Worked

- Added eight slides:
  - `Da costa à Amazônia: muda o cenário`
  - `João Daniel: “parece outra língua diversa”`
  - `“Os verdadeiros topinambares já quase de todo se acabaram”`
  - `Aldeamentos multiétnicos e aprendizagem pela imersão`
  - `A língua muda porque a comunidade muda`
  - `Duas normas: catecismo e fala cotidiana`
  - `Mudança não é invenção`
  - `A Língua Geral Amazônica nasce de uma ecologia colonial`
- Added speaker notes tying the block to Finbow 2022, João Daniel, the 1660-1700 demographic/linguistic watershed, Tapuia learners, written-vs-vernacular norms, and the later transition to the Diretório pombalino.
- Kept the direct João Daniel quotes short on-slide while leaving interpretive detail in speaker notes.
- Added `amazonia-*` CSS classes for this block only.
- `npm run build` completed successfully.
- `git diff --check` reported no whitespace errors.
- A static count now finds 42 `oficina-unb` slide declarations.

## What Failed

- No build failures. Browser screenshots were not taken, per repo instruction.

## Remaining Questions

- Whether the Amazônia/LGA block should remain at the end for now or eventually move before a future Diretório pombalino block.
- Whether the block should gain one manuscript/source image later, for example a João Daniel or Finbow citation slide, or stay text-first.
- Whether future Nheengatu/retomada slides should be appended after the Diretório section or developed as a separate closing section.

## Suggested Next Prompt

Add the Diretório pombalino block after the Amazônia/LGA ecology block, showing how the state attempted to impose Portuguese against an already widespread everyday Língua Geral Amazônica.
