# 2026-05-15 Handoff: Actions Configure Pages Failure

## Goal

Fix the GitHub Actions failure at `actions/configure-pages@v5` where GitHub returned `Get Pages site failed` because the repository was not already configured to deploy Pages via GitHub Actions.

## Files Inspected

- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/open-questions.md`
- `.github/workflows/deploy.yml`
- `Makefile`
- `README.md`
- `docs/agent/log.md`

## Files Changed

- `.github/workflows/deploy.yml`
- `README.md`
- `docs/agent/current-state.md`
- `docs/agent/repo-map.md`
- `docs/agent/log.md`
- `docs/agent/session-handoffs/2026-05-15-actions-configure-pages-failure.md`

## Commands Run

- `sed -n '1,220p' docs/agent/index.md`
- `sed -n '1,260p' docs/agent/current-state.md`
- `sed -n '1,260p' docs/agent/repo-map.md`
- `sed -n '1,220p' docs/agent/open-questions.md`
- `sed -n '1,240p' .github/workflows/deploy.yml`
- `sed -n '1,160p' Makefile`
- `git status --short`
- `find .github -maxdepth 3 -type f -print`
- `sed -n '1,120p' README.md`
- `sed -n '1,130p' docs/agent/current-state.md`
- `sed -n '32,70p' docs/agent/repo-map.md`
- `sed -n '1,120p' docs/agent/log.md`
- `ruby -e 'require "yaml"; YAML.load_file(".github/workflows/deploy.yml"); puts "workflow yaml ok"'`
- `make -n deploy-gh-pages`
- `make help`
- `git diff --check`
- `make build`
- `sed -n '1,180p' .github/workflows/deploy.yml`
- `git diff -- .github/workflows/deploy.yml README.md docs/agent/current-state.md docs/agent/repo-map.md docs/agent/log.md docs/agent/session-handoffs/2026-05-15-actions-configure-pages-failure.md`
- `git status --short`

## What Worked

- Replaced the Pages artifact workflow with a build-only workflow.
- Removed `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages` from the workflow.
- Changed workflow permissions from `pages: write` and `id-token: write` to `contents: read`.
- Updated README and agent docs to say Pages should be configured to serve from `gh-pages` branch root.
- Kept real branch publishing in `make deploy-gh-pages`, which should be run from local credentials rather than `GITHUB_TOKEN` if the repository is configured for branch-based Pages.
- Workflow YAML parses locally.
- `make -n deploy-gh-pages`, `make help`, `git diff --check`, and `make build` succeed locally.

## What Failed

- The live GitHub Actions workflow was not rerun from this local session.
- The real deploy command was not run locally because it would commit generated output and push to `origin/gh-pages`.

## Remaining Questions

- Confirm GitHub repository settings: Pages source should be `Deploy from a branch`, branch `gh-pages`, folder `/`.
- If the repository wants to return to GitHub Actions artifact deployment later, Pages must first be configured for GitHub Actions or `actions/configure-pages` must be given a non-`GITHUB_TOKEN` token with the required Pages/admin permissions.
- If the repository wants fully automatic branch deployment from Actions, use a PAT or GitHub App token rather than `GITHUB_TOKEN`; GitHub does not trigger Pages branch builds from `GITHUB_TOKEN` commits.

## Suggested Next Prompt

Push this workflow change to `main` to confirm Actions now passes as a build check, then run `make deploy-gh-pages` from a local checkout when ready to publish.
