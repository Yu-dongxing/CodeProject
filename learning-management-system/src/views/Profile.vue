<template>
  <div class="profile-page">
    <div class="profile-header">
      <div class="header-content">
        <div class="user-info">
          <el-avatar :size="80" :src="userInfo.avatar" class="user-avatar">
            {{ userInfo.username?.charAt(0).toUpperCase() }}
          </el-avatar>
          <div class="user-details">
            <h2>{{ userInfo.username }}</h2>
            <p>{{ userInfo.role === 'admin' ? '管理员' : '普通用户' }}</p>
          </div>
        </div>
        <div class="quick-stats">
          <div class="stat-item">
            <div class="stat-value">{{ userInfo.resourceCount }}</div>
            <div class="stat-label">上传资源</div>
          </div>
          <div class="stat-item">
            <div class="stat-value">{{ userInfo.downloadCount }}</div>
            <div class="stat-label">资源下载</div>
          </div>
          <div class="stat-item">
            <div class="stat-value">{{ userInfo.lastLoginDays }}</div>
            <div class="stat-label">连续登录</div>
          </div>
        </div>
      </div>
    </div>

    <el-row :gutter="24" class="profile-content">
      <el-col :span="16">
        <el-card class="profile-form-card">
          <template #header>
            <div class="card-header">
              <span>个人信息设置</span>
              <el-tag type="success" effect="plain" v-if="userInfo.verified">已认证</el-tag>
            </div>
          </template>
          
          <el-form 
            :model="form" 
            label-width="100px"
            :rules="rules"
            ref="formRef"
          >
            <el-form-item label="头像" class="avatar-upload">
              <el-upload
                class="avatar-uploader"
                action="/api/upload"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
              >
                <el-avatar v-if="form.avatar" :src="form.avatar" :size="100" />
                <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
              </el-upload>
            </el-form-item>
            
            <el-form-item label="用户名" prop="username">
              <el-input v-model="form.username" placeholder="请输入用户名">
                <template #prefix>
                  <el-icon><User /></el-icon>
                </template>
              </el-input>
            </el-form-item>
            
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="form.email" placeholder="请输入邮箱">
                <template #prefix>
                  <el-icon><Message /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-form-item label="手机号" prop="phone">
              <el-input v-model="form.phone" placeholder="请输入手机号">
                <template #prefix>
                  <el-icon><Phone /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <el-divider content-position="left">安全设置</el-divider>
            
            <el-form-item label="旧密码" prop="oldPassword">
              <el-input 
                v-model="form.oldPassword" 
                type="password" 
                show-password
                placeholder="请输入旧密码"
              >
                <template #prefix>
                  <el-icon><Lock /></el-icon>
                </template>
              </el-input>
            </el-form-item>
            
            <el-form-item label="新密码" prop="newPassword">
              <el-input 
                v-model="form.newPassword" 
                type="password" 
                show-password
                placeholder="请输入新密码"
              >
                <template #prefix>
                  <el-icon><Key /></el-icon>
                </template>
              </el-input>
            </el-form-item>
            
            <el-form-item label="确认密码" prop="confirmPassword">
              <el-input 
                v-model="form.confirmPassword" 
                type="password" 
                show-password
                placeholder="请再次输入新密码"
              >
                <template #prefix>
                  <el-icon><Key /></el-icon>
                </template>
              </el-input>
            </el-form-item>
            
            <el-form-item>
              <el-button type="primary" @click="handleSubmit" :loading="loading">
                保存修改
              </el-button>
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
      
      <el-col :span="8">
        <el-card class="activity-card">
          <template #header>
            <div class="card-header">
              <span>最近活动</span>
            </div>
          </template>
          <div class="activity-timeline">
            <el-timeline>
              <el-timeline-item
                v-for="(activity, index) in activities"
                :key="index"
                :type="activity.type"
                :color="activity.color"
                :timestamp="activity.time"
                :hollow="activity.hollow"
              >
                {{ activity.content }}
              </el-timeline-item>
            </el-timeline>
          </div>
        </el-card>

        <el-card class="security-card">
          <template #header>
            <div class="card-header">
              <span>账号安全</span>
            </div>
          </template>
          <div class="security-items">
            <div class="security-item" v-for="(item, index) in securityItems" :key="index">
              <div class="security-item-info">
                <el-icon :class="item.status"><component :is="item.icon" /></el-icon>
                <div class="security-item-text">
                  <div class="security-item-title">{{ item.title }}</div>
                  <div class="security-item-desc">{{ item.description }}</div>
                </div>
              </div>
              <el-button :type="item.buttonType" link>{{ item.buttonText }}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'ProfilePage'
}
</script>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { ElMessage } from 'element-plus'
import {
  User,
  Lock,
  Key,
  Message,
  Phone,
  Plus
} from '@element-plus/icons-vue'

