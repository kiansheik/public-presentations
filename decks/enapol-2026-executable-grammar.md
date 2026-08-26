---
theme: seriph
title: "Corpus Computacional e Gramática Executável do Tupi Antigo"
info: |
  Apresentação ENAPOL 2026 sobre uma gramática executável que transforma análises de linhas históricas em testes cumulativos do corpus de Tupi Antigo.
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
Hoje eu apresento o projeto Corpus Computacional e Gramática Executável do Tupi Antigo.
O ponto central não é apresentar uma aplicação de PLN, nem uma demonstração de ferramentas.
O objeto científico é uma gramática: uma descrição formal capaz de gerar, anotar e testar as próprias linhas do corpus que ela pretende explicar.
Transição: começo situando exatamente o que o projeto faz.
-->

---
class: enapol-exec
---

<div class="enapol-canvas project-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que o projeto faz</p>
    <h1>Transformo análise linguística em uma gramática executável.</h1>
  </header>

  <section class="project-grid">
    <article>
      <span>corpus</span>
      <p>cada ocorrência recebe fonte, leitura, alvo normalizado, segmentação, glosas e interpretação controladas.</p>
    </article>
    <article>
      <span>gramática</span>
      <p>morfemas, alomorfes, relações sintáticas e valores semânticos são escritos como objetos formais reutilizáveis.</p>
    </article>
    <article>
      <span>teste</span>
      <p>a estrutura roda, gera uma forma de superfície e confronta a hipótese com a análise linguística daquela linha.</p>
    </article>
  </section>

  <p class="focus-line">O caso concreto é Tupi Antigo; a contribuição maior é um método reutilizável para línguas de corpus.</p>
</div>

<!--
Tempo: 0:55.
Antes de entrar no exemplo, quero deixar claro o que eu faço na prática.
Eu parto de linhas do corpus histórico: fonte, leitura, alvo normalizado, segmentação, glosas e interpretação.
Depois escrevo os elementos da análise como objetos formais: morfemas, alomorfes, relações sintáticas e valores semânticos.
Por fim, rodo a estrutura. A gramática faz o spell-out e produz uma forma de superfície que pode ser comparada ao alvo analisado.
O Tupi Antigo é o caso concreto; a contribuição maior é um método para línguas de corpus com documentação delimitada.
Transição: isso muda a forma como uma gramática presta contas.
-->

---
class: enapol-exec
---

<div class="enapol-canvas comparison-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Da gramática como texto à gramática como teste</p>
    <h1>A metalinguagem muda; a hipótese gramatical continua.</h1>
  </header>

  <section class="comparison-grid">
    <figure>
      <EnapolImage image="TODO_anchieta_grammar_page_same_topic" alt="TODO: página de Anchieta sobre o mesmo tópico gramatical" />
      <figcaption>gramática histórica<br><span>Anchieta, 1595</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="TODO_gerardi_tupinamba_page_same_topic" alt="TODO: página de Gerardi ou gramática moderna sobre o mesmo tópico" />
      <figcaption>descrição moderna<br><span>Gerardi / descrição atual</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="TODO_pydicate_executable_grammar_screenshot" alt="TODO: screenshot de uma representação pydicate" />
      <figcaption>camada executável<br><span>mesma análise, novo modo de teste</span></figcaption>
    </figure>
  </section>

  <p class="keyline">A proposta não substitui a gramática escrita; acrescenta uma camada formal que pode ser executada, versionada e corrigida.</p>
</div>

<!--
Tempo: 1:00.
Aqui eu situo o projeto dentro de uma continuidade de descrição gramatical.
Não estou contrapondo Anchieta, gramática moderna e código como se uma etapa apagasse a outra.
O projeto depende das gramáticas históricas e das descrições modernas.
O que muda é a metalinguagem: além da prosa gramatical e da análise publicada, acrescento uma camada formal que pode ser rodada.
Com isso, uma decisão gramatical deixa rastros: ela gera formas, produz estrutura, falha quando a análise não está suficientemente explícita e pode ser corrigida depois.
Transição: a necessidade aparece melhor quando olhamos para o tipo de problema que uma linha histórica cria.
-->

---
class: enapol-exec
---

