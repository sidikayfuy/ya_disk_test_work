<script setup lang="ts">
import type {FormError} from '#ui/types'
import {useAuthStore} from "~/stores/authStore";

const auth = useAuthStore()
const validate = (state: any) => {
  const errors: FormError[] = []
  if (!state.email) errors.push({ path: 'email', message: 'Email обязателен' })
  if (!state.password) errors.push({ path: 'password', message: 'Пароль обязателен' })
  if (!state.password_confirmation) errors.push({ path: 'password_confirmation', message: 'Подтверждение обязательно' })
  if (state.password !== state.password_confirmation) errors.push({ path: 'password_confirmation', message: 'Пароли не совпадают' })
  return errors
}

const registering = ref(false)

const toast = useToast()
const register = async (state: any) => {
  if (validate(state).length > 0) {
    return
  }

  registering.value = true
  try {
    const response = await auth.register(state)

    if (response.error) {
      toast.add({'title': response.error})
    }
    else {
      toast.add({'title': 'Регистрация прошла успешно'})
      navigateTo('login')
    }
  }
  catch (err) {
    toast.add({'title': 'Ошибка'})
  }
  finally {
    registering.value = false
  }
}

const validateOnList = ['blur']
const fields = [
  { type: 'email', label: 'Email', name: 'email', placeholder: 'Введите e-mail', color: 'gray' },
  { type: 'password', label: 'Пароль', name: 'password', placeholder: 'Введите пароль', color: 'gray' },
  { type: 'password', label: 'Подтверждение пароля', name: 'password_confirmation', placeholder: 'Повторите пароль', color: 'gray' }
]
</script>

<template>
  <div class="flex justify-center">
    <UAuthForm
      title="Регистрация"
      class="mt-5"
      :validate-on=validateOnList
      :validate="validate"
      icon="i-heroicons-user-circle"
      :fields="fields"
      :loading="registering"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      @submit="register"
    >
      <template #description>
        Есть аккаунт? <NuxtLink to="login" class="text-primary font-medium">Авторизируйтесь</NuxtLink>.
      </template>
    </UAuthForm>
  </div>
</template>

<style scoped>

</style>
