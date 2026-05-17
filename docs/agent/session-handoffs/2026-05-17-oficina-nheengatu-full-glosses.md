# Handoff: Full Glosses For Nheengatu Grammar Slides

## Goal

Replace the shortened examples in the newly added `O que mudou do Tupi Antigo ao Nheengatu?` block with the full original, morpheme gloss, and translation lines from the user's paper.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `/Users/kian/code/latex/nheengatu_loss/main.pdf`
- `/Users/kian/code/latex/nheengatu_loss/main.tex`
- `/Users/kian/code/latex/nheengatu_loss/references.bib`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-nheengatu-full-glosses.md`

## Commands Run

- `find /Users/kian/code/latex/nheengatu_loss -maxdepth 2 -type f`
- `pdftotext -layout /Users/kian/code/latex/nheengatu_loss/main.pdf -`
- `rg` searches over `main.tex`, `references.bib`, `decks/oficina-unb.md`, and generated Slidev modules.
- `sed` targeted reads over the deck, CSS, and paper source.
- `npm run build`
- `git diff --check`
- `curl -I http://localhost:3033/`
- Headless Playwright DOM bounds check for slides 57-64.

## What Worked

- `main.tex` contained the full `expex` examples adjacent to the user-provided PDF, which was the most reliable way to preserve the full `\gla`, `\glb`, and `\glft` lines.
- Replaced shortened slide examples with full gloss blocks for:
  - estatives
  - gerund/subordination
  - negation
  - future
  - phonetic composition
  - Indicative II/existential fossilization
- Added `change-gloss` and `change-dense-grid` CSS so original line, morpheme gloss, translation, and source can fit within the existing slide structure.
- `npm run build` succeeds.
- `git diff --check` succeeds.
- Generated modules include representative full strings from the paper source and contain no raw `<pre>` / `<code>` markers.
- Headless DOM bounds check reports slides 57-64 as `ok`.

## What Failed

- `pdftotext` is not installed in this environment, so the PDF could not be text-extracted directly.
- Chromium still needs to run outside the sandbox for DOM checks on this macOS setup.

## Remaining Questions

- The visible translations are now the English translations from the paper source. If the workshop audience should see Portuguese translations instead, that should be a separate pass because it would no longer be “as is” from the paper.
- The reserve topics from the longer 18-slide draft remain unadded.

## Suggested Next Prompt

Review slides 57-64 at `http://localhost:3033/` and decide whether to keep the paper's English gloss translations or add Portuguese paraphrases as separate presenter notes.
