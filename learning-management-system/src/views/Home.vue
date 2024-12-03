<template>
  <div class="home-page">
    <div class="welcome-section">
      <div class="welcome-header">
        <h1>欢迎回来，{{ authStore.user?.username || '管理员' }}</h1>
        <p class="welcome-text">{{ currentDate }}</p>
      </div>
      <div class="quick-actions">
        <el-button type="primary" class="action-button" @click="$router.push('/resources')">
          <el-icon><FolderOpened /></el-icon>上传资源
        </el-button>
        <el-button type="success" class="action-button" @click="$router.push('/profile')">
          <el-icon><User /></el-icon>个人设置
        </el-button>
      </div>
    </div>
    
    <el-row :gutter="24" class="statistics-cards">
      <el-col :span="6" v-for="(stat, index) in statistics" :key="index">
        <el-card shadow="hover" class="stat-card">
          <div class="stat-content">
            <div class="stat-icon" :class="stat.type">
              <el-icon><component :is="stat.icon" /></el-icon>
            </div>
            <div class="stat-info">
              <div class="stat-value">
                {{ stat.value }}<span v-if="stat.unit" class="unit">{{ stat.unit }}</span>
              </div>
              <div class="stat-label">{{ stat.label }}</div>
            </div>
          </div>
          <div class="stat-footer">
            <span class="trend" :class="stat.trend > 0 ? 'trend-up' : 'trend-down'">
              {{ stat.trend > 0 ? '↑' : '↓' }} {{ Math.abs(stat.trend) }}%
            </span>
            <span class="period">较上月</span>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="24" class="data-section">
      <el-col :span="16">
        <el-card class="chart-card">
          <template #header>
            <div class="card-header">
              <span class="section-title">学习趋势</span>
              <el-radio-group v-model="timeRange" size="small">
                <el-radio-button label="week">本周</el-radio-button>
                <el-radio-button label="month">本月</el-radio-button>
                <el-radio-button label="year">全年</el-radio-button>
              </el-radio-group>
            </div>
          </template>
          <div class="chart-placeholder">
            图表区域（需要集成图表库）
          </div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card class="recent-card">
          <template #header>
            <div class="card-header">
              <span class="section-title">最近活动</span>
              <el-button text>查看全部</el-button>
            </div>
          </template>
          <div class="activity-list">
            <div v-for="(activity, index) in recentActivities" :key="index" class="activity-item">
              <div class="activity-icon" :class="activity.type">
                <el-icon><component :is="activity.icon" /></el-icon>
              </div>
              <div class="activity-content">
                <div class="activity-title">{{ activity.title }}</div>
                <div class="activity-time">{{ activity.time }}</div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<script setup>
import { ref } from 'vue'
import { Reading, User, Document, Timer, FolderOpened } from '@element-plus/icons-vue'
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()
const timeRange = ref('week')

const currentDate = ref(new Date().toLocaleDateString('zh-CN', {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  weekday: 'long'
}))

const statistics = [
  {
    type: 'courses',
    icon: Reading,
    value: 10,
    label: '课程总数',
    trend: 10,
    unit: ''
  },
  {
    type: 'students',
    icon: User,
    value: 50,
    label: '学员总数',
    trend: 15,
    unit: ''
  },
  {
    type: 'assignments',
    icon: Document,
    value: 85,
    label: '作业完成率',
    trend: 5,
    unit: '%'
  },
  {
    type: 'active',
    icon: Timer,
    value: 25,
    label: '活跃课程',
    trend: -3,
    unit: ''
  }
]

const recentActivities = [
  { 
    type: 'course',
    icon: Reading,
    title: '新课程"Vue.js进阶"已发布',
    time: '10分钟前'
  },
  {
    type: 'student',
    icon: User,
    title: '新学员张三已注册',
    time: '30分钟前'
  },
  {
    type: 'assignment',
    icon: Document,
    title: '课程作业已更新',
    time: '1小时前'
  }
]
</script>

<style scoped>
.home-page {
  padding: 24px;
  background-color: #f6f8fb;
  min-height: 100%;
}

.welcome-section {
  margin-bottom: 32px;
  padding: 24px;
  background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%);
  border-radius: 16px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.welcome-header h1 {
  font-size: 28px;
  margin: 0 0 8px 0;
  font-weight: 600;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.welcome-text {
  font-size: 16px;
  margin: 0;
  opacity: 0.9;
}

.quick-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  padding: 12px 24px;
  font-weight: 500;
  border: none;
  transition: all 0.3s;
}

.action-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.statistics-cards {
  margin-bottom: 24px;
}

.stat-card {
  height: 160px;
  padding: 24px;
  transition: all 0.3s ease;
  border: none;
  background: white;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.stat-content {
  display: flex;
  align-items: center;
  margin-bottom: 24px;
}

.stat-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
  transition: all 0.3s;
}

.stat-icon .el-icon {
  font-size: 28px;
  color: white;
}

.stat-icon.courses { background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%); }
.stat-icon.students { background: linear-gradient(135deg, #52c41a 0%, #73d13d 100%); }
.stat-icon.assignments { background: linear-gradient(135deg, #faad14 0%, #ffc53d 100%); }
.stat-icon.active { background: linear-gradient(135deg, #f5222d 0%, #ff4d4f 100%); }

.stat-info {
  flex: 1;
}

.stat-value {
  font-size: 32px;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1.2;
  display: flex;
  align-items: baseline;
}

.unit {
  font-size: 16px;
  margin-left: 4px;
  color: #666;
}

.stat-label {
  font-size: 15px;
  color: #666;
  margin-top: 6px;
}

.stat-footer {
  font-size: 13px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.trend {
  font-weight: 500;
}

.trend-up {
  color: #52c41a;
}

.trend-down {
  color: #f5222d;
}

.period {
  color: #8c8c8c;
}

.data-section {
  margin-top: 24px;
}

.chart-card, .recent-card {
  height: 450px;
  border: none;
  background: white;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
}

.section-title {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
}

.chart-placeholder {
  height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fafafa;
  border-radius: 8px;
  color: #8c8c8c;
  margin: 16px;
}

.activity-list {
  padding: 16px;
}

.activity-item {
  display: flex;
  align-items: center;
  padding: 16px;
  border-radius: 8px;
  transition: all 0.3s;
  border-bottom: 1px solid #f0f0f0;
}

.activity-item:last-child {
  border-bottom: none;
}

.activity-item:hover {
  background-color: #f6f8fb;
}

.activity-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 16px;
}

.activity-icon .el-icon {
  font-size: 20px;
  color: white;
}

.activity-icon.course { background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%); }
.activity-icon.student { background: linear-gradient(135deg, #52c41a 0%, #73d13d 100%); }
.activity-icon.assignment { background: linear-gradient(135deg, #faad14 0%, #ffc53d 100%); }

.activity-content {
  flex: 1;
}

.activity-title {
  font-size: 14px;
  color: #1a1a1a;
  margin-bottom: 4px;
  font-weight: 500;
}

.activity-time {
  font-size: 13px;
  color: #8c8c8c;
}

:deep(.el-card) {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

:deep(.el-card__header) {
  border-bottom: 1px solid #f0f0f0;
  padding: 0;
}

:deep(.el-card__body) {
  padding: 0;
}

:deep(.el-radio-button__inner) {
  border-radius: 6px;
}

:deep(.el-radio-group) {
  --el-radio-button-checked-bg-color: #1890ff;
  --el-radio-button-checked-text-color: white;
  --el-radio-button-checked-border-color: #1890ff;
}
</style> 