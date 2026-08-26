# ENAPOL 2026 Rehearsal Script

Target total: about 10 minutes.

## Slide 1

Approximate time: 0:45

Click cues: none

Script:

Hoje eu vou apresentar o projeto "Corpus Computacional e Gramática Executável do Tupi Antigo". Eu quero enquadrar esse trabalho como uma proposta de descrição linguística, não como uma aplicação de PLN. A pergunta central é se uma gramática pode deixar de ser apenas um texto interpretativo e passar a ser também uma hipótese formal que se deixa executar e testar contra o corpus. A ideia que organiza a apresentação é esta: cada linha analisada passa a criar uma obrigação para a gramática.

Transition:

Para entender por que isso é útil, primeiro precisamos olhar para o tipo de documentação com que o Tupi Antigo nos obriga a trabalhar.

## Slide 2

Approximate time: 0:55

Click cues: none

Script:

O problema não é falta absoluta de fontes. O Tupi Antigo tem uma tradição documental importante: gramáticas missionárias, catecismos, vocabulários, textos do corpus, dicionários e descrições modernas. Mas essas fontes foram organizadas para leitura humana, cada uma com seus objetivos, sua terminologia e suas convenções editoriais. Então a dificuldade científica é tornar esse material comparável, testável e revisável em conjunto. O projeto tenta construir uma infraestrutura em que a análise gramatical possa se confrontar de forma sistemática com as linhas que ela pretende descrever.

Transition:

Para não ficar abstrato, eu passo agora para uma única linha do corpus.

## Slide 3

Approximate time: 1:25

Click cues: none

Script:

Aqui deve entrar um exemplo real. [INSERIR EXEMPLO AQUI] A estrutura da slide já mostra o movimento: primeiro, a forma atestada na fonte; depois, a minha análise linguística daquela linha; em seguida, a expressão formal escrita com os objetos e relações da gramática; por fim, a saída gerada. O ponto importante é que a fonte escaneada não é chamada de "verdade" de modo ingênuo. O que funciona como referência do teste é a análise linguística explícita daquela ocorrência: forma esperada, segmentação, glosses, interpretação e alvo ortográfico normalizado. Quando a saída não bate, a diferença vira uma pergunta linguística: o problema está na regra, na análise, no léxico, na ortografia, ou na própria tradição textual?

Transition:

Depois desse exemplo, dá para explicar por que escrever isso em código não é uma mudança de assunto, mas uma extensão de metalinguagens que linguistas já usam.

## Slide 4

Approximate time: 0:50

Click cues: none

Script:

Linguistas já trabalham com metalinguagens formais há muito tempo. Usamos glosas, árvores sintáticas, matrizes de traços, paradigmas, regras, representações fonológicas. Uma linguagem de programação pode entrar nessa família quando ela está a serviço da análise linguística. Código não substitui a análise; ele obriga a análise a ser explícita. Se uma regra está vaga demais para ser executada, isso mostra precisamente onde a descrição ainda depende de intuição não formalizada.

Transition:

Essa continuidade fica mais clara quando colocamos lado a lado uma gramática histórica, uma descrição moderna e uma formalização executável.

## Slide 5

Approximate time: 0:55

Click cues: none

Script:

Esta slide ainda precisa de um fenômeno específico. [INSERIR FENÔMENO E REFERÊNCIAS AQUI] O objetivo não é dizer que Anchieta, uma gramática moderna e uma expressão em pydicate fazem a mesma coisa. O objetivo é mostrar que a necessidade de metalinguagem permanece. Anchieta descreve em prosa gramatical missionária; uma descrição moderna reorganiza o fenômeno com categorias contemporâneas; a gramática executável acrescenta uma camada em que a hipótese precisa produzir ou anotar dados. Essa camada não substitui a gramática em prosa, mas cria uma forma adicional de teste.

Transition:

Agora eu mostro o método cumulativo que transforma esse tipo de formalização em um processo de pesquisa.

## Slide 6

Approximate time: 1:55

Click cues:

- [CLICK] reveal spell-out and linguistic comparison.
- [CLICK] reveal validated line.
- [CLICK] reveal full regression.
- [CLICK] reveal YES/NO branches.
- [CLICK] reveal long-term correction callout.

Script:

Esta é a slide metodológica central. O processo começa com a linha n do corpus. O linguista determina a leitura, segmentação, glosses, interpretação e alvo ortográfico normalizado. Depois, para cada morfema necessário, eu reuso um objeto já existente ou defino um novo. Esses objetos não vivem só naquela frase: eles entram num estado persistente de gramática e léxico. Em seguida, escrevo a estrutura abstrata da sentença com objetos, relações e sintaxe.

[CLICK] Depois eu rodo o spell-out, isto é, avalio essa estrutura. A gramática produz uma forma de superfície padronizada e a estrutura ou anotação associada. A comparação não é só igualdade de string. É uma conferência linguística: a forma está certa? os morfemas estão certos? a estrutura está certa? os rótulos fazem sentido?

