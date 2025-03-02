<template>
    <div class="error-page">
      <el-result
        icon="warning"
        title="404 页面不存在"
        sub-title="抱歉，您访问的页面不存在"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push('/')">返回首页</el-button>
        </template>
      </el-result>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Err404'
  }
  </script>
  
  <style scoped>
  .error-page {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f6f8fb;
    border-radius: 10px;
  }
  </style> 