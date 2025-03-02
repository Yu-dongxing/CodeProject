<template>
    <div class="error-page">
      <el-result
        icon="warning"
        title="500 服务器错误"
        sub-title="抱歉，服务器发生错误，请稍后再试"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push('/')">返回首页</el-button>
        </template>
      </el-result>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Err500'
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