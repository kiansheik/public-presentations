# ENAPOL 2026 Rehearsal Script

Target total: about 9:35. Hard cap: 10:00.

Pacing rule: once the landing sentence for a slide is said, change slides. Do not add a second explanation of the same point.

## Slide 1 — título
Maximum time: 0:35

Meu projeto tem um objetivo amplo: construir uma descrição computacional do Tupi Antigo ancorada no corpus histórico.

Hoje eu não vou tentar mostrar o projeto inteiro. Quero mostrar um problema pequeno, mas representativo: como uma forma histórica deixa de ser apenas texto e entra numa análise formal que pode ser executada e testada.

O objeto científico aqui não é uma aplicação de PLN. É a gramática executável.

**[TROCAR SLIDE]**

## Slide 2 — o que eu faço
Maximum time: 0:50

Eu começo pela fonte, não pelo modelo.

Primeiro preciso estabelecer o que estou lendo: fonte, normalização, glosa e interpretação. Depois, morfemas, alomorfes e relações gramaticais viram objetos formais reutilizáveis.

Finalmente eu executo essa representação e confronto o resultado com a linha que ela pretende explicar.

Então o computador não substitui a análise linguística. Ele obriga a análise a ser explícita o suficiente para poder falhar.

**[TROCAR SLIDE]**

## Slide 3 — duas camadas complementares
Maximum time: 0:45

E isso não pretende substituir a gramática escrita.

É na descrição escrita que eu posso comparar fontes, argumentar por uma categoria, explicar uma exceção e dizer por que uma análise é melhor que outra.

A camada executável acrescenta outra obrigação: algumas dessas decisões precisam ter uma representação formal suficientemente precisa para produzir resultados verificáveis.

E isso faz com que a descrição se torne cumulativa.

**[TROCAR SLIDE]**

## Slide 4 — çupê / supe / supé
Maximum time: 1:05

Aqui dá para ver a mesma categoria atravessando três metalinguagens.

Em Anchieta, em 1595, temos **çupê** descrito como dativo. Em Ferraz Gerardi, em 2023, **supe** aparece numa análise linguística moderna do Tupinambá.

E à direita está a minha terceira camada: `supé` passa a existir também como um objeto gramatical executável, uma posposição dativa que pode entrar nas operações da gramática.

Não estou dizendo que a terceira descrição substitui as anteriores. É justamente o contrário: eu consigo formalizá-la porque existe uma tradição descritiva que me permite saber o que estou formalizando.

Agora eu posso perguntar o que acontece quando esse objeto encontra formas reais do corpus.

**[TROCAR SLIDE]**

## Slide 5 — o problema concreto
Maximum time: 0:35

E aí aparece o problema concreto.

A fonte histórica não chega até nós segmentada em morfemas. Ela registra uma forma de superfície.

Mas a análise pode recuperar relações que não coincidem com as fronteiras gráficas da fonte.

Então eu preciso conservar ao mesmo tempo duas coisas: o que efetivamente aparece no documento e a hipótese sobre a estrutura dessa forma.

**[TROCAR SLIDE]**

## Slide 6 — Araújo / orébe
Maximum time: 1:05

Por exemplo, no Padre Nosso do Catecismo de Araújo, de 1686, aparece aqui **orébe**.

Funcionalmente, é "a nós" ou "para nós". Essa é a forma que eu quero preservar como superfície: **orébe**.

Mas a análise que eu quero reutilizar na gramática é **oré + supé**: o pronome `oré` combinado com a posposição dativa que acabamos de ver.

Se eu tratasse essa frase apenas como uma sequência de palavras separadas por espaço, essa relação desapareceria.

A segmentação analítica, portanto, não precisa coincidir com a segmentação gráfica da fonte.

**[TROCAR SLIDE]**

## Slide 7 — análise executável
Maximum time: 0:55

E é assim que isso entra no corpus executável.

No léxico, `orébe` é explicitamente definido a partir de `oré * supé`, com a variante superficial correspondente. Depois eu posso usar `orébe` dentro da representação da frase inteira.

O resultado esperado não é apenas que o sistema devolva a string correta. A árvore à direita mostra que a estrutura que produziu essa forma continua disponível.

Então a hipótese tem duas responsabilidades: produzir a forma e conservar a análise que eu estou defendendo.

**[TROCAR SLIDE]**

## Slide 8 — bootstrapping e regressão
Maximum time: 1:35

Este é o ponto metodológico principal.

Eu parto de uma linha da fonte, proponho uma estrutura e deixo a gramática produzir aquilo que decorre dessa análise.

**[CLICK 1]** Comparo o resultado com o ground truth linguístico que eu validei. Se não bate, eu preciso revisar a regra, o léxico ou a própria análise.

**[CLICK 2]** Quando bate, essa linha deixa de ser só um exemplo. Ela vira um **teste de regressão**. Então, quando eu modificar a gramática para analisar uma nova linha, rodo novamente as anteriores. Uma regra que resolve o exemplo de hoje mas quebra dez exemplos de ontem não pode passar silenciosamente.

**[CLICK 3]** É nesse sentido que a descrição se torna cumulativa: cada análise aprovada vira um compromisso da gramática inteira.

**[CLICK 4]** O corpus obriga a gramática a prestar contas.

**[TROCAR SLIDE. NÃO EXPLICAR BOOTSTRAPPING DE NOVO.]**

## Slide 9 — o que isso torna possível
Maximum time: 0:50

A partir daí aparecem várias possibilidades.

Eu posso consultar morfemas e ambientes sintáticos, mudar uma generalização e descobrir exatamente quais linhas deixam de funcionar, ou investigar distribuições no corpus.

E a mesma infraestrutura pode sustentar produtos como dicionários e geração.

O QR aponta para o corpus digital, onde essa infraestrutura aparece como consulta pública.

Mas eu quero manter a ordem da argumentação clara: essas ferramentas são saídas.

O objeto científico é a gramática executável, uma hipótese sobre o corpus que o próprio corpus pode testar.

**[TROCAR SLIDE]**

## Slide 10 — saída pública
Maximum time: 0:40

E termino só com uma consequência concreta.

Esse código já está sendo reutilizado num dicionário colaborativo de neologismos em Tupi Antigo.

O projeto começou em **13 de março deste ano** e, em pouco mais de cinco meses, já passou de **mil verbetes**, com áudio, citações, exemplos e revisão comunitária.

É uma comunidade pequena, mas é um exemplo de uma gramática executável deixando de ser apenas infraestrutura de pesquisa e sustentando uma ferramenta aberta.

Quem quiser conhecer, o QR code e o endereço clicável estão aqui. Obrigado.
