# Current State

Last updated: 2026-05-18

This is a Slidev repository for public presentations. The active deck lives under `decks/`; older starter decks still live at the repository root.

Current decks:

- `decks/oficina-unb.md` is the active Oficina UnB deck and the only deck in the current build manifest.
- `oficina-tupi-antigo.md`
- `lingua-geral-brasil.md`
- `anchieta-contexto.md`

Shared presentation infrastructure:

- `AGENTS.md` is the repo-local instruction file for future agents. It explicitly says not to take Playwright screenshots unless the user requests screenshots.
- `decks/components/DeckImage.vue` renders Oficina UnB manuscript images as real `<img>` tags by importing files from `public/assets/oficina-unb/`. This avoids Slidev rewriting raw `/assets/...` or `../public/assets/...` paths in slide Markdown.
- `decks/styles/index.css` is the active global Slidev style entry for the `decks/` user root and imports `styles/oficina-unb.css`. Do not rely on a deck-level `<style>` tag for shared Oficina CSS; Slidev scopes slide `<style>` tags by default.
- `components/` contains reusable Vue slide components for the older root-level starter decks.
- `styles/custom.css` contains the shared visual language.
- `styles/oficina-unb.css` contains the Oficina UnB layout and positioning CSS.
- `public/assets/` is organized by deck slug plus `shared/`.
- `scripts/build-all.mjs` clears `dist/`, builds every deck into `dist/<slug>/`, and writes `dist/index.html`.
- `.github/workflows/deploy.yml` is a build check only: it installs with `npm ci` and runs `npm run build`. It does not use `actions/configure-pages`, because that path requires the repository Pages source to be configured for GitHub Actions before it runs.
- `Makefile` exposes `make help`, `make build`, `make prepare-gh-pages`, `make deploy-gh-pages`, and `make push-gh-pages`. `deploy-gh-pages` builds, commits, and pushes the `.gh-pages` worktree to the configured Pages branch.
- `README.md` is the project-facing guide for commands, adding decks, styling decks under `decks/`, and handling image assets.

Verified on 2026-05-13:

- `npm run build` succeeds for the current `oficina-unb` build manifest.
- `npm ci --dry-run` accepts the current `package.json` and `package-lock.json`.
- Generated deck assets use `/public-presentations/<deck>/` base paths by default.
- `dist/`, `.gh-pages/`, and `node_modules/` are ignored by git.
- A local `oficina-tupi-antigo.md` dev server was started at `http://localhost:3030/` during the 2026-05-13 session.
- A fresh `oficina-unb` dev server was started at `http://localhost:3031/`.
- Browser verification on `http://localhost:3031/3` found zero escaped `<pre><code>` quote blocks, one rendered blockquote, and a loaded manuscript image with natural size `944x1432`.
- Oficina content slides now use a consistent half-split frame: left text column ends around x=609 and right manuscript column starts around x=666 on a 1280px viewport.

Verified on 2026-05-14:

- Added five Brasil witness slides to `decks/oficina-unb.md` after the question slide: Anchieta title page, Anchieta biography/quote, Cardim biography/quote, Gabriel Soares biography/quote, and a convergence slide.
- Added `styles/oficina-unb.css` layout classes for the Brasil source, witness, quote-panel, and convergence slide variants.
- `npm run build` succeeds after the Brasil slide block.
- A static generated-bundle check found the new slide modules/classes and the `DeckImage` import for `anchieta-arte-grammatica.png`.
- Browser screenshot verification was not run for the new slides; future agents should avoid Playwright screenshots unless explicitly requested.
- `make build` succeeds and wraps the same `npm run build` flow.
- `make help` prints the Makefile command index and deploy variables.

Verified on 2026-05-15:

- `.github/workflows/deploy.yml` was switched from Pages artifact deployment to a build-only workflow to avoid `actions/configure-pages@v5` failing when Pages is not already configured for GitHub Actions.
- Branch publishing remains available through `make deploy-gh-pages`; the repository Pages setting should publish from `gh-pages` branch root.
- Added a five-slide Anchieta grammar/use block to the end of `decks/oficina-unb.md`: title framing, regional variation, use as teacher, oral use/viva voz, and universal/local systematization.
- Added `styles/oficina-unb.css` classes for the Anchieta grammar block and right-side text screenshot placeholders.
- `npm run build` succeeds after the appended slides.
- A local Slidev server for review is running at `http://localhost:3032/` and returned `HTTP/1.1 200 OK`; no Playwright screenshots were taken.

