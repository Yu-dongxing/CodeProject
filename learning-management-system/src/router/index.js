import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { usePermissionStore } from '../stores/permission'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { 
      requiresAuth: true,
      permissions: ['view_dashboard']
    }
  },
  {
    path: '/resources',
    name: 'Resources',
    component: () => import('../views/Resources.vue'),
    meta: { 
      requiresAuth: true,
      permissions: ['manage_resources']
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
    meta: { 
      requiresAuth: true
    }
  },
  // 添加 403 错误页面路由
  {
    path: '/403',
    name: 'Error403',
    component: () => import('../views/Error403.vue'),
    meta: { requiresAuth: false }
  },
  // 添加 404 错误页面路由
  {
    path: '/:pathMatch(.*)*',
    name: 'Error404',
    component: () => import('../views/Error404.vue'),
    meta: { requiresAuth: false }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  const permissionStore = usePermissionStore()
  
  // 检查是否需要认证
  if (to.meta.requiresAuth && !authStore.isAuthenticated()) {
    next({ name: 'Login' })
    return
  }

  // 已登录用户访问登录页,重定向到首页
  if (to.name === 'Login' && authStore.isAuthenticated()) {
    next({ name: 'Home' })
    return
  }

  // 检查权限
  if (to.meta.permissions) {
    const hasPermission = to.meta.permissions.some(permission => 
      permissionStore.hasPermission(permission)
    )
    if (!hasPermission) {
      next({ name: 'Error403' })
      return
    }
  }

  // 检查角色
  if (to.meta.roles) {
    const hasRole = to.meta.roles.some(role => 
      permissionStore.hasRole(role)
    )
    if (!hasRole) {
      next({ name: 'Error403' })
      return
    }
  }

  next()
})

export default router 