---
theme: seriph
title: "Corpus Computacional e Gramática Executável do Tupi Antigo"
info: |
  Apresentação ENAPOL 2026 sobre descrição linguística, corpus computacional e gramática executável do Tupi Antigo.
class: enapol-exec
layout: default
highlighter: shiki
drawings:
  persist: false
transition: fade
css: unocss
---

<div class="enapol-canvas title-slide">
  <main class="title-block">
    <p class="eyebrow">ENAPOL 2026</p>
    <h1>Corpus Computacional e Gramática Executável do Tupi Antigo</h1>
    <p class="subtitle">quando cada linha do corpus se torna um teste da análise</p>
  </main>

  <footer class="presenter-block">
    <strong>Kian Arad Sheik</strong>
    <span>USP / PPG Linguística</span>
  </footer>
</div>

<!--
Tempo: 0:45.
Começo apresentando o projeto não como uma aplicação de PLN, mas como uma proposta de descrição linguística.
O ponto central é que uma gramática pode ser mais do que um texto interpretativo: ela pode ser uma hipótese formal que se deixa executar e testar contra o corpus.
Eu quero que a plateia guarde esta formulação desde o começo: cada linha analisada vira uma obrigação para a gramática.
Transição: para entender por que isso importa, primeiro preciso mostrar o tipo de material com que trabalhamos.
-->

---
class: enapol-exec
---

<div class="enapol-canvas split-slide source-problem-slide">
  <header class="slide-header">
    <p class="eyebrow">O problema</p>
    <h1>Tupi Antigo tem fontes.</h1>
  </header>

  <section class="source-problem-copy">
    <p>O conhecimento linguístico está distribuído entre gramáticas históricas, catecismos, textos do corpus, dicionários, descrições modernas e convenções editoriais.</p>
    <p>Esses dados foram organizados para leitura humana. O desafio é torná-los comparáveis, testáveis e revisáveis de modo sistemático.</p>
  </section>

  <section class="source-strip" aria-label="Fontes a substituir">
    <figure>
      <EnapolImage image="source-anchieta" alt="Placeholder para fonte de Anchieta" />
      <figcaption>Anchieta, 1595<br><span>[REFERÊNCIA / PÁGINA A INSERIR]</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="source-corpus" alt="Placeholder para fonte de Araújo ou Bettendorff" />
      <figcaption>Araújo ou Bettendorff<br><span>[FONTE / PÁGINA A INSERIR]</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="source-modern" alt="Placeholder para fonte moderna ou dicionário" />
      <figcaption>Descrição ou dicionário moderno<br><span>[REFERÊNCIA A INSERIR]</span></figcaption>
    </figure>
  </section>
</div>

<!--
Tempo: 0:55.
Aqui eu explico que o problema não é ausência de documentação.
O Tupi Antigo tem uma tradição documental importante, mas ela está espalhada em gramáticas missionárias, catecismos, vocabulários, textos editados, dicionários e descrições modernas.
Essas fontes foram feitas para leitura humana, cada uma com seus objetivos e suas convenções.
O desafio do projeto é transformar esse material em um espaço em que análises possam ser comparadas, corrigidas e testadas de forma cumulativa.
Transição: para tornar isso menos abstrato, passo agora para uma única linha do corpus.
-->

---
class: enapol-exec
---

<div class="enapol-canvas worked-example-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Uma linha concreta</p>
    <h1>Uma linha do corpus pode testar uma gramática</h1>
  </header>

  <section class="example-pipeline">
    <figure>
      <span>1. forma atestada</span>
      <EnapolImage image="corpus-example-source" alt="Placeholder para linha histórica do corpus" />
      <figcaption>[FONTE / PÁGINA A INSERIR]</figcaption>
    </figure>
    <article class="analysis-placeholder">
      <span>2. análise linguística</span>
      <p>[INSERIR AQUI O FENÔMENO ESCOLHIDO, A SEGMENTAÇÃO E A LEITURA GRAMATICAL DA MESMA LINHA]</p>
    </article>
    <figure>
      <span>3. expressão formal</span>
      <EnapolImage image="corpus-example-formal" alt="Placeholder para expressão formal da mesma linha" />
      <figcaption>pydicate / representação formal</figcaption>
    </figure>
    <figure>
      <span>4. saída gerada</span>
      <EnapolImage image="corpus-example-output" alt="Placeholder para saída gerada da mesma linha" />
      <figcaption>forma e anotação geradas</figcaption>
    </figure>
  </section>

  <section class="mismatch-panel">
    <p>A forma atestada confronta a análise formal.</p>
    <ul>
      <li>regra?</li>
      <li>análise?</li>
      <li>léxico?</li>
      <li>variação ortográfica?</li>
      <li>tradição textual?</li>
    </ul>
  </section>
