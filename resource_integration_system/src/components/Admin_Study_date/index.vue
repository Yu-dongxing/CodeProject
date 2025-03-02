<template>
  <div>
    <el-button @click="openAddDialog()">添加</el-button>
    <el-table :data="study_data">
      <el-table-column prop="title" label="标题"></el-table-column>
      <el-table-column prop="taskTitle" label="任务标题"></el-table-column>
      <el-table-column prop="dueDate" label="截止日期"></el-table-column>
      <el-table-column prop="description" label="描述">
        <template #default="scope">
            <el-button @click="openPreviewDialog(scope.row.description)">预览</el-button>
        </template>
      </el-table-column>
      <el-table-column prop="priority" label="优先级"></el-table-column>
      <el-table-column prop="difficultyLevel" label="难度等级"></el-table-column>
      <el-table-column prop="resourceFileUuid" label="资源文件"></el-table-column>
      <el-table-column prop="id" label="操作">
        <template #default="scope">
            <!-- @click="deleteStudyData(scope.row.id)" -->
            <el-button @click="adautData(scope.row.id)" >编辑 {{ scope.row.id }}</el-button> 
          <el-button @click="deleteStudyData(scope.row.id)" >删除 {{ scope.row.id }}</el-button>  
          <el-button @click="selectBytask(scope.row.id)" >查看任务回答 {{ scope.row.id }}</el-button>  
        </template>
      </el-table-column>
    </el-table>
    <!-- 预览 -->
    <el-dialog v-model="dialogport" title="任务预览" width="80%">
                <div v-html="description_data"></div>
    </el-dialog>
    <!-- 查看该任务回答 -->
    <el-dialog v-model="dialogportselect" title="查看该任务所有回答" width="80%">
      <el-table :data="tasks_answer_data">
        <el-table-column prop="postUserName" label="回答用户"></el-table-column>
        <el-table-column prop="userFinishDesc" label="回答描述">
          <template #default="scope">
            <el-button @click="openPreviewDialog(scope.row.userFinishDesc)">预览</el-button>
        </template>
        </el-table-column>
        <el-table-column prop="id" label="操作">
          <template #default="scope">
            <el-button @click="deleteAnswerTask(scope.row.id)" >删除 {{ scope.row.id }}</el-button>  
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <!-- 编辑以及更新 -->
    <el-dialog v-model="dialogFormVisible" :title="isAddOrUpdate ? '添加学习任务' :'编辑任务'" width="80%">
      <el-form :model="from_study_data">
        <el-form-item label="标题" >
          <el-input v-model="from_study_data.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="任务标题" >
          <el-input v-model="from_study_data.taskTitle" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="截止日期" >
            <el-date-picker
                v-model="from_study_data.dueDate"
                type="datetime"
                placeholder="选择日期时间"
                format="YYYY/MM/DD hh:mm:ss"
                value-format="YYYY-MM-DD hh:mm:ss"
                @change="handleDateChange"
                ></el-date-picker>
        </el-form-item>
        <el-form-item label="描述" >
          <wangeditor v-model="from_study_data.description"></wangeditor>
        </el-form-item>
        <el-form-item label="优先级" >
          <el-select v-model="from_study_data.priority" placeholder="请选择优先级">
            <el-option label="优先级高" value="优先级高"></el-option>
            <el-option label="优先级中" value="优先级中"></el-option>
            <el-option label="优先级低" value="优先级低"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="难度等级">
          <el-select v-model="from_study_data.difficultyLevel" placeholder="请选择难度等级">
            <el-option label="简单" value="简单"></el-option>
            <el-option label="中等" value="中等"></el-option>
            <el-option label="困难" value="困难"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="资源文件">
          <el-card>
            <FileUpload :resourceid="from_study_data.resourceFileUuid"></FileUpload>  
          </el-card>
            <el-button @click="getStudyFileData(from_study_data.resourceFileUuid)">刷新文件</el-button>
            <el-table  :data="study_file_data" >
                <el-table-column prop="fileName" label="文件名"></el-table-column>
                <el-table-column prop="fileSize" label="文件大小"></el-table-column>
                <el-table-column prop="uploadTime" label="文件类型"></el-table-column>
                <el-table-column prop="fileUrl" label="文件地址"></el-table-column>
            </el-table>
        </el-form-item>
        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取消</el-button>
                <el-button type="primary" @click="addStudyData()">
                    提交
                </el-button>
            </div>
        </template>
    </el-dialog>
  </div>
