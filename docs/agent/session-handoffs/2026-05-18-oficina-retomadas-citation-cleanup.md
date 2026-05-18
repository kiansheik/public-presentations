# 2026-05-18 Oficina Retomadas Citation Cleanup

## Goal

Remove visible citations to unpublished/self-authored qualification material from the final contemporary/retomadas block while preserving the slide information and grounding citations in source-specific public or supplied materials.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `/Users/kian/code/latex/mestrado/body/contemporary.tex`
- `/Users/kian/code/latex/mestrado/body/content.tex`
- `/Users/kian/code/latex/references.bib`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-retomadas-citation-cleanup.md`

## Commands Run

- `rg -n "public-presentations|oficina-unb|contemporary|Sheik|qualification" /Users/kian/.codex/memories/MEMORY.md`
- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,260p' docs/agent/current-state.md`
- `sed -n '1,260p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `rg -n "Sheik|qualification|Contemporary|contemporary|retomada|Potiguara|Tupinambá|Tupinakyîa|Akangatara|Toré|USP|Navarro|Cabral|Araújo|Silva" decks/oficina-unb.md styles/oficina-unb.css README.md docs public package.json`
- `find . -maxdepth 4 -type f \( -name '*.bib' -o -name '*.tex' -o -name '*.md' \) | sort`
- `git status --short`
- `sed -n '2670,2875p' decks/oficina-unb.md`
- `rg -n "revitalization|Potiguara|Tupinamb|Tupinaky|Tupiniquim|Akangatara|CPB|Contemporary|speaker|native|Old Tupi|USP|Navarro|José|Romildo|Araújo|Cabral|Oliven" /Users/kian/code/latex/mestrado /Users/kian/code/latex/qualification -g '*.tex' -g '*.bib'`
- `sed -n '1,120p' public/assets/oficina-unb/README.md`
- `sed -n '1,80p' /Users/kian/code/latex/mestrado/body/contemporary.tex`
- `find /Users/kian/code/latex/mestrado /Users/kian/code/latex/qualification -type f \( -name '*.bib' -o -name '*.biblatex' -o -name 'references*' \) -print`
- `rg -n "bibliography|addbibresource|biblatex|bib" /Users/kian/code/latex/mestrado /Users/kian/code/latex/qualification -g '*.tex'`
- `rg -n "Silva_2024|araujo2024|navarro2005|navarro2013|carta_potiguara_navarro2022|Cabral2024-potiguara-neologismos|costa2013_revitalizacao|santos2023_revitalizacao|SantanaCohn2018|Santana2020|SantosPorto2020|Costa2016TupinambaCom|Cimi2025|MPI2025|Pavelic2023|AkangataraYouTube|soares2023_kuarasy|sheik2024grammar" /Users/kian/code/latex/references.bib`
- `sed -n '285,320p' /Users/kian/code/latex/references.bib`
- `sed -n '430,525p' /Users/kian/code/latex/references.bib`
- `sed -n '930,980p' /Users/kian/code/latex/references.bib`
- `sed -n '1078,1102p' /Users/kian/code/latex/references.bib`
- `sed -n '1530,1565p' /Users/kian/code/latex/references.bib`
- `sed -n '1728,1810p' /Users/kian/code/latex/references.bib`
- `sed -n '2800,3195p' styles/oficina-unb.css`
- `npm run build`
- `git diff --check`
- `rg -n '<pre[[:space:]>]|<code[[:space:]>]' dist/oficina-unb/assets/md-*.js`
- `rg -n "Sheik,|qualificationtr|A Computational Grammar|seção Contemporary|seções Nomenclature|Página 22 da qualificação" dist/oficina-unb/assets/md-*.js decks/oficina-unb.md`
- `rg -n "Akangatara Produções|Tupi Potiguara Kuapa|Costa \(2013\)|Santos & Porto|Síntese a partir" dist/oficina-unb/assets/md-*.js decks/oficina-unb.md`

## What Worked

- The contemporary-context content already aligned with the thesis source; the main issue was visible citation provenance.
- All visible slide footers in the retomadas block now avoid `Sheik`, `A Computational Grammar of Old Tupi`, and `qualificationtr.pdf`.
- Potiguara, Tupinambá, Tupinakyîa, university/online, and closing sources now point to the public/supplied source layer: Araújo da Silva Toré material, Araújo da Silva Guyraakanga Potiguara 2024, Cabral 2024, Costa 2013, Santos & Porto 2020, Santana & Cohn 2018, Pavelic 2023, Navarro 2005/2013, and Akangatara Produções.
- The Tupinakyîa slide no longer uses the qualification page crop; it now has a right-side sources/circulation card.
- `npm run build`, `git diff --check`, and generated module checks pass.

## What Failed

- An initial `rg` regex over `references.bib` had an unclosed group; rerun with a simpler alternation worked.
- One generated raw-HTML marker check accidentally used shell backticks around `` `pre` ``, triggering command substitution; rerun with a single-quoted `<pre>/<code>` pattern worked.

## Remaining Questions

- The `Entre universidade, internet e tecnologia` slide still uses local `qualification-dic.png`, `qualification-gint.png`, `qualification-trad.png`, and `qualification-quiz.png` screenshots as visual examples, but it no longer cites the unpublished qualification. If the standard is “no unpublished visuals at all,” replace that collage with a non-self visual or a text/card layout.
- The broader repo has existing uncommitted changes in `decks/oficina-unb.md` and `styles/oficina-unb.css` outside this cleanup; do not assume all current diff belongs to this task.

## Suggested Next Prompt

Review the final retomadas slides and replace the remaining internal digital-tool screenshots with source-neutral visuals if we want zero unpublished material visible, not just zero unpublished citations.