</div>

<!--
Tempo: 1:25.
Esta é uma das pausas principais da apresentação.
Quando o exemplo real entrar, eu devo explicar os quatro blocos com calma: primeiro a linha atestada, depois a análise linguística, depois a expressão formal e por fim a saída gerada.
O ponto não é dizer que a fonte escaneada é automaticamente a verdade final. O que entra no teste é a minha análise linguística explícita daquela linha: forma esperada, segmentação, glosses, interpretação e alvo ortográfico normalizado.
Se a saída não coincide, a diferença vira uma pergunta linguística: a regra está errada, a análise está errada, falta léxico, há uma variante ortográfica ou a própria tradição textual precisa ser tratada com cuidado?
Transição: depois desse exemplo, posso explicar por que escrever código aqui é uma extensão de práticas que linguistas já usam.
-->

---
class: enapol-exec
---

<div class="enapol-canvas flow-slide programming-slide">
  <header class="slide-header">
    <p class="eyebrow">Código como metalinguagem linguística</p>
    <h1>Linguistas já usam metalinguagens formais.</h1>
  </header>

  <section class="formal-flow" aria-label="Progressão de metalinguagens">
    <div><span>prosa</span><p>regra formulada em linguagem natural</p></div>
    <div><span>glosa</span><p>segmentação e valores gramaticais</p></div>
    <div><span>representação formal</span><p>análise escrita como estrutura explícita</p></div>
    <div><span>saída verificável</span><p>forma comparável ao corpus</p></div>
  </section>

  <p class="keyline">Uma linguagem de programação também pode funcionar como metalinguagem formal para descrição linguística.</p>
</div>

<!--
Tempo: 0:50.
Aqui eu amplio o argumento.
Linguistas já usam metalinguagens formais: glosas, árvores, matrizes de traços, regras, paradigmas, representações fonológicas.
Uma linguagem de programação entra nessa família quando está a serviço da análise linguística.
Ela não substitui a análise; ela obriga a análise a ser explícita o bastante para produzir uma saída verificável.
Transição: essa ideia fica mais clara quando colocamos gramáticas históricas, descrição moderna e formalização executável lado a lado.
-->

---
class: enapol-exec
---

<div class="enapol-canvas comparison-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Metalinguagens em comparação</p>
    <h1>Da prosa gramatical à formalização executável</h1>
  </header>

  <section class="comparison-grid">
    <figure>
      <EnapolImage image="comparison-anchieta" alt="Placeholder para passagem de Anchieta sobre fenômeno específico" />
      <figcaption>Anchieta, 1595<br><span>[PASSAGEM / PÁGINA A INSERIR]</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="comparison-modern" alt="Placeholder para descrição moderna do mesmo fenômeno" />
      <figcaption>Descrição moderna<br><span>[AUTOR, OBRA, PÁGINA A INSERIR]</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="corpus-example-formal" alt="Placeholder para representação executável do mesmo fenômeno" />
      <figcaption>Gramática executável<br><span>mesmo fenômeno, camada formal</span></figcaption>
    </figure>
  </section>

  <p class="keyline">A necessidade de uma metalinguagem permanece; as metalinguagens disponíveis mudam.</p>
</div>

<!--
Tempo: 0:55.
Esta slide ainda depende de um fenômeno específico.
Eu devo deixar claro que não estou dizendo que Anchieta, uma gramática moderna e código fazem a mesma coisa.
O que estou mostrando é uma continuidade: sempre precisamos de uma metalinguagem para falar da língua.
Anchieta descreve em prosa gramatical missionária; a descrição moderna reorganiza os fatos com categorias contemporâneas; a gramática executável acrescenta uma camada em que a hipótese precisa gerar ou anotar dados.
Transição: agora eu mostro o método cumulativo que faz essa camada deixar de ser apenas um exemplo isolado.
-->

---
class: enapol-exec
---

