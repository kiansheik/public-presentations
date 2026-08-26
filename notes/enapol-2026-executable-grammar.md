# ENAPOL 2026 Rehearsal Script

Target total: about 10 minutes.

## Slide 1 — título
Approximate time: 0:35

O projeto tem um objetivo amplo: construir uma descrição computacional do Tupi Antigo ancorada no corpus histórico. Hoje eu não vou tentar mostrar o projeto inteiro. Vou mostrar um problema pequeno, mas representativo: como uma forma histórica deixa de ser apenas texto e entra numa análise formal que pode ser executada e testada. O objeto científico não é uma aplicação de PLN. É a gramática executável.

## Slide 2 — o que eu faço
Approximate time: 0:55

Na prática, começo pela fonte. Não começo por um modelo, um tokenizer ou uma aplicação. Primeiro preciso decidir o que estou lendo e qual análise linguística quero defender. Depois escrevo essa análise numa representação formal reutilizável. Por fim, a representação roda e precisa voltar à linha histórica que motivou a análise. É nesse último passo que a gramática deixa de ser apenas uma descrição que parece plausível e passa a poder falhar de maneira observável.

## Slide 3 — duas camadas complementares
Approximate time: 0:50

A gramática escrita continua sendo essencial. É nela que se argumenta, compara fontes e explica por que uma análise é preferível a outra. A camada executável acrescenta outra obrigação: certas decisões precisam ser suficientemente explícitas para participar de operações formais e produzir resultados verificáveis. Isso transforma a descrição num objeto cumulativo: uma regra nova não responde só pelo exemplo que estou olhando agora, mas também pelo que já foi analisado antes.

## Slide 4 — çupê / supe / supé
Approximate time: 1:10

Anchieta descreve çupê em prosa gramatical. Gerardi analisa supe com uma metalinguagem linguística moderna. Aqui, supé entra como objeto gramatical executável: uma peça que pode participar da geração, anotação e teste da frase. Não é uma competição entre três descrições. A terceira só existe porque as anteriores tornam a categoria e seus usos inteligíveis. O ganho específico é poder perguntar o que acontece quando esse objeto encontra argumentos concretos no corpus.

## Slide 5 — o problema concreto
Approximate time: 0:45

A fonte não chega até nós já segmentada em morfemas. Ela registra uma forma de superfície. A análise linguística pode dizer que essa forma envolve elementos menores, alomorfia ou relações que não correspondem a espaços gráficos. Então a representação precisa preservar as duas coisas: o que efetivamente aparece e a hipótese sobre como aquilo é estruturado.

## Slide 6 — Araújo / orébe
Approximate time: 1:15

No Padre Nosso de Araújo, a forma que aparece para o destinatário é orébe. Na tradução funcional, aqui é “a nós” ou “para nós”. Mas a análise que quero poder reutilizar é mais profunda: o pronome oré combinado com a posposição dativa supé, numa realização superficial específica. Esse é exatamente o tipo de informação que se perde se tratarmos a linha apenas como uma sequência de tokens gráficos. Eu preservo orébe como forma de superfície e, ao mesmo tempo, registro a relação oré mais supé como hipótese gramatical.

## Slide 7 — análise executável
Approximate time: 1:00

Aqui estão as duas camadas juntas. No léxico do corpus, orébe é explicitamente definido como oré combinado com supé, com a variante correspondente. Na linha de Araújo, eu posso então usar orébe como a forma superficial esperada sem apagar a estrutura de que ele deriva. A árvore mostra o outro lado da mesma análise: a saída não é só uma string. Relações e decomposições continuam disponíveis para inspeção e anotação.

## Slide 8 — bootstrapping e regressão
Approximate time: 1:40

Click cues:

- [CLICK] comparação com ground truth e revisão.
- [CLICK] regressão nas linhas anteriores e próxima linha.
- [CLICK] síntese: uma linha aprovada vira compromisso cumulativo.
- [CLICK] callout final: o corpus obriga a gramática a prestar contas.

Eu parto da fonte histórica, proponho uma estrutura formal e deixo a gramática produzir a forma e a anotação que decorrem dessa estrutura.

[CLICK] Comparo isso com o ground truth linguístico que foi validado. Se não bate, volto à regra, ao léxico ou à própria análise.

[CLICK] Quando uma linha é aprovada, ela vira teste. Qualquer mudança futura roda novamente sobre as linhas anteriores. Por isso o bootstrapping não é apenas uma forma de construir software aos poucos. Ele mantém o linguista responsável por suas decisões anteriores. Uma regra que resolve o exemplo de hoje, mas quebra dez linhas de ontem, não pode passar silenciosamente.

[CLICK] Em síntese, uma análise aprovada deixa de ser exemplo isolado e vira compromisso da gramática inteira.

[CLICK] O corpus obriga a gramática a prestar contas.

## Slide 9 — o que isso torna possível
Approximate time: 0:50

Depois disso, várias ferramentas ficam possíveis, mas eu quero inverter a ordem habitual da apresentação. Dicionário, geração, busca ou interfaces não são o argumento principal. São saídas de uma infraestrutura descritiva comum. O ganho científico é poder consultar a análise, revisar generalizações e formular perguntas sobre o corpus sem perder de vista quais decisões gramaticais produziram aqueles dados.

## Slide 10 — materiais e saída pública
Approximate time: 0:45

Fecho com os materiais e com uma saída pública que já está em uso, mesmo sem divulgação ampla. O dicionário de neologismos é aberto e financiado coletivamente, com áudio, citações, perfis, karma, votos e revisão comunitária. O repositório começou em 13 de março de 2026. Circulando sobretudo entre grupos de entusiastas de Tupi, indígenas e não indígenas, ele já tem 24 usuários, 1.096 entradas atuais, 189 exemplos, 619 entradas pendentes e nenhum relatório aberto. No último mês foram 25 entradas novas, 19 aprovadas, 6 exemplos novos, 40 votos e 2 contribuidores ativos. Isso é uma saída pública; o argumento científico continua sendo a gramática executável e testável que torna essas saídas mais responsáveis.

Encerrar com os QR codes na tela.
