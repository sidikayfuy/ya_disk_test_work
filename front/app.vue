<template>
  <div>
    <UNotifications />
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
  </div>
</template>
<script setup lang="ts">
onMounted(async () => {
  const auth = useAuthStore()
  auth.checkAuth()
  if (auth.isAuthenticated && !auth.user) {
    await auth.get_user()
  }
})
</script>
