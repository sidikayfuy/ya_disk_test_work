<script setup lang="ts">
import Header from "~/components/header.vue";

</script>

<template>
  <div>
    <Header/>
    <UContainer>
    <slot/>
    </UContainer>
  </div>
</template>

<style scoped>

</style>
