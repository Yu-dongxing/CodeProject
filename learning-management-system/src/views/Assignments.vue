<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="assignments-page">
    <h2>作业管理</h2>
    <el-table :data="assignments" style="width: 100%">
      <el-table-column prop="title" label="作业标题" />
      <el-table-column prop="course" label="所属课程" />
      <el-table-column prop="deadline" label="截止日期" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" @click="handleView(scope.row)">查看</el-button>
          <el-button size="small" type="primary" @click="handleEdit(scope.row)">
            编辑
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'AssignmentPage'
}
</script>

<script setup>
import { ref } from 'vue'

const assignments = ref([
  {
    title: 'Vue.js 基础作业',
    course: 'Vue.js 基础教程',
    deadline: '2024-03-30',
    status: '进行中'
  }
])

const handleView = (assignment) => {
  console.log('查看作业:', assignment)
}

const handleEdit = (assignment) => {
  console.log('编辑作业:', assignment)
}
</script> 