<template>
  <div class="side-menu-container" :class="{ 'is-collapsed': isCollapse }">
    <div class="logo-container">
      <div class="logo">
        <el-icon :size="24" color="#409EFF"><Monitor /></el-icon>
      </div>
      <h1 class="title">学习管理系统</h1>
    </div>
    <el-menu
      class="side-menu"
      :default-active="activeMenu"
      background-color="transparent"
      text-color="#b7bdc3"
      active-text-color="#ffffff"
      :router="true"
      :collapse="isCollapse"
    >
      <el-menu-item index="/">
        <el-icon><HomeFilled /></el-icon>
        <template #title>
          <span>首页</span>
        </template>
      </el-menu-item>



      <el-menu-item index="/assignments">
        <el-icon><Document /></el-icon>
        <template #title>
          <span>作业管理</span>
        </template>
      </el-menu-item>

      <el-menu-item index="/resources">
        <el-icon><FolderOpened /></el-icon>
        <template #title>
          <span>电子资源库</span>
        </template>
      </el-menu-item>
      
      <el-menu-item index="/profile">
        <el-icon><User /></el-icon>
        <template #title>
          <span>个人中心</span>
        </template>
      </el-menu-item>
    </el-menu>

    <div class="menu-footer">
      <el-button 
        type="text" 
        class="collapse-button"
        @click="toggleCollapse"
      >
        <el-icon>
          <ArrowLeft v-if="!isCollapse" />
          <ArrowRight v-else />
        </el-icon>
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { 
  HomeFilled, 
  User, 
  Document,
  Monitor,
  ArrowLeft,
  ArrowRight,
  FolderOpened
} from '@element-plus/icons-vue'

const route = useRoute()
const isCollapse = ref(false)

const activeMenu = computed(() => route.path)

const toggleCollapse = () => {
  isCollapse.value = !isCollapse.value
  window.dispatchEvent(new CustomEvent('menu-collapse', { 
    detail: { collapsed: isCollapse.value }
  }))
}

watch(isCollapse, (newVal) => {
  document.body.style.setProperty('--side-menu-width', newVal ? '64px' : '200px')
})
</script>

<style scoped>
.side-menu-container {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #304156 0%, #1f2d3d 100%);
  width: var(--side-menu-width, 200px);
  transition: width 0.3s;
}

.logo-container {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 16px;
  color: #fff;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.logo {
  min-width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 8px;
  background: rgba(64, 158, 255, 0.1);
  border-radius: 6px;
}

.title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  white-space: nowrap;
  opacity: 1;
  transition: opacity 0.3s;
}

.is-collapsed .title {
  opacity: 0;
  width: 0;
  margin: 0;
}

.side-menu {
  flex: 1;
  border: none;
}

.menu-footer {
  padding: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: center;
}

.collapse-button {
  color: #b7bdc3;
  padding: 8px;
  border-radius: 4px;
}

.collapse-button:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

:deep(.el-menu) {
  border-right: none !important;
}

:deep(.el-menu-item) {
  height: 50px;
  line-height: 50px;
  margin: 4px 0;
}

:deep(.el-menu-item.is-active) {
  background: linear-gradient(90deg, rgba(64, 158, 255, 0.1) 0%, rgba(64, 158, 255, 0) 100%);
  border-left: 3px solid #409EFF;
}

:deep(.el-menu-item:hover) {
  background-color: rgba(255, 255, 255, 0.05) !important;
}

:deep(.el-menu-item .el-icon) {
  font-size: 18px;
  margin-right: 10px;
}

/* 折叠时的样式 */
:deep(.el-menu--collapse) {
  width: 64px;
}

/* 动画效果 */
.side-menu {
  transition: width 0.3s;
}

.logo-container {
  transition: all 0.3s;
}

:deep(.el-menu-item) {
  transition: all 0.3s;
}
</style> 