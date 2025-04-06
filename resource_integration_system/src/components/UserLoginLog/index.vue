<template>
  <div>
    <!-- <h1>{{userLoginLogData}}</h1> -->
    <el-table :data="userLoginLogData" style="width: 100%">
      <el-table-column prop="loginIp" label="登录IP" >
      </el-table-column>
      <el-table-column prop="loginTime" label="登录时间">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { UserLoginLog } from '@/api/user_login_log';
export default {
    name:"UserLoginLog",
    data(){
      return {
        userLoginLogData:[],
      }
    },
    methods:{
      // 获取用户登录日志
      async getUserLoginLog(){
        const res = await UserLoginLog.GetUserLoginLog();
        if(res.code === 200){
          this.userLoginLogData = res.data;
        }else{
          this.$message.error(res.msg);
        }
      }
    },
    created(){
      this.getUserLoginLog()
    },
}
</script>

<style>

</style>