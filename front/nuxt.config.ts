// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@pinia/nuxt'],
  extends: ['@nuxt/ui-pro'],
  runtimeConfig: {
    public: {
       apiUrl: process.env.API_URL // Exposed to the frontend as well.
    }
  }
})
