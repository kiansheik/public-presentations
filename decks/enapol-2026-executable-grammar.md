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

<div class="enapol-canvas enapol-title-slide">
  <section class="enapol-title-main">
    <p class="enapol-kicker">ENAPOL 2026</p>
    <h1>Corpus Computacional e Gramática Executável do Tupi Antigo</h1>
    <p class="enapol-subtitle">quando cada linha do corpus se torna um teste da análise</p>
  </section>

  <section class="enapol-presenter">
    <p>Kian Arad Sheik</p>
    <span>USP / PPG Linguística</span>
  </section>
</div>

<!--
Este projeto pergunta se uma gramática pode deixar de ser apenas um texto sobre a língua e passar a ser também uma hipótese executável sobre o corpus.
-->

---
class: enapol-exec
---

<div class="enapol-canvas source-problem-slide">
  <section class="enapol-copy">
    <p class="enapol-kicker">O problema</p>
    <h1>Tupi Antigo tem fontes.</h1>
    <p class="enapol-large">O problema é que os dados ficam distribuídos em gramáticas, dicionários, catecismos e edições textuais.</p>
  </section>

  <section class="source-collage" aria-label="Fontes históricas e modernas">
    <EnapolImage image="anchieta_arte_page_or_cover.svg" alt="Placeholder para capa ou página da gramática de Anchieta" />
    <EnapolImage image="araujo_catecismo_page_or_cover.svg" alt="Placeholder para capa ou página do catecismo de Araújo" />
    <EnapolImage image="bettendorff_compendio_page_or_cover.svg" alt="Placeholder para capa ou página do compêndio de Bettendorff" />
    <EnapolImage image="navarro_dictionary_cover.svg" alt="Placeholder para capa do dicionário de Navarro" />
  </section>
</div>

<!--
Não é falta absoluta de fontes. É que a informação linguística está espalhada, escrita em formatos humanos, difíceis de testar sistematicamente.
-->

---
class: enapol-exec
---

<div class="enapol-canvas metalanguage-slide">
  <p class="enapol-kicker">Quatro séculos de metalinguagem</p>
  <h1>Da primeira gramática à gramática executável</h1>

  <section class="three-panel-grid">
    <article>
      <EnapolImage image="anchieta_grammar_page_specific_topic.svg" alt="Placeholder para página de Anchieta sobre um tópico gramatical" />
      <h2>Anchieta, 1595</h2>
    </article>
    <article>
      <EnapolImage image="gerardi_tupinamba_same_topic_page.svg" alt="Placeholder para trabalho de Gerardi sobre tópico comparável" />
      <h2>Gerardi, gramática moderna</h2>
    </article>
    <article class="code-panel">
      <EnapolImage image="pydicate_expression_screenshot.svg" alt="Placeholder para expressão pydicate" />
      <h2>Gramática executável</h2>
    </article>
  </section>

  <p class="enapol-bottom-line">A metalinguagem mudou. A gramática continua sendo, quase sempre, um texto fixo.</p>
</div>

<!--
A proposta não é negar esse trabalho. Pelo contrário, este projeto depende dessas fontes. A questão é acrescentar uma camada nova: uma descrição que também roda.
-->

---
class: enapol-exec
---

<div class="enapol-canvas programming-slide">
  <p class="enapol-kicker">Código como metalinguagem</p>
  <h1>Linguistas já trabalham com formas explícitas.</h1>

  <section class="formal-layers">
    <div>
      <span>prosa</span>
      <p>Regra formulada em linguagem natural</p>
    </div>
    <div>
      <span>glosa</span>
      <p>Segmentação e valores gramaticais</p>
    </div>
    <div>
      <span>código</span>
      <p>Expressão formal da mesma análise</p>
    </div>
    <div>
      <span>saída</span>
      <p>Forma anotada que pode ser comparada ao corpus</p>
    </div>
  </section>

  <p class="enapol-thesis">Uma linguagem de programação também é uma metalinguagem formal.</p>
</div>

<!--
Código aqui não substitui análise linguística. Ele exige que a análise seja mais explícita.
-->