<div class="enapol-canvas problem-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O problema</p>
    <h1>Uma linha histórica concentra muitas decisões linguísticas.</h1>
  </header>

  <section class="problem-grid">
    <article>
      <span>fonte</span>
      <p>ortografia histórica, edição, variantes, leitura paleográfica e tradição textual.</p>
    </article>
    <article>
      <span>análise</span>
      <p>segmentação, glosas, relações sintáticas, morfemas abstratos e alvo normalizado.</p>
    </article>
    <article>
      <span>responsabilidade</span>
      <p>cada regra criada para uma linha pode mudar a saída de linhas já analisadas.</p>
    </article>
  </section>

  <section class="question-panel">
    <span>pergunta da fala</span>
    <p>Como transformar uma frase histórica em uma hipótese gramatical testável?</p>
  </section>
</div>

<!--
Tempo: 0:55.
O problema não é simplesmente digitalizar uma fonte.
Uma linha histórica concentra decisões de vários tipos: leitura da fonte, normalização ortográfica, segmentação, glossas, morfemas abstratos, relações sintáticas e interpretação.
Além disso, nenhuma decisão fica isolada. Quando eu crio uma regra para uma linha, essa regra pode afetar outras linhas já analisadas.
Então a pergunta da fala é concreta: como transformar uma frase histórica em uma hipótese gramatical testável?
Transição: agora mostro a linha que vou usar como exemplo.
-->

---
class: enapol-exec
---

<div class="enapol-canvas corpus-line-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Exemplo</p>
    <h1>Araújo, Catecismo, Padre Nosso</h1>
  </header>

  <section class="line-layout">
    <figure>
      <EnapolImage image="TODO_araujo_or_bettendorff_short_line" alt="TODO: recorte da linha de Araújo ou Bettendorff" />
      <figcaption>Araújo, 1686, Livro I, Padre Nosso, p. 2, linhas 1-2</figcaption>
    </figure>
    <article class="line-card">
      <span>alvo normalizado atual</span>
      <p class="tupi-line">oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe</p>
      <p class="translation">"Dá-nos hoje o nosso alimento de cada dia."</p>
      <div class="orebe-note">
        <strong>orébe</strong>
        <span>forma de superfície própria; analisável mais profundamente como <span class="inline-code">oré + supé</span>.</span>
      </div>
    </article>
  </section>

  <section class="difficulty-strip">
    <div>posse nominal</div>
    <div>nominalização</div>
    <div>expressão temporal</div>
    <div>imperativo</div>
    <div>dativo: orébe</div>
  </section>
</div>

<!--
Tempo: 1:20.
O exemplo vem de Araújo, Catecismo de 1686, na oração do Padre Nosso.
A linha corresponde a "dá-nos hoje o nosso alimento de cada dia".
O alvo normalizado atual é: oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe.
A frase é pequena, mas já obriga várias decisões: posse nominal, nominalização em rembi'u, expressão temporal, imperativo e destinatário.
Aqui é importante tratar orébe com cuidado. Na superfície, orébe é a forma própria que aparece na sentença; em uma análise mais profunda, ela pode ser decomposta como oré mais supé.
Transição: agora mostro como essa análise aparece na metalinguagem executável.
-->

---
class: enapol-exec
---

<div class="enapol-canvas encoding-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Análise executável</p>
    <h1>A mesma análise, escrita como estrutura formal.</h1>
  </header>

  <section class="encoding-grid">
    <article class="code-card">
      <span>estrutura formal</span>
      <p class="code-line">(((emi * (u * oré)) @ (nduara * (ara * iabiõ))) * (meeng * +endé).imp()) + kori + orébe</p>
    </article>
    <article class="output-card">
      <span>spell-out</span>
      <p class="tupi-line">oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe</p>
      <p>Registro local: <span class="inline-code">araujo_catecismo_1686:0007</span></p>
    </article>
  </section>

  <section class="analysis-grid">
    <div><span>morfemas</span><p>reusar ou definir cada objeto necessário para a sentença.</p></div>
    <div><span>sintaxe</span><p>compor posse, modificação temporal, imperativo e dativo.</p></div>
    <div><span>verificação</span><p>comparar forma gerada, estrutura e rótulos com a análise aprovada.</p></div>
  </section>
</div>

<!--
Tempo: 1:20.
Esta é a mesma análise, agora escrita em uma metalinguagem executável.
Eu não preciso explicar cada operador na fala, mas preciso deixar claro o princípio.
Cada morfema é definido ou reaproveitado como objeto; a sentença é composta com relações explícitas; depois a estrutura é avaliada.
O spell-out gera a forma de superfície padronizada.
Se a forma, a estrutura e os rótulos batem com a análise aprovada, essa linha vira teste.
Se não batem, a falha aponta para uma decisão linguística a revisar, não apenas para um erro técnico.
Transição: para tornar visível o que fica escondido numa linha de código, mostro a estrutura como árvore.
-->

---
class: enapol-exec
---

<div class="enapol-canvas tree-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Estrutura</p>
    <h1>A linha do corpus vira uma árvore consultável.</h1>
  </header>

  <section class="tree-layout">
    <figure class="tree-frame">
      <EnapolImage image="araujo-line-tree" alt="Árvore formal da linha de Araújo com posse, tempo, imperativo e dativo" />
    </figure>
    <article class="tree-explain">
      <span>o ganho descritivo</span>
      <p>A forma gerada não é só uma string. A análise guarda morfemas, relações, rótulos e decomposições.</p>
      <ul>
        <li><span class="inline-code">rembi'u</span> como estrutura possuída;</li>
        <li>tempo e frequência como modificador;</li>
        <li>imperativo como forma verbal derivada;</li>
        <li><span class="inline-code">orébe</span> como forma superficial com análise interna possível.</li>
      </ul>
    </article>
  </section>
</div>

<!--
Tempo: 0:55.
Esta árvore mostra por que o resultado não é apenas uma string correta.
A estrutura explicita que rembi'u pertence a uma relação de posse, que a expressão temporal modifica o pedido, que eîme'eng está no imperativo e que orébe é tratado como forma dativa própria, sem impedir uma decomposição mais profunda como oré mais supé.
Isso faz a análise ficar consultável: posso perguntar por morfemas, alomorfes, relações e ambientes.
Transição: o exemplo individual só vira método quando entra num ciclo cumulativo de testes.
-->

---
class: enapol-exec
---

<div class="enapol-canvas method-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Bootstrapping e regressão</p>
    <h1>Cada linha validada aumenta a obrigação das regras anteriores.</h1>
  </header>

  <section class="method-layout">
    <aside class="shared-state">
      <span>estado persistente</span>
      <strong>GRAMÁTICA + LÉXICO</strong>
      <p>morfemas, alomorfes, valores gramaticais, relações sintáticas e etiquetas semânticas acumulam no mesmo sistema.</p>
    </aside>
    <main class="method-flowchart" aria-label="Fluxo de bootstrapping gramatical">
      <div class="method-row method-row-top">
        <article class="method-step"><span>1</span><h2>linha n</h2><p>fonte, leitura, alvo e glosa</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>2</span><h2>morfemas</h2><p>reusar ou definir objetos</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>3</span><h2>estrutura</h2><p>sintaxe e relações abstratas</p></article>
      </div>
      <div class="method-row method-row-mid" v-click>
        <article class="method-step"><span>4</span><h2>spell-out</h2><p><span class="inline-code">eval</span> gera forma de superfície</p></article>
        <div class="method-arrow">→</div>
        <article class="method-step"><span>5</span><h2>conferência</h2><p>forma, estrutura e rótulos</p></article>
      </div>
      <div class="method-row method-row-validate" v-click>
        <article class="method-step method-step-valid"><span>6</span><h2>ground truth</h2><p>linha aprovada vira teste futuro</p></article>
      </div>
      <div class="method-row method-row-bottom" v-click>
        <article class="method-step"><span>7</span><h2>regressão</h2><p>regenerar tudo de <span class="inline-code">1...n</span></p></article>
        <div class="method-arrow">→</div>
        <article class="method-step decision-step"><span>8</span><h2>diff</h2><p>mostrar onde e o que mudou</p></article>
      </div>
      <div class="method-branches" v-click>
        <div class="branch branch-bad">regressão → corrigir regra / léxico / análise</div>
        <div class="branch branch-good">sem regressão → próxima linha</div>
      </div>
    </main>
  </section>

  <p class="method-callout" v-click>Uma correção local pode ser testada contra todo o corpus já validado.</p>
</div>

<!--
Tempo: 1:45.
Esta é a slide metodológica central e pode ser apresentada por cliques.
Primeiro escolho a linha n: fonte, leitura, alvo normalizado, segmentação e glosas.
Depois reuso ou defino os morfemas presentes na sentença. A gramática e o léxico crescem automaticamente como conjunto de tudo que já foi definido.
Em seguida escrevo a sentença com esses objetos e com a sintaxe mais abstrata possível.
[CLICK] Rodo o eval, ou spell-out, para gerar a forma de superfície, e confiro se a saída e a estrutura são de fato a análise que eu quero aprovar naquele momento.
[CLICK] Quando a linha é aprovada, ela entra no arquivo de referência e vira obrigação futura.
[CLICK] A cada nova linha, o sistema regenera todas as linhas anteriores e produz um diff.
[CLICK] Se há regressão, volto e corrijo regra, léxico ou análise; se não há, sigo para a próxima linha.
[CLICK] O valor de longo prazo é que uma correção local pode melhorar toda a gramática, e a regressão mostra exatamente o que mudou.
Transição: isso explica por que o corpus completo é mais do que uma coleção de exemplos.
-->

---
class: enapol-exec
---

<div class="enapol-canvas outputs-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que isso torna possível</p>
    <h1>Um corpus integral seria uma infraestrutura de pesquisa.</h1>
  </header>

  <section class="outputs-grid">
    <article class="doctorate-card">
      <span>trajetória</span>
      <p>O primeiro passo começou no mestrado. Com gramática suficiente implementada, o projeto foi aprovado para Doutorado Direto para avançar no corpus conhecido de Tupi Antigo.</p>
    </article>
    <article>
      <span>consulta</span>
      <p>morfemas, alomorfes, ambientes sintáticos, estruturas argumentais, rótulos semânticos e variação ortográfica ficam consultáveis.</p>
    </article>
    <article>
      <span>revisão</span>
      <p>se uma regra estiver errada ou mal rotulada, ela é corrigida em um ponto e testada contra tudo que já foi implementado.</p>
    </article>
    <article class="switch-card">
      <span>exemplo já produzido</span>
      <p>O trabalho sobre switch reference apresentado na Amazônicas X já usou corpus parcialmente anotado para localizar e quantificar padrões gramaticais.</p>
    </article>
  </section>

  <p class="science-line">Tupi Antigo é finito o bastante para implementação séria e amplo o bastante para análise linguística substantiva.</p>
</div>

<!--
Tempo: 0:55.
Aqui eu volto para a escala do doutorado.
O primeiro passo começou no mestrado: construir uma gramática computacional capaz de produzir formas reais.
Como já havia gramática suficiente implementada, o projeto foi aprovado para Doutorado Direto, agora com a tarefa de avançar sobre o corpus conhecido de Tupi Antigo e consolidar o método.
O ganho não é apenas velocidade. O ganho é que morfemas, alomorfes, ambientes sintáticos, estruturas argumentais, rótulos semânticos e variação ortográfica passam a ficar consultáveis.
Também cito rapidamente o trabalho de switch reference que apresentei na Amazônicas X: mesmo com corpus parcial, a anotação já permitiu localizar e quantificar padrões de outro modo muito mais lentos.
Transição: fecho com pontos de entrada públicos para esse ecossistema.
-->

---
class: enapol-exec
---

<div class="enapol-canvas resource-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Links</p>
    <h1>Saídas públicas da mesma infraestrutura formal</h1>
  </header>

  <section class="resource-grid">
    <article>
      <EnapolImage image="qr-presentation" alt="QR code para esta apresentação" />
      <h2>Apresentação</h2>
      <p>kiansheik.github.io/public-presentations</p>
      <span>slides e PDF exportável</span>
    </article>
    <article>
      <EnapolImage image="qr-corpus" alt="QR code para o repositório oldtupicorpus" />
      <h2>Corpus / gramática</h2>
      <p>github.com/kiansheik/oldtupicorpus</p>
      <span>implementação composicional e testes</span>
    </article>
    <article>
      <EnapolImage image="qr-dictionary" alt="QR code para o dicionário digital de Tupi Antigo" />
      <h2>Dicionário</h2>
      <p>kiansheik.io/nhe-enga</p>
      <span>consulta lexical e formas geradas</span>
    </article>
    <article>
      <EnapolImage image="qr-neo" alt="QR code para o gerador de neologismos" />
      <h2>Neologismos</h2>
      <p>neo.academiatupi.com</p>
      <span>formas novas seguindo a gramática</span>
    </article>
  </section>

  <footer class="resource-closing">
    <p>As aplicações são saídas. O objeto científico é a gramática executável.</p>
    <strong>A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</strong>
  </footer>
</div>

<!--
Tempo: 0:45.
Esta tela final fica aberta para perguntas.
Os QR codes mostram saídas públicas da mesma infraestrutura formal: a apresentação, o corpus e a gramática, o dicionário e o gerador de neologismos.
Eu devo enfatizar que esses produtos são saídas, não o centro científico da fala.
O centro é a gramática executável como descrição testável.
Última frase: a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.
-->
