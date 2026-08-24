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
Este projeto pergunta se uma gramática pode deixar de ser apenas um texto sobre a língua e passar a ser também uma hipótese executável sobre o corpus.
O ponto de partida é simples: quando descrevemos uma língua de corpus, cada análise que fazemos precisa se confrontar com as formas efetivamente atestadas.
Aqui eu não vou apresentar o projeto como uma aplicação de PLN, nem como um conjunto de ferramentas digitais.
Vou apresentar uma proposta de descrição linguística: usar uma gramática computacional como uma camada formal que pode ser lida, executada, testada e revisada.
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
Não é falta absoluta de fontes. Pelo contrário: o Tupi Antigo tem uma tradição documental importante.
O problema é que essa tradição está espalhada em objetos diferentes, com finalidades diferentes: gramáticas missionárias, catecismos, vocabulários, edições textuais, dicionários modernos e descrições contemporâneas.
Cada fonte carrega informação linguística, mas normalmente em formatos feitos para serem lidos por uma pessoa, não para serem testados em conjunto.
Então a pergunta do projeto é: como transformar esse material em um corpus em que a análise gramatical possa ser confrontada com as linhas que ela afirma descrever?
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
Esta é a slide central da apresentação, e ela ainda precisa receber um exemplo real.
A ideia é que todos os quatro blocos mostrem a mesma linha: primeiro a forma atestada na fonte; depois a análise linguística; depois a expressão formal; e por fim a forma ou anotação que o sistema gera.
O importante é que a fonte histórica não é tratada como uma verdade simples e infalível. Ela é o alvo da comparação.
Quando a forma gerada não bate com a forma atestada, isso não é apenas um erro técnico. Vira uma pergunta linguística.
A regra gramatical está formulada de modo insuficiente? A análise daquela linha está errada? Falta uma entrada lexical? Há variação ortográfica? A edição ou a tradição textual exige cuidado?
Esse é o ponto: cada divergência força a análise a explicitar melhor o que está assumindo.
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
Depois do exemplo, dá para generalizar o argumento.
Linguistas já trabalham com metalinguagens formais há muito tempo: árvores sintáticas, glosas interlineares, matrizes de traços, regras, paradigmas, representações fonológicas.
Uma linguagem de programação pode entrar nessa mesma família de instrumentos, desde que ela esteja a serviço da análise linguística.
Código aqui não substitui a análise. Ele obriga a análise a ser explícita.
Se uma regra está vaga demais para ser executada, isso nos mostra exatamente onde a descrição ainda depende de uma intuição não formalizada.
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
Esta comparação também precisa ser preenchida com um fenômeno específico.
O objetivo não é colocar Anchieta, uma gramática moderna e código como se fossem equivalentes, nem sugerir que quatro séculos de gramática ficaram parados.
O objetivo é mostrar continuidade e mudança no modo de descrever.
Anchieta oferece uma descrição gramatical em prosa missionária. Um trabalho moderno reformula fenômenos com categorias, teoria e terminologia contemporâneas.
A gramática executável acrescenta outra camada: a mesma hipótese precisa gerar ou anotar dados e continuar funcionando quando confrontada com o corpus.
Então a contribuição não é substituir a gramática em prosa, mas criar uma camada formal adicional para descrição e teste.
-->

---
class: enapol-exec
---

<div class="enapol-canvas loop-slide">
  <header class="slide-header">
    <p class="eyebrow">Bootstrapping gramatical</p>
    <h1>Cada linha validada vira um teste.</h1>
  </header>

  <section class="cycle-diagram" aria-label="Ciclo de bootstrapping gramatical">
    <div>corpus</div>
    <div>estrutura formal</div>
    <div>geração</div>
    <div>comparação</div>
    <div>revisão da gramática</div>
    <div>testes de regressão</div>
  </section>

  <p class="secondary-line">Quando uma regra muda, as análises anteriores são regeneradas e testadas novamente.</p>
</div>

<!--
Esse processo é cíclico.
Uma linha do corpus é formalizada; a gramática gera uma forma ou uma anotação; essa saída é comparada à forma atestada; a divergência leva a revisar regra, análise, léxico ou tratamento ortográfico.
Quando a revisão é feita, o sistema não testa só a linha nova. Ele regenera também as linhas anteriores.
Isso é diferente de anotar frase por frase manualmente, como tarefas independentes.
Aqui, a anotação deriva de uma gramática que precisa continuar dando conta do material já analisado.
Em termos linguísticos, cada linha validada vira uma pequena obrigação descritiva que a gramática não pode simplesmente esquecer.
-->

---
class: enapol-exec
---

