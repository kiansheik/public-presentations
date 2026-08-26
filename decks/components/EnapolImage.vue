<script setup>
import { computed } from 'vue'

const props = defineProps({
  image: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    default: '',
  },
})

const images = import.meta.glob([
  '../../public/assets/enapol-2026-executable-grammar/*.png',
  '../../public/assets/enapol-2026-executable-grammar/*.jpg',
  '../../public/assets/enapol-2026-executable-grammar/*.jpeg',
  '../../public/assets/enapol-2026-executable-grammar/*.svg',
], {
  eager: true,
  import: 'default',
})

const src = computed(() => {
  const base = '../../public/assets/enapol-2026-executable-grammar/'
  const requested = `${base}${props.image}`

  if (images[requested]) return images[requested]

  for (const extension of ['png', 'jpg', 'jpeg', 'svg']) {
    const candidate = `${requested}.${extension}`
    if (images[candidate]) return images[candidate]
  }

  return undefined
})
</script>

<template>
  <img :src="src" :alt="alt">
</template>
