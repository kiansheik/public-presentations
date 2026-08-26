# Agent Log

## 2026-05-13

- Converted the single-deck starter into a root-level multi-deck Slidev repo.
- Renamed `slides.md` to `oficina-tupi-antigo.md`.
- Added starter decks for `lingua-geral-brasil.md` and `anchieta-contexto.md`.
- Added `scripts/build-all.mjs` to clean `dist/` and build each deck into `dist/<slug>/` with per-deck base paths.
- Added GitHub Pages Actions deployment for generated `dist`.
- Added `.gitignore` for `node_modules/`, `dist/`, `.slidev/`, and logs.
- Added deck-specific and shared asset folders.
- Verified `npm run build`.
- Fixed `decks/oficina-unb.md` rendering so nested raw HTML blockquotes are not parsed as escaped code blocks.
- Added `decks/components/DeckImage.vue` and switched Oficina UnB manuscript images to it so local/dev/build URLs resolve from `public/assets/oficina-unb/`.
- Verified `npm run build` and browser-checked slide 3 at `http://localhost:3031/3`.
- Moved Oficina CSS loading into `decks/styles/index.css` so Slidev applies it globally across split slide components.
- Normalized Oficina content slides to a half-split left text/right manuscript layout and fixed Seriph theme overrides on titles, blockquotes, and custom bullets.
- Re-verified with `npm run build`, browser measurements across slides 2-8, and screenshots for slides 3, 5, and 8.
- Expanded `README.md` into a project guide covering commands, repo structure, new deck setup, global style loading, image component conventions, and Oficina layout notes.

## 2026-05-14

- Added five Brasil witness slides to `decks/oficina-unb.md`: Anchieta title page, Anchieta, Cardim, Gabriel Soares de Sousa, and a convergence slide.
- Added Oficina CSS classes for Brasil source/witness/quote-panel/convergence layouts.
- Verified the deck with `npm run build` and static generated-bundle checks.
- Added root `AGENTS.md` and recorded that future agents should not take Playwright screenshots unless the user explicitly requests screenshots.
- Added Makefile targets for manual branch-based GitHub Pages deploy: `build`, `deploy-gh-pages`, and `push-gh-pages`.
- Documented the `.gh-pages` worktree deploy flow in `README.md`.
- Added `.gh-pages/` to `.gitignore`.
- Added `make help`, split no-push publishing into `make prepare-gh-pages`, and consolidated `make deploy-gh-pages` so it builds, commits, and pushes `gh-pages`.
- Updated the README Makefile docs to reflect the one-command branch deploy and deploy variable overrides.

## 2026-05-15

- Changed `.github/workflows/deploy.yml` from GitHub Pages artifact deployment to a build-only workflow, avoiding `actions/configure-pages@v5` when Pages is not configured for Actions.
- Kept branch publishing in `make deploy-gh-pages` and updated deploy docs to say GitHub Pages should serve from the `gh-pages` branch root.
- Appended five Anchieta grammar/use slides to `decks/oficina-unb.md` with right-side screenshot placeholders and speaker notes.
- Added Oficina CSS for the new grammar block, regional form lists, point labels, and placeholder text-shot frames.
- Verified with `npm run build`, a static generated-bundle title check, and `curl -I http://localhost:3032/`; started Slidev locally at `http://localhost:3032/`.

## 2026-05-16

