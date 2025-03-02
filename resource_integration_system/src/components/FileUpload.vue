<template>
  <div v-loading="isLoading">
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
            <el-button type="primary">点击上传文件</el-button>
            <!-- <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
              Drop file here or <em>click to upload</em>
            </div>
            <template #tip>
              <div class="el-upload__tip">
                jpg/png files with a size less than 500kb
              </div>
            </template> -->
        </el-upload>
        <el-button @click="onSubmit()">提交文件</el-button>
  </div>
</template>

<script>
import { resourceApi } from '@/api/resource'
import { ElMessage } from 'element-plus'
export default {
    name:'FileUpload',
    props: {
        // 定义 resourceid 作为 prop
        resourceid: {
            type: String, // 或者其他类型，根据实际需求调整
            required: true, // 如果这个参数是必须的，可以设置 required: true
            default: '', // 如果有默认值，可以设置默认值
        },
    },
    data(){
        return{
            filelist: [], // 用于存储已上传文件的列表   
            isLoading:false,
            resourceUUID:""
        }
    },
    methods:{
        handleUpload(file) {
          // 将文件添加到 filelist 中
          this.filelist.push(file.raw); // 如果 file.raw 是文件对象，直接添加
        },
        // 处理文件移除
        handleRemove(file, fileList) {
          // 在 filelist 中移除文件
          const index = this.filelist.findIndex(f => f.name === file.name);
          if (index !== -1) {
            this.filelist.splice(index, 1); // 从数组中移除文件
          }
          // 更新 filelist
          this.filelist = fileList;
          console.log("文件移除", file, fileList);
        },
        // 移除文件前的确认
        beforeRemove(file, fileList) {
          // 弹出确认框，返回 Promise
          return this.$confirm(`确定移除 ${file.name}？`);
        },
      // 总提交
      async onSubmit() {
        if (this.filelist.length === 0) {
          ElMessage.error("请上传至少一个文件");
          return;
        }

        try {
          this.isLoading = true;
          // 先提交文件
          await this.submitResourceFiles();
          this.filelist = []; // 清空文件列表
          this.isLoading = false;
          ElMessage.success("文件添加成功！");
        } catch (error) {
          this.isLoading = false;
          ElMessage.error("文件添加失败，请稍后再试");
        }
      },
      // 提交文件数据
      async submitResourceFiles() {
        try {
          await resourceApi.submitResourceFiles(this.filelist,this.resourceid);
        } catch (error) {
          console.error('添加资源失败:', error);
        }
      },
    }

}
</script>

<style>

</style>