<template>
  <section class="timeline-slide">
    <h1>{{ title }}</h1>
    <div class="timeline">
      <div v-for="event in events" :key="event[0]" class="timeline-item">
        <div class="year">{{ event[0] }}</div>
        <div class="event">{{ event[1] }}</div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  title: { type: String, required: true },
  events: { type: Array, required: true }
})
</script>