- Inserted a fourteen-slide Tupi Antigo corpus-definition block into `decks/oficina-unb.md`, positioned after the Brasil convergence slide and before the Anchieta grammar slides.
- Defined Tupi Antigo as a finite corpus designation and added modular source fichas plus a central-corpus timeline.
- Added matching Oficina CSS for corpus definition, source-card, terminology-note, footer, and timeline layouts.
- Verified with `npm run build` and a static Slidev parser check showing 33 slides, with the corpus block on slides 15-28.
- Improved the opening quote-heavy source slides with scoped `source-quote-block` styling: warmer quote color, subtle dark backing, accent rule, tighter quote/source spacing, and softer citation color.
- Fixed the unclosed `<div>` in the Anchieta variation slide so the deck builds again with the new `apab.png` asset.
- Verified with `npm run build` and checked the user's existing `3030` Slidev server at `http://[::1]:3030/`; no Playwright screenshots were taken.
- Reworked the Quechua, Nahuatl, and Guarani case-study slides into clearer `language-case-block` layouts with dated source rows and separate takeaway/note styles.
- Verified the language case-slide readability pass with `npm run build` and `git diff --check`; no Playwright screenshots were taken.
- Corrected the speaker note for “A língua geral como objeto de ensino formal” so it focuses on cátedras, Lima/México, and formal missionary formation.
- Added a transition speaker note before the Tupi Antigo corpus-definition block and a presenter reminder to handle the source fichas as a fast archive map.
- Added the missing Anchieta closeout slide, “Entre o uso local e o uso mais universal,” and verified the deck with `npm run build`.
- Added an eight-slide “Quando a língua geral muda de ecologia” Amazônia/LGA block after the Anchieta closeout, using Finbow 2022 and João Daniel as the main scholarly frame.
- Styled the new block with `amazonia-*` CSS utilities for dense lists, two-column comparisons, demographic cycles, key points, and the closing thesis slide.
- Verified the expanded deck with `npm run build`; a static count now finds 42 `oficina-unb` slide declarations.

## 2026-05-17

