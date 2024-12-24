import { defineStore } from 'pinia'
import { ref } from 'vue'
import { usePermissionStore } from './permission'
import api from '../services/api'
import { ElMessage } from 'element-plus'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const permissionStore = usePermissionStore()

  const login = async (credentials) => {
    try {
      // 测试账号验证
      if (credentials.username === 'admin' && credentials.password === '123456') {
        // 模拟测试数据
        const mockData = {
          token: 'test_token_' + Date.now(),
          user: {
            id: 1,
            username: 'admin',
            role: 'admin',
            roles: ['admin'],
            permissions: [
              'view_dashboard',
              'manage_users',
              'manage_resources',
              'manage_students',
              'upload_resource',
              'create_folder'
            ]
          }
        }

        // 设置用户信息和 token
        token.value = mockData.token
        user.value = mockData.user
        localStorage.setItem('token', mockData.token)

        // 设置用户角色和权限
        permissionStore.setRoles(mockData.user.roles)
        permissionStore.setPermissions(mockData.user.permissions)

        ElMessage.success('登录成功')
        return true
      }

      // 如果不是测试账号,则调用实际的登录 API
      const response = await api.post('/auth/login', credentials)
      
      const { token: userToken, user: userData } = response.data
      
      // 设置用户信息和 token
      token.value = userToken
      user.value = userData
      localStorage.setItem('token', userToken)

      // 设置用户角色和权限
      permissionStore.setRoles(userData.roles)
      permissionStore.setPermissions(userData.permissions)

      ElMessage.success('登录成功')
      return true
    } catch (error) {
      console.error('登录失败:', error)
      ElMessage.error('用户名或密码错误')
      return false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
    localStorage.removeItem('token')
    
    // 清除权限信息
    permissionStore.resetPermissions()
    
    ElMessage.success('已退出登录')
  }

  const isAuthenticated = () => {
    return !!token.value
  }

  return {
    user,
    token,
    login,
    logout,
    isAuthenticated
  }
}) 