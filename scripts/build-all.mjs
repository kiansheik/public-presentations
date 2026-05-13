import { spawnSync } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const fallbackRepo = "public-presentations";
const repository = process.env.GITHUB_REPOSITORY?.split("/")[1] || fallbackRepo;
const baseRoot = normalizeBase(process.env.SLIDEV_BASE || `/${repository}/`);
const slidevBin = fileURLToPath(
  new URL(`../node_modules/.bin/slidev${process.platform === "win32" ? ".cmd" : ""}`, import.meta.url)
);

const decks = [
  {
    file: "decks/oficina-unb.md",
    slug: "oficina-unb",
    title: "Tupi Antigo: uma língua de contato no Brasil colonial",
  },
];

rmSync("dist", { recursive: true, force: true });
mkdirSync("dist", { recursive: true });

for (const deck of decks) {
  const outDir = resolve("dist", deck.slug);
  const base = `${baseRoot}${deck.slug}/`;
  const result = spawnSync(
    slidevBin,
    ["build", deck.file, "--out", outDir, "--base", base],
    { stdio: "inherit" }
  );

  if (result.error) {
    console.error(`Failed to run Slidev for ${deck.file}: ${result.error.message}`);
    process.exit(1);
  }

  if (result.status !== 0) {
    process.exit(result.status || 1);
  }
}

const links = decks
  .map((deck) => `      <li><a href="./${deck.slug}/">${deck.title}</a></li>`)
  .join("\n");

writeFileSync(
  "dist/index.html",
  `<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Oficinas e apresentações</title>
  <style>
    :root {
      color-scheme: light;
      --red: #7a1f1f;
      --cream: #f7efe2;
      --ink: #231f20;
      --gold: #b78b3b;
    }

    body {
      font-family: system-ui, sans-serif;
      max-width: 760px;
      margin: 5rem auto;
      padding: 0 1.5rem;
      line-height: 1.5;
      background: var(--cream);
      color: var(--ink);
    }

    h1 {
      font-size: clamp(2rem, 6vw, 2.75rem);
      line-height: 1.05;
    }

    a {
      color: var(--red);
      font-weight: 750;
      text-decoration-thickness: 0.08em;
      text-underline-offset: 0.2em;
    }

    ul {
      padding-left: 1.25rem;
    }

    li {
      margin: 0.8rem 0;
      font-size: 1.15rem;
    }

    .note {
      border-top: 3px solid var(--gold);
      margin-top: 2.5rem;
      padding-top: 1rem;
    }
  </style>
</head>
<body>
  <main>
    <h1>Oficinas e apresentações</h1>
    <ul>
${links}
    </ul>
    <p class="note">Apresentações HTML interativas construídas com Slidev.</p>
  </main>
</body>
</html>
`
);

function normalizeBase(value) {
  const withLeadingSlash = value.startsWith("/") ? value : `/${value}`;
  return withLeadingSlash.endsWith("/") ? withLeadingSlash : `${withLeadingSlash}/`;
}