- Fixed raw HTML spacing in the Amazônia/LGA block so nested lists, key points, contrast panels, cycles, and closing text render as slide UI instead of visible code blocks.
- Rebuilt with `npm run build` and verified generated slide modules contain no `<pre>`, `<code>`, or `` `pre` `` markers.
- Added a follow-up João Daniel slide, “A arte já não garantia entendimento,” with the Daniel/Finbow catechism-and-arte quote plus four takeaways about book norms, mission speech, Amazonas usage, and new nations learning the vernacular.
- Added CSS for the follow-up quote/takeaway layout and verified with `npm run build`.
- Added two João Maia da Gama slides after the Daniel follow-up: one frames the governor's question about non-Tupi aldeados learning Portuguese directly, and the next answers with the social-time contrast between brief Portuguese instruction and daily Língua Geral contact.
- Added `maia-*` CSS for the question and answer layouts.
- Verified with `npm run build`, `git diff --check`, generated slide-module raw-HTML checks, and generated `md-*.js` slide-module count.
- Appended two Finbow/Rodrigues caution slides to `decks/oficina-unb.md`, using the recommended two-slide structure: LGP/LGA as useful modern labels, then the Paulista Maranhão-Pará evidence for broad intelligibility.
- Verified the Finbow article page/PDF, rebuilt with `npm run build`, checked `git diff --check`, and confirmed generated `md-*.js` modules include both new titles without raw HTML code markers.
- Added a proportional names/glottonyms timeline slide before the Nheengatu-name block, covering 1547 through today across comparative Iberian, Brazil/Amazônia, and modern-label lanes.
- Added `name-timeline-*` CSS for the proportional rail and dense staggered labels; verified with `npm run build`, `git diff --check`, and generated slide-module raw-HTML checks.
- Simplified that dense names/glottonyms slide into `Quatro nomes na documentação`, limited to the Brazil/Amazônia labels requested by the user: Anchieta 1595, Araújo 1618, Manoel Gomes 1616, and Seixas 1853.
- Replaced the proportional timeline styling with a four-card `name-sequence-*` layout, moved the simplified slide before the Nheengatu detail slides, and re-verified with `npm run build`, `git diff --check`, generated-module content checks, and raw-HTML marker checks.
- Added a single Pombal/Diretório bridge slide between the names/descriptions synthesis and the Nheengatu-name detail slides, framing the Diretório as the state attempt to impose Portuguese and restrict Língua Geral.
- Retitled the Nheengatu transition to `Depois da repressão, o nome Nheengatu`; verified with `npm run build`, `git diff --check`, and generated-module checks for the new bridge/transition slides.
- Moved the Pai Nosso comparison table slide after every existing slide and rebuilt its layout in the Oficina dark theme, using a responsive grid/table treatment instead of the temporary white document-page CSS.
- Enlarged the Pai Nosso table typography after review feedback that the text was too small for the available whitespace.
- Verified the final slide order and rendering with `npm run build`, `git diff --check`, generated-module checks for `slidev_55`/`slidev_56`, raw HTML marker checks, and headless DOM layout checks on `/56`; no Playwright screenshots were taken.
- Added an eight-slide `O que mudou do Tupi Antigo ao Nheengatu?` grammar-change block after the Pai Nosso slide, using the user's shorter workshop sequence: thesis, estatives, gerund loss, negation, future, phonetic composition, Indicative II fossilization, and conclusion.
- Added shared `change-*` CSS for the new grammar-change cards and comparison layouts.
- Verified with `npm run build`, `git diff --check`, generated-module title/raw-HTML checks, `curl -I http://localhost:3033/`, and a headless DOM bounds check for slides 57-64; the first DOM attempt failed because it selected the wrong visible Slidev canvas, then the corrected indexed check passed. No screenshots were taken.
- Replaced the shortened grammar examples with full gloss blocks from `/Users/kian/code/latex/nheengatu_loss/main.tex`, preserving original line, morpheme gloss, and translation for the new linguistic example slides.
- Added denser `change-gloss` and `change-dense-grid` styling so the full paper examples fit within the existing eight-slide sequence.
- Verified with `npm run build`, `git diff --check`, generated-module raw-HTML checks, generated full-string checks, `curl -I http://localhost:3033/`, and a headless DOM bounds check for slides 57-64. `pdftotext` was not installed, so the adjacent paper source was used instead. No screenshots were taken.
- Added a dedicated `Switch reference: o sujeito ainda é o mesmo?` slide before the grammar-change synthesis, contrasting Old Tupi `-bo`/`-reme` with Nheengatu `ramé` in DS and SS contexts.
- Added `switch-reference-grid`, `switch-panel`, `switch-tag`, and `switch-keypoint` CSS under the shared grammar-change styles after the slide markup was added.
- Verified with `npm run build`, `git diff --check`, generated-module checks for the new title/examples, generated `<pre>/<code` checks, and `curl -I http://localhost:3033/64`; no Playwright screenshots were taken.
- Inserted a six-slide ms. 1089 bridge block immediately after the Finbow `Mudança não é invenção` slide, using the user's bibliographic correction that Coimbra ms. 1089 should be treated as anonymous/undated 18th-century Língua Geral Amazônica rather than confidently dated 1689.
- Added shared `ms1089-*` CSS for the manuscript bridge, including hero, comparison, rule, evidence, trajectory, and positioning layouts.
- Verified with `npm run build`, `git diff --check`, generated-module checks for all six new slide titles/examples, generated `<pre>/<code` checks, and `curl -I` checks on `http://localhost:3033/50` and `/55`. Starting the local Slidev server inside the sandbox failed with `EPERM`, then succeeded with approved escalation; no screenshots were taken.
- Added a final seven-slide retomadas atuais block after the Nheengatu grammar-change synthesis, covering everyday Tupi vocabulary, no confirmed current L1 Old Tupi speakers, Potiguara, Tupinambá, Tupinakyîa, university/online/technology uses, and the archive-to-retomada close.
- Styled the new block with shared `retomada-*` CSS and documented the qualification-derived page/appendix assets in `public/assets/oficina-unb/README.md`.
- Verified with `npm run build`, `git diff --check`, generated-title checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/72`, and headless DOM bounds/image-load checks on slides 72-78. No screenshots were taken.
- Replaced the static vocabulary cloud on `O Tupi que o Brasil já fala` with `decks/components/TupiVocabularyLookup.vue`, an interactive chip-and-definition panel using summarized dictionary data from `kiansheik.io/nhe-enga`.
- Added JPG/JPEG support to `DeckImage.vue`, extracted Toré PDF images, and documented the new `tore-*.jpg` assets in `public/assets/oficina-unb/README.md`.
- Swapped the side images on the retomadas overview, Potiguara, and Tupinambá slides to Toré PDF-derived visuals and added context from the supplied computational grammar/Toré PDFs around Tupi potiguara, Tupi tupinambá, and community-adapted revitalization.
- Verified with `npm run build`, `git diff --check`, generated-module checks for the interactive component and Toré assets, generated `<pre>/<code` checks, `curl -I` checks on slides 72/74/75, and a headless DOM click/image-load check. Starting Slidev inside the sandbox failed with `EPERM`; rerunning with approved escalation started `http://localhost:3033/`. No screenshots were taken.
- Redesigned the Oficina UnB title slide with a clearer title/subtitle/presenter hierarchy, topic chips, an accent rail, and a right-side Anchieta source panel.
- Verified the title-slide redesign with `npm run build`, `git diff --check`, generated-module checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/1`, and a headless DOM bounds/image-load check. No screenshots were taken.

## 2026-05-18

- Added a `Roteiro da oficina` roadmap slide after the title slide to summarize the major arcs of the deck.
- Added seven section-divider slides before the main transitions: línguas gerais, Brazil coast/Tupi Antigo corpus, Anchieta/use/variation, Amazonian language ecology, naming/Nheengatu, grammar change, and modern retomadas.
- Added shared `section-map-*` and `section-divider-*` CSS for the new pacing slides, keeping them in the Oficina visual system.
- Verified with `npm run build`, `git diff --check`, generated-module checks for all new section titles, generated `<pre>/<code` checks, `curl -I http://localhost:3033/2`, and a no-screenshot DOM overflow check for the roadmap/divider slides.
- Replaced the previous interactive `O Tupi que o Brasil já fala` vocabulary slide with three `O Tupi que o português já fala` table slides: actions, food/body/slang, and people/animals/names.
- Deleted the now-unused `decks/components/TupiVocabularyLookup.vue` component and replaced its old CSS with reusable `tupi-word-table` styling.
- Verified with `npm run build`, `git diff --check`, generated-module content checks for the new vocabulary slides, stale interactive-vocabulary checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/80`, and a no-screenshot DOM overflow check for routes 80-82. The first DOM pass caught horizontal table overflow; wrapping rules fixed it.
- Expanded visible Finbow slide footnotes so the cited work title and year appear directly on the relevant Amazônia/Língua Geral slides instead of bare `Finbow, 2022/2025` references.
- Added compact `finbow-source` citation styling and added missing visible source lines to Finbow-derived argument slides that had only speaker-note citations.
- Verified with `npm run build`, `git diff --check`, generated-module citation checks, stale bare-Finbow checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/40`, and a no-screenshot DOM overflow check for routes 40-45, 48-54, and 62.
- Added a new map slide immediately after `Três olhares, uma convergência`, with `/Users/kian/code/latex/mestrado/tupi_dist_mapa.jpg` copied as `public/assets/oficina-unb/tupi-dist-mapa.jpg` on the left and `/Users/kian/code/latex/mestrado/rendtrans.png` copied as `public/assets/oficina-unb/rendtrans.png` on the right.
- Added `distribution-map-*` CSS to keep the two map cards contained above an estimate caveat, and documented the new mestrado-derived assets in `public/assets/oficina-unb/README.md`.
- Verified with `npm run build`, `git diff --check`, generated-module checks for the slide/assets/caveat, generated `<pre>/<code` checks, and a no-screenshot Playwright DOM image/bounds check on route `/18`. Starting Slidev inside the sandbox failed with `EPERM`, then the approved local server ran at `http://localhost:3034/`.
- Polished the `Língua geral: não uma língua, mas uma categoria` concept slide CSS into a cleaner two-column contrast, with the definition spanning the bottom instead of being squeezed into one side.
- Verified with `npm run build`, `git diff --check`, generated-module checks for the concept slide, generated `<pre>/<code` checks, and `curl -I http://localhost:3034/11`. A headless DOM check could not run because `playwright` is not installed in this checkout; no screenshots were taken.
- Removed visible self/unpublished citations from the retomadas atuais block: no slide footer now cites `Sheik`, `A Computational Grammar of Old Tupi`, or `qualificationtr.pdf`.
- Replaced those footers with source-specific citations to Araújo da Silva's Toré material, Araújo da Silva Guyraakanga Potiguara 2024, Cabral 2024, Costa 2013, Santos & Porto 2020, Santana & Cohn 2018, Pavelic 2023, Navarro 2005/2013, and Akangatara Produções.
- Replaced the Tupinakyîa qualification-page crop with a right-side sources/circulation card and added `retomada-right-*` CSS for that layout.
- Verified with `npm run build`, `git diff --check`, generated-module checks for stale unpublished/self-citation strings, and generated `<pre>/<code` checks. No screenshots were taken.
- Scoped the dense retomadas overview slide to `retomada-overview-slide`, reducing title/card/pill/source sizes and giving the citation a right-column position under the image so the elements no longer overlap.
- Changed the visible variety labels to Portuguese order: `Tupi potiguara`, `Tupi tupinambá`, and `Tupi tupinakyîa`, while keeping exact cited titles untouched.
- Verified with `npm run build`, `git diff --check`, generated-module checks for the overview class/labels, stale English-order label checks, and `curl -I http://localhost:3034/83`. Starting Slidev inside the sandbox failed with `EPERM`; rerunning with approved escalation started `http://localhost:3034/`. No screenshots were taken.
- Fixed follow-on footer collisions in the retomadas block by adding `retomada-image-slide` for the Potiguara/Tupinambá image pages and `retomada-circulation-slide` for the Tupinakyîa two-column page.
- The image-page footers now live in the right image column below the image; the circulation page has compacted card typography/spacing so its source line does not intersect either column.
- Verified with `npm run build` and a no-screenshot headless DOM overlap check on routes 84-86; no source line overlaps the left stack, right stack, or image.
- Normalized the title/body spacing on the final six project and participation slides by adding scoped `retomada-project-slide` and `retomada-project-block` classes.
- Removed the inline top/margin spacing overrides from those six slides and moved the shared rhythm into `styles/oficina-unb.css`.
- Verified with `npm run build`, `git diff --check`, generated `<pre>/<code` checks, generated-module checks for the new classes, `curl -I http://localhost:3034/89`, and a no-screenshot Playwright DOM check on routes 89-94. The first browser launch failed under sandbox permissions, then the approved rerun passed; a first selector attempt selected hidden Slidev canvases and was corrected by choosing the visible canvas.

