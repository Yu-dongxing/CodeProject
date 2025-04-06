<template>
    <div class="error-page">
      <el-result
        icon="warning"
        title="201 内容已删除"
        sub-title="抱歉,您访问的内容已被删除"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push('/')">返回首页</el-button>
        </template>
      </el-result>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Err201'
  }
  </script> 