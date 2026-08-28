---
theme: seriph
title: "Corpus Computacional e Gramática Executável do Tupi Antigo"
info: |
  Apresentação ENAPOL 2026 sobre descrição linguística executável e teste cumulativo contra o corpus de Tupi Antigo.
class: enapol-exec
layout: default
highlighter: shiki
drawings:
  persist: false
transition: fade
css: unocss
---

<div class="enapol-canvas title-slide">
  <img class="fflch-logo" src="https://linguistica.fflch.usp.br/themes/contrib/fflch-theme/images/logo.png" alt="FFLCH USP" />

  <main class="title-block">
    <p class="eyebrow">29º ENAPOL, USP, 2026</p>
    <h1>Corpus Computacional e Gramática Executável do Tupi Antigo</h1>
    <p class="subtitle">quando cada linha do corpus se torna um teste da análise</p>
  </main>

  <footer class="presenter-block">
    <strong>Kian Arad Sheik</strong>
    <span>USP / PPG Linguística</span>
    <span class="advisor-line">Orientador: Prof. Dr. Thomas Daniel Finbow</span>
  </footer>
</div>

<!--
Tempo máximo: 0:35.
Meu projeto, orientado pelo Prof. Dr. Thomas Daniel Finbow, tem um objetivo amplo: construir uma descrição computacional do Tupi Antigo ancorada no corpus histórico.
Hoje eu não vou tentar mostrar o projeto inteiro. Quero mostrar um problema pequeno, mas representativo: como uma forma histórica deixa de ser apenas texto e entra numa análise formal que pode ser executada e testada.
O objeto científico aqui não é uma aplicação de PLN. É a gramática executável.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas project-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que eu faço</p>
    <h1>Da fonte histórica a uma hipótese gramatical que pode falhar.</h1>
  </header>

  <section class="project-grid">
    <article>
      <span>1 · corpus</span>
      <p>localizo a ocorrência, preservo a fonte e estabeleço leitura, normalização, glosas e interpretação.</p>
    </article>
    <article>
      <span>2 · descrição</span>
      <p>morfemas, alomorfes e relações gramaticais viram objetos formais reutilizáveis.</p>
    </article>
    <article>
      <span>3 · teste</span>
      <p>a estrutura é executada e confrontada com a linha que pretende explicar.</p>
    </article>
  </section>

  <p class="focus-line">O computador não substitui a análise linguística. Ele obriga a análise a ser explícita.</p>
</div>

<!--
Tempo máximo: 0:50.
Eu começo pela fonte, não pelo modelo.
Primeiro preciso estabelecer o que estou lendo: fonte, normalização, glosa e interpretação. Depois, morfemas, alomorfes e relações gramaticais viram objetos formais reutilizáveis.
Finalmente eu executo essa representação e confronto o resultado com a linha que ela pretende explicar.
Então o computador não substitui a análise linguística. Ele obriga a análise a ser explícita o suficiente para poder falhar.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas comparison-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Duas camadas complementares</p>
    <h1>A proposta não é substituir a gramática escrita.</h1>
  </header>

  <section class="comparison-grid">
    <figure>
      <div class="statement-panel">
        <strong>descrição escrita</strong>
        <p>explica categorias, generalizações, exceções e argumentos em linguagem humana.</p>
      </div>
      <figcaption>indispensável para interpretar e justificar</figcaption>
    </figure>
    <figure>
      <div class="statement-panel executable-panel">
        <strong>camada executável</strong>
        <p>obriga essas decisões a terem forma suficiente para gerar, anotar e ser testadas.</p>
      </div>
      <figcaption>uma hipótese formal que o corpus pode contrariar</figcaption>
    </figure>
    <figure>
      <div class="statement-panel consequence-panel">
        <strong>efeito metodológico</strong>
        <p>cada decisão nova precisa continuar compatível com as linhas já validadas.</p>
      </div>
      <figcaption>descrição cumulativa, não exemplos isolados</figcaption>
    </figure>
  </section>

  <p class="keyline">A proposta não é substituir a gramática escrita. É acrescentar uma camada formal executável.</p>
</div>

