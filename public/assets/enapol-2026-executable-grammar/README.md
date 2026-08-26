# ENAPOL 2026 Asset Checklist

The deck uses logical asset names through `decks/components/EnapolImage.vue`.
Save replacement screenshots or page crops in this folder with the same basename
as the SVG placeholder, preferably as `.png`. The component checks `.png`,
`.jpg`, `.jpeg`, and then `.svg`, so a file like `source-anchieta.png` will
automatically replace `source-anchieta.svg` without editing the deck.

Recommended capture rules:

- Crop to the useful page, passage, or app panel. Avoid browser chrome unless the URL is itself evidence.
- Keep margins small but leave page numbers, headers, or titles visible when they help citation.
- Prefer light, legible screenshots over dark terminal captures for code/output panels.
- Use PNG for text-heavy material; JPG is acceptable for scanned pages.
- Do not delete the SVG placeholders until the real assets are checked in.

## Required Image Assets

### `source-anchieta.png`

- Logical name: `source-anchieta`
- Save location: `public/assets/enapol-2026-executable-grammar/source-anchieta.png`
- Used on slide 2: one of the three source panels for the problem statement.
- Purpose: show that the project begins from primary historical documentation.
- What to capture: a cover, title page, or representative page from Anchieta's grammar.
- Preferred source: the Anchieta PDF/scan you will cite in the bibliography.
- Crop guidance: document page only; keep title/page header/page number visible if possible.
- Replacement status: REQUIRED

### `source-corpus.png`

- Logical name: `source-corpus`
- Save location: `public/assets/enapol-2026-executable-grammar/source-corpus.png`
- Used on slide 2: corpus/source panel beside Anchieta and the modern source.
- Purpose: show the historical corpus material that supplies testable examples.
- What to capture: a cover, title page, or representative page from Araujo, Bettendorff, or the source family used for the worked line.
- Preferred source: the same digitized source family used for `corpus-example-source`.
- Crop guidance: document page only; avoid tiny full-browser screenshots.
- Replacement status: REQUIRED

### `source-modern.png`

- Logical name: `source-modern`
- Save location: `public/assets/enapol-2026-executable-grammar/source-modern.png`
- Used on slide 2: modern descriptive/dictionary source panel.
- Purpose: make the bridge between colonial sources and current linguistic description visible.
- What to capture: a cover, title page, or representative dictionary/grammar page from Navarro, Gerardi, or the modern reference chosen for the presentation.
- Preferred source: the modern work you will cite directly in the slide notes/bibliography.
- Crop guidance: keep the work title or section heading readable.
- Replacement status: REQUIRED

### `corpus-example-source.png`

- Logical name: `corpus-example-source`
- Save location: `public/assets/enapol-2026-executable-grammar/corpus-example-source.png`
- Used on slide 3: first panel in the worked corpus example.
- Purpose: anchor the computational analysis in one concrete attested line.
- What to capture: the exact Old Tupi line from Araujo, Bettendorff, or another corpus source.
- Preferred source: the primary scan/PDF page that contains the line you will analyze.
- Crop guidance: crop around the line and enough neighboring context to make the source credible; keep page number if possible.
- Replacement status: REQUIRED

### `corpus-example-formal.png`

- Logical name: `corpus-example-formal`
- Save location: `public/assets/enapol-2026-executable-grammar/corpus-example-formal.png`
- Used on slides 3 and 5: formal representation/code panel.
- Purpose: show the executable expression for the same source line or grammatical phenomenon.
- What to capture: syntax-highlighted pydicate/code/formal notation for exactly the same line or phenomenon.
- Preferred source: the local project/editor or a rendered code snippet used in the doctorate materials.
- Crop guidance: use a light theme or high-contrast editor theme; no terminal prompt unless it adds necessary context.
- Replacement status: REQUIRED

### `corpus-example-output.png`

- Logical name: `corpus-example-output`
- Save location: `public/assets/enapol-2026-executable-grammar/corpus-example-output.png`
- Used on slide 3: generated output panel.
- Purpose: show what the executable grammar produces and how it can be checked against the source line.
- What to capture: generated annotation, parsed output, conjugated form, or diagnostic output for the same worked example.
- Preferred source: project output from the same code path used to generate or test the example.
- Crop guidance: make the analyzed form and key labels readable; crop away unrelated console noise.
- Replacement status: REQUIRED

### `comparison-anchieta.png`

