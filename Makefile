PAGES_BRANCH ?= gh-pages
PAGES_WORKTREE ?= .gh-pages
PAGES_REMOTE ?= origin
PAGES_SOURCE_REF := $(shell git rev-parse --short HEAD 2>/dev/null || echo unknown)
PAGES_MESSAGE ?= Deploy public presentations from $(PAGES_SOURCE_REF)

.DEFAULT_GOAL := help

.PHONY: help build gh-pages-worktree prepare-gh-pages deploy-gh-pages push-gh-pages push

help:
	@printf "Public presentation commands:\n"
	@printf "  make build             Build all Slidev decks into dist/\n"
	@printf "  make prepare-gh-pages  Build and commit dist/ into $(PAGES_BRANCH) without pushing\n"
	@printf "  make deploy-gh-pages   Build, commit, and push dist/ to $(PAGES_REMOTE)/$(PAGES_BRANCH)\n"
	@printf "  make push-gh-pages     Push the prepared $(PAGES_WORKTREE) worktree\n"
	@printf "\nDeploy variables:\n"
	@printf "  PAGES_BRANCH=%s\n" "$(PAGES_BRANCH)"
	@printf "  PAGES_WORKTREE=%s\n" "$(PAGES_WORKTREE)"
	@printf "  PAGES_REMOTE=%s\n" "$(PAGES_REMOTE)"
	@printf "  PAGES_MESSAGE=\"%s\"\n" "$(PAGES_MESSAGE)"

build:
	npm run build

gh-pages-worktree:
	@if git -C "$(PAGES_WORKTREE)" rev-parse --is-inside-work-tree >/dev/null 2>&1; then \
		current_branch=$$(git -C "$(PAGES_WORKTREE)" branch --show-current); \
		if [ "$$current_branch" != "$(PAGES_BRANCH)" ]; then \
			echo "$(PAGES_WORKTREE) is on '$$current_branch', expected '$(PAGES_BRANCH)'."; \
			exit 1; \
		fi; \
		echo "Using existing $(PAGES_WORKTREE) worktree"; \
	elif git show-ref --verify --quiet refs/heads/$(PAGES_BRANCH); then \
		git worktree add "$(PAGES_WORKTREE)" "$(PAGES_BRANCH)"; \
	elif git ls-remote --exit-code --heads "$(PAGES_REMOTE)" "$(PAGES_BRANCH)" >/dev/null 2>&1; then \
		git fetch "$(PAGES_REMOTE)" "$(PAGES_BRANCH):$(PAGES_BRANCH)"; \
		git worktree add "$(PAGES_WORKTREE)" "$(PAGES_BRANCH)"; \
	else \
		echo "Creating orphan $(PAGES_BRANCH) worktree at $(PAGES_WORKTREE)"; \
		git worktree add --orphan -b "$(PAGES_BRANCH)" "$(PAGES_WORKTREE)"; \
	fi

prepare-gh-pages: build gh-pages-worktree
	@find "$(PAGES_WORKTREE)" -mindepth 1 -maxdepth 1 ! -name .git ! -name CNAME -exec rm -rf {} +
	@cp -R dist/. "$(PAGES_WORKTREE)/"
	@touch "$(PAGES_WORKTREE)/.nojekyll"
	@git -C "$(PAGES_WORKTREE)" add -A
	@if git -C "$(PAGES_WORKTREE)" diff --cached --quiet; then \
		echo "No gh-pages changes to commit."; \
	else \
		git -C "$(PAGES_WORKTREE)" commit -m "$(PAGES_MESSAGE)"; \
	fi
	@echo "Prepared $(PAGES_BRANCH). Push with: make push-gh-pages"

deploy-gh-pages: prepare-gh-pages
	git -C "$(PAGES_WORKTREE)" push -u "$(PAGES_REMOTE)" "HEAD:$(PAGES_BRANCH)"
	@echo "Deployed $(PAGES_BRANCH) to $(PAGES_REMOTE)."

push-gh-pages: gh-pages-worktree
	git -C "$(PAGES_WORKTREE)" push -u "$(PAGES_REMOTE)" "HEAD:$(PAGES_BRANCH)"

push:
	git add .
	git commit
	git push origin HEAD
