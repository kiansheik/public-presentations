# ENAPOL 2026 Rehearsal Script

Target total: about 10 minutes.

## Slide 1

Approximate time: 0:35

Script:

Hoje eu apresento o projeto "Corpus Computacional e Gramática Executável do Tupi Antigo". O ponto central não é apresentar uma aplicação de PLN, nem uma demonstração de ferramentas. O objeto científico é uma gramática: uma descrição formal capaz de gerar, anotar e testar as próprias linhas do corpus que ela pretende explicar.

Transition:

Começo situando exatamente o que o projeto faz.

## Slide 2

Approximate time: 0:55

Script:

Antes de entrar no exemplo, quero deixar claro o que eu faço na prática. Eu parto de linhas do corpus histórico: fonte, leitura, alvo normalizado, segmentação, glosas e interpretação. Depois escrevo os elementos da análise como objetos formais: morfemas, alomorfes, relações sintáticas e valores semânticos. Por fim, rodo a estrutura. A gramática faz o spell-out e produz uma forma de superfície que pode ser comparada ao alvo analisado. O Tupi Antigo é o caso concreto; a contribuição maior é um método para línguas de corpus com documentação delimitada.

Transition:

Isso muda a forma como uma gramática presta contas.

## Slide 3

Approximate time: 1:00

Script:

Aqui eu situo o projeto dentro de uma continuidade de descrição gramatical. Não estou contrapondo Anchieta, gramática moderna e código como se uma etapa apagasse a outra. O projeto depende das gramáticas históricas e das descrições modernas. O que muda é a metalinguagem: além da prosa gramatical e da análise publicada, acrescento uma camada formal que pode ser rodada. Com isso, uma decisão gramatical deixa rastros: ela gera formas, produz estrutura, falha quando a análise não está suficientemente explícita e pode ser corrigida depois.

Transition:

A necessidade aparece melhor quando olhamos para o tipo de problema que uma linha histórica cria.

## Slide 4

Approximate time: 0:55

Script:

Esta é a dificuldade principal: o sistema não automatiza a análise. Ele exige o mesmo trabalho gramatical que aparece em Anchieta, em Gerardi e em outras descrições: analisar formas, formular categorias e justificar relações. A diferença é que a metalinguagem não é só uma língua europeia em prosa descritiva; é Python, com uma camada pequena em cima dele. Isso abre muitas possibilidades, porque Python já circula inclusive dentro da linguística computacional, mas cria um gargalo no começo. Nesta etapa, a mesma pessoa precisa saber linguística, analisar Tupi Antigo e programar. Depois que o primeiro caso estiver consolidado, esse caminho deve ficar mais fácil para outros pesquisadores, inclusive com agentes e ferramentas de edição. Por enquanto, o processo iterativo revela necessidades que eu não poderia ter previsto no começo do mestrado.

Transition:

Agora mostro a linha que vou usar como exemplo.

## Slide 5

Approximate time: 1:20

Script:

O exemplo vem de Araújo, Catecismo de 1686, na oração do Padre Nosso. A linha corresponde a "dá-nos hoje o nosso alimento de cada dia". O alvo normalizado atual é: oré rembi'u 'ara îabi'õndûara eîme'eng kori orébe. A frase é pequena, mas já obriga várias decisões: posse nominal, nominalização em rembi'u, expressão temporal, imperativo e destinatário. Na superfície aparece orébe, mas a análise que a gramática manipula por baixo é o dativo supé aplicado a oré.

Transition:

Agora mostro como essa análise aparece na metalinguagem executável.

## Slide 6

Approximate time: 1:20

Script:

Esta é a mesma análise, agora escrita em uma metalinguagem executável. Eu não preciso explicar cada operador na fala, mas preciso deixar claro o princípio. Cada morfema de base é definido ou reaproveitado como objeto; a sentença é composta com relações explícitas; depois a estrutura é avaliada. Por isso, orébe não aparece aqui como morfema de base. Ele é a forma de superfície gerada por supé aplicado a oré, com variação 1. O spell-out gera a forma de superfície padronizada. Se a forma, a estrutura e os rótulos batem com a análise aprovada, essa linha vira teste. Se não batem, a falha aponta para uma decisão linguística a revisar, não apenas para um erro técnico.

Transition:

Para tornar visível o que fica escondido numa linha de código, mostro a estrutura como árvore.

## Slide 7

Approximate time: 0:55

Script:

Esta árvore mostra por que o resultado não é apenas uma string correta. A estrutura explicita que rembi'u pertence a uma relação de posse, que a expressão temporal modifica o pedido, que eîme'eng está no imperativo e que o nó dativo tem base supé e argumento oré, gerando a superfície orébe. Isso faz a análise ficar consultável: posso perguntar por morfemas, alomorfes, relações e ambientes.

Transition:

O exemplo individual só vira método quando entra num ciclo cumulativo de testes.

## Slide 8

Approximate time: 1:45

Click cues:

- [CLICK] reveal spell-out and linguistic comparison.
- [CLICK] reveal validated reference line.
- [CLICK] reveal full regression run.
- [CLICK] reveal regression/no-regression branches.
- [CLICK] reveal long-term correction callout.

Script:

Esta é a slide metodológica central. Primeiro escolho a linha n: fonte, leitura, alvo normalizado, segmentação e glosas. Depois reuso ou defino os morfemas presentes na sentença. A gramática e o léxico crescem automaticamente como conjunto de tudo que já foi definido. Em seguida escrevo a sentença com esses objetos e com a sintaxe mais abstrata possível.

[CLICK] Rodo o eval, ou spell-out, para gerar a forma de superfície, e confiro se a saída e a estrutura são de fato a análise que eu quero aprovar naquele momento.

[CLICK] Quando a linha é aprovada, ela entra no arquivo de referência e vira obrigação futura.

[CLICK] A cada nova linha, o sistema regenera todas as linhas anteriores e produz um diff.

[CLICK] Se há regressão, volto e corrijo regra, léxico ou análise; se não há, sigo para a próxima linha.

[CLICK] O valor de longo prazo é que uma correção local pode melhorar toda a gramática, e a regressão mostra exatamente o que mudou.

Transition:

Isso explica por que o corpus completo é mais do que uma coleção de exemplos.

## Slide 9

Approximate time: 0:55

Script:

Aqui eu volto para a escala do doutorado. O primeiro passo começou no mestrado: construir uma gramática computacional capaz de produzir formas reais. Como já havia gramática suficiente implementada, o projeto foi aprovado para Doutorado Direto, agora com a tarefa de avançar sobre o corpus conhecido de Tupi Antigo e consolidar o método. O ganho não é apenas velocidade. O ganho é que morfemas, alomorfes, ambientes sintáticos, estruturas argumentais, rótulos semânticos e variação ortográfica passam a ficar consultáveis. Também cito rapidamente o trabalho de switch reference que apresentei na Amazônicas X: mesmo com corpus parcial, a anotação já permitiu localizar e quantificar padrões de outro modo muito mais lentos.

Transition:

Fecho com pontos de entrada públicos para esse ecossistema.

## Slide 10

Approximate time: 0:45

Script:

Esta tela final fica aberta para perguntas. Os QR codes mostram duas saídas públicas da mesma infraestrutura formal: o dicionário e o gerador de neologismos. Eu devo enfatizar que esses produtos são saídas, não o centro científico da fala. O centro é a gramática executável como descrição testável. Última frase: a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.

Transition:

Encerrar aqui e deixar a tela com os QR codes.