- Logical name: `comparison-anchieta`
- Save location: `public/assets/enapol-2026-executable-grammar/comparison-anchieta.png`
- Used on slide 5: first panel in the "four centuries" comparison.
- Purpose: show an early metalinguistic description for one selected grammatical phenomenon.
- What to capture: the exact Anchieta passage for the phenomenon compared against the modern and executable descriptions.
- Preferred source: Anchieta grammar PDF/scan with page number visible.
- Crop guidance: crop the paragraph/table tightly enough to read it in the slide.
- Replacement status: REQUIRED

### `comparison-modern.png`

- Logical name: `comparison-modern`
- Save location: `public/assets/enapol-2026-executable-grammar/comparison-modern.png`
- Used on slide 5: second panel in the "four centuries" comparison.
- Purpose: show how a modern grammar, paper, or dictionary describes the same phenomenon.
- What to capture: the matching passage from Gerardi, Navarro, or the chosen modern reference.
- Preferred source: the modern source that best matches the phenomenon used in `comparison-anchieta`.
- Crop guidance: keep section title and page number if available.
- Replacement status: REQUIRED

### `project-dictionary.png`

- Logical name: `project-dictionary`
- Save location: `public/assets/enapol-2026-executable-grammar/project-dictionary.png`
- Used on slide 7: implemented-output screenshot.
- Purpose: show current project outputs, such as dictionary, conjugation, quiz, or generated forms.
- What to capture: the clearest app/site view that demonstrates an already implemented output.
- Preferred source: the current project UI or local/public app page.
- Crop guidance: 4:3 or 16:10 crop; light theme preferred; hide browser chrome unless the URL matters.
- Replacement status: REQUIRED

### `project-public-facing.png`

- Logical name: `project-public-facing`
- Save location: `public/assets/enapol-2026-executable-grammar/project-public-facing.png`
- Used on slide 7: second screenshot of project outputs.
- Purpose: show the public-facing or community-facing side of the work.
- What to capture: TupiTrail, neologism dictionary, public dictionary, quiz, or another interface that shows reuse beyond the internal grammar.
- Preferred source: the live public site/app or a local equivalent if the public version is not current.
- Crop guidance: keep the actual interface readable; avoid decorative landing-page areas.
- Replacement status: REQUIRED

## Generated QR Assets

These QR codes were generated from verified live URLs on 2026-08-24. Regenerate
them if the canonical URL changes.

### `qr-dictionary.svg`

- Logical name: `qr-dictionary`
- Used on slide 10: Dicionario / dictionary resource.
- URL: `https://kiansheik.io/nhe-enga/`
- Verification: `curl -I` returned `HTTP/2 200`.
- Replacement status: GENERATED

### `qr-corpus.svg`

- Logical name: `qr-corpus`
- Used on slide 10: grammar/corpus implementation resource.
- URL: `https://github.com/kiansheik/oldtupicorpus`
- Verification: `curl -I` returned `HTTP/2 200`.
- Replacement status: GENERATED

### `qr-neo.svg`

- Logical name: `qr-neo`
- Used on slide 10: Dicionario de Tupi / neologism-public-app resource.
- URL: `https://neo.academiatupi.com`
- Verification: `curl -I` returned `HTTP/2 200`.
- Replacement status: GENERATED

## Non-Image Information To Provide Manually

1. Exact corpus line for slide 3, with source, page, and transcription.
2. Segmentation, gloss, translation, and the intended grammatical phenomenon for that line.
3. The formal/executable expression that corresponds to the slide 3 line.
4. One concrete generated output or diagnostic from the executable grammar for that same line.
5. The grammatical phenomenon used on slide 5 for the Anchieta/modern/executable comparison.
6. Exact page references for the Anchieta passage and modern-source passage on slide 5.
7. One empirical result for slide 7, such as number of encoded rules, number of corpus lines tested, number of generated forms, a rule revision caused by a corpus counterexample, or an ambiguity class found by the implementation.
8. Final bibliography entries for all primary and modern sources shown in screenshots.
9. Switch-reference citation version: ResearchGate's public abstract reports 53 examples and 96.23% DS, while the local LaTeX source and dataset currently report 62 examples, 60 DS, 2 SS, 96.77% DS and 3.23% SS. Choose which version should be cited in the live talk.

## Exact Replacement Workflow

1. Save each real screenshot/page crop in this folder with the exact basename listed above.
2. Prefer `.png`; `.jpg` and `.jpeg` also work. Keep the `.svg` placeholder in place as fallback.
3. Do not edit the Markdown just to switch from placeholder to real asset; `EnapolImage` resolves the extensionless logical names automatically.
4. Run `npm run dev:enapol-2026 -- --port 3036` and check slides 2, 3, 5, and 7.
5. Run `npm run build`.
6. Run `npm run export:enapol-2026:pdf` after the visuals are final.