<!--
Tempo máximo: 0:45.
E isso não pretende substituir a gramática escrita.
É na descrição escrita que eu posso comparar fontes, argumentar por uma categoria, explicar uma exceção e dizer por que uma análise é melhor que outra.
A camada executável acrescenta outra obrigação: algumas dessas decisões precisam ter uma representação formal suficientemente precisa para produzir resultados verificáveis.
E isso faz com que a descrição se torne cumulativa.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas comparison-slide supe-comparison-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Um mesmo problema em três metalinguagens</p>
    <h1><span class="inline-code">çupê / supe / supé</span>: da descrição à execução</h1>
  </header>

  <section class="comparison-grid supe-grid">
    <figure class="source-shot">
      <div class="source-image-frame">
        <EnapolImage image="anchietaSupe" alt="Recorte da gramática de Anchieta com çupê" />
      </div>
      <figcaption><strong>Anchieta, 1595</strong><span><em>Arte de grammatica da lingoa mais usada na costa do Brasil</em><br>“çupê”: dativo, para, por</span></figcaption>
    </figure>
    <figure class="source-shot">
      <div class="source-image-frame">
        <EnapolImage image="gerardiSupe" alt="Recorte de Gerardi com supe" />
      </div>
      <figcaption><strong>Ferraz Gerardi, 2023</strong><span><em>A Role and Reference Grammar Description of Tupinambá</em><br>“supe”: dativo / posposição na análise moderna</span></figcaption>
    </figure>
    <figure class="code-figure">
      <div class="source-code-panel compact-code">
        <p><span class="code-keyword">class</span> Dative(Postposition):</p>
        <p class="indent-1">def __init__(self,</p>
        <p class="indent-2">definition="to, for, in favor of"):</p>
        <p class="indent-2">super().__init__(</p>
        <p class="indent-3">"supé",</p>
        <p class="indent-3">definition=definition,</p>
        <p class="indent-3">tag="[POSTPOSITION:DATIVE]"</p>
        <p class="indent-2">)</p>
        <p class="code-gap">supé = Dative()</p>
      </div>
      <figcaption><strong>pydicate</strong><br><span><span class="inline-code">supé</span> como objeto gramatical executável</span></figcaption>
    </figure>
  </section>

  <p class="keyline">A metalinguagem muda; o projeto depende das descrições anteriores para tornar a hipótese executável.</p>
</div>

<!--
Tempo máximo: 1:05.
Aqui dá para ver a mesma categoria atravessando três metalinguagens.
Em Anchieta, em 1595, temos çupê descrito como dativo. Em Ferraz Gerardi, em 2023, supe aparece numa análise linguística moderna do Tupinambá.
E à direita está a minha terceira camada: supé passa a existir também como um objeto gramatical executável, uma posposição dativa que pode entrar nas operações da gramática.
Não estou dizendo que a terceira descrição substitui as anteriores. É justamente o contrário: eu consigo formalizá-la porque existe uma tradição descritiva que me permite saber o que estou formalizando.
Agora eu posso perguntar o que acontece quando esse objeto encontra formas reais do corpus.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas problem-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O problema concreto</p>
    <h1>Uma frase histórica não é apenas uma sequência de palavras.</h1>
  </header>

  <section class="problem-grid">
    <article>
      <span>superfície</span>
      <p>a fonte registra formas já compostas, com ortografia histórica e fronteiras que nem sempre coincidem com a análise.</p>
    </article>
    <article>
      <span>estrutura</span>
      <p>a descrição precisa recuperar relações morfológicas e sintáticas que não estão separadas visualmente.</p>
    </article>
    <article>
      <span>responsabilidade</span>
      <p>se eu proponho uma decomposição, a gramática precisa conseguir usá-la sem perder as formas já explicadas.</p>
    </article>
  </section>

  <section class="question-panel">
    <span>questão</span>
    <p>Como representar a forma que aparece na fonte sem confundir superfície gráfica com estrutura gramatical?</p>
  </section>
</div>

<!--
Tempo máximo: 0:35.
E aí aparece o problema concreto.
A fonte histórica não chega até nós segmentada em morfemas. Ela registra uma forma de superfície.
Mas a análise pode recuperar relações que não coincidem com as fronteiras gráficas da fonte.
Então eu preciso conservar ao mesmo tempo duas coisas: o que efetivamente aparece no documento e a hipótese sobre a estrutura dessa forma.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas corpus-line-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Araújo, Catecismo, Padre Nosso</p>
    <h1><span class="inline-code">orébe</span> na superfície; <span class="inline-code">oré + supé</span> na análise.</h1>
  </header>

  <section class="line-layout">
    <figure>
      <EnapolImage image="araujoPaiNosso" alt="Recorte do Padre Nosso no Catecismo de Araújo" />
      <figcaption>Araújo, 1686, Livro I, Padre Nosso</figcaption>
    </figure>
    <article class="line-card layered-analysis-card">
      <span>alvo normalizado</span>
      <p class="tupi-line">oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe</p>
      <p class="translation">“Dá-nos hoje o nosso alimento de cada dia.”</p>
      <div class="layer-row"><strong>forma de superfície</strong><span class="inline-code">orébe</span></div>
      <div class="layer-row"><strong>função</strong><span>dativo: “a nós / para nós”</span></div>
      <div class="layer-row"><strong>análise mais profunda</strong><span><span class="inline-code">oré</span> + <span class="inline-code">supé</span></span></div>
    </article>
  </section>

  <p class="focus-line">A segmentação analítica não precisa coincidir com espaços na fonte.</p>
