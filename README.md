# Public Presentations

Repositório de apresentações públicas em Slidev. A ideia é manter cada apresentação como um deck editável, com textos em Markdown/HTML, estilos versionados e imagens locais em `public/assets/`.

O deck principal atual é [decks/oficina-unb.md](./decks/oficina-unb.md), uma recriação editável da oficina UnB a partir dos arquivos exportados do Google Slides. O texto continua em Markdown/HTML editável, e as imagens são assets locais extraídos do PPTX.

## Comandos

```bash
npm install
npm run dev:oficina-unb
npm run build
npm run export:oficina-unb:pdf
```

`npm run dev` também abre `decks/oficina-unb.md`.

O build usa [scripts/build-all.mjs](./scripts/build-all.mjs) e gera:

- `dist/index.html`
- `dist/oficina-unb/`

Em GitHub Actions, o base path de cada deck usa o nome do repositório vindo de `GITHUB_REPOSITORY`, por exemplo `/public-presentations/oficina-unb/`. Para testar outro base path localmente:

```bash
SLIDEV_BASE=/nome-do-repo/ npm run build
```

Exports disponíveis:

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
- `decks/components/` — componentes Vue disponíveis para decks dentro de `decks/`
- `decks/styles/index.css` — entrada global de CSS para decks dentro de `decks/`
- `scripts/build-all.mjs` — build multi-deck para GitHub Pages
- `.github/workflows/deploy.yml` — deploy de `dist` via GitHub Actions
- `components/` — componentes Vue dos decks antigos na raiz
- `styles/oficina-unb.css` — estilo fiel ao visual do Google Slides original
- `styles/custom.css` — estilo dos decks iniciais de rascunho
- `public/assets/oficina-unb/` — imagens extraídas do PPTX da oficina
- `public/assets/shared/` — assets reutilizáveis entre apresentações

## Decks e estilos

Decks novos devem ficar em `decks/<slug>.md`. Use um `slug` curto, sem espaços, porque ele também vira a pasta de build em `dist/<slug>/` e a rota pública em `/public-presentations/<slug>/`.

Um deck com visual próprio deve ter:

- `decks/<slug>.md` com `class: <slug>` no frontmatter.
- `styles/<slug>.css` com as regras específicas do deck.
- Uma importação em `decks/styles/index.css`.
- Assets em `public/assets/<slug>/`.
- Entrada em `scripts/build-all.mjs`.
- Scripts úteis em `package.json`, por exemplo `dev:<slug>` e `export:<slug>:pdf`.

Importante: em Slidev, `<style>` dentro do Markdown é escopado por padrão. Para CSS compartilhado por vários slides do deck, use `decks/styles/index.css`; não dependa de `<style src="...">` dentro do próprio `.md`.

## Imagens

Para imagens usadas por decks em `decks/`, evite caminhos crus como `../public/assets/...` ou `/assets/...` dentro do Markdown. O Slidev/Vite pode reescrever esses caminhos de forma diferente em dev e build.

O padrão atual é usar um componente Vue que importa os assets. A oficina usa [decks/components/DeckImage.vue](./decks/components/DeckImage.vue):

```html
<DeckImage
  class="manuscript pos-doctrinas"
  image="recopilacion-1681-doctrinas.png"
  alt="Recopilación de leyes de los reynos de las Indias"
/>
```

Para um deck novo com outra pasta de imagens, crie um componente parecido ou generalize `DeckImage.vue` com cuidado. O ponto importante é que o componente deve importar os arquivos com `import.meta.glob`, não montar URLs manualmente.

## Layout da Oficina UnB

O deck `oficina-unb` segue um layout meio a meio, aproximando o PPTX original:

- texto e título na metade esquerda;
- manuscrito ou colagem na metade direita;
- variáveis `--oficina-left-*` e `--oficina-right-*` em [styles/oficina-unb.css](./styles/oficina-unb.css);
- classes de posição como `pos-doctrinas`, `pos-quechua-main` e `collage-tupi`.

Se ajustar esse deck, prefira mudar as classes/variáveis em `styles/oficina-unb.css` em vez de colocar estilos inline no Markdown.

## Adicionar decks futuros

1. Crie um novo Markdown em `decks/<slug>.md`.
2. Coloque imagens/documentos em `public/assets/<slug>/` ou `public/assets/shared/`.
3. Crie `styles/<slug>.css` se o deck tiver visual próprio.
4. Importe esse CSS em `decks/styles/index.css`.
5. Se usar imagens locais, crie ou adapte um componente em `decks/components/`.
6. Adicione o deck ao array `decks` em `scripts/build-all.mjs`.
7. Adicione scripts `dev:<slug>` e `export:<slug>:pdf` em `package.json` se forem úteis.
8. Rode `npm run build` antes de publicar.
