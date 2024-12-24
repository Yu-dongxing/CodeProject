<template>
  <div class="app-container">
    <el-container>
      <el-aside width="200px">
        <SideMenu />
      </el-aside>
      <el-container>
        <el-header>
          <HeaderNav />
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import SideMenu from './components/SideMenu.vue'
import HeaderNav from './components/HeaderNav.vue'
</script>

<style scoped>
.app-container {
  height: 100vh;
}
.el-header {
  background-color: #fff;
  border-bottom: 1px solid #dcdfe6;
}
.el-aside {
  background-color: #304156;
  color: #fff;
}
</style> 