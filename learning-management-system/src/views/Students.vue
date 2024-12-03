<template>
  <div class="students-page">
    <h2>学员管理</h2>
    <el-table :data="students" style="width: 100%">
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="studentId" label="学号" />
      <el-table-column prop="email" label="邮箱" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.row)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'StudentPage'
}
</script>

<script setup>
import { ref } from 'vue'

const students = ref([
  {
    name: '张三',
    studentId: '2021001',
    email: 'zhangsan@example.com',
    status: '在读'
  }
])

const handleEdit = (student) => {
  console.log('编辑学员:', student)
}

const handleDelete = (student) => {
  console.log('删除学员:', student)
}
</script> 