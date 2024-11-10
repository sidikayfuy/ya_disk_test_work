<script setup lang="ts">
const auth = useAuthStore()
const link = ref(null)
const loading = ref(false)
const toast = useToast()
const files = ref([])
const selected = ref([])
const columns = [{
    key: 'name',
    label: 'Название'
  }, {
    key: 'type',
    label: 'Тип'
  }]
const download = async () => {
    const token = <string>localStorage.getItem('authTokens')

    try {
        const paths = selected.value.map((object: any) => ({
          path: object.path,
          public_key: object.public_key
        }));

        const response = await fetch(config.public.apiUrl+'/api/download/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + JSON.parse(token).access
          },
          body: JSON.stringify(paths)
        });
        const data = await response.json()

        data.links.forEach((href: string) => {
          window.open(href, '_blank');
        });

      }
      catch (err) {
      }
      finally {

    }
  }
const config = useRuntimeConfig()
const  checkUrl = async () => {
    files.value = []
    loading.value = true
    try {
      const token = <string>localStorage.getItem('authTokens')
      const response = await fetch(config.public.apiUrl+'/api/show?public_key='+link.value, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + JSON.parse(token).access
        },
      });
      localStorage.getItem('authToken')
      const data = await response.json()
      if (response.ok) {
        files.value = data.map((object: any) => ({
          name: object.name,
          type: object.type ? object.type === 'file' ? `Файл ${object.media_type ? ` (${object.media_type})` : ''}` : 'Папка' : '',
          media_type: object.media_type ? object.media_type : null,
          public_key: object.public_key,
          path: object.path
        }))
        console.log(files)
        if (files.value.length === 0) {
          toast.add({'title': "Папка пуста"})
        }
      }
      else {
        toast.add({'title': JSON.parse(data.error).message})
      }

    } catch (error) {
      toast.add({'title': "Ошибка"})
    }
    finally {
      loading.value = false
    }
  }


</script>

<template>
  <div class="mt-5">
    <h1 v-if="!auth.isAuthenticated"><NuxtLink class="text-primary hover:text-gray-100" to="login">Войдите</NuxtLink>, чтобы польоваться сервисом</h1>
    <div v-else>
      <h1>Введите пубиличную ссылку:</h1>
      <UInput class="mt-5" :disabled="loading" v-model="link" />
      <UButton class="mt-5" :loading="loading" @click="checkUrl">Проверить</UButton>
      <UTable class="mt-10" v-if="files.length > 0" v-model="selected" :rows="files" :columns="columns" />
      <UButton v-if="files.length > 0" :disabled="selected.length === 0" @click="download">Скачать</UButton>
    </div>
  </div>
</template>

<style scoped>

</style>
