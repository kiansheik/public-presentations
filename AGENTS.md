# Agent Instructions

For the given repo you are editing...

## Before Editing Code

1. Read `docs/agent/index.md`.
2. Read `docs/agent/current-state.md`.
3. Read `docs/agent/repo-map.md`.
4. Check `docs/agent/open-questions.md`.
5. Use `rg`, `git grep`, `find`, and targeted file reads before opening large files.

## Source Of Truth

- Code, tests, schemas, and checked-in configs are the source of truth.
- `docs/agent/` is compiled memory. If it disagrees with the code, trust the code and update the wiki.
- Do not invent behavior. Mark uncertainty clearly.

## Context Discipline

- Do not load the whole repo into context.
- Prefer compact summaries and targeted reads.
- When exploring broadly, summarize findings into `docs/agent/repo-map.md` or a domain page.
- Keep generated notes concise and linked.

## Browser Verification

- Do not take Playwright screenshots unless the user explicitly requests screenshots.
- Prefer build checks, DOM/static assertions, and a local dev-server URL for visual review; the user can inspect slides directly and give feedback faster.

## After Significant Work

Update these files:

1. `docs/agent/current-state.md`
2. `docs/agent/log.md`
3. A new handoff in `docs/agent/session-handoffs/`

The handoff must include:

- Goal
- Files inspected
- Files changed
- Commands run
- What worked
- What failed
- Remaining questions
- Suggested next prompt

## Coding Rules

- Prefer small, reviewable diffs.
- Do not edit generated files unless explicitly asked.
- Do not run destructive commands without explicit user approval.
- Run the narrowest useful tests/checks for the change.
- If tests cannot be run, explain why in the handoff.