</template>

<script>
import { StudyApi } from '@/api/study'
import {FileApi } from '@/api/file'
import FileUpload from '@/components/FileUpload.vue'
import wangeditor from '@/components/wangeditor.vue'
import { v4 as uuidv4 } from 'uuid';
export default {
    name: 'Admin_Study_date',
    components:{FileUpload,wangeditor},
    data(){
        return{
            dialogportselect:false,
            dialogport:false,
            dialogFormVisible:false,
            isAddOrUpdate:true,
            study_uuid:uuidv4(),
            study_data:[],
            description_data:'',
            autitId:'',
            from_study_data:{
                "title":"任务名称",
                "taskTitle":"任务主题",
                "dueDate":"2025-02-05 12:00:00",
                "description":"编写任务描述",
                "priority":"优先级高",
                "difficultyLevel":"简单",
                "resourceFileUuid":""
            },
            study_file_data:[],
            tasks_answer_data:[],
        }
    },
    methods:{
        handleDateChange(value) {
        // 当日期选择发生变化时，可以在这里进行处理
        console.log('选中的日期时间:', value); // 输出格式为 "2025-02-05 12:00:00"
        },
        // 获取所有学习任务
        async getStudyData(){
            const res = await StudyApi.getAllStudyTasks()
            this.study_data = res.data
        },
        // 添加学习任务
        async addStudyData(){
          if(this.isAddOrUpdate){
            await StudyApi.addStudyTask(this.from_study_data)
             this.dialogFormVisible= false
             this.getStudyData();
             this.$message.success('添加成功')
          }else{
            await StudyApi.updateStudyTask(this.from_study_data,this.autitId)
            this.dialogFormVisible= false
            this.$message.success('修改成功')
            this.getStudyData();
          }
        },
        //删除学习任务
        async deleteStudyData(id){
            this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(async () => {
                await StudyApi.deleteStudyTask(id)
                this.$message.success('删除成功')
                this.getStudyData();
            })
        },
        // 传入id-根据id寻找log_date中对应id是数据-返回数据
        findLogById(id) {
          console.log(id);
          const inoo = this.study_data.find(info => info.id === id);
          console.log(inoo);
          return inoo;
        },
        // 获取文件数据
        async getStudyFileData(id){
          const res = await FileApi.findFileByUuid(id)
          this.study_file_data = res.data
          console.log(this.study_file_data)
        },
        // 编辑学习任务
        adautData(id){
            this.dialogFormVisible=true
            this.isAddOrUpdate=false
            const from_data = this.findLogById(id);
            console.log(from_data);

            this.autitId = id
            this.from_study_data.description = from_data.description
            this.from_study_data.title = from_data.title
            this.from_study_data.dueDate = from_data.dueDate
            this.from_study_data.difficultyLevel = from_data.difficultyLevel
            this.from_study_data.priority = from_data.priority
            this.from_study_data.resourceFileUuid = from_data.resourceFileUuid
            this.from_study_data.taskTitle = from_data.taskTitle

        },
        
        // 查看任务所有回答
        async getAnswerTaskData(id){
            const res = await StudyApi.getAllAnswerTaskByTaskId(id)
            this.tasks_answer_data = res.data
        },
        selectBytask(id){
          this.dialogportselect = true
          this.getAnswerTaskData(id)
        },
        // 打开预览对话框
        openPreviewDialog(res) {
            this.dialogport = true;
            this.description_data = res;
        },
        // 打开添加对话框
        openAddDialog(){
            this.dialogFormVisible=true
            this.isAddOrUpdate=true
            this.from_study_data.resourceFileUuid = uuidv4();
            console.log(this.from_study_data.resourceFileUuid);
        }
    },
    created(){
        this.getStudyData();
    },
}
</script>

<style>

</style>