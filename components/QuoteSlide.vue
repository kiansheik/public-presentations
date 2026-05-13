<template>
  <section class="quote-slide">
    <div class="quote-mark">“</div>
    <blockquote>{{ quote }}</blockquote>
    <div class="quote-source">{{ source }}</div>
    <p v-if="note" class="quote-note">{{ note }}</p>
  </section>
</template>

<script setup>
defineProps({
  quote: { type: String, required: true },
  source: { type: String, required: true },
  note: { type: String, default: "" }
})
</script>
