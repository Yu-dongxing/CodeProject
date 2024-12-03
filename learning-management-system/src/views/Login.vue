<template>
  <div class="login-container">
    <el-card class="login-card">
      <template #header>
        <h2 class="login-title">学习管理系统</h2>
      </template>
      <el-form 
        :model="loginForm" 
        :rules="rules" 
        ref="loginFormRef"
        label-position="top"
      >
        <el-form-item prop="username" label="用户名">
          <el-input 
            v-model="loginForm.username"
            placeholder="请输入用户名"
          >
            <template #prefix>
              <el-icon><User /></el-icon>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码">
          <el-input 
            v-model="loginForm.password" 
            type="password"
            placeholder="请输入密码"
            show-password
          >
            <template #prefix>
              <el-icon><Lock /></el-icon>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button 
            type="primary" 
            @click="handleLogin" 
            :loading="loading"
            class="login-button"
          >
            登录
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'LoginPage'
}
</script>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'
import { User, Lock } from '@element-plus/icons-vue'

const authStore = useAuthStore()
const router = useRouter()
const loading = ref(false)

const loginForm = ref({
  username: '',
  password: ''
})

const rules = {
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

const handleLogin = async () => {
  loading.value = true
  try {
    const success = await authStore.login(loginForm.value)
    if (success) {
      router.push('/')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #2d3a4b;
}

.login-card {
  width: 400px;
  border-radius: 8px;
}

.login-title {
  text-align: center;
  color: #303133;
  margin: 0;
}

.login-button {
  width: 100%;
}

:deep(.el-form-item__label) {
  color: #606266;
}

:deep(.el-input__wrapper) {
  border-radius: 4px;
}

:deep(.el-input__prefix) {
  color: #909399;
}
</style> 