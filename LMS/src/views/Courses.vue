<template>
  <div class="courses-container">
    <el-row :gutter="20" class="mb-4">
      <el-col :span="24">
        <el-button type="primary" @click="dialogVisible = true">
          添加课程
        </el-button>
      </el-col>
    </el-row>

    <el-table :data="courses" style="width: 100%">
      <el-table-column prop="name" label="课程名称" />
      <el-table-column prop="teacher" label="授课教师" />
      <el-table-column prop="duration" label="课程时长" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" @click="editCourse(scope.row)">编辑</el-button>
          <el-button
            size="small"
            type="danger"
            @click="deleteCourse(scope.row)"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="dialogVisible" title="添加课程">
      <el-form :model="courseForm" label-width="100px">
        <el-form-item label="课程名称">
          <el-input v-model="courseForm.name" />
        </el-form-item>
        <el-form-item label="授课教师">
          <el-input v-model="courseForm.teacher" />
        </el-form-item>
        <el-form-item label="课程时长">
          <el-input v-model="courseForm.duration" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveCourse">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const dialogVisible = ref(false)
const courses = ref([
  {
    name: 'Vue.js 基础教程',
    teacher: '张老师',
    duration: '30课时',
    status: '进行中'
  }
])

const courseForm = ref({
  name: '',
  teacher: '',
  duration: ''
})

const saveCourse = () => {
  courses.value.push({
    ...courseForm.value,
    status: '未开始'
  })
  dialogVisible.value = false
  courseForm.value = {
    name: '',
    teacher: '',
    duration: ''
  }
}

const editCourse = (course) => {
  // 实现编辑功能
}

const deleteCourse = (course) => {
  // 实现删除功能
}
</script> 