<div class="enapol-canvas doctorate-slide">
  <header class="slide-header compact">
    <p class="eyebrow">O que existe e o que muda agora</p>
    <h1>As aplicações são saídas. O objeto científico é a gramática.</h1>
  </header>

  <section class="doctorate-grid">
    <article class="implemented-panel">
      <h2>Já implementado</h2>
      <p>flexão e conjugação, geração de dicionários, exercícios, variantes ortográficas e ferramentas ligadas à anotação.</p>
      <div class="screenshot-row">
        <EnapolImage image="project-dictionary" alt="Placeholder para dicionário ou conjugação" />
        <EnapolImage image="project-public-facing" alt="Placeholder para aplicação pública ou material de acesso comunitário" />
      </div>
    </article>
    <article class="doctorate-panel">
      <h2>Agora, no doutorado</h2>
      <p>aplicar e aperfeiçoar essa gramática contra o corpus conhecido do Tupi Antigo, linha por linha.</p>
      <ol>
        <li>corpus histórico</li>
        <li>formalização linha por linha</li>
        <li>gramática revisada</li>
        <li>análises anteriores ainda testáveis</li>
        <li>corpus cada vez mais estruturado</li>
      </ol>
      <div class="result-box">
        <span>Resultado atual</span>
        <p>[INSERIR UM RESULTADO EMPÍRICO CONCRETO]</p>
      </div>
    </article>
  </section>
</div>

<!--
Aqui é importante separar duas coisas.
O framework formal já apoiou saídas práticas: formas flexionadas, geração de dicionários, exercícios de conjugação, tratamento de variantes ortográficas e outras ferramentas relacionadas à anotação.
Essas saídas são úteis, mas elas não são o centro científico do doutorado.
O movimento agora é aplicar e aperfeiçoar a gramática contra o corpus conhecido do Tupi Antigo.
Isso significa formalizar linhas, testar a geração ou anotação, revisar a gramática e manter as análises anteriores verificáveis.
Nesta caixa de resultado eu quero inserir um dado empírico real: por exemplo, quantas linhas já foram codificadas, quantos testes existem, qual subsistema gramatical já está implementado, ou uma regra que precisou mudar depois da comparação com o corpus.
-->

---
class: enapol-exec
---

<div class="enapol-canvas significance-slide">
  <header class="slide-header">
    <p class="eyebrow">Por que importa</p>
    <h1>O corpus obriga a gramática a prestar contas.</h1>
  </header>

  <section class="accountability-grid">
    <article>
      <h2>Uma gramática publicada</h2>
      <p>registra uma análise e fixa uma versão argumentada da descrição.</p>
    </article>
    <article>
      <h2>Uma gramática executável e versionada</h2>
      <ul>
        <li>mostra que regra mudou;</li>
        <li>indica quais exemplos motivaram a mudança;</li>
        <li>revela o que continua funcionando;</li>
        <li>expõe quais análises quebram;</li>
        <li>testa se a mudança melhora a cobertura do corpus.</li>
      </ul>
    </article>
  </section>

  <p class="science-line">Isso acrescenta explicitude, reprodutibilidade e testabilidade à descrição linguística.</p>
</div>

<!--
Uma gramática publicada é fundamental porque registra uma análise e permite que outros pesquisadores leiam, critiquem e citem essa análise.
A gramática executável não diminui isso. Ela acrescenta outro tipo de prestação de contas.
Quando uma regra muda, fica possível perguntar: que exemplos motivaram a mudança? O que passou a funcionar? O que deixou de funcionar? A alteração realmente melhora a cobertura do corpus?
Versionamento e testes não são a contribuição científica em si; eles são a infraestrutura que torna essa prestação de contas mais visível.
O ganho científico está na explicitude, na reprodutibilidade e na possibilidade de acumular conhecimento descritivo sem perder de vista os dados que sustentam cada revisão.
Depois, a mesma infraestrutura pode apoiar pesquisa, ensino e acesso comunitário, mas isso vem como consequência.
-->

---
class: enapol-exec
---

<div class="enapol-canvas closing-slide">
  <header class="slide-header">
    <p class="eyebrow">Descrição linguística em 2026</p>
    <h1>Não é transformar o Tupi Antigo em um problema de PLN.</h1>
  </header>

  <p class="closing-statement">É tornar a descrição linguística mais explícita, verificável, revisável e reutilizável.</p>
  <p class="final-line">A gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.</p>
</div>

<!--
Para fechar, eu voltaria à formulação inicial.
Este não é principalmente um projeto de PLN, de tradução automática, nem de aplicativos.
É um projeto de descrição linguística que usa métodos computacionais para tornar a gramática mais explícita e mais vulnerável ao teste.
Em 2026, linguistas têm à disposição uma metalinguagem formal a mais: linguagens de programação.
Com ela, a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o próprio corpus pode testar.
-->
