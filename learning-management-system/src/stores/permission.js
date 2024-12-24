import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePermissionStore = defineStore('permission', () => {
  // 用户角色
  const roles = ref([])
  
  // 用户权限列表
  const permissions = ref([])

  // 设置用户角色和权限
  const setRoles = (userRoles) => {
    roles.value = userRoles
  }

  const setPermissions = (userPermissions) => {
    permissions.value = userPermissions
  }

  // 检查是否有某个权限
  const hasPermission = (permission) => {
    return permissions.value.includes(permission)
  }

  // 检查是否包含某个角色
  const hasRole = (role) => {
    return roles.value.includes(role)
  }

  // 重置权限状态
  const resetPermissions = () => {
    roles.value = []
    permissions.value = []
  }

  return {
    roles,
    permissions,
    setRoles,
    setPermissions,
    hasPermission,
    hasRole,
    resetPermissions
  }
}) 