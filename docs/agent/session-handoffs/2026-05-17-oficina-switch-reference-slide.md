# Handoff: Switch Reference Slide

## Goal

Add a dedicated switch-reference slide because the grammar-change synthesis mentioned switch reference without giving it its own explanation.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/code/latex/swith_ref_tupi_2025/main.tex`
- `/Users/kian/code/latex/swith_ref_tupi_2025/references.bib`
- `/Users/kian/code/latex/nheengatu_loss/main.tex`
- `/Users/kian/code/latex/nheengatu_loss/references.bib`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-switch-reference-slide.md`

## Commands Run

- `sed` targeted reads over the agent wiki, deck, CSS, and LaTeX sources.
- `find . /Users/kian/code/latex -maxdepth 4 -type f \( -iname '*.pdf' -o -iname '*.tex' -o -iname '*.bib' \)`
- `rg` searches for switch-reference, `ramé`, and gloss examples.
- `npm run build`
- `git diff --check`
- `rg --files dist/oficina-unb/assets | rg '/md-.*\.js$' | wc -l`
- `rg` generated-module checks for the new slide title, examples, and `<pre>/<code` markers.
- `curl -I http://localhost:3033/64`

## What Worked

- Added `Switch reference: o sujeito ainda é o mesmo?` before the grammar-change synthesis.
- Used Old Tupi examples from the switch-reference paper source:
  - `A-nhe'eng gûi-xó-bo.`
  - `A-nhe'eng nde-só-reme.`
- Used the Nheengatu `ramé` examples from the Nheengatu-loss paper source:
  - `Awá ramé u-muaíwa Deus r-uka...`
  - `Ya-manú ramé, makití ya-sú?`
- Added dedicated `switch-*` CSS in `styles/oficina-unb.css` after the user noticed the first edit had only added markup.
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated output now has 65 `md-*.js` slide modules; switch reference is `slidev_64` and the synthesis is `slidev_65`.
- `curl -I http://localhost:3033/64` returns `HTTP/1.1 200 OK`.

## What Failed

- The first broad `rg` over LaTeX gloss commands failed because the regex treated `\gla`-style patterns as escapes; fixed-string and narrower searches were used instead.
- A generated-module search for backtick code markers produced a false positive on JavaScript template literals around `Preservou`; the reliable check was narrowed to real `<pre` / `<code` markers and found none.

## Remaining Questions

- The visible example translations remain in English to match the paper sources. A later Portuguese translation pass could localize the gloss translations if preferred.
- No browser screenshot was taken, following the repo instruction.

## Suggested Next Prompt

Review slide 64 at `http://localhost:3033/64` and tighten the switch-reference wording if you want it more technical or more workshop-friendly.
