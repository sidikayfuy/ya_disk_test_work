<script setup lang="ts">

import {useAuthStore} from "~/stores/authStore";
const auth = useAuthStore()

const links = [{
  label: 'Главная',
  icon: 'i-heroicons-book-open',
  to: '/'
}]

const logout = () => {
  auth.logout()
}

</script>

<template>
  <UHeader :links="links">
    <template #logo>
      YADISK
    </template>

    <template v-if="auth.isAuthenticated" #right>
      <UBadge>Пользователь: {{auth.user ? auth.user['email'] : ''}}</UBadge>
      <UButton color="gray" variant="ghost" @click="logout">Выйти</UButton>
    </template>
    <template v-else #right>
      <UButton color="gray" to="login">Войти</UButton>
      <UButton color="gray" variant="ghost" to="register">Зарегистрироваться</UButton>
    </template>
  </UHeader>
</template>

