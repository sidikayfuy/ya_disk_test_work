<script setup lang="ts">
import type {FormError} from "#ui/types";
import {useAuthStore} from "~/stores/authStore";

const logging = ref(false)

const toast = useToast()
const auth = useAuthStore()

const validate = (state: any) => {
  const errors: FormError[] = []
  if (!state.email) errors.push({ path: 'email', message: 'Email обязателен' })
  if (!state.password) errors.push({ path: 'password', message: 'Пароль обязателен' })
  return errors
}

const login = async (state: any) => {
  if (validate(state).length > 0) {
    return
  }
  logging.value = true

  try {
    const response = await auth.login(state)

    if (response.error) {
      toast.add({'title': response.error})
    }
    else {
      toast.add({'title': 'Вы успешно вошли'})
      navigateTo('/')
    }
  }
  catch (err) {
    toast.add({'title': 'Ошибка'})
  }
  finally {
    logging.value = false
  }
}
</script>

<template>
  <div class="flex justify-center">
    <UAuthForm
      title="Вход"
      class="mt-5"
      :validate="validate"
      icon="i-heroicons-user-circle"
      :fields="[
          { type: 'email', label: 'Email', name: 'email', placeholder: 'Введите e-mail', color: 'gray' },
          { type: 'password', label: 'Пароль', name: 'password', placeholder: 'Введите пароль', color: 'gray' }]"
      :loading="logging"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      @submit="login"
    >
      <template #description>
        Нет аккаунта? <NuxtLink to="register" class="text-primary font-medium">Зарегистрируйтесь</NuxtLink>.
      </template>
    </UAuthForm>
  </div>
</template>

<style scoped>

</style>
