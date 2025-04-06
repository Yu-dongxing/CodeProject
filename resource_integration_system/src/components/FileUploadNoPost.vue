<template>
    <div v-loading="isLoading" style="width: 50%;">
      <el-upload
        class="upload-demo"
        :auto-upload="false"
        :on-change="handleUpload"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        :file-list="filelist"
        multiple
        accept="*"
      >
        <el-button type="primary">点击选择文件</el-button>
      </el-upload>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FileUploadNoPost',
    props: {
      // 通过 prop 接收父组件传递的文件列表
      value: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {
        filelist: [],
      };
    },
    watch: {
      // 监听父组件传递的 value，更新本地的 filelist
      value: {
        immediate: true,
        handler(newVal) {
          this.filelist = newVal;
        },
      },
    },
    methods: {
      handleUpload(file) {
        // 将文件添加到 filelist 中
        this.filelist.push(file.raw); // 如果 file.raw 是文件对象，直接添加
        //通过 事件通知父组件文件列表已更新
        this.$emit('input', this.filelist);
      },
      // 处理文件移除
      handleRemove(file, fileList) {
        // 在 filelist 中移除文件
        const index  = this.filelist.findIndex(f => f.name === file.name);
        if (index !== -1) {
          this.filelist.splice(index, 1); // 从数组中移除文件
        }
        // 更新 filelist
        this.filelist = fileList;
        // 通过事件通知父组件文件列表已更新
        this.$emit('input', this.filelist);
        console.log('文件移除', file, fileList);
      },
      // 移除文件前的确认
      beforeRemove(file, fileList) {
        // 弹出确认框，返回 Promise
        return this.$confirm(`确定移除 ${file.name}？`);
      },
    },
  };
  </script>
  
  <style>
  </style>