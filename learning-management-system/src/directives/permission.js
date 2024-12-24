import { usePermissionStore } from '../stores/permission'

export const permission = {
  mounted(el, binding) {
    const permissionStore = usePermissionStore()
    const { value } = binding

    if (value && value.length > 0) {
      const hasPermission = permissionStore.hasPermission(value)
      if (!hasPermission) {
        el.parentNode && el.parentNode.removeChild(el)
      }
    }
  }
}

export const role = {
  mounted(el, binding) {
    const permissionStore = usePermissionStore()
    const { value } = binding

    if (value && value.length > 0) {
      const hasRole = permissionStore.hasRole(value)
      if (!hasRole) {
        el.parentNode && el.parentNode.removeChild(el)
      }
    }
  }
} 