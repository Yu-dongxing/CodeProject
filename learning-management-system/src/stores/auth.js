import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))

  const login = async (credentials) => {
    try {
      // 临时使用模拟数据
      const mockResponse = {
        data: {
          token: 'mock_token_' + Date.now(),
          user: {
            username: credentials.username,
            role: 'admin'
          }
        }
      }
      token.value = mockResponse.data.token
      user.value = mockResponse.data.user
      localStorage.setItem('token', token.value)
      return true
    } catch (error) {
      console.error('登录失败:', error)
      return false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
    localStorage.removeItem('token')
  }

  const isAuthenticated = () => {
    return !!token.value
  }

  // 初始化时检查 token
  if (token.value) {
    // 验证存储的 token
    const validateToken = async () => {
      try {
        // 实际项目中，这里应该调用后端 API 验证 token
        console.log('Token 验证成功')
      } catch (error) {
        console.error('Token 验证失败:', error)
        logout()
      }
    }
    validateToken()
  }

  return {
    user,
    token,
    login,
    logout,
    isAuthenticated
  }
}) 