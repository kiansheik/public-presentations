# 2026-05-14 Handoff: gh-pages Make Deploy

## Goal

Add a Makefile command path for building all Slidev decks and deploying the generated `dist/` files to a `gh-pages` branch after the user initializes that branch.

## Files Inspected

- `AGENTS.md`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `Makefile`
- `package.json`
- `scripts/build-all.mjs`
- `README.md`

## Files Changed

- `Makefile`
- `.gitignore`
- `README.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-14-gh-pages-make-deploy.md`

## Commands Run

- `sed -n '1,160p' AGENTS.md`
- `sed -n '1,140p' docs/agent/index.md`
- `sed -n '1,160p' docs/agent/current-state.md`
- `sed -n '1,180p' docs/agent/repo-map.md`
- `sed -n '1,120p' docs/agent/open-questions.md`
- `sed -n '1,220p' Makefile`
- `sed -n '1,240p' package.json`
- `sed -n '1,260p' scripts/build-all.mjs`
- `sed -n '1,260p' README.md`
- `git branch --show-current`
- `make -n deploy-gh-pages`
- `make -n push-gh-pages`
- `make build`

## What Worked

- Added `make build` as a wrapper around `npm run build`.
- Added `make deploy-gh-pages` to build `dist/`, create or reuse a `.gh-pages` worktree for the `gh-pages` branch, replace published files with the current `dist/`, preserve `CNAME`, add `.nojekyll`, and commit the result.
- Added `make push-gh-pages` as a separate explicit push step.
- Documented one-time `gh-pages` branch initialization through `git worktree add --orphan .gh-pages gh-pages`.
- Added `.gh-pages/` to `.gitignore` so the main branch does not show the deploy worktree as untracked.
- `make -n deploy-gh-pages` and `make -n push-gh-pages` expand as expected.
- `make build` succeeds.

## What Failed

- The deploy target itself was not run because it modifies a branch worktree and commits generated output.

## Remaining Questions

- Confirm the GitHub Pages repository setting after the branch is pushed: source should be the `gh-pages` branch, root folder.
- If the repository name changes from `public-presentations`, set `SLIDEV_BASE=/repo-name/ make deploy-gh-pages`.

## Suggested Next Prompt

After committing the source branch and initializing `gh-pages`, run `make deploy-gh-pages` and `make push-gh-pages`; if GitHub Pages serves a wrong base path, ask to adjust `SLIDEV_BASE` or the build fallback.
