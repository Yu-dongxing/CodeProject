<template>
    <div class="error-page">
      <el-result
        icon="warning"
        title="403 禁止访问"
        sub-title="抱歉,您没有权限访问此页面"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push('/')">返回首页</el-button>
        </template>
      </el-result>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Err403'
  }
  </script> 