const authStore = useAuthStore()
const formRef = ref(null)
const loading = ref(false)

// 模拟用户数据
const userInfo = ref({
  username: authStore.user?.username || '用户',
  role: authStore.user?.role || 'user',
  email: 'user@example.com',
  phone: '13800138000',
  avatar: '',
  verified: true,
  resourceCount: 15,
  downloadCount: 128,
  lastLoginDays: 7
})

const form = ref({
  username: userInfo.value.username,
  email: userInfo.value.email,
  phone: userInfo.value.phone,
  avatar: userInfo.value.avatar,
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

// 表单验证规则
const validatePass = (rule, value, callback) => {
  if (form.value.newPassword && value !== form.value.newPassword) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
  ],
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  oldPassword: [
    { required: true, message: '请输入旧密码', trigger: 'blur' }
  ],
  newPassword: [
    { required: true, message: '请输入新密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请再次输入密码', trigger: 'blur' },
    { validator: validatePass, trigger: 'blur' }
  ]
}

// 活动时间线数据
const activities = [
  {
    content: '修改了个人信息',
    time: '刚刚',
    type: 'primary',
    color: '#409EFF'
  },
  {
    content: '上传了新的学习资料',
    time: '2小时前',
    type: 'success',
    color: '#67C23A'
  },
  {
    content: '完成了实名认证',
    time: '昨天 12:30',
    type: 'warning',
    color: '#E6A23C'
  },
  {
    content: '首次登录系统',
    time: '2024-03-20 15:30',
    type: 'info',
    color: '#909399',
    hollow: true
  }
]

// 安全设置项
const securityItems = [
  {
    icon: 'Message',
    title: '邮箱绑定',
    description: '已绑定邮箱：user@example.com',
    buttonText: '修改',
    buttonType: 'primary',
    status: 'verified'
  },
  {
    icon: 'Phone',
    title: '手机绑定',
    description: '已绑定手机：138****8000',
    buttonText: '修改',
    buttonType: 'primary',
    status: 'verified'
  },
  {
    icon: 'Key',
    title: '密码强度',
    description: '密码强度较弱，建议修改',
    buttonText: '修改',
    buttonType: 'warning',
    status: 'warning'
  }
]

const handleSubmit = async () => {
  if (!formRef.value) return
  
  try {
    await formRef.value.validate()
    loading.value = true
    // 这里添加实际的更新逻辑
    setTimeout(() => {
      ElMessage.success('更新成功')
      loading.value = false
    }, 1000)
  } catch (error) {
    console.error('表单验证失败:', error)
  }
}

const resetForm = () => {
  if (formRef.value) {
    formRef.value.resetFields()
  }
}

const handleAvatarSuccess = (response) => {
  form.value.avatar = response.url
  ElMessage.success('头像上传成功')
}
</script>

<style scoped>
.profile-page {
  padding: 24px;
  background-color: #f6f8fb;
  min-height: 100%;
}

.profile-header {
  background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%);
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 24px;
  color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-avatar {
  border: 4px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.user-details h2 {
  margin: 0 0 8px 0;
  font-size: 24px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-details p {
  margin: 0;
  opacity: 0.8;
  font-size: 14px;
}

.quick-stats {
  display: flex;
  gap: 32px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 4px;
}

.stat-label {
  font-size: 14px;
  opacity: 0.8;
}

.profile-content {
  margin-top: 24px;
}

.profile-form-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  font-size: 16px;
  font-weight: 600;
}

.avatar-upload {
  display: flex;
  justify-content: center;
}

.avatar-uploader {
  border: 1px dashed var(--el-border-color);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  width: 100px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.avatar-uploader:hover {
  border-color: var(--el-color-primary);
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
}

.activity-card, .security-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
  margin-bottom: 24px;
}

.activity-timeline {
  padding: 20px;
}

.security-items {
  padding: 16px;
}

.security-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border-bottom: 1px solid #f0f0f0;
}

.security-item:last-child {
  border-bottom: none;
}

.security-item-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.security-item-info .el-icon {
  font-size: 24px;
  color: #8c939d;
}

.security-item-info .verified {
  color: #67C23A;
}

.security-item-info .warning {
  color: #E6A23C;
}

.security-item-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.security-item-title {
  font-weight: 500;
  color: #1a1a1a;
}

.security-item-desc {
  font-size: 13px;
  color: #8c939d;
}

:deep(.el-form-item) {
  margin-bottom: 24px;
}

:deep(.el-input) {
  width: 350px;
}

:deep(.el-timeline-item__node) {
  background-color: transparent;
}

:deep(.el-timeline-item__content) {
  color: #1a1a1a;
}

:deep(.el-timeline-item__timestamp) {
  color: #8c939d;
}
</style> 