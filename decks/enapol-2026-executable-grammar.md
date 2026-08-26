---
theme: seriph
title: "Corpus Computacional e Gramática Executável do Tupi Antigo"
info: |
  Apresentação ENAPOL 2026 sobre uma pergunta concreta: como transformar uma linha histórica do corpus em teste de uma gramática executável.
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
Mas, em vez de tentar apresentar o projeto inteiro, vou fazer um recorte.
A pergunta da fala é: como uma linha histórica do corpus pode deixar de ser apenas um exemplo citado e passar a funcionar como teste de uma análise gramatical?
Transição: começo com o objetivo geral, só para situar esse recorte.
-->

---
class: enapol-exec
---

<div class="enapol-canvas objective-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Objetivo geral</p>
    <h1>Construir uma gramática que gera, testa e anota o corpus que descreve.</h1>
  </header>

  <section class="objective-grid">
    <article>
      <span>corpus</span>
      <p>fontes históricas em Tupi Antigo, com transcrição, normalização e análise linguística controladas.</p>
    </article>
    <article>
      <span>gramática</span>
      <p>morfemas, alomorfes, flexão, relações sintáticas e valores semânticos escritos como objetos formais.</p>
    </article>
    <article>
      <span>teste</span>
      <p>cada análise precisa gerar uma forma comparável ao alvo definido pelo trabalho filológico e linguístico.</p>
    </article>
  </section>

  <p class="focus-line">Nesta apresentação, o zoom é uma pergunta: como transformar uma linha histórica em uma hipótese gramatical testável?</p>
</div>

<!--
Tempo: 0:50.
O objetivo geral do projeto é construir uma gramática computacional do Tupi Antigo capaz de gerar, testar e anotar o corpus que ela descreve.
Isso envolve o corpus histórico, a gramática propriamente dita e um sistema de testes.
Mas esta apresentação não é um passeio pelo doutorado inteiro.
O recorte é bem menor: o que acontece quando uma única linha histórica precisa ser transformada em uma hipótese gramatical verificável?
Transição: antes do exemplo, vale explicar por que chamo isso de uma nova camada de descrição, e não de substituição da gramática escrita.
-->

---
class: enapol-exec
---

<div class="enapol-canvas comparison-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Motivação</p>
    <h1>A metalinguagem muda; a descrição continua sendo uma hipótese.</h1>
  </header>

  <section class="comparison-grid">
    <figure>
      <EnapolImage image="TODO_anchieta_grammar_page_same_topic" alt="TODO: página de Anchieta sobre o mesmo tópico gramatical" />
      <figcaption>primeira gramática<br><span>Anchieta, 1595</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="TODO_gerardi_tupinamba_page_same_topic" alt="TODO: página de Gerardi ou gramática moderna sobre o mesmo tópico" />
      <figcaption>gramática moderna<br><span>Gerardi / descrição atual</span></figcaption>
    </figure>
    <figure>
      <EnapolImage image="TODO_pydicate_executable_grammar_screenshot" alt="TODO: screenshot de uma representação pydicate" />
      <figcaption>gramática executável<br><span>mesma análise, outra camada</span></figcaption>
    </figure>
  </section>

  <p class="keyline">A proposta não é substituir a gramática escrita. É acrescentar uma camada formal executável.</p>
</div>

<!--
Tempo: 1:05.
Aqui a comparação precisa ser cuidadosa.
Não estou dizendo que Anchieta é ruim e que a gramática moderna é boa.
O projeto depende dessas fontes, inclusive das gramáticas históricas e das descrições modernas.
O ponto é outro: a metalinguagem mudou profundamente em quatro séculos, mas o suporte principal continua sendo uma descrição textual publicada como versão fixa.
A gramática executável acrescenta uma terceira camada: uma descrição que também pode ser rodada, gerar formas e ser confrontada com o corpus.
Transição: agora faço o zoom num detalhe, como a apresentação precisa fazer.
-->

---
class: enapol-exec
---

<div class="enapol-canvas zoom-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O zoom</p>
    <h1>Uma linha do corpus como teste gramatical</h1>
  </header>

  <section class="question-panel">
    <span>pergunta da fala</span>
    <p>Como transformar uma frase histórica em uma hipótese gramatical testável?</p>
  </section>

  <section class="zoom-steps">
    <div>fonte histórica</div>
    <span>→</span>
    <div>análise linguística</div>
    <span>→</span>
    <div>estrutura formal</div>
    <span>→</span>
    <div>saída verificável</div>
  </section>
</div>

<!--
Tempo: 0:55.
Este é o recorte central.
Não vou tentar provar todas as vantagens possíveis da gramática executável.
Vou me concentrar em uma operação: pegar uma frase histórica e transformá-la em uma hipótese gramatical testável.
Isso exige passar da fonte histórica para uma análise linguística, depois para uma estrutura formal, e finalmente para uma saída verificável.
Transição: agora mostro a linha concreta que vou usar como exemplo.
-->

---
class: enapol-exec
---

<div class="enapol-canvas corpus-line-slide">
  <header class="slide-header compact">
    <p class="eyebrow">A linha concreta</p>
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
    </article>
  </section>

  <section class="difficulty-strip">
    <div>posse nominal</div>
    <div>expressão temporal</div>
    <div>imperativo</div>
    <div>destinatário em <span class="inline-code">orébe</span></div>
    <div>forma de superfície</div>
  </section>
</div>

