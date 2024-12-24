<template>
  <el-menu
    default-active="1"
    class="side-menu"
    background-color="#304156"
    text-color="#fff"
    active-text-color="#409EFF"
  >
    <el-menu-item index="1" @click="router.push('/')">
      <el-icon><HomeFilled /></el-icon>
      <span>首页</span>
    </el-menu-item>
    <el-menu-item index="2" @click="router.push('/courses')">
      <el-icon><Reading /></el-icon>
      <span>课程管理</span>
    </el-menu-item>
    <el-menu-item index="3" @click="router.push('/students')">
      <el-icon><User /></el-icon>
      <span>学员管理</span>
    </el-menu-item>
    <el-menu-item index="4" @click="router.push('/assignments')">
      <el-icon><Document /></el-icon>
      <span>作业管理</span>
    </el-menu-item>
  </el-menu>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { HomeFilled, Reading, User, Document } from '@element-plus/icons-vue'

const router = useRouter()
</script> 