## 2026-08-23

- Added `decks/enapol-2026-executable-grammar.md`, a 9-slide ENAPOL 2026 deck for Kian Arad Sheik's `Corpus Computacional e Gramática Executável do Tupi Antigo` project.
- Added `styles/enapol-2026-executable-grammar.css`, imported it through `decks/styles/index.css`, and kept the visual system scoped to `class: enapol-exec`.
- Added `decks/components/EnapolImage.vue` and SVG placeholder assets under `public/assets/enapol-2026-executable-grammar/`, with `README.md` listing every screenshot/page crop still needed.
- Registered the deck in `scripts/build-all.mjs`, `package.json`, and `README.md`, including `npm run dev:enapol-2026` and `npm run export:enapol-2026:pdf`.
- Updated `docs/agent/current-state.md` and `docs/agent/repo-map.md` to reflect the new built deck.
- Verified with `npm run build`, `git diff --check`, generated Markdown-module raw-marker checks, and `curl -I http://localhost:3035/`. Starting Slidev first failed with unsupported `--host`, then with sandbox `EPERM`, then succeeded after approved escalation at `http://localhost:3035/`.

## 2026-08-24

- Inspected PR #1, `enapol presentation`, on branch `enapol-kian`; no push, commit, merge, or PR mutation was performed.
- Reworked the existing ENAPOL deck instead of rebuilding from scratch, keeping it to nine slides and tightening the argument around executable grammar as linguistic description with computational methods.
- Moved the worked corpus example to slide 3, removed the phrase `ground truth`, added clearer citation/result placeholders, and expanded the Portuguese speaker notes into a rehearsable 10-minute path.
- Replaced the ENAPOL CSS with stable grid/flex layouts and tuned slides 1, 3, 6, and 7 after visual QA caught collisions, clipping, and raw HTML rendering.
- Simplified the ENAPOL asset placeholders to ten logical SVG files and updated `EnapolImage.vue` so same-basename `.png`, `.jpg`, or `.jpeg` replacements take precedence automatically.
- Recreated `public/assets/enapol-2026-executable-grammar/README.md` as a detailed checklist listing each remaining asset, slide use, capture target, source guidance, crop guidance, and replacement status.
- Verified with `npm run build`, `git diff --check`, generated Markdown-module `<pre>`/`<code>` checks, all-slide dev-server visual screenshots, and `npm run export:enapol-2026:pdf`.
- A fresh dev server is running at `http://localhost:3036/`. PDF export produced `enapol-2026-executable-grammar-export.pdf`; full all-page PDF raster QA was limited because `pdfinfo`/`pdftoppm` are unavailable and Ghostscript is missing `gs_init.ps`.
- Refined the committed second-pass ENAPOL deck on branch `enapol-kian`: removed repeated vertical-line backgrounds everywhere, replaced the old bootstrapping oval with a click-revealed arrow methodology, and expanded the deck to 10 logical slides.
- Added the mestrado-to-Doutorado Direto trajectory, an Amazônicas X switch-reference payoff slide, a full-corpus research-infrastructure slide, and a QR/resource closing slide retaining the core closing sentence.
- Verified the installed Slidev exporter supports `--with-clicks`, added `npm run export:enapol-2026:pdf:clicks`, and configured it to write `enapol-2026-executable-grammar-clicks-export.pdf` separately from the normal export.
- Generated three QR SVGs for verified live URLs: `kiansheik.io/nhe-enga`, `github.com/kiansheik/oldtupicorpus`, and `neo.academiatupi.com`.
- Added `notes/enapol-2026-executable-grammar.md`, a slide-by-slide Portuguese rehearsal script with approximate timing, click cues, full spoken script, and transitions.
- Verified the switch-reference data against local paper/dataset files. Current local source files report 62 examples, 60 DS, 2 SS, 96.77% DS, and 3.23% SS; the ENAPOL asset README records the discrepancy with the ResearchGate abstract's 53-example version.
- Final checks passed: `npm run build`, `git diff --check`, stale raw-marker search for repeated backgrounds/old cycle/raw code tags, Chromium screenshot/bounds checks for all 10 slides and slide 6 click states, normal PDF export, and click-state PDF export.
- Made a surgical follow-up pass on the latest `enapol-kian` state without committing or merging: slide 6 keeps the same cumulative methodology but has tighter boxes, wider flowchart space, separated YES/NO branch and callout bands, and no visible branch/regression collisions in the final click state.
- Reframed the doctorate trajectory slide as `Progresso e dificuldades`: first state covers mestrado progress and approval for Doutorado Direto; click reveals the current expert bottleneck; final click centers `produção → edição` as the methodological direction.
- Updated both embedded presenter notes and `notes/enapol-2026-executable-grammar.md` for the new slide 7 timing, click cues, bottleneck language, and production-to-editing explanation.
- Regenerated `enapol-2026-executable-grammar-export.pdf` and `enapol-2026-executable-grammar-clicks-export.pdf`.
- Verified with `npm run build`, `git diff --check`, stale source marker checks, generated ENAPOL `<pre>/<code>` checks, `curl -I http://localhost:3037/`, and Chromium screenshots for slide 6 click states 0-5 plus slide 7 click states 0-2. The local dev server returns 404 for `/svg/6?clicks=5`, so the browser visual QA used `/6?clicks=5`.

