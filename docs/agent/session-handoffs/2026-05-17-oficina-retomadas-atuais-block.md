# Oficina UnB Retomadas Atuais Block

## Goal

Add the missing final block promised by the workshop description: continuities after Tupi Antigo through Nheengatu plus current retomadas of Tupi Antigo, using images and citations from the qualification PDF/assets.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `/Users/kian/code/latex/qualification/qualification.tex`
- `/Users/kian/code/latex/mestrado/body/content.tex`
- `/Users/kian/code/latex/mestrado/body/contemporary.tex`
- `/Users/kian/code/latex/qualification/qualificationtr.pdf` via existing page-image assets

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-17-oficina-retomadas-atuais-block.md`

## Commands Run

- `rg -n "Pai Nosso|retom|Potiguara|Tupinamb|Tupinaky|Tupiniquim|USP|Nheengatu|Do arquivo|O Tupi que" decks/oficina-unb.md`
- `tail -n 420 decks/oficina-unb.md`
- `find public/assets/oficina-unb -maxdepth 2 -type f | sort`
- `rg -n '\\(include|input)|Contemporary|context|revitali|Potiguara|Tupinamb|Tupinaky|Tupiniquim|Akangatara|CPB|Navarro|Tor[eé]|Oliven|no known|native' /Users/kian/code/latex/qualification -g '*.tex'`
- `rg -n "revitalization|Potiguara|Tupinamb|Tupinaky|Tupiniquim|Akangatara|CPB|Contemporary|speaker|native|No known|Old Tupi" /Users/kian/code/latex/mestrado -g '*.tex'`
- `sips -g pixelWidth -g pixelHeight public/assets/oficina-unb/qualification-*.png`
- `npm run build`
- `git diff --check`
- generated module title checks against `dist/oficina-unb/assets/md-*.js`
- generated `<pre>/<code` and `` `pre` `` checks against `dist/oficina-unb/assets/md-*.js`
- `curl -I http://localhost:3033/72`
- headless Playwright DOM bounds/image-load checks for slides 72-78; no screenshots

## What Worked

- The existing `decks/oficina-unb.md` already contained the requested seven-slide content block and referenced the qualification-derived images.
- Added the missing shared `retomada-*` CSS so those slides render in the Oficina visual system with left-side content, right-side qualification crops, a media collage, and a closing grid.
- Documented qualification-derived assets in `public/assets/oficina-unb/README.md`.
- `npm run build` succeeds.
- Generated output contains 78 slide modules and 7 retomada slide modules.
- DOM checks on `http://localhost:3033/72` through `/78` found the expected titles, loaded image natural sizes, and no element overflow in a 1280x720 viewport.

## What Failed

- `pdfimages`, `pdftotext`, `magick`, `convert`, `mutool`, and `pdfinfo` were not available.
- The first headless browser launch failed in the sandbox with macOS Mach port permission errors; rerunning with approved escalation worked.
- The first DOM selector attempted to wait for a visible `.retomada-slide` while Slidev had multiple preloaded slides; switching to `.slidev-page-<n> .retomada-slide` fixed the check.

## Remaining Questions

- Confirm whether the qualification screenshots should remain cropped page images or be replaced later with tighter excerpt images for each retomada subsection.
- `qualification-retomadas-p22.png` is a PDF page crop used across Potiguara, Tupinambá, and Tupinakyîa; a future pass could add more specific images if the qualification PDF is regenerated with the expanded Tupinambá source text.

## Suggested Next Prompt

Review slides 72-78 at `http://localhost:3033/` and tell me which of the retomada slides should be shortened, expanded, or swapped to a tighter source image crop.
