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
  '../../public/assets/oficina-unb/*.png',
  '../../public/assets/oficina-unb/*.jpg',
  '../../public/assets/oficina-unb/*.jpeg',
], {
  eager: true,
  import: 'default',
})

const src = computed(() => images[`../../public/assets/oficina-unb/${props.image}`])
</script>

<template>
  <img :src="src" :alt="alt">
</template>