</div>

<!--
Tempo máximo: 1:05.
Por exemplo, no Padre Nosso do Catecismo de Araújo, de 1686, aparece aqui orébe.
Funcionalmente, é “a nós” ou “para nós”. Essa é a forma que eu quero preservar como superfície: orébe.
Mas a análise que eu quero reutilizar na gramática é oré + supé: o pronome oré combinado com a posposição dativa que acabamos de ver.
Se eu tratasse essa frase apenas como uma sequência de palavras separadas por espaço, essa relação desapareceria.
A segmentação analítica, portanto, não precisa coincidir com a segmentação gráfica da fonte.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas tree-slide executable-example-slide">
  <header class="slide-header compact">
    <p class="eyebrow">A mesma linha como objeto formal</p>
    <h1>A análise precisa produzir a forma e conservar a estrutura.</h1>
  </header>

  <section class="tree-layout executable-tree-layout">
    <article class="tree-explain executable-code-card">
      <span>no corpus executável</span>
      <div class="code-block">
        <p>orébe = (oré * supé).var(1)</p>
        <p class="code-gap">...</p>
        <p>(((emi * (u * oré))</p>
        <p class="indent-1">@ (nduara * (ara * iabiõ)))</p>
        <p class="indent-1">* (meeng * +endé).imp())</p>
        <p>+ kori</p>
        <p>+ orébe</p>
      </div>
      <p>O objeto guarda a análise; o spell-out devolve <span class="inline-code">orébe</span>.</p>
    </article>
    <figure class="tree-frame">
      <EnapolImage image="araujo-line-tree" alt="Árvore formal da linha de Araújo com o dativo analisado" />
    </figure>
  </section>

  <p class="method-callout">A forma correta não basta: a estrutura produzida também faz parte da hipótese.</p>
</div>

<!--
Tempo máximo: 0:55.
E é assim que isso entra no corpus executável.
No léxico, orébe é explicitamente definido a partir de oré * supé, com a variante superficial correspondente. Depois eu posso usar orébe dentro da representação da frase inteira.
O resultado esperado não é apenas que o sistema devolva a string correta. A árvore à direita mostra que a estrutura que produziu essa forma continua disponível.
Então a hipótese tem duas responsabilidades: produzir a forma e conservar a análise que eu estou defendendo.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas method-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Do exemplo ao método</p>
    <h1>Cada linha validada vira um teste.</h1>
  </header>

  <section class="method-layout">
    <aside class="shared-state">
      <span>estado persistente</span>
      <strong>GRAMÁTICA + LÉXICO</strong>
      <p>cada análise aprovada aumenta o conjunto de decisões que uma mudança futura precisa respeitar.</p>
    </aside>
    <main class="method-flowchart" aria-label="Fluxo de bootstrapping e regressão">
      <div class="method-row method-row-top">
        <article class="method-step"><span>1</span><h2>fonte histórica</h2><p>linha e contexto documental</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>2</span><h2>estrutura formal</h2><p>morfemas e relações explícitas</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>3</span><h2>forma gerada / anotada</h2><p>resultado da hipótese</p></article>
      </div>
      <div class="method-row method-row-mid" v-click>
        <article class="method-step"><span>4</span><h2>ground truth</h2><p>comparar com a linha validada</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>5</span><h2>revisão</h2><p>regra, léxico ou análise</p></article>
      </div>
      <div class="method-row method-row-bottom" v-click>
        <article class="method-step method-step-valid"><span>6</span><h2>regressão</h2><p>rodar novamente as linhas anteriores</p></article>
        <div class="method-arrow">↺</div>
        <article class="method-step decision-step"><span>7</span><h2>próxima linha</h2><p>só depois de preservar o que já funcionava</p></article>
      </div>
      <div class="method-summary-strip" v-click>
        <strong>síntese</strong>
        <p>Uma análise aprovada deixa de ser exemplo isolado e passa a ser compromisso da gramática inteira.</p>
      </div>
    </main>
  </section>

  <p class="method-callout" v-click>O corpus obriga a gramática a prestar contas.</p>
</div>

<!--
Tempo máximo: 1:35.
Este é o ponto metodológico principal.
Eu parto de uma linha da fonte, proponho uma estrutura e deixo a gramática produzir aquilo que decorre dessa análise.
[CLICK 1] Comparo o resultado com o ground truth linguístico que eu validei. Se não bate, eu preciso revisar a regra, o léxico ou a própria análise.
[CLICK 2] Quando bate, essa linha deixa de ser só um exemplo. Ela vira um teste de regressão. Então, quando eu modificar a gramática para analisar uma nova linha, rodo novamente as anteriores. Uma regra que resolve o exemplo de hoje mas quebra dez exemplos de ontem não pode passar silenciosamente.
[CLICK 3] É nesse sentido que a descrição se torna cumulativa: cada análise aprovada vira um compromisso da gramática inteira.
[CLICK 4] O corpus obriga a gramática a prestar contas.
[TROCAR SLIDE. NÃO EXPLICAR BOOTSTRAPPING DE NOVO.]
-->

---
class: enapol-exec
---

<div class="enapol-canvas outputs-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que isso torna possível</p>
    <h1>As ferramentas são saídas. O objeto científico é a gramática executável.</h1>
  </header>

  <section class="outputs-content">
    <div class="outputs-grid">
      <article>
        <span>consulta linguística</span>
        <p>buscar morfemas, alomorfes, ambientes sintáticos e estruturas em um corpus analisado de modo consistente.</p>
      </article>
      <article>
        <span>revisão explícita</span>
        <p>mudar uma generalização e ver exatamente quais análises anteriores deixam de funcionar.</p>
      </article>
      <article>
        <span>novas perguntas</span>
        <p>quantificar distribuições e localizar padrões sem separar a busca dos pressupostos gramaticais que a tornam possível.</p>
      </article>
      <article>
        <span>produtos derivados</span>
        <p>dicionários, geração e outras interfaces podem reutilizar a mesma descrição sem se tornarem o centro do projeto.</p>
      </article>
    </div>
    <aside class="corpus-qr-card">
      <a class="qr-image-link" href="https://kiansheik.io/oldtupicorpus/" target="_blank" rel="noopener noreferrer" aria-label="Abrir o corpus digital de Tupi Antigo">
        <EnapolImage image="qr-oldtupicorpus" alt="QR code para o corpus digital de Tupi Antigo" />
      </a>
      <a class="qr-label-link" href="https://kiansheik.io/oldtupicorpus/" target="_blank" rel="noopener noreferrer">kiansheik.io/oldtupicorpus</a>
    </aside>
  </section>

  <p class="science-line">A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</p>
</div>

<!--
Tempo máximo: 0:50.
A partir daí aparecem várias possibilidades.
Eu posso consultar morfemas e ambientes sintáticos, mudar uma generalização e descobrir exatamente quais linhas deixam de funcionar, ou investigar distribuições no corpus.
E a mesma infraestrutura pode sustentar produtos como dicionários e geração.
O QR aponta para o corpus digital, onde essa infraestrutura aparece como consulta pública.
Mas eu quero manter a ordem da argumentação clara: essas ferramentas são saídas.
O objeto científico é a gramática executável, uma hipótese sobre o corpus que o próprio corpus pode testar.
[TROCAR SLIDE]
-->

---
class: enapol-exec
---

<div class="enapol-canvas resource-slide public-output-slide neo-only-slide">
<header class="slide-header compact">
<p class="eyebrow">Uma saída pública da mesma infraestrutura</p>
<h1>O código da gramática já alimenta um dicionário colaborativo.</h1>
</header>
<section class="neo-only-layout">
<article class="neo-qr-card">
<EnapolImage image="qr-neo" alt="QR code para o dicionário de neologismos" />
<h2>neo.academiatupi.com</h2>
<p>dicionário colaborativo de neologismos em Tupi Antigo</p>
</article>
<article class="neo-stats-card simplified-neo-card">
<span>projeto iniciado em março de 2026</span>
<h2>Em pouco mais de cinco meses: mais de 1000 verbetes, com áudio, citações e revisão comunitária</h2>
<p>Aberto e financiado coletivamente. A comunidade propõe verbetes e exemplos, vota, revisa fontes e participa por meio de perfis e karma.</p>
<div class="stats-grid">
<div><strong>1096</strong><span>verbetes</span></div>
<div><strong>189</strong><span>exemplos</span></div>
<div><strong>24</strong><span>usuários</span></div>
</div>
<p class="stats-note">Não é o objeto da pesquisa. É um lugar em que a gramática executável já está sendo usada por uma comunidade.</p>
</article>
</section>
<footer class="resource-closing">
<strong>A gramática executável não termina no teste: ela também pode sustentar ferramentas abertas.</strong>
</footer>
</div>

<!--
Tempo máximo: 0:40.
E termino só com uma consequência concreta.
Esse código já está sendo reutilizado num dicionário colaborativo de neologismos em Tupi Antigo.
O projeto começou em 13 de março deste ano e, em pouco mais de cinco meses, já passou de mil verbetes, com áudio, citações, exemplos e revisão comunitária.
É uma comunidade pequena, mas é um exemplo de uma gramática executável deixando de ser apenas infraestrutura de pesquisa e sustentando uma ferramenta aberta.
Quem quiser conhecer, o QR code está aqui. Obrigado.
-->
