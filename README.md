# Public Presentations

Repositório de apresentações públicas em Slidev.

O deck principal atual é [decks/oficina-unb.md](./decks/oficina-unb.md), uma recriação editável da oficina UnB a partir dos arquivos exportados do Google Slides. O texto continua em Markdown/HTML editável, e as imagens são assets locais extraídos do PPTX.

## Rodar localmente

```bash
npm install
npm run dev:oficina-unb
```

`npm run dev` também abre `decks/oficina-unb.md`.

## Build para GitHub Pages

```bash
npm run build
```

O script `scripts/build-all.mjs` gera:

- `dist/index.html`
- `dist/oficina-unb/`

Em GitHub Actions, o base path de cada deck usa o nome do repositório vindo de `GITHUB_REPOSITORY`, por exemplo `/public-presentations/oficina-unb/`. Para testar outro base path localmente:

```bash
SLIDEV_BASE=/nome-do-repo/ npm run build
```

## Exportar

```bash
npm run export:oficina-unb:pdf
npm run export:oficina:pdf
npm run export:oficina:pptx
npm run export:oficina:png
npm run export:lingua-geral:pdf
npm run export:anchieta:pdf
```

## Estrutura

- `decks/oficina-unb.md` — deck editável da oficina UnB
- `scripts/build-all.mjs` — build multi-deck para GitHub Pages
- `.github/workflows/deploy.yml` — deploy de `dist` via GitHub Actions
- `components/` — componentes Vue reutilizáveis para citações, biografias e linhas do tempo
- `styles/oficina-unb.css` — estilo fiel ao visual do Google Slides original
- `public/assets/oficina-unb/` — imagens extraídas do PPTX da oficina
- `styles/custom.css` — estilo dos decks iniciais de rascunho
- `public/assets/` — assets organizados por deck ou em `shared/`

## Adicionar decks futuros

1. Crie um novo Markdown em `decks/<slug>.md`.
2. Coloque imagens/documentos em `public/assets/<slug>/` ou `public/assets/shared/`.
3. Crie um CSS em `styles/<slug>.css` se o deck tiver visual próprio.
4. Adicione o deck ao array `decks` em `scripts/build-all.mjs`.
5. Adicione scripts `dev:<slug>` e `export:<slug>:pdf` em `package.json` se forem úteis.
