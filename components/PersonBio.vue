<template>
  <section class="person-bio">
    <div>
      <p class="eyebrow">Quem está falando?</p>
      <h1>{{ name }}</h1>
      <h2>{{ dates }}</h2>
    </div>

    <div class="bio-body">
      <p class="role">{{ role }}</p>
      <p>{{ why }}</p>
    </div>
  </section>
</template>

<script setup>
defineProps({
  name: { type: String, required: true },
  dates: { type: String, default: "" },
  role: { type: String, required: true },
  why: { type: String, required: true }
})
</script>
