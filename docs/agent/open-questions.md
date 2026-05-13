# Open Questions

- Confirm whether `public-presentations` is the final GitHub repository name. `scripts/build-all.mjs` uses that as the local fallback base path and `GITHUB_REPOSITORY` in Actions.
- Confirm whether a tracked source-level `index.html` is wanted. The deployed landing page is currently generated as `dist/index.html`.
- Confirm the final deck list and titles before publishing beyond the three starter decks.
- Decide whether `@slidev/theme-default` should remain installed as an optional fallback theme or be removed in a later dependency cleanup.
