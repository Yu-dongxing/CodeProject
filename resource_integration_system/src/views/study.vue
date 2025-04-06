<template>
  <div class="Study">
    <!-- <h1>Study</h1> -->
    <el-card class="ccard" shadow="hover" v-for="(item , index ) in tasks" :key="index">
        <template #header>
            <div class=" display-x-center" >
                <el-icon><MessageBox /></el-icon>
                <el-text style="margin-left: 5px;">{{ item.title }}</el-text>
                <el-tag style="float: right; margin-left: 20px;">创建时间：{{item.createdAt}}</el-tag>
            </div>
        </template>
        <el-text>{{item.taskTitle}}</el-text>
        <template #footer>
            <div class=" display-x-center">
                <el-button @click="goDetail(item.id)" >
                    查看详情
                    <el-tag type="success" style="float: right; margin-left: 20px;">截止日期：{{item.dueDate}}</el-tag>
                </el-button>
            </div>
        </template>
    </el-card>
  </div>
</template>

<script>
import { StudyApi } from '@/api/study'
export default {
    data(){
        return{
            tasks:[]
        }
    },
    methods:{
        // 获取任务列表
        async getTasksAll(){
            try{
                const res = await  StudyApi.getAllStudyTasks();
                this.tasks = res.data;
                console.log(res);
            } catch(e){
                console.log(e)
            }
        },
        // 资源详情跳转
        goDetail(id) {
            this.$router.push({ path: '/StudyDetails', query:  { id: id } }) 
        },
    },
    created(){
        this.getTasksAll();
    },
    

}
</script>

<style>
.ccard {
    padding: 5px;
}
.el-card__header,.el-card__footer{
    padding: 5px;
}

</style>