<template>
  <div class="header-nav">
    <div class="user-info">
      <el-dropdown>
        <span class="el-dropdown-link">
          {{ authStore.user?.username || '用户' }}
          <el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'
import { ArrowDown } from '@element-plus/icons-vue'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.header-nav {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 0 20px;
}

.el-dropdown-link {
  cursor: pointer;
  display: flex;
  align-items: center;
}
</style> 