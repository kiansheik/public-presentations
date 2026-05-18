<script setup>
import { computed, ref } from 'vue'

const entries = [
  {
    word: 'pipoca',
    group: 'Português brasileiro',
    headword: 'pok / pira + pok + -a',
    kind: 'formação',
    definition: 'pok: estalar, arrebentar, estourar; a nota deriva pipoca de “pele estourada”, em referência ao milho.',
    context: 'Bom exemplo para mostrar composição: uma palavra cotidiana guarda uma pequena análise morfológica.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbetes pok, pira e notas sobre pipoca.',
  },
  {
    word: 'jacaré',
    group: 'Português brasileiro',
    headword: 'îakaré',
    kind: 'substantivo',
    definition: 'Jacaré; nome comum aos répteis crocodilianos da família dos aligatorídeos.',
    context: 'O dicionário também registra derivados e topônimos como Jacareí e Itacaré.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete îakaré.',
  },
  {
    word: 'tatu',
    group: 'Português brasileiro',
    headword: 'tatu',
    kind: 'substantivo',
    definition: 'Tatu; mamífero desdentado com o corpo coberto por couraça.',
    context: 'Aqui a forma portuguesa preserva de modo quase direto o verbete tupi.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete tatu.',
  },
  {
    word: 'capivara',
    group: 'Português brasileiro',
    headword: 'kapibara',
    kind: 'substantivo',
    definition: 'Capivara, carpincho; literalmente “comedor de capim”.',
    context: 'O verbete ainda explica topônimos como Capibaribe e Capivari.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete kapibara.',
  },
  {
    word: 'caju',
    group: 'Português brasileiro',
    headword: 'akaîu',
    kind: 'substantivo',
    definition: 'Cajueiro; também caju ou acaju, o fruto dessa árvore.',
    context: 'O inglês cashew entra por essa cadeia lexical, via português caju/acaju.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete akaîu.',
  },
  {
    word: 'mandioca',
    group: 'Português brasileiro',
    headword: "mani'oka / mandi'oka",
    kind: 'substantivo',
    definition: 'Mandioca, mandioca-mansa; planta Manihot esculenta, base alimentar ampla.',
    context: 'O dicionário distingue a raiz mandi’oka do arbusto mandi’yba.',
    source: "Navarro, Dicionário de Tupi Antigo, verbetes mani'oka e mandi'oka.",
  },
  {
    word: 'jaguar',
    group: 'Outras línguas',
    headword: 'îagûara',
    kind: 'substantivo',
    definition: 'Jaguar, onça, onça-pintada; felino americano Panthera onca.',
    context: 'O dicionário observa que jaguar circulou em muitas línguas do mundo.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete îagûara e nota sobre jaguar.',
  },
  {
    word: 'maraca',
    group: 'Outras línguas',
    headword: 'maraká',
    kind: 'substantivo',
    definition: 'Maracá; instrumento chocalhante usado em solenidades religiosas e guerreiras.',
    context: 'O Toré ajuda a recolocar a palavra no uso ritual, não só no inventário lexical.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete maraká.',
  },
  {
    word: 'açaí',
    group: 'Outras línguas',
    headword: 'îeîsara / îusara',
    kind: 'verbete relacionado',
    definition: 'Juçara; palmeira alta e delgada da Mata Atlântica, Euterpe edulis.',
    context: 'Açaí é melhor tratado como circulação posterior amazônica; o corpus costeiro aproxima pelo campo das palmeiras Euterpe.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbetes îeîsara e îusara.',
  },
  {
    word: 'cashew',
    group: 'Outras línguas',
    headword: 'akaîu',
    kind: 'cadeia lexical',
    definition: 'Caju/acaju; fruto do cajueiro. A forma inglesa cashew passa pelo português.',
    context: 'Este caso mostra como uma palavra tupi pode chegar a outras línguas mediada pelo português colonial.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete akaîu.',
  },
  {
    word: 'manatee',
    group: 'Outras línguas',
    headword: 'gûaragûá / manati',
    kind: 'cuidado etimológico',
    definition: 'gûaragûá: peixe-boi; manati: peixe-boi, provavelmente de taíno.',
    context: 'Ótimo contraexemplo: nem toda palavra americana internacional deve ser atribuída ao Tupi Antigo.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbetes gûaragûá e manati.',
  },
  {
    word: 'capybara',
    group: 'Outras línguas',
    headword: 'kapibara',
    kind: 'substantivo',
    definition: 'Capivara, carpincho; literalmente “comedor de capim”.',
    context: 'A forma internacional conserva a mesma base do português capivara.',
    source: 'Navarro, Dicionário de Tupi Antigo, verbete kapibara.',
  },
]

const selectedWord = ref('pipoca')
const selected = computed(() => entries.find((entry) => entry.word === selectedWord.value) || entries[0])
const groups = computed(() => {
  const map = new Map()
  entries.forEach((entry) => {
    if (!map.has(entry.group)) map.set(entry.group, [])
    map.get(entry.group).push(entry)
  })
  return Array.from(map.entries()).map(([label, words]) => ({ label, words }))
})
</script>

<template>
  <section class="vocab-lookup">
    <div class="vocab-selector">
      <div v-for="group in groups" :key="group.label" class="retomada-word-panel vocab-selector-panel">
        <p class="retomada-card-label">{{ group.label }}</p>
        <div class="retomada-word-cloud vocab-button-cloud">
          <button
            v-for="entry in group.words"
            :key="entry.word"
            type="button"
            :class="{ active: entry.word === selected.word }"
            @click.stop="selectedWord = entry.word"
          >
            {{ entry.word }}
          </button>
        </div>
      </div>
    </div>

    <article class="vocab-definition-panel">
      <p class="retomada-card-label">Entrada selecionada</p>
      <div class="vocab-entry-head">
        <span class="vocab-query">{{ selected.word }}</span>
        <span class="vocab-arrow">→</span>
        <span class="vocab-headword">{{ selected.headword }}</span>
      </div>
      <p class="vocab-kind">{{ selected.kind }}</p>
      <p class="vocab-definition">{{ selected.definition }}</p>
      <p class="vocab-context">{{ selected.context }}</p>
      <p class="vocab-entry-source">{{ selected.source }}</p>
    </article>

    <p class="retomada-keypoint">O Tupi não está só no arquivo: ele continua no vocabulário cotidiano, mas cada palavra precisa ser conferida no corpus.</p>
    <p class="retomada-source">Dados resumidos de Navarro, <em>Dicionário de Tupi Antigo</em>, via <em>kiansheik.io/nhe-enga</em>; consulta em 2026-05-17.</p>
  </section>
</template>