---
class: enapol-exec
---

<div class="enapol-canvas corpus-line-slide">
  <p class="enapol-kicker">Uma linha concreta</p>
  <h1>Cada linha do corpus vira estrutura linguística formal.</h1>

  <section class="line-pipeline">
    <article>
      <span>fonte histórica</span>
      <EnapolImage image="araujo_or_bettendorff_line_screenshot.svg" alt="Placeholder para linha de Araújo ou Bettendorff" />
    </article>
    <article>
      <span>expressão formal</span>
      <EnapolImage image="formal_expression_for_same_line.svg" alt="Placeholder para expressão formal da mesma linha" />
    </article>
    <article>
      <span>saída gerada</span>
      <EnapolImage image="generated_output_for_same_line.svg" alt="Placeholder para saída anotada gerada" />
    </article>
  </section>

  <p class="ground-truth">A fonte histórica funciona como ground truth.</p>
</div>

<!--
Se a forma gerada diverge da fonte, a pergunta é linguística: a regra está errada? a análise está errada? há variação ortográfica? a entrada lexical precisa mudar?
-->

---
class: enapol-exec
---

<div class="enapol-canvas loop-slide">
  <p class="enapol-kicker">Bootstrapping gramatical</p>
  <h1>Cada linha validada vira um teste.</h1>

  <section class="loop-diagram" aria-label="Ciclo de bootstrapping gramatical">
    <div>linha do corpus</div>
    <div>estrutura formal</div>
    <div>forma gerada</div>
    <div>comparação</div>
    <div>correção da gramática</div>
    <div>testes de regressão</div>
  </section>

  <p class="enapol-bottom-line">Cada alteração na gramática regenera as linhas anteriores.</p>
</div>

<!--
Isso é diferente de anotar frase por frase manualmente. A anotação deriva de uma gramática que precisa continuar funcionando.
-->

---
class: enapol-exec
---

<div class="enapol-canvas products-slide">
  <section class="enapol-copy">
    <p class="enapol-kicker">O que isso já produz</p>
    <h1>Aplicações são saídas. O objeto científico é a gramática.</h1>
    <p class="enapol-large">Dicionários com formas flexionadas. Exercícios de conjugação. Variantes ortográficas. Dados para tokenização e tradução.</p>
  </section>

  <section class="product-grid">
    <EnapolImage image="dictionary_conjugated_forms_screenshot.svg" alt="Placeholder para dicionário com formas conjugadas" />
    <EnapolImage image="quiz_conjugation_screenshot.svg" alt="Placeholder para quiz de conjugação" />
    <EnapolImage image="orthographic_variants_screenshot.svg" alt="Placeholder para variantes ortográficas" />
    <EnapolImage image="tupi_trail_or_neologism_dictionary_screenshot.svg" alt="Placeholder para TupiTrail ou dicionário de neologismos" />
  </section>
</div>

<!--
Esses aplicativos são saídas. O objeto científico é a gramática executável.
-->

---
class: enapol-exec
---

<div class="enapol-canvas accountability-slide">
  <p class="enapol-kicker">Por que importa</p>
  <h1>O corpus obriga a gramática a prestar contas.</h1>

  <section class="version-contrast">
    <div>
      <span>gramática publicada</span>
      <p>fixa uma versão da análise</p>
    </div>
    <div>
      <span>gramática versionada</span>
      <p>mostra o que mudou, por que mudou, quais exemplos passaram a funcionar e quais quebraram</p>
    </div>
  </section>
</div>

<!--
Isso não diminui o rigor da publicação. Ao contrário: torna a análise mais vulnerável ao teste.
-->

---
class: enapol-exec
---

<div class="enapol-canvas closing-slide">
  <p class="enapol-kicker">Descrição linguística em 2026</p>
  <h1>Não é transformar Tupi Antigo em um problema de PLN.</h1>
  <p class="closing-statement">É transformar a descrição linguística em um objeto mais explícito, verificável e reutilizável.</p>
  <p class="final-line">A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</p>
</div>

<!--
A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.
-->