<div class="enapol-canvas method-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Bootstrapping gramatical cumulativo</p>
    <h1>Cada linha acrescenta uma nova obrigação à gramática.</h1>
  </header>

  <section class="method-layout">
    <aside class="shared-state">
      <span>estado persistente</span>
      <strong>GRAMÁTICA + LÉXICO</strong>
      <p>morfemas, alomorfes, valores gramaticais, relações sintáticas e etiquetas semânticas acumulam no mesmo sistema.</p>
    </aside>
    <main class="method-flowchart" aria-label="Fluxo de bootstrapping gramatical">
      <div class="method-row method-row-top">
        <article class="method-step">
          <span>1</span>
          <h2>linha n</h2>
          <p>forma e análise esperadas</p>
        </article>
        <div class="method-arrow">→</div>
        <article class="method-step">
          <span>2</span>
          <h2>morfemas</h2>
          <p>reusar ou definir objetos</p>
        </article>
        <div class="method-arrow">→</div>
        <article class="method-step">
          <span>3</span>
          <h2>estrutura abstrata</h2>
          <p>objetos + relações + sintaxe</p>
        </article>
      </div>
      <div class="method-row method-row-mid" v-click>
        <article class="method-step">
          <span>4</span>
          <h2>spell-out</h2>
          <p><span class="inline-code">eval</span> → forma de superfície</p>
        </article>
        <div class="method-arrow">→</div>
        <article class="method-step">
          <span>5</span>
          <h2>conferência linguística</h2>
          <p>forma, morfemas, estrutura, rótulos</p>
        </article>
      </div>
      <div class="method-row method-row-validate" v-click>
        <article class="method-step method-step-valid">
          <span>6</span>
          <h2>linha validada</h2>
          <p>novo teste para versões futuras</p>
        </article>
      </div>
      <div class="method-row method-row-bottom" v-click>
        <article class="method-step">
          <span>7</span>
          <h2>regressão completa</h2>
          <p><span class="inline-code">1...n</span> → regenerar → diff</p>
        </article>
        <div class="method-arrow">→</div>
        <article class="method-step decision-step">
          <span>8</span>
          <h2>Regressões?</h2>
          <p>o sistema mostra onde e o que mudou</p>
        </article>
      </div>
      <div class="method-branches" v-click>
        <div class="branch branch-bad">SIM → corrigir regra / léxico / análise</div>
        <div class="branch branch-good">NÃO → próxima linha: <span class="inline-code">n ← n + 1</span></div>
      </div>
    </main>
  </section>

  <p class="method-callout" v-click>Uma correção local pode ser testada imediatamente contra todo o corpus validado.</p>
</div>

<!--
Tempo: 1:55.
Esta slide tem cliques.
Primeiro explico só a primeira linha: escolho a linha n, faço a leitura, segmentação, glosses e alvo ortográfico normalizado; depois reuso ou defino os morfemas necessários; por fim escrevo a estrutura abstrata com objetos e relações.
[CLICK] Agora explico o spell-out: a estrutura é avaliada e a gramática produz uma forma de superfície padronizada, além da estrutura ou anotação associada. A comparação não é só igualdade de string; é uma conferência linguística sobre forma, morfemas, estrutura e rótulos.
[CLICK] Se a análise passa, a linha validada vira um novo teste. Cada caso correto passa a ser uma obrigação que a gramática futura precisa continuar explicando.
[CLICK] Depois de adicionar a linha nova, o sistema regenera tudo de 1 até n e mostra os diffs. Isso é o que transforma o trabalho em uma prestação de contas cumulativa.
[CLICK] Se há regressão, volto para corrigir regra, léxico ou análise. Se não há regressão, passo para a próxima linha.
[CLICK] O ponto metodológico maior é este: uma mudança local pode ser testada contra tudo que já foi validado. O Tupi Antigo é o primeiro caso de implementação; a metodologia pode ser reutilizada em outras línguas com corpus suficientemente delimitado e tradição analisável.
Transição: com esse método em mente, dá para explicar por que o projeto mudou de escala no Doutorado Direto.
-->

---
class: enapol-exec
---