## 2026-08-26

- Reworked the ENAPOL deck directly on `main` into an 8-slide focused research presentation following Prof. Dr. Thomas Daniel Finbow's guidance: objective geral, zoom into one question, concrete line, encoding, difficulty, response loop, and close.
- Removed the broader doctorate/progress/switch-reference/full-corpus/QR arc from the live deck so the talk centers on the question: how does one historical corpus line become a test of a grammar?
- Chose `araujo_catecismo_1686:0007` as the concrete line, using local `oldtupicorpus` source and generated ground-truth records for the expression, location, and normalized target.
- Replaced the ENAPOL stylesheet with a slimmer set of layouts for the 8-slide deck and added SVG fallbacks for the requested TODO visual names: Anchieta same-topic page, Gerardi/modern same-topic page, pydicate screenshot, and Araújo/Bettendorff short-line crop.
- Updated the standalone rehearsal script and embedded presenter notes to match the new 10-minute pacing.
- Updated `scripts/build-all.mjs` so the generated public homepage links to `ENAPOL 2026 — Corpus Computacional e Gramática Executável do Tupi Antigo` and shows `29º ENAPOL, USP, 2026`.
- Verification passed: `npm run build`, `git diff --check`, generated homepage link check, generated ENAPOL slide count check, generated ENAPOL `<pre>/<code>` checks, fresh dev server at `http://localhost:3038/`, no-screenshot Chromium layout/image-load check for slides 1-8, and both ENAPOL PDF exports.
- Ran the required `git log --oneline --decorate -n 10`; the current rewrite commit was `778c43b Focus ENAPOL deck on corpus line test`, and the commit before that rewrite was `297405c Merge pull request #1 from kiansheik/enapol-kian`.
- Compared the current 8-slide deck with the previous PR version and synthesized the useful pieces back into the live deck: the cumulative bootstrapping/regression process, Doutorado Direto/full-corpus framing, switch-reference payoff mention, and QR close.
- Expanded `decks/enapol-2026-executable-grammar.md` to a concise 10-slide structure: title, what the project does, grammar as test, problem, Araújo example, executable analysis, tree visualization, bootstrapping/regression, research possibilities, and links.
- Removed explicit `zoom` wording and removed the old vertical-line background treatment from `styles/enapol-2026-executable-grammar.css`.
- Added `public/assets/enapol-2026-executable-grammar/araujo-line-tree.svg` for the Araújo line. A targeted source check found `build_graphviz` in `/Users/kian/code/nhe-enga/test_pydicate.py`, but it is demo/test code rather than a ready export path for this exact corpus expression.
- Added `public/assets/enapol-2026-executable-grammar/qr-presentation.svg` and restored the final QR slide alongside the existing corpus, dictionary, and neologism QR assets.
- Updated `notes/enapol-2026-executable-grammar.md` and the ENAPOL asset README to match the new deck, tree asset, QR asset, and 10-minute script.
- Verification passed: `npm run build`, `git diff --check`, generated homepage link check, generated ENAPOL slide count of 10, generated ENAPOL `<pre>/<code>` checks, stale `zoom`/old-background checks, `curl -I http://localhost:3039/`, normal PDF export, and click-expanded PDF export. A fresh Slidev server is running at `http://localhost:3039/`. The no-screenshot DOM/browser check could not run because this checkout lacks the `playwright` package.
- Corrected the ENAPOL Araújo example so `orébe` is treated as the surface form generated from the deeper pydicate structure `(supé * oré).var(1)`, while the visible morpheme list now includes the base forms `oré` and `supé`.
- Added `scripts/generate-pydicate-tree-svg.py` and `npm run generate:enapol-tree`, replacing the manually maintained tree asset with a generated SVG from the real `oldtupicorpus` Araújo pydicate object.
- Reworked the difficulty slide to state that the project is not NLP automation at this stage; it is traditional grammatical analysis expressed in Python/pydicate, with a current expert bottleneck and future reuse path for other languages, researchers, and agents.
- Reformatted the executable-analysis code into indented lines and added a base-morpheme declaration column beside the formal structure and spell-out output.
- Regenerated both ENAPOL PDF exports and verified with `python3 -m py_compile scripts/generate-pydicate-tree-svg.py`, `npm run generate:enapol-tree`, `npm run build`, generated slide count/raw marker checks, stale explicit-`orébe` note checks, `git diff --check`, `curl -I http://localhost:3039/`, no-screenshot Chromium DOM checks on slides 4-7, and both PDF export commands.
