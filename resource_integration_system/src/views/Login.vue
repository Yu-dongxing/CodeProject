<template>
  <div class="login-container">
    <el-card class="login-card">
      <template #header>
        <h3 class="login-title">用户登录</h3>
      </template>
      <el-form 
        ref="loginForm"
        :model="loginForm"
        :rules="loginRules"
        label-position="top"
      >
        <el-form-item label="用户名" prop="username">
          <el-input 
            v-model="loginForm.username"
            placeholder="请输入用户名"
          />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input 
            v-model="loginForm.password"
            type="password"
            placeholder="请输入密码"
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-button 
            type="primary" 
            :loading="loading"
            @click="handleLogin"
          >
            登录
          </el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

export default {
  name: 'Login',
  setup() {
    const store = useStore()
    const router = useRouter()
    const loginForm = ref({
      username: '',
      password: ''
    })
    const loading = ref(false)
    const loginFormRef = ref(null)

    const loginRules = {
      username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
      ]
    }

    const handleLogin = async () => {
      try {
        loading.value = true
        await store.dispatch('user/login', loginForm.value)
        await store.dispatch('user/getUserInfo')
        ElMessage.success('登录成功')
        router.push('/')
      } catch (error) {
        ElMessage.error(error.message || '登录失败')
      } finally {
        loading.value = false
      }
    }

    const resetForm = () => {
      loginFormRef.value?.resetFields()
    }

    return {
      loginForm,
      loginRules,
      loading,
      loginFormRef,
      handleLogin,
      resetForm
    }
  }
}
</script>

<style lang="less" scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 120px);

  .login-card {
    width: 400px;
    
    .login-title {
      text-align: center;
      margin: 0;
    }
  }
}
</style> 