<div class="enapol-canvas doctorate-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Do mestrado ao Doutorado Direto</p>
    <h1>As aplicações são saídas. O objeto científico é a gramática.</h1>
  </header>

  <section class="trajectory-row" aria-label="Trajetória do projeto">
    <div>gramática computacional</div>
    <span>→</span>
    <div>prova de conceito</div>
    <span>→</span>
    <div>Doutorado Direto</div>
    <span>→</span>
    <div>corpus integral + metodologia</div>
  </section>

  <section class="doctorate-grid">
    <article class="implemented-panel">
      <h2>Primeira fase</h2>
      <p>O projeto começou no mestrado com a construção da gramática computacional. Ela amadureceu o bastante para sustentar flexão, dicionários, ensino, ortografia, neologismos e infraestrutura de anotação.</p>
      <div class="screenshot-row">
        <EnapolImage image="project-dictionary" alt="Placeholder para dicionário ou conjugação" />
        <EnapolImage image="project-public-facing" alt="Placeholder para aplicação pública ou material de acesso comunitário" />
      </div>
    </article>
    <article class="doctorate-panel">
      <h2>Agora, no doutorado</h2>
      <p>Com a maturação da gramática computacional, o projeto foi aprovado para Doutorado Direto.</p>
      <p>O objetivo agora é implementar sistematicamente o corpus conhecido do Tupi Antigo dentro dessa gramática e, ao fazê-lo, aperfeiçoar simultaneamente a gramática e o método.</p>
      <div class="result-box">
        <span>mudança de escala</span>
        <p>de ferramentas geradas pela gramática para uma gramática testada linha por linha pelo corpus.</p>
      </div>
    </article>
  </section>
</div>

<!--
Tempo: 1:00.
Aqui eu quero contar a trajetória sem transformar a slide em burocracia acadêmica.
O projeto começou no mestrado, com a construção da gramática computacional e das ferramentas que ela permitia gerar.
Essas aplicações são importantes porque demonstraram que a gramática já tinha substância formal suficiente para produzir saídas úteis: conjugação, dicionários, exercícios, transformações ortográficas, neologismos e apoio à anotação.
Mas o objeto científico não é a lista de aplicativos. O objeto científico é a gramática e o método de testá-la.
Com essa maturação, o projeto foi aprovado para Doutorado Direto, e a escala passa a ser implementar sistematicamente o corpus conhecido do Tupi Antigo.
Transição: agora mostro que essa estruturação já produziu resultado linguístico concreto antes mesmo do corpus completo.
-->

---
class: enapol-exec
---

<div class="enapol-canvas payoff-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Payoff científico</p>
    <h1>Um corpus parcial já permitiu inferência gramatical.</h1>
  </header>

  <section class="payoff-grid">
    <article class="payoff-result">
      <p class="payoff-label">Amazônicas X</p>
      <h2>Switch reference em Tupi Antigo</h2>
      <p class="paper-title">Establishing Switch Reference in Old Tupi: Evidence for Conjunctive as a DS Marker</p>
      <div class="stat-row">
        <strong>62</strong>
        <span>exemplos anotados</span>
      </div>
      <div class="stat-pair">
        <div><strong>96,77%</strong><span>DS</span></div>
        <div><strong>3,23%</strong><span>SS</span></div>
      </div>
      <p class="source-note">Fonte verificada: versão local do artigo e `annotated_citations.json`. O resumo público do ResearchGate registra uma versão anterior com 53 exemplos.</p>
    </article>
    <article class="payoff-argument">
      <h2>O que isso demonstra?</h2>
      <p>Mesmo uma anotação parcial já tornou mais rápido localizar, comparar e quantificar exemplos relevantes.</p>
      <div class="mini-flow">
        <span>corpus parcial</span>
        <span>→</span>
        <span>exemplos consultáveis</span>
        <span>→</span>
        <span>padrão detectável</span>
      </div>
      <p>O corpus integral amplia esse ganho para morfemas, alomorfia, ambientes sintáticos, estrutura argumental, variação ortográfica, mudança semântica e contraexemplos.</p>
    </article>
  </section>
</div>

<!--
Tempo: 1:05.
Aqui eu mostro um resultado concreto para evitar que a vantagem pareça apenas promessa futura.
O trabalho apresentado na Amazônicas X analisou exemplos de formas conjuntivas em Tupi Antigo e perguntou se -reme funcionava como marcador de sujeito diferente.
Na versão local atual do artigo e do conjunto de dados, há 62 exemplos: 60 DS e 2 SS, isto é, 96,77% DS e 3,23% SS.
[CONFIRMAR ANTES DA APRESENTAÇÃO: o resumo público do ResearchGate registra 53 exemplos e 96,23% DS; escolher a versão final que será citada.]
O ponto retórico não é vender porcentagem como prova automática de teoria. O ponto é que a estruturação do corpus permitiu encontrar, comparar e quantificar exemplos que seriam muito mais lentos de levantar manualmente.
Transição: se isso já acontece com um corpus parcial, a pergunta natural é o que muda quando o corpus conhecido inteiro fica estruturado.
-->

