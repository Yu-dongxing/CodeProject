<template>
  <div class="StudyDetails">
    <!-- 任务主题 -->
    <el-card class=" ccard display-center" shadow="hover">
        <el-text class="title">{{ studyDetails.taskTitle }}</el-text>
    </el-card>
    <!-- 任务详细信息 -->
    <div class="docx">
      <el-card class="ccard min-width-1000">
        <template #header>
            <div class="header card-header">
                <el-icon><Grid /></el-icon>
                <el-text style="margin-left: 10px">任务详细内容</el-text>
            </div>
        </template>
        <div class="hhtml" v-html="studyDetails.description">
             
        </div>
      </el-card>
      <el-card class="docx-index ccard"></el-card>
    </div>
    <!-- 任务附件 -->
    <el-card class="ccard">
        <template #header>
            <div class="header card-header">
                <el-icon><Document /></el-icon>
                <el-text style="margin-left: 10px">任务附件</el-text>
            </div>
        </template>
        <el-table :data="task_fileList">
          <!-- fileName -->
          <el-table-column prop="fileName" label="文件名" />
          <el-table-column  label="附件下载" >
            <template #default="scope">
              <el-button @click="downloadFile(scope.row.fileUrl,scope.row.fileName)" type="primary" size="small">下载</el-button>
            </template>
          </el-table-column>
        </el-table>
    </el-card>
    <!-- 任务完成提交 -->
    <el-card class="ccard">
        <template #header>
            <div class="header card-header">
                <el-icon><Finished /></el-icon>
                <el-text style="margin-left: 10px;">提交任务</el-text>
            </div>
        </template>
        <el-form :model="answerStudyTask"  class="demo-ruleForm">
            <el-form-item>
                <wangeditor v-model="answerStudyTask.userFinishDesc" />
                <!-- <tiptap></tiptap> -->
            </el-form-item>
            <el-form-item label="选择附件">
                <!-- <file-upload :resourceid="answerStudyTask.userFinishDescResoursefileid" /> -->
                <!-- FileUploadNoPost -->
                <FileUploadNoPost :value="postFileList"></FileUploadNoPost>
                <!-- <el-button @click="selectFileList">查看文件</el-button> -->
            </el-form-item>
            <!-- <el-button @click="findFileByUserUuid(answerStudyTask.userFinishDescResoursefileid)">刷新文件列表</el-button> -->
            <el-table :data="user_fileList">
              <el-table-column prop="fileName" label="文件名" />
              <el-table-column  label="操作" >
                <template #default="scope">
                  <el-button tag="a" target="_blank" :href="scope.row.fileUrl" type="primary" size="small">查看</el-button>
                  <el-button @click="deleteFile(scope.row.id)" type="danger" size="small">删除</el-button>
                </template>
              </el-table-column>
          </el-table>
        </el-form>
        <template #footer>
          <el-button style="float: right;" type="primary" @click="answerTask">提交</el-button>
        </template>
    </el-card>
  </div>
</template>