<!--
Tempo: 1:35.
O exemplo vem de Araújo, Catecismo de 1686, na oração do Padre Nosso.
A linha corresponde ao pedido "dá-nos hoje o nosso alimento de cada dia".
O alvo normalizado atual no corpus é: oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe.
A dificuldade linguística é que a frase não é apenas uma sequência de palavras.
Ela envolve uma expressão nominal possuída, uma expressão temporal, um verbo em imperativo, um destinatário marcado por orébe, além da distância entre ortografia histórica, normalização e forma gerada.
Transição: a pergunta é como escrever essa mesma análise numa metalinguagem executável.
-->

---
class: enapol-exec
---

<div class="enapol-canvas encoding-slide">
  <header class="slide-header compact">
    <p class="eyebrow">A análise codificada</p>
    <h1>A mesma análise, mas em uma metalinguagem executável</h1>
  </header>

  <section class="encoding-grid">
    <article class="code-card">
      <span>estrutura formal</span>
      <p class="code-line">(((emi * (u * oré)) @ (nduara * (ara * iabiõ))) * (meeng * +endé).imp()) + kori + orébe</p>
    </article>
    <article class="output-card">
      <span>saída gerada / alvo aprovado</span>
      <p class="tupi-line">oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe</p>
      <p>Registro local: <span class="inline-code">araujo_catecismo_1686:0007</span></p>
    </article>
  </section>

  <section class="analysis-grid">
    <div><span>morfemas</span><p><span class="inline-code">oré</span>, <span class="inline-code">u</span>, <span class="inline-code">me'eng</span>, <span class="inline-code">kori</span>, <span class="inline-code">orébe</span></p></div>
    <div><span>relações</span><p>posse, nominalização, adjunção temporal, imperativo e complemento dativo.</p></div>
    <div><span>teste</span><p>o spell-out precisa reconstruir a forma esperada e seus rótulos analíticos.</p></div>
  </section>
</div>

<!--
Tempo: 2:00.
Esta é a mesma análise, agora escrita em uma metalinguagem executável.
Eu não preciso explicar cada símbolo para a plateia.
O essencial é mostrar que a representação separa unidades e relações: morfemas, posse, nominalização, adjunção temporal, imperativo e destinatário.
Depois a gramática roda o spell-out e produz uma forma de superfície.
Se a saída coincide com o alvo aprovado, a linha passa a ser um teste da gramática.
Se não coincide, o erro não é só técnico: ele aponta para uma decisão linguística que precisa ser revista.
Transição: isso leva diretamente à dificuldade principal e à forma como estou trabalhando nela.
-->

---
class: enapol-exec
---

<div class="enapol-canvas difficulty-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Dificuldade</p>
    <h1>Uma frase histórica não é apenas uma sequência de palavras.</h1>
  </header>

  <section class="difficulty-grid">
    <article>
      <h2>O que precisa ser decidido</h2>
      <p>ortografia, segmentação, entradas lexicais, flexão, relações sintáticas, variação de fonte e alvo normalizado.</p>
    </article>
    <article>
      <h2>Como estou respondendo</h2>
      <div class="loop-diagram">
        <div>fonte histórica</div>
        <span>→</span>
        <div>estrutura formal</div>
        <span>→</span>
        <div>forma gerada</div>
        <span>→</span>
        <div>comparação</div>
        <span>→</span>
        <div>revisão</div>
        <span>→</span>
        <div>regressão</div>
      </div>
    </article>
  </section>

  <p class="response-line">Cada nova linha validada aumenta a responsabilidade das regras anteriores.</p>
</div>

<!--
Tempo: 2:00.
Esta slide responde diretamente à orientação de relatar a dificuldade e como venho trabalhando na solução.
A dificuldade é que uma sentença histórica exige decisões simultâneas: como normalizar a ortografia, como segmentar, que entradas lexicais existem, que flexão está presente, que relações sintáticas estão ativas e como tratar variação entre fontes.
A resposta do projeto é transformar essas decisões em estrutura formal, gerar uma saída, comparar com o alvo linguístico e filológico, revisar a gramática ou o léxico e rerodar as linhas anteriores como testes de regressão.
Assim, cada linha nova não é só mais uma anotação. Ela aumenta a responsabilidade das regras já escritas.
Transição: fecho com a contribuição do recorte.
-->

---
class: enapol-exec
---

<div class="enapol-canvas closing-slide">
  <header class="slide-header compact">
    <p class="eyebrow">Contribuição</p>
    <h1>O corpus obriga a gramática a prestar contas.</h1>
  </header>

  <section class="closing-grid">
    <article>
      <h2>Não é um problema de PLN.</h2>
      <p>É transformar a descrição linguística em um objeto mais explícito, verificável e reutilizável.</p>
    </article>
    <article>
      <h2>As ferramentas são saídas.</h2>
      <p>Essas ferramentas são saídas. O objeto científico é a gramática executável.</p>
    </article>
  </section>

  <p class="final-line">A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</p>
</div>

<!--
Tempo: 1:00.
Fecho voltando à pergunta inicial.
O objetivo não é transformar o Tupi Antigo em um problema de PLN, nem fazer uma demonstração de aplicativos.
Aplicações como dicionários, exercícios ou geração de formas são saídas possíveis.
O objeto científico é a gramática executável: uma descrição que pode ser confrontada linha por linha com o corpus.
Última frase para dizer devagar: a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.
-->
