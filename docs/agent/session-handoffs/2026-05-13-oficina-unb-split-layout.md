# 2026-05-13 Oficina UnB Split Layout Handoff

## Goal

Restore the PPTX-like half-split Oficina layout after manuscript image loading was fixed: text on the left, images on the right, with theme defaults no longer overriding the deck styling.

## Files inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `decks/components/DeckImage.vue`
- `node_modules/@slidev/cli/skills/slidev/references/style-scoped.md`
- selected Slidev CLI internals for style entry resolution

## Files changed

- `decks/oficina-unb.md`
- `decks/styles/index.css`
- `styles/oficina-unb.css`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-13-oficina-unb-split-layout.md`

## Commands run

- `sed -n ... docs/agent/*`
- `sed -n ... styles/oficina-unb.css`
- `sed -n ... decks/oficina-unb.md`
- `find . -maxdepth 4 -type f ...`
- `rg -n "style.*src|global src|<style" node_modules/@slidev ...`
- `sed -n ... node_modules/@slidev/cli/skills/slidev/references/style-scoped.md`
- `sed -n ... node_modules/@slidev/cli/dist/shared-CmTSrQGO.mjs`
- `npm run build`
- Headless Playwright layout measurements for slides 2-8 at `http://localhost:3031/`
- Headless Playwright screenshots for slides 3, 5, and 8

## What worked

- Moving the stylesheet import from `decks/oficina-unb.md` into `decks/styles/index.css` made the Oficina CSS global for all generated slide components.
- `styles/oficina-unb.css` now defines a consistent split frame with left and right column variables.
- Left-column titles/body text now stay in the left half, and manuscript images are normalized inside the right half.
- The Seriph theme blockquote background, title color, and default list markers are overridden for `.slidev-layout.oficina-unb`.
- `npm run build` succeeds.
- Browser checks on slides 2-8 showed the left text column ending around x=609 and right image content starting around x=666 on a 1280px viewport.

## What failed

- The previous deck-level `<style global src="../styles/oficina-unb.css">` did not work as intended. Slidev scoped it, so CSS either applied only through generated scoped selectors or did not apply to the currently loaded split slide components.
- Once the CSS was correctly global, Seriph theme defaults still overrode some title, blockquote, and list styling until higher-specificity Oficina selectors were added.

## Remaining questions

- Confirm by eye whether the current slide 5 and slide 8 image overlap matches the original PPTX closely enough, or whether each image needs per-slide tuning.

## Suggested next prompt

Compare the current `oficina-unb` screenshots against the original PPTX and tune individual slide image placements where the side-by-side split is correct but the collage/overlay proportions still differ.