Verified on 2026-05-16:

- Added a fourteen-slide Tupi Antigo corpus-definition block to `decks/oficina-unb.md` after the Brasil convergence slide and before the Anchieta grammar close-reading slides.
- The new block defines Tupi Antigo as a finite corpus designation and adds modular source fichas for Staden, Thevet, Léry, Gândavo, Gabriel Soares de Sousa, Cardim, Anchieta, Araújo, Figueira, the `Vocabulário na Língua Brasílica`, the Cartas dos Camarões, Bettendorff, and a central-corpus timeline.
- Added `styles/oficina-unb.css` classes for the corpus definition slide, two-column source fichas, terminology notes, footers, and timeline layout.
- `npm run build` succeeds after the corpus block.
- A static Slidev parser check reports 33 slides, with the new corpus block spanning slides 15-28; no Playwright screenshots were taken.
- Refined the first three content slides with a scoped `source-quote-block` style so source quotations have warmer color, a subtle dark backing, accent rule, and clearer spacing from source citations.
- `npm run build` succeeds after the opening quote contrast pass.
- The user's existing local Slidev server on port `3030` is reachable from this shell at `http://[::1]:3030/` and returns `HTTP/1.1 200 OK`; `127.0.0.1:3030` is not reachable because the process is listening on IPv6 loopback only. No Playwright screenshots were taken.
- Reworked the Quechua, Nahuatl, and Guarani case-study slides so source entries are no longer same-weight paragraphs: each now uses a `language-case-block` with a label, dated source rows, and a stronger takeaway/note style.
- `npm run build` succeeds after the language case-slide readability pass.
- Corrected the cátedra slide speaker note so it emphasizes formal university formation rather than repeating the mission-requirement note.
- Added explicit speaker-note bridging from the Brasil coastal-language convergence into the Tupi Antigo corpus-definition block, plus a note to treat the corpus fichas as a quick archive map.
- Added the missing final Anchieta slide, “Entre o uso local e o uso mais universal,” bringing `decks/oficina-unb.md` to 34 `oficina-unb` slides.
- `npm run build` succeeds after the transition-note and final Anchieta closeout pass.
- Added an eight-slide Amazônia/Língua Geral Amazônica block after the Anchieta closeout, moving from Tupi Antigo/Língua Brasílica as a classical corpus into LGA as a living language of aldeamento, contact, and change.
- The new Amazônia block uses Finbow 2022 and João Daniel to frame LGA through linguistic ecology, demographic collapse, descimentos, multiethnic aldeamentos, Tapuia learners, written-vs-vernacular norms, and continuity plus restructuring rather than a simplistic “Jesuit simplification” thesis.
- Added `styles/oficina-unb.css` classes for the new `amazonia-slide` layouts, including list, contrast, cycle, two-column, keypoint, and closing-slide treatments.
- `npm run build` succeeds after the Amazônia block; a static slide count reports 42 `oficina-unb` slides.

Verified on 2026-05-17:

