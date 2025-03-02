<template>
    <div>
      <div class="addResource" v-loading="isLoading">
        <el-card>
          <el-form label-position="top" label-width="80px" :model="formData">
            <el-form-item label="资源名称:">
              <el-input v-model="resource_date.name" placeholder="请输入资源名称" />
            </el-form-item>

            <el-form-item label="资源说明:" >
            <!-- <el-input type="textarea" autosize  v-model="resource_date.desc" placeholder="请输入资源说明" /> -->
            <wangeditor v-model="resource_date.desc"></wangeditor>
          </el-form-item>
  
            <el-form-item label="资源文件源地址:"> 
              <el-input @change="extractDomain" v-model="resource_date.url" placeholder="请输入资源文件源地址" />
            </el-form-item>
  
            <el-form-item label="资源图标(资源地址输入完成后点击图标输入框自动获取网站图标):">
              <el-input v-model="resource_date.img" placeholder="请输入资源展示图标" />
            </el-form-item>
  
            <el-form-item label="标签:">
              <el-input-tag disabled v-model="resource_date.tab" placeholder="请输入标签" tag-type="success" />
            </el-form-item>
  <!-- :on-exceed="handleExceed" -->
            <el-form-item label="文件上传：">
              <el-upload
                class="upload-demo"
                :auto-upload="false"
                :on-change="handleUpload"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                
                :file-list="filelist"
                multiple
                :limit="3"
                accept="*"
              >
                <el-button type="primary">点击上传文件</el-button>
              </el-upload>
            </el-form-item>
  
            <el-form-item>
              <el-button type="primary" @click="onSubmit()">提交</el-button>
              <el-button @click="resetSubmit">重置</el-button>
            </el-form-item>
          </el-form>
          <el-alert class="board-rids-10" title="提交后资源将进入审核阶段，审核通过后资源将展示在首页" type="info" show-icon />
        </el-card>
      </div>
    </div>
  </template>
  
  <script>
  import { resourceApi } from '@/api/resource'
  import { ElMessage } from 'element-plus'
  import { v4 as uuidv4 } from 'uuid';
  import wangeditor from '@/components/wangeditor.vue'
  export default {
    name: 'AddFileResource',
    components:{wangeditor},
    data() {
      return {
        // formData: {
        //   resourceData: {
        //     name: "",
        //     url: "",
        //     tab: "文件", // 根据示例值设置默认值
        //     img: "",
            
        //   },
        //   files: [] // 用于存储多个文件
        // },
        isLoading:false,
        resource_date:{
            name: "",
            url: "",
            tab: "文件", // 根据示例值设置默认值
            img: "",
            desc:"",
            resourceFileId:""
          },
        filelist: [], // 用于存储已上传文件的列表
        resourceUUID: uuidv4() // 生成一个唯一的资源UUID
      }
    },
    methods: {
      handleUpload(file) {
          // 将文件添加到 filelist 中
          this.filelist.push(file.raw); // 如果 file.raw 是文件对象，直接添加
          // 更新 resource_date 中的文件信息（如果有需要）
          console.log(this.filelist);
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

        // 文件超出限制时的处理
        handleExceed(files, fileList) {
          // 提示用户文件数量限制
          this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
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
          // 再提交资源数据
          await this.submitResourceData();
          this.isLoading = false;
          ElMessage.success("资源添加成功，等待审核！");
          // this.$router.push("/");
        } catch (error) {
          this.isLoading = false;
          ElMessage.error("资源添加失败，请稍后再试");
          console.error("资源提交失败:", error);
        }
      },
      // async onSubmit() {
        // try {
        //   if (this.formData.files.length === 0) {
        //     ElMessage.error('请上传至少一个文件');
        //     return;
        //   }
        //   await resourceApi.submitResourceFile(this.formData);
        //   ElMessage.success('添加成功,等待审核！！！');
        //   this.$router.push('/');
        // } catch (error) {
        //   ElMessage.error('添加失败');
        //   console.error('添加资源失败:', error);
        // }
      // },
      // 提交资源数据
      async submitResourceData() {
        this.resource_date.resourceFileId = this.resourceUUID;
        try {
          await resourceApi.submitResourceData(this.resource_date);
          ElMessage.success('添加资源数据成功,等待审核！！！');
          // this.$router.push('/');
        } catch (error) {
          ElMessage.error('添加资源数据失败');
          console.error('添加资源失败:', error);
        }
      },
      // 提交文件数据
      async submitResourceFiles() {
        try {
          await resourceApi.submitResourceFiles(this.filelist,this.resourceUUID);
          ElMessage.success('添加资源文件成功,等待审核！！！');
          // this.$router.push('/');
        } catch (error) {
          ElMessage.error('添加资源文件失败');
          console.error('添加资源失败:', error);
        }
      },

      extractDomainurl(url) {
        const parsedUrl = new URL(url);
        this.formData.resourceData.img = `https://api.akams.cn/favicon/${parsedUrl.hostname}`;
        return `https://api.akams.cn/favicon/${parsedUrl.hostname}`;
      },
      extractDomain() {
        this.formData.resourceData.img = this.formData.resourceData.url ? this.extractDomainurl(this.formData.resourceData.url) : '';
      },
      resetSubmit() {
        this.formData = {
          resourceData: {
            name: '',
            url: '',
            tab: "文件",
            img: ""
          },
          files: []
        };
        this.filelist = [];
      }
    }
  }
  </script>
  
  <style>
  .board-rids-10 {
    border-radius: 10px;
  }
  </style>