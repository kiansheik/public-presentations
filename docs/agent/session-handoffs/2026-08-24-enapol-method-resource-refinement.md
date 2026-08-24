# ENAPOL Method And Resource Refinement Handoff

## Goal

Refine the committed second-pass ENAPOL deck without restarting it: remove the disliked vertical-line background, replace the generic bootstrapping cycle with the actual reusable method, add click reveals and a with-clicks PDF export, clarify the Doutorado Direto transition, add a concrete research payoff, add a final resource/QR slide, and produce a real speaker script.

## Files Inspected

- `/Users/kian/.codex/attachments/61aa7b96-562c-460a-90c0-7d465fc4251b/pasted-text.txt`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `decks/components/EnapolImage.vue`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `package.json`
- `scripts/build-all.mjs`
- `/Users/kian/code/nhe-enga/README.md`
- `/Users/kian/code/neologismotupi/README.md`
- `/Users/kian/code/oldtupicorpus/README.md`
- `/Users/kian/code/tupi-antigo-switch-reference/README.md`
- `/Users/kian/code/latex/swith_ref_tupi_2025/main.tex`
- `/Users/kian/code/tupi-antigo-switch-reference/annotated_citations.json`

## Files Changed

- `README.md`
- `decks/enapol-2026-executable-grammar.md`
- `styles/enapol-2026-executable-grammar.css`
- `package.json`
- `public/assets/enapol-2026-executable-grammar/README.md`
- `public/assets/enapol-2026-executable-grammar/qr-dictionary.svg`
- `public/assets/enapol-2026-executable-grammar/qr-corpus.svg`
- `public/assets/enapol-2026-executable-grammar/qr-neo.svg`
- `notes/enapol-2026-executable-grammar.md`
- `enapol-2026-executable-grammar-export.pdf`
- `enapol-2026-executable-grammar-clicks-export.pdf`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-08-24-enapol-method-resource-refinement.md`

## Commands Run

- `git status --short --branch`
- `git log --oneline --decorate -5`
- `./node_modules/.bin/slidev export --help`
- `curl -I https://kiansheik.io/nhe-enga/`
- `curl -I https://neo.academiatupi.com`
- `curl -I https://github.com/kiansheik/oldtupicorpus`
- `curl -I https://github.com/kiansheik/tupi-antigo-switch-reference`
- `curl -I https://kiansheik.io/nhe-enga/gramatica/`
- Node script using `uqr` to generate QR SVGs
- Node script computing switch-reference DS/SS counts from `annotated_citations.json`
- `npm run build`
- `git diff --check`
- `rg -n "repeating-linear-gradient|cycle-diagram|loop-slide|<code|<pre" decks/enapol-2026-executable-grammar.md styles/enapol-2026-executable-grammar.css`
- `npm run dev:enapol-2026 -- --port 3037`
- Playwright/Chromium screenshot and DOM bounds checks for all 10 slides and slide 6 click states
- `npm run export:enapol-2026:pdf:clicks`
- `npm run export:enapol-2026:pdf`
- `file enapol-2026-executable-grammar-export.pdf enapol-2026-executable-grammar-clicks-export.pdf`

## What Worked

- The ENAPOL repeated vertical-line backgrounds were removed from the deck CSS.
- The bootstrapping slide now uses a click-revealed arrow methodology with persistent `GRAMATICA + LEXICO`, line selection, morpheme reuse/definition, abstract pydicate structure, spell-out, linguistic comparison, validation, full regression, YES/NO branch, and long-term local-correction callout.
- The deck is now 10 logical slides and includes the Doutorado Direto trajectory, switch-reference payoff, full-corpus infrastructure, and QR resource close.
- Slidev 52.15.2 supports `--with-clicks`; the new export script produced a separate click-state PDF.
- The final visual pass found no out-of-canvas elements; manual screenshot inspection caught and fixed slide 6 raw HTML/overlap and slide 10/9 text overlap issues.

## What Failed

- Starting Slidev inside the sandbox failed with `EPERM` on `::1:3037`; the approved escalated rerun started `http://localhost:3037/`.
- The first slide 6 markup rendered raw HTML because a blank line split nested raw HTML blocks; removing the blank lines fixed it.
- The first slide 6 final click state overlapped because the method diagram was too tall; tighter typography and row allocation fixed it.
- The first slide 10 QR layout and slide 9 bullet list had text overlap/clipping; both were fixed with targeted CSS.

## Remaining Questions

- Decide whether the Amazônicas X slide should cite the current local source numbers (62 examples, 96.77% DS) or the ResearchGate abstract numbers (53 examples, 96.23% DS).
- Replace the remaining source/example/app placeholders with real screenshots and page references.
- Confirm final exact corpus example, glossing, and phenomenon for slides 3 and 5.

## Suggested Next Prompt

Use the current deck at `http://localhost:3037/` to rehearse once with presenter notes and the standalone script, then choose the switch-reference citation version and replace the remaining screenshot placeholders.