- Fixed the Amazônia block Markdown/HTML spacing so nested `amazonia-*` slide elements render as normal DOM instead of escaped `<pre><code>` blocks.
- `npm run build` succeeds after the raw-HTML rendering fix.
- Static generated-module checks find no `<pre>`, `<code>`, or `` `pre` `` markers in generated `dist/oficina-unb/assets/md-*.js` slide modules.
- Added a João Daniel follow-up slide, “A arte já não garantia entendimento,” after the first “parece outra língua diversa” slide. It quotes Daniel/Finbow on catechism, grammar study, mission speech in the Amazonas, and new nations learning the vernacular mission language.
- Added `daniel-followup-*` and `takeaway-list` CSS for a quote-plus-takeaways layout.
- `npm run build` succeeds after the follow-up slide; static slide count reports 43 `oficina-unb` slides.
- Added two João Maia da Gama follow-up slides after the Daniel/Finbow slide to answer “why Língua Geral if they were Tapuias?” using the Reis 1961 apud Bessa Freire 2003 citation and the daily-exposure argument.
- Added `maia-*` CSS for the setup question slide and the “missionary instruction vs aldeamento life” answer slide.
- `npm run build` succeeds after the Maia da Gama slides; generated output includes 44 `md-*.js` slide modules and the generated slide modules contain no `<pre>`, `<code>`, or `` `pre` `` markers.
- Added two Finbow/Rodrigues caution slides at the end of `decks/oficina-unb.md`: `LGP/LGA: rótulos úteis, mas modernos` and `Paulistas no Maranhão-Pará`.
- The new slides frame LGP/LGA as useful modern labels that should not be projected rigidly onto 16th- and 17th-century sources, then use Anchieta’s mixed features and the Paulista Maranhão-Pará mission evidence as the stronger intelligibility point.
- Verified the Revista do GEL article page/PDF for the Finbow citation and source framing.
- `npm run build` succeeds after the Finbow caution slides; generated `md-*.js` checks find 45 slide modules, both new titles, and no `<pre>`, `<code>`, or `` `pre` `` markers.
- Simplified the names/glotonyms synthesis slide to `Quatro nomes na documentação`, positioned before the Nheengatu-name detail slides.
- The simplified slide now shows only the Brazil/Amazônia sequence requested by the user: `lingva mais vsada na costa do Brasil` (Anchieta, 1595), `lingoa brasílica` (Araújo, 1618), `língua geral dos Tupynambás` (Manoel Gomes, 1616), and `Nheengatu` (Seixas, 1853).
- Replaced the dense proportional rail/comparative-language layout with a four-card `name-sequence-*` layout in `styles/oficina-unb.css`.
- `npm run build` and `git diff --check` succeed after the simplified name-sequence slide; generated checks find the new slide module without raw HTML code markers.
- Added a concise Pombal/Diretório bridge slide, `Quando o Estado tenta substituir a Língua Geral`, after the names/descriptions synthesis and before the Nheengatu-name detail slides.
- Retitled the following transition slide to `Depois da repressão, o nome Nheengatu` and reframed its text around post-Diretório naming rather than only asking when the name appears.
- `npm run build` and `git diff --check` succeed after the Pombal bridge; generated checks find the new `slidev_51` bridge and `slidev_52` transition without raw HTML code markers.
- Moved the `Pai Nosso: Tupi Antigo, Nheengatu e português` comparison slide to the physical end of `decks/oficina-unb.md`, after `Nome posterior, continuidade histórica`.
- Restyled the Pai Nosso slide to stay in the Oficina dark visual system while preserving the academic table structure: title, justification note, ruled comparison table, caption, and FOIRN footnote.
- The Pai Nosso slide CSS now uses a grid with height-responsive spacing and enlarged type sizing so the table fills the available slide area without the white document-page treatment.
- `npm run build`, `git diff --check`, generated-module raw-HTML marker checks, and a headless DOM layout check on `http://localhost:3033/56` succeed; the final DOM check reports no overflow and table/body/header/caption font sizes of roughly `10.24px` / `12.16px` / `10.88px` inside the Slidev canvas. No screenshots were taken.
- A local Slidev dev server is running at `http://localhost:3033/` for review.
- Added an eight-slide grammar-change block after the Pai Nosso slide: `Continuidade não significa imobilidade`, estative continuity, gerund loss, negation shift to `ti`, future shift to `kurí`, less phonetic fusion, Indicative II fossilization, and a closing changed/preserved synthesis.
- Added `change-*` CSS classes in `styles/oficina-unb.css` for the grammar-change cards, comparison examples, key points, and closing two-column list.
- `npm run build`, `git diff --check`, generated-module raw-HTML marker checks, generated-title checks, and a headless DOM bounds check for slides 57-64 succeed after the grammar-change block. No screenshots were taken.
- Replaced shortened examples in the grammar-change slides with full original/gloss/translation blocks from `/Users/kian/code/latex/nheengatu_loss/main.tex`, the LaTeX source adjacent to the user-provided `main.pdf`.
- `pdftotext` was unavailable in this environment, so the checked-in paper source was used to preserve the `\gla`, `\glb`, and `\glft` lines exactly.
- `npm run build`, `git diff --check`, generated-module checks for the full example strings, raw-HTML marker checks, and headless DOM bounds checks for slides 57-64 succeed after the full-gloss pass. No screenshots were taken.
- Added a dedicated switch-reference slide before the grammar-change synthesis slide, using examples from `/Users/kian/code/latex/swith_ref_tupi_2025/main.tex` plus the Nheengatu `ramé` examples from `/Users/kian/code/latex/nheengatu_loss/main.tex`.
- Added `switch-*` CSS in `styles/oficina-unb.css` for the new two-panel switch-reference layout; the generated slide is `slidev_64`, and the closing synthesis moved to `slidev_65`.
- `npm run build`, `git diff --check`, generated-module content checks, generated `<pre>/<code` checks, and `curl -I http://localhost:3033/64` succeed after the switch-reference slide. No screenshots were taken.
- Added a six-slide Coimbra ms. 1089 bridge block after `Mudança não é invenção` and before `Nomes e descrições na documentação`, framing the manuscript as mid-18th-century Língua Geral Amazônica rather than classical Tupi Antigo or Nheengatu by name.
- The bridge covers: `Um manuscrito de transição`, `Duas formas de dizer “não tem corpo”`, `O catecismo oficial conserva a norma antiga`, `Antes de “ti”: nitio / nitíu`, `Da moldura verbal à partícula negativa`, and `Nem Tupi Antigo clássico, nem ainda “Nheengatu”`.
- Added `ms1089-*` CSS in `styles/oficina-unb.css` for the bridge layouts and compact gloss panels. `npm run build`, `git diff --check`, generated-module content checks, generated `<pre>/<code` checks, and `curl -I` checks for `http://localhost:3033/50` and `/55` succeed. A local Slidev server is running at `http://localhost:3033/`; no screenshots were taken.
- Added the final retomadas atuais block after the Nheengatu grammar-change synthesis: three `O Tupi que o português já fala` vocabulary slides, `Tupi Antigo hoje: sem falantes nativos, mas em retomada`, Potiguara, Tupinambá, Tupinakyîa, universidade/internet/tecnologia, and `Do arquivo à retomada`.
- The retomadas block uses qualification-derived assets from `/Users/kian/code/latex/qualification/qualificationtr.pdf` and appendix figures: `qualification-contemporary-p21.png`, `qualification-retomadas-p22.png`, `qualification-dic.png`, `qualification-gint.png`, `qualification-trad.png`, and `qualification-quiz.png`.
- Added `retomada-*` CSS in `styles/oficina-unb.css` for the new cards, word-cloud panels, PDF page crops, media collage, and closing grid. `npm run build`, `git diff --check`, generated-title checks, generated `<pre>/<code` checks, and headless DOM bounds checks for slides 72-78 succeed. No screenshots were taken.
- Replaced the earlier interactive `TupiVocabularyLookup` vocabulary slide with three static table slides: actions (`mutirão`, `socar`, `cutucar`, `pocar`), food/body/slang (`paçoca`, `pamonha`, `peba`, `pereba`, `pitiú`), and people/animals/names (`curumim`, `cunhantã`, `capivara`, `Potiguara`). The obsolete Vue component was deleted.
- Extended `DeckImage.vue` to include JPG/JPEG assets and extracted Toré PDF images from `/Users/kian/Downloads/A Língua Tupinambá nas músicas do Toré (1).pptx.pdf` by José Romildo Araújo da Silva.
- Replaced right-side qualification screenshots in the retomadas overview, Potiguara, and Tupinambá slides with Toré-derived images: `tore-nada-sem-nos.jpg`, `tore-rorypaba.jpg`, and `tore-tupinamba-olivenca.jpg`.
- Added more context from the supplied PDFs: Potiguara revitalization since 2001, Tupi Potiguara as a community-adapted identity label, Toré lyrics as living use, and the caution that contemporary Tupinambá Tupi should not be collapsed into the colonial corpus label.
- `npm run build`, `git diff --check`, generated-module checks, generated `<pre>/<code` checks, `curl -I` checks on the local server, and a headless DOM interaction check for slide 72 succeed. The DOM check confirmed that clicking `jacaré` changes the dictionary panel and that the Potiguara Toré image loads at 923x744. No screenshots were taken.
- A local Slidev server is running at `http://localhost:3033/`.
- Redesigned the title slide so `Tupi Antigo` is the clear title, the workshop subtitle is separated, and `Kian Sheik` appears only in a distinct presenter block labeled `com`.
- The new cover adds an Oficina UnB kicker, topic chips, an accent rail, and a right-side Anchieta 1595 source-image panel using `DeckImage`.
- `npm run build`, `git diff --check`, generated-module checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/1`, and a headless DOM bounds/image-load check for slide 1 succeed. No screenshots were taken.

Verified on 2026-05-18:

- Added a `Roteiro da oficina` roadmap slide after the title slide, summarizing the deck into seven large arcs: Línguas gerais, Costa do Brasil, Anchieta, Amazônia, Nheengatu, mudança gramatical, and Retomadas.
- Added seven typographic section-divider slides before the major turns in `decks/oficina-unb.md`: colonial línguas gerais, Brazil coast/Tupi Antigo corpus, Anchieta/use/variation, Amazonian language ecology, naming/Nheengatu, grammar change, and modern retomadas.
- Added shared `section-map-*` and `section-divider-*` CSS in `styles/oficina-unb.css` for the pacing slides; no inline per-slide styling was needed.
- `npm run build` succeeds and now emits 86 slide modules.
- `git diff --check`, generated-module checks for all new roadmap/divider titles, generated `<pre>/<code` checks, `curl -I http://localhost:3033/2`, and a no-screenshot headless DOM overflow check for slides 2, 3, 12, 32, 38, 61, 69, and 79 all succeed.
- Replaced the end vocabulary slide with three source-backed `O Tupi que o português já fala` table slides on routes 80-82 and deleted `decks/components/TupiVocabularyLookup.vue`.
- `npm run build` succeeds and now emits 88 slide modules. `git diff --check`, generated-module checks for the new vocabulary titles/content, generated `<pre>/<code` checks, stale interactive-vocabulary checks, `curl -I http://localhost:3033/80`, and a no-screenshot headless DOM overflow check for routes 80-82 all succeed.
- Expanded visible Finbow citations across the Amazônia/Língua Geral block so slide footnotes name the full 2022 article, `The Nature and Emergence of the Língua Geral Amazônica according to Mufwene’s Language Ecology Model`, or the full 2025 SciELO preprint, `A sociophilological account of the formation and evolution of the term Língua Geral, with emphasis on Amazonia`.
- Added `finbow-source` CSS to keep the longer academic footnotes compact. `npm run build`, `git diff --check`, generated-module citation checks, stale bare-Finbow checks, generated `<pre>/<code` checks, `curl -I http://localhost:3033/40`, and a no-screenshot DOM overflow check for routes 40-45, 48-54, and 62 all succeed.
- Added a side-by-side estimated-distribution map slide after `Três olhares, uma convergência`, using `tupi-dist-mapa.jpg` on the left and `rendtrans.png` on the right.
- Copied the source images from `/Users/kian/code/latex/mestrado/` into `public/assets/oficina-unb/` and documented their provenance in the Oficina asset README.
- Added `distribution-map-*` CSS for contained two-column map cards and a visible caveat that the maps are estimates of 16th-century geographic distributions, not fixed boundaries.
- `npm run build`, `git diff --check`, generated-module content checks, generated `<pre>/<code` checks, and a no-screenshot headless DOM image/bounds check on `http://localhost:3034/18` all succeed. A local Slidev server is running at `http://localhost:3034/`.
- Reworked the concept slide `Língua geral: não uma língua, mas uma categoria` CSS so the content reads as a two-column contrast: muted rejected question, accented preferred question, and the working definition spanning the bottom.
- `npm run build`, `git diff --check`, generated-module checks for the concept slide, generated `<pre>/<code` checks, and `curl -I http://localhost:3034/11` succeed after the concept-slide polish. A Playwright DOM check could not run because the `playwright` package is not installed in this checkout; no screenshots were taken.
