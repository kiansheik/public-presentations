# 2026-05-14 Handoff: Oficina Brasil Witness Slides

## Goal

Implement the first Brasil block in `decks/oficina-unb.md` with five slides covering Anchieta, Cardim, Gabriel Soares de Sousa, and their convergence around a broad coastal Indigenous language. Also preserve the user's workflow preference that agents should not take Playwright screenshots unless explicitly requested.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `public/assets/oficina-unb/`
- `dist/oficina-unb/`

## Files Changed

- `AGENTS.md`
- `decks/oficina-unb.md`
- `styles/oficina-unb.css`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-14-oficina-brasil-witness-slides.md`

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,220p' docs/agent/current-state.md`
- `sed -n '1,220p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `rg --files public/assets/oficina-unb`
- `sed -n '1,320p' decks/oficina-unb.md`
- `sed -n '1,460p' styles/oficina-unb.css`
- `npm run build`
- `curl -I http://localhost:3031/`
- `rg -n "A língua mais usada|Anchieta: um missionário|Cardim: muitas nações|Gabriel Soares de Sousa|Três olhares|anchieta-arte-grammatica|&lt;blockquote|<pre><code>" dist/oficina-unb`
- `find .. -name AGENTS.md -print`
- `git status --short`
- `sed -n '1,220p' AGENTS.md`
- `rg -n "Do not take Playwright screenshots|Verified on 2026-05-14|Brasil witness|A língua mais usada|Três olhares" AGENTS.md docs decks/oficina-unb.md styles/oficina-unb.css`

## What Worked

- The five new slides were added after the question slide, keeping the existing Oficina visual system.
- The first Brasil slide uses the existing `DeckImage` component with `anchieta-arte-grammatica.png`, so the manuscript asset is bundled through Vite instead of a fragile raw path.
- New CSS classes keep the Brasil source/witness slides aligned with the existing half-split system while giving quote and convergence slides their own layout.
- `npm run build` completed successfully.
- Static generated-bundle checks found the new slide titles/classes and the Anchieta image import.
- A root `AGENTS.md` was created because the repo did not have one checked in. It now includes the no-Playwright-screenshots-unless-requested rule.

## What Failed

- Headless Chromium visual verification for slides 11-15 was not completed because the escalation request was rejected.
- No Playwright screenshots were taken for the new slides, matching the later user preference.

## Remaining Questions

- The new Brasil witness slides should be visually reviewed by the user in the running deck and adjusted if any title, quote, or text block feels too dense.
- The exact primary-source citation wording for the Anchieta/Cardim/Gabriel quotes may still need bibliographic tightening if the final deck needs formal references.

## Suggested Next Prompt

Review slides 11-15 in the local deck, then ask for any specific spacing, hierarchy, citation, or image-placement adjustments based on what you see.