---
class: enapol-exec
---

<div class="enapol-canvas corpus-infra-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Infraestrutura de pesquisa</p>
    <h1>Quando o corpus conhecido inteiro se torna consultável</h1>
  </header>

  <section class="corpus-infra-grid">
    <article>
      <h2>Não é só velocidade</h2>
      <p>É colocar análises diferentes dentro da mesma representação explícita, versionada e regenerável.</p>
    </article>
    <article>
      <h2>O que se torna perguntável</h2>
      <ul>
        <li>distribuição de morfemas e alomorfes;</li>
        <li>ambientes sintáticos e estrutura argumental;</li>
        <li>rótulos semânticos e mudança de sentido;</li>
        <li>variação ortográfica e tradição textual;</li>
        <li>análises concorrentes, exceções e contraexemplos.</li>
      </ul>
    </article>
    <article class="corpus-method-card">
      <h2>Escopo metodológico</h2>
      <p>Tupi Antigo é o caso concreto: finito o bastante para ser implementável, amplo o bastante para análise séria, documentado o bastante para não depender de especulação pura.</p>
      <p>A proposta pode ser reutilizada em outras línguas de corpus com tradições suficientemente delimitadas e analisáveis.</p>
    </article>
  </section>

  <p class="science-line">Tupi Antigo é o primeiro caso de implementação; a metodologia não precisa terminar nele.</p>
</div>

<!--
Tempo: 0:55.
Nesta slide eu explico a ideia do corpus completo sem prometer algo impossível.
Completo aqui significa o corpus histórico conhecido e selecionado para o projeto, não todas as frases já faladas por pessoas em Tupi Antigo.
O ganho não é apenas achar exemplos mais rápido. O ganho é que morfologia, sintaxe, alomorfia, léxico, semântica, ortografia e análises concorrentes passam a compartilhar uma representação explícita.
Quando uma regra melhora, o corpus pode ser regenerado. Quando uma análise muda, as consequências aparecem em vez de ficarem escondidas em anotações isoladas.
Transição: fecho mostrando alguns lugares onde essa infraestrutura já aparece como saída consultável.
-->

---
class: enapol-exec
---

<div class="enapol-canvas resource-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Explore o ecossistema</p>
    <h1>Saídas públicas da mesma infraestrutura formal</h1>
  </header>

  <section class="resource-grid">
    <article>
      <EnapolImage image="qr-dictionary" alt="QR code para o dicionário digital de Tupi Antigo" />
      <h2>Dicionário</h2>
      <p>kiansheik.io/nhe-enga</p>
      <span>consulta lexical e formas geradas</span>
    </article>
    <article>
      <EnapolImage image="qr-corpus" alt="QR code para o repositório oldtupicorpus" />
      <h2>Gramática / corpus</h2>
      <p>github.com/kiansheik/oldtupicorpus</p>
      <span>implementação composicional do corpus</span>
    </article>
    <article>
      <EnapolImage image="qr-neo" alt="QR code para o Dicionário de Tupi" />
      <h2>Neologismos</h2>
      <p>neo.academiatupi.com</p>
      <span>aplicação pública apoiada pelo trabalho formal</span>
    </article>
  </section>

  <footer class="resource-closing">
    <p>Tupi Antigo é o caso concreto. A proposta metodológica é maior que uma língua.</p>
    <strong>A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</strong>
  </footer>
</div>

<!--
Tempo: 0:55.
Esta é a tela final para a plateia explorar depois da fala.
Eu devo dizer que estes links não são o centro científico da apresentação, mas mostram saídas possíveis da mesma infraestrutura formal.
O dicionário mostra consulta lexical e formas geradas. O repositório do corpus mostra a implementação composicional e o sistema de testes. O Dicionário de Tupi mostra uma aplicação pública que se beneficia dessa base formal.
Fecho com a tese principal: Tupi Antigo é o caso concreto, mas a proposta metodológica é maior que uma língua.
Última frase para dizer devagar: a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.
-->
