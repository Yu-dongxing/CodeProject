<template>
  <div class="app-container">
    <!-- 根据路由判断是否显示主布局 -->
    <template v-if="!isLoginPage">
      <el-container class="main-container">
        <el-aside :width="sideMenuWidth">
          <SideMenu @update:collapsed="handleCollapse" />
        </el-aside>
        <el-container>
          <el-header height="60px">
            <HeaderNav />
          </el-header>
          <el-main>
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>
    </template>
    <!-- 登录页面直接显示路由内容 -->
    <template v-else>
      <router-view></router-view>
    </template>
  </div>
</template>

<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import SideMenu from './components/SideMenu.vue'
import HeaderNav from './components/HeaderNav.vue'

const route = useRoute()
const isLoginPage = computed(() => route.name === 'Login')
const isCollapsed = ref(false)

const sideMenuWidth = computed(() => isCollapsed.value ? '64px' : '200px')

const handleMenuCollapse = (event) => {
  isCollapsed.value = event.detail.collapsed
}

// 添加和移除事件监听器
onMounted(() => {
  window.addEventListener('menu-collapse', handleMenuCollapse)
})

onUnmounted(() => {
  window.removeEventListener('menu-collapse', handleMenuCollapse)
})
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

.app-container {
  height: 100vh;
}

.main-container {
  height: 100vh;
}

.el-header {
  background-color: #fff;
  border-bottom: 1px solid #dcdfe6;
  padding: 0 20px;
  display: flex;
  align-items: center;
}

.el-aside {
  background-color: #304156;
  color: #fff;
  overflow: hidden;
  transition: width 0.3s;
}

.el-main {
  background-color: #f0f2f5;
  padding: 20px;
  overflow-y: auto;
}

/* 移除 el-main 的默认内边距 */
.el-main {
  --el-main-padding: 20px;
}

/* 确保内容区域占满剩余空间 */
.el-container {
  height: 100%;
}
</style> 