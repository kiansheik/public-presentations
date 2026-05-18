# 2026-05-18 Oficina Distribution Map Slide

## Goal

Add a slide after `Três olhares, uma convergência` with two side-by-side images from the user's mestrado files, framing them as estimates of geographic distributions of peoples in 16th-century Brazil.

## Files Inspected

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `decks/components/DeckImage.vue`
- `/Users/kian/code/latex/mestrado/tupi_dist_mapa.jpg`
- `/Users/kian/code/latex/mestrado/rendtrans.png`

## Files Changed

- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/README.md`
- `public/assets/oficina-unb/tupi-dist-mapa.jpg`
- `public/assets/oficina-unb/rendtrans.png`
- `docs/agent/current-state.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-18-oficina-distribution-map-slide.md`

## Commands Run

- `rg -n "Três olhares|O que vamos chamar|distribution-map|tupi-dist|rendtrans" decks/oficina-unb.md styles/oficina-unb.css public/assets/oficina-unb/README.md`
- `ls -lh public/assets/oficina-unb/tupi-dist-mapa.jpg public/assets/oficina-unb/rendtrans.png`
- `sed -n '450,530p' decks/oficina-unb.md`
- `sed -n '680,750p' styles/oficina-unb.css`
- `sed -n '1,180p' public/assets/oficina-unb/README.md`
- `cp /Users/kian/code/latex/mestrado/tupi_dist_mapa.jpg public/assets/oficina-unb/tupi-dist-mapa.jpg`
- `cp /Users/kian/code/latex/mestrado/rendtrans.png public/assets/oficina-unb/rendtrans.png`
- `git diff --check`
- `npm run build`
- `rg -n "Distribuições estimadas no Brasil do século XVI|tupi-dist-mapa.jpg|rendtrans.png|Estimativas de distribuição de povos" dist/oficina-unb/assets/md-*.js`
- `rg -n '<raw HTML code marker pattern>' dist/oficina-unb/assets/md-*.js`
- `rg --files dist/oficina-unb/assets | rg '/md-.*\.js$' | wc -l`
- `./node_modules/.bin/slidev decks/oficina-unb.md -p 3034 --bind 127.0.0.1 --log info`
- Playwright Chromium DOM checks on `http://localhost:3034/18` without screenshots.

## What Worked

- The new slide is route `/18` and comes immediately after `Três olhares, uma convergência`.
- Both copied images are resolved by `DeckImage`: `tupi-dist-mapa.jpg` and `rendtrans.png`.
- The final DOM check confirms two loaded images, no overflow, and no overlap between the map cards and the estimate note.
- The production build emits 89 generated slide modules.

## What Failed

- Starting Slidev with `--host` failed because this Slidev version does not support that argument; `--bind` is the supported option.
- Starting Slidev inside the sandbox failed with `EPERM`; the local server required approved escalation.
- Port `3033` was already in use, so the verified server is on `http://localhost:3034/`.
- The first Markdown version had a blank line between the two `<figure>` tags; generated output showed the second image as a code block. Removing that blank line fixed the raw-HTML parsing.

## Remaining Questions

- None for this request. The user may still want source labels or a bibliography footnote for the two maps if these images need formal publication citations beyond local provenance.

## Suggested Next Prompt

Review slide 18 at `http://localhost:3034/18` and decide whether the map captions should name the original map/source more explicitly.
