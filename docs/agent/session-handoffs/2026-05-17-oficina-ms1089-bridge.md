# Handoff: Coimbra ms. 1089 Bridge

## Goal

Add a bridge between the Finbow/Língua Geral Amazônica restructuring block and the later Nheengatu/grammar material using Coimbra ms. 1089 as evidence that the vulgar Amazonian Língua Geral entered catechetical writing.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/Downloads/admdoi,+REL-2004-71.pdf`
- `/Users/kian/Downloads/Fontes manuscritas sobre a língua geral da Amazônia escritas por jesuítas tapuitinga (século XVIII).pdf`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-ms1089-bridge.md`

## Commands Run

- `sed` targeted reads over agent docs, deck, and CSS.
- `rg` searches over the deck, CSS, memory index, and generated modules.
- `ls -l` and `file` on the two user-mentioned PDFs.
- `command -v pdftotext; command -v mutool; command -v qpdf; command -v pdfinfo; command -v strings`
- `strings -n 8 ... | rg ...` on both PDFs.
- `mdls -name kMDItemTextContent ...` on both PDFs.
- `textutil -convert txt -stdout ... | rg ...` on both PDFs.
- `npm run build`
- `git diff --check`
- `rg --files dist/oficina-unb/assets | rg '/md-.*\.js$' | wc -l`
- Generated-module `rg` checks for the six new slide titles and key examples.
- Generated-module `<pre>/<code` checks.
- `./node_modules/.bin/slidev decks/oficina-unb.md --port 3033`
- `curl -I http://localhost:3033/50`
- `curl -I http://localhost:3033/55`

## What Worked

- Inserted six slides after `Mudança não é invenção` and before `Nomes e descrições na documentação`.
- The slides treat ms. 1089 as anonymous/undated Coimbra ms. 1089, safely framed as 18th-century Amazonian Língua Geral rather than classical Tupi Antigo or named Nheengatu.
- The block now covers:
  - `Um manuscrito de transição`
  - `Duas formas de dizer “não tem corpo”`
  - `O catecismo oficial conserva a norma antiga`
  - `Antes de “ti”: nitio / nitíu`
  - `Da moldura verbal à partícula negativa`
  - `Nem Tupi Antigo clássico, nem ainda “Nheengatu”`
- Added `ms1089-*` CSS for text-first manuscript bridge layouts and compact gloss cards.
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated output contains 71 `md-*.js` slide modules.
- The new bridge slides are generated as `slidev_50` through `slidev_55`.
- `curl -I http://localhost:3033/50` and `/55` return `HTTP/1.1 200 OK`.

## What Failed

- No dedicated PDF text extractor was available in the shell (`pdftotext`, `mutool`, `qpdf`, and `pdfinfo` were not present).
- `strings` only surfaced PDF metadata; it did not expose the relevant article text.
- `mdls` did not return Spotlight text content for the provided PDF paths.
- `textutil` treated the PDFs as binary and did not produce usable text.
- Starting Slidev inside the sandbox failed with `listen EPERM` on `::1:3033`; rerunning with approved escalation started the local server.

## Remaining Questions

- The slide content follows the user's pasted source notes because local PDF text extraction was not available. If exact wording from the PDFs is needed later, install/use a PDF text extractor or inspect the PDFs manually.
- No Playwright screenshots were taken, per repo instruction.

## Suggested Next Prompt

Review slides 50-55 at `http://localhost:3033/50` and decide whether the six-slide bridge should stay as a full block or be compressed to the negation-focused subset.
