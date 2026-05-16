# 2026-05-14 Handoff: Make Help And Consolidated gh-pages Deploy

## Goal

Add a Makefile help command and make `deploy-gh-pages` perform the full branch deploy: build `dist/`, update the `gh-pages` worktree, create an automated commit, and push that branch.

## Files Inspected

- `AGENTS.md`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `.gitignore`
- `Makefile`
- `README.md`
- `package.json`
- `scripts/build-all.mjs`

## Files Changed

- `Makefile`
- `README.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-14-make-help-consolidated-gh-pages-deploy.md`

Note: `.gitignore` already had a pending `.gh-pages/` ignore entry before this pass; it remains part of the deploy-related worktree diff.

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,260p' docs/agent/current-state.md`
- `sed -n '1,260p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `sed -n '1,240p' Makefile`
- `sed -n '1,260p' README.md`
- `sed -n '1,240p' package.json`
- `git status --short`
- `git diff -- Makefile`
- `git diff -- README.md`
- `git diff -- docs/agent/current-state.md docs/agent/log.md docs/agent/repo-map.md`
- `sed -n '1,180p' .gitignore`
- `sed -n '1,260p' scripts/build-all.mjs`
- `git branch --show-current`
- `git worktree add -h`
- `make help`
- `make -n prepare-gh-pages`
- `make -n deploy-gh-pages`
- `make build`
- Temporary Git repo check for `git worktree add --orphan -b gh-pages gh-pages-worktree`
- `sed -n '1,220p' AGENTS.md`
- `rg -n "deploy-gh-pages|prepare-gh-pages|push-gh-pages|gh-pages|Makefile" Makefile README.md docs/agent`

## What Worked

- `make help` prints the Makefile command index and current deploy variables.
- `make prepare-gh-pages` dry-run expands to build, create or reuse `.gh-pages`, copy `dist/`, preserve `CNAME`, add `.nojekyll`, stage, and commit with `PAGES_MESSAGE`.
- `make deploy-gh-pages` dry-run now includes the push: `git -C ".gh-pages" push -u "origin" "HEAD:gh-pages"`.
- The default commit message is generated as `Deploy public presentations from <source-sha>` and can be overridden with `PAGES_MESSAGE=...`.
- Existing `.gh-pages` worktrees are reused only when their current branch matches `PAGES_BRANCH`.
- The orphan worktree creation form `git worktree add --orphan -b gh-pages <path>` was verified in a temporary Git repo.
- `make build` succeeds.

## What Failed

- The real `make deploy-gh-pages` target was not run because it would commit generated output in the Pages worktree and push to `origin/gh-pages`.

## Remaining Questions

- Confirm the GitHub Pages repository setting after first push: source should be the `gh-pages` branch, root folder.
- If the repository name changes from `public-presentations`, run deploy with `SLIDEV_BASE=/repo-name/` or update the build fallback.

## Suggested Next Prompt

Run `make deploy-gh-pages` when ready to publish; if GitHub Pages serves broken asset paths after the push, ask to verify the configured Pages URL and `SLIDEV_BASE`.