[CLICK] Se a linha passa por essa conferência, ela é validada e vira um novo teste. Ela se torna uma nova obrigação descritiva para a gramática.

[CLICK] A partir daí, o sistema regenera tudo de 1 até n e mostra os diffs. Isso é o que dá accountability cumulativa ao processo.

[CLICK] Se aparece regressão, eu volto para corrigir regra, léxico ou análise. Se não aparece regressão, sigo para a próxima linha: n mais um.

[CLICK] O valor de longo prazo é que uma correção local pode ser testada imediatamente contra todo o corpus validado. O Tupi Antigo é o primeiro caso de implementação, mas a metodologia pode ser reutilizada para outras línguas de corpus com tradição suficientemente delimitada e analisável.

Transition:

Com esse método em mente, fica mais claro por que o projeto mudou de escala no Doutorado Direto.

## Slide 7

Approximate time: 1:10

Click cues:

- [CLICK] reveal the current expert bottleneck.
- [CLICK] reveal production to editing as future direction.

Script:

Aqui eu mostro progresso, dificuldade e direção futura no mesmo movimento. O projeto começou no mestrado com a construção da gramática computacional. Com a maturação dessa gramática, o projeto foi aprovado para Doutorado Direto. O ponto não é listar produtos, mas mostrar que a gramática ficou suficientemente real para produzir saídas: flexão, dicionários, exercícios, transformações ortográficas, neologismos, anotação e ferramentas experimentais. No doutorado, a escala passa a ser implementar o corpus conhecido do Tupi Antigo e deixar que esse processo aperfeiçoe simultaneamente a gramática e o método.

[CLICK] A dificuldade também muda. Hoje, a primeira implementação ainda exige na mesma pessoa conhecimento da fonte histórica, da gramática do Tupi, da segmentação e glosa, das decisões representacionais e de parte da camada técnica. O gargalo atual é a interface entre análise linguística e implementação.

[CLICK] A direção metodológica é deslocar o trabalho de produção para edição. O sistema não substitui o linguista. A ideia é que, conforme gramática e léxico ganham cobertura, ele proponha análises progressivamente mais completas. O linguista passa a revisar, corrigir, rejeitar, refinar e interpretar os casos difíceis. O objetivo não é retirar o linguista do processo, mas deslocar seu trabalho da produção para a edição.

Transition:

Antes mesmo do corpus completo, esse tipo de estruturação já produziu um resultado linguístico concreto.

## Slide 8

Approximate time: 1:05

Click cues: none

Script:

Um exemplo é o trabalho que apresentei na Amazônicas X sobre switch reference em Tupi Antigo. A pergunta era se o conjuntivo em -reme funcionava como marcador de sujeito diferente. Na versão local atual do artigo e do conjunto de dados, há 62 exemplos anotados: 60 DS e 2 SS, ou 96,77% DS e 3,23% SS. [CONFIRMAR REFERÊNCIA: o resumo público do ResearchGate registra uma versão anterior com 53 exemplos e 96,23% DS.] O ponto não é dizer que a anotação computacional prova uma teoria automaticamente. O ponto é que uma anotação parcial já tornou mais rápido localizar, comparar e quantificar exemplos relevantes. Isso mostra o tipo de ganho que se expande quando o corpus inteiro passa a ser estruturado.

Transition:

Então a pergunta seguinte é: o que muda quando o corpus conhecido inteiro se torna consultável nessa representação?

## Slide 9

Approximate time: 0:55

Click cues: none

Script:

Quando eu digo corpus completo, não quero dizer todas as frases já faladas em Tupi Antigo. Quero dizer o corpus histórico conhecido e selecionado para o projeto. O ganho não é apenas velocidade. O ganho é colocar morfologia, sintaxe, alomorfia, léxico, semântica, ortografia e análises concorrentes dentro da mesma representação explícita. Isso permite perguntar pelo corpus inteiro: onde aparece um morfema? em quais ambientes sintáticos? com quais alomorfes? em quais interpretações semânticas? E quando uma regra melhora, a análise pode ser regenerada em vez de corrigida manualmente exemplo por exemplo.

Transition:

Para fechar, mostro alguns pontos de entrada públicos para esse ecossistema.

## Slide 10

Approximate time: 0:55

Click cues: none

Script:

Estes QR codes não são o centro científico da apresentação, mas mostram saídas possíveis da mesma infraestrutura formal. O dicionário mostra consulta lexical e formas geradas. O repositório do corpus mostra a implementação composicional e o sistema de testes. O Dicionário de Tupi mostra uma aplicação pública que se apoia nesse trabalho formal. Então eu fecho com duas ideias. Primeiro: Tupi Antigo é o caso concreto, mas a proposta metodológica é maior que uma língua. Segundo: a gramática deixa de ser apenas uma interpretação do corpus e passa a ser uma hipótese que o corpus pode testar.

Transition:

Encerrar aqui e deixar a tela com os QR codes para perguntas.