<script>
import { StudyApi } from '@/api/study'
import {FileApi } from '@/api/file'
import { resourceApi } from '@/api/resource'
import { v4 as uuidv4 } from 'uuid';
import FileUpload from '@/components/FileUpload.vue'
import wangeditor from '@/components/wangeditor.vue'
// import tiptap from '@/components/tiptap.vue'
import FileUploadNoPost from "@/components/FileUploadNoPost.vue"
export default {
  name: 'StudyDetails',
  components: { wangeditor, FileUpload,FileUploadNoPost},
  data(){
    return{
      studyDetails: {},
      task_fileList:[],
      user_fileList:[],
      postFileList:[],
      answerStudyTask:{
        "taskId": "",
        "userFinishDesc": "",
        "userFinishDescResoursefileid":""
      }
    }
  },
  methods:{
    
    // {{ this.$route.query.id }}
    // 根据id获取任务信息
    async getStudyDetails(){
      const res = await StudyApi. getStudyTaskById(this.$route.query.id)
      this.studyDetails = res.data
      this.findFileByUuid(this.studyDetails.resourceFileUuid)
      console.log(res)
    },


    // resourceFileUuid 根据文件uuid获取文件列表
    async findFileByUuid(resourceFileUuid){
      const res = await FileApi.findFileByUuid(resourceFileUuid)
      this.task_fileList = res.data
    },
    // 根据文件uuid获取用户文件列表
    async findFileByUserUuid(resourceFileUuid){
      const res = await FileApi.findFileByUuid(resourceFileUuid)
      this.user_fileList = res.data
      console.log(res);
    },



    // 回答任务
    async answerTask(){
      this.answerStudyTask.taskId = this.$route.query.id;
      await StudyApi.answerStudyTask(this.answerStudyTask);
      if(this.postFileList.length > 0){
        await this.submitResourceFiles();
      }
      this.findFileByUserUuid(this.answerStudyTask.userFinishDescResoursefileid);
      this.$message.success('任务提交成功')
    },

    // 提交任务文件
    async submitResourceFiles() {
        try {
          await resourceApi.submitResourceFiles(this.postFileList,this.answerStudyTask.userFinishDescResoursefileid);
          this.$message.success('文件提交成功')
          console.log("提交文件成功");
        } catch (error) {
          this.$message.success('文件提交失败')
          console.error('添加文件失败:', error);
        }
    },
    // 查看文件列表
    selectFileList(){
      console.log(this.postFileList);
    },

    // 根据任务id获取回答信息
    async getAnswerStudyTask(){
      const res = await StudyApi.getAnswerTaskById(this.$route.query.id)
      console.log("根据任务id获取回答",res)
      if(res.data == null){
        this.answerStudyTask.userFinishDescResoursefileid = uuidv4()
        console.log("uuid",this.answerStudyTask.userFinishDescResoursefileid);

      }else{
        this.answerStudyTask.userFinishDesc = res.data.userFinishDesc
        this.answerStudyTask.userFinishDescResoursefileid = res.data.userFinishDescResoursefileid
        this.findFileByUserUuid(this.answerStudyTask.userFinishDescResoursefileid)
        console.log("查询到回答",this.answerStudyTask);
      }
    },
    // 根据文件id删除文件
    deleteFile(fileId){
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
      }).then(async () => {
        try{
          // 删除文件
          await resourceApi.deleteResourceFile(fileId)
          // 获取文件列表
          this.findFileByUserUuid(this.answerStudyTask.userFinishDescResoursefileid)
        } catch (error) {
          console.log(error);
        }
      })
    },

    // 文件下载downloadFile(scope.row.fileUrl)
    downloadFile(fileUrl,fileName){
      const a = document.createElement('a');
      a.href = fileUrl;
      a.download = fileName;
      a.style.display = 'none'; // 隐藏下载链接
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a); // 移除下载链接
    }

  },
  created(){
    this.getStudyDetails()
    this.getAnswerStudyTask()
    console.log("111",this.answerStudyTask.userFinishDescResoursefileid);
  }
}
</script>

<style lang="less" scoped>
.margin-top-10{
  margin-top: 10px;
}
.title{
  font-size: large;
  font-weight: bold;
  color: var(--text-200);
}
.icon-q{
  color: var(--el-text-color);
}
.display-center{
  display: flex;
  justify-content: center;
  align-items: center;
}
.display-x-center{
    display: flex;
    align-items: center;
}
.file{
  display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.file-item{
  margin-top: 5px;
  margin-bottom: 5px;
}
.display-inline{
  // display: inline;
}
.details{
  // display: grid;
  // grid-template-columns: repeat(3, 1fr);
  // grid-gap: 10px;
}
.ccard{
  border-radius:15px ;
  margin-bottom: 10px;
  // aspect-ratio: 16/9;
}
.card-header{
  display: flex;
  align-items: center;
  color: var(--el-text-color);
}
.el-card__footer{
   display:flex;
    justify-content: flex-end;
}
.docx{
  display: flex;
}
.docx-index{
  display: none;
  width: 280px;
  position: fixed;
  right: 0;
}
//宽度低于500px时，将卡片宽度设置为100%
@media screen and (min-width: 1000px) {
  .min-width-1000-o{
    width: calc(100% - 280px);
  }
}
    
</style>