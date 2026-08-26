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
  </footer>
</div>

<!--
Tempo: 0:35.
O projeto tem um objetivo amplo: construir uma descrição computacional do Tupi Antigo ancorada no corpus histórico.
Hoje eu não vou tentar mostrar o projeto inteiro. Vou mostrar um problema pequeno, mas representativo: como uma forma histórica deixa de ser apenas texto e entra numa análise formal que pode ser executada e testada.
O objeto científico não é uma aplicação de PLN. É a gramática executável.
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
Tempo: 0:55.
Na prática, começo pela fonte. Não começo por um modelo, um tokenizer ou uma aplicação.
Primeiro preciso decidir o que estou lendo e qual análise linguística quero defender.
Depois escrevo essa análise numa representação formal reutilizável.
Por fim, a representação roda e precisa voltar à linha histórica que motivou a análise.
É nesse último passo que a gramática deixa de ser apenas uma descrição que parece plausível e passa a poder falhar de maneira observável.
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
Tempo: 0:50.
A gramática escrita continua sendo essencial. É nela que se argumenta, compara fontes e explica por que uma análise é preferível a outra.
A camada executável acrescenta outra obrigação: certas decisões precisam ser suficientemente explícitas para participar de operações formais e produzir resultados verificáveis.
Isso transforma a descrição num objeto cumulativo: uma regra nova não responde só pelo exemplo que estou olhando agora, mas também pelo que já foi analisado antes.
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
      <figcaption><strong>Anchieta</strong><br><span>“çupê”: dativo, para, por</span></figcaption>
    </figure>
    <figure class="source-shot">
      <div class="source-image-frame">
        <EnapolImage image="gerardiSupe" alt="Recorte de Gerardi com supe" />
      </div>
      <figcaption><strong>Gerardi</strong><br><span>“supe”: dativo / posposição na análise moderna</span></figcaption>
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
Tempo: 1:10.
Anchieta descreve çupê em prosa gramatical. Gerardi analisa supe com uma metalinguagem linguística moderna.
Aqui, supé entra como objeto gramatical executável: uma peça que pode participar da geração, anotação e teste da frase.
Não é uma competição entre três descrições. A terceira só existe porque as anteriores tornam a categoria e seus usos inteligíveis.
O ganho específico é poder perguntar o que acontece quando esse objeto encontra argumentos concretos no corpus.
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
Tempo: 0:45.
Esse é o problema que quero isolar nesta fala.
A fonte não chega até nós já segmentada em morfemas. Ela registra uma forma de superfície.
A análise linguística pode dizer que essa forma envolve elementos menores, alomorfia ou relações que não correspondem a espaços gráficos.
Então a representação precisa preservar as duas coisas: o que efetivamente aparece e a hipótese sobre como aquilo é estruturado.
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
Tempo: 1:15.
No Padre Nosso de Araújo, a forma que aparece para o destinatário é orébe.
Na tradução funcional, aqui é “a nós” ou “para nós”.
Mas a análise que quero poder reutilizar é mais profunda: o pronome oré combinado com a posposição dativa supé, numa realização superficial específica.
Esse é exatamente o tipo de informação que se perde se tratarmos a linha apenas como uma sequência de tokens gráficos.
Eu preservo orébe como forma de superfície e, ao mesmo tempo, registro a relação oré mais supé como hipótese gramatical.
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
Tempo: 1:00.
Aqui estão as duas camadas juntas.
No léxico do corpus, orébe é explicitamente definido como oré combinado com supé, com a variante correspondente.
Na linha de Araújo, eu posso então usar orébe como a forma superficial esperada sem apagar a estrutura de que ele deriva.
A árvore mostra o outro lado da mesma análise: a saída não é só uma string. Relações e decomposições continuam disponíveis para inspeção e anotação.
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
Tempo: 1:35.
Este é o ponto metodológico central.
Eu parto da fonte histórica, proponho uma estrutura formal e deixo a gramática produzir a forma e a anotação que decorrem dessa estrutura.
[CLICK] Comparo isso com o ground truth linguístico que foi validado. Se não bate, volto à regra, ao léxico ou à própria análise.
[CLICK] Quando uma linha é aprovada, ela vira teste. Qualquer mudança futura roda novamente sobre as linhas anteriores.
Por isso o bootstrapping não é apenas uma forma de construir software aos poucos. Ele mantém o linguista responsável por suas decisões anteriores.
Uma regra que resolve o exemplo de hoje, mas quebra dez linhas de ontem, não pode passar silenciosamente.
[CLICK] Em síntese, uma análise aprovada deixa de ser exemplo isolado e vira compromisso da gramática inteira.
[CLICK] O corpus obriga a gramática a prestar contas.
-->

---
class: enapol-exec
---

<div class="enapol-canvas outputs-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que isso torna possível</p>
    <h1>As ferramentas são saídas. O objeto científico é a gramática executável.</h1>
  </header>

  <section class="outputs-grid">
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
  </section>

  <p class="science-line">A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</p>
</div>

<!--
Tempo: 0:55.
Depois disso, várias ferramentas ficam possíveis, mas eu quero inverter a ordem habitual da apresentação.
Dicionário, geração, busca ou interfaces não são o argumento principal. São saídas de uma infraestrutura descritiva comum.
O ganho científico é poder consultar a análise, revisar generalizações e formular perguntas sobre o corpus sem perder de vista quais decisões gramaticais produziram aqueles dados.
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
Tempo: 0:40.
Fecho com uma consequência concreta do trabalho.
O repositório do dicionário começou em 13 de março de 2026. Em pouco mais de cinco meses, ele já passou de mil verbetes.
O dicionário colaborativo de neologismos não é o centro científico da apresentação, mas o código da gramática já está sendo usado ali.
Ele é aberto e financiado coletivamente, com áudio, citações, perfis, karma, votos e revisão comunitária.
Mesmo sem divulgação ampla ao público geral, já reúne uma pequena comunidade em torno dele.
-->
