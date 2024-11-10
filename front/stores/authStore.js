import {defineStore} from 'pinia'
export const useAuthStore = defineStore('auth', () => {
    const user = ref(null)
    const isAuthenticated = ref(false)
    const authTokens = ref(null)

    async function register(credentials){
      try {
        const response = await fetch(useRuntimeConfig().public.apiUrl+'/api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(credentials),
        });
        const data = await response.json()
        if (response.ok) {
            return {data: data}
        }
        else {
            return {error: data}
        }
      } catch (error) {
        return {
            'error': 'Ошибка сети'
        }
      }
    }

    function checkAuth() {
      this.authTokens = JSON.parse(localStorage.getItem('authTokens'))
      if (this.authTokens) {
        this.isAuthenticated = true
      }
    }

    async function get_user (){
        try {
        const response = await fetch(useRuntimeConfig().public.apiUrl+'/api/user/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+JSON.parse(localStorage.getItem('authTokens')).access
          },
        });
        this.user =  await response.json()

      } catch (error) {

        return {
            'error': 'Ошибка сети'
        }
      }
    }

    async function login (credentials){
      try {
        const response = await fetch(useRuntimeConfig().public.apiUrl+'/api/token/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(credentials),
        });
        const data = await response.json()

        if (response.ok) {
            this.isAuthenticated = true
            this.authTokens = data
            localStorage.setItem('authTokens', JSON.stringify(data))
            await this.get_user()
            return {ok: true}
        }
        else {
            return {error: data}
        }

      } catch (error) {
        return {
            'error': 'Ошибка сети'
        }
      }
    }

    function logout() {
      this.user = null
      this.isAuthenticated = false
      localStorage.removeItem('authTokens')
    }

    return { user, isAuthenticated, authTokens, register, login, get_user, checkAuth, logout }
})
