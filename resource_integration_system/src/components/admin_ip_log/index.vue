<template>
  <div>
    <!-- {{ user }} -->
    <el-table :data="ip_log" style="width: 100%"  v-loading="isLoading">
      <el-table-column prop="ipAddress" label="IP地址">
      </el-table-column>
      <el-table-column prop="ipAccessTime" label="访问时间">
      </el-table-column>
      <el-table-column prop="ipUserDevice" label="访问设备">
      </el-table-column>
      <el-table-column label="访问地区">
        <template v-slot="scope">
             {{ scope.row.ipProvince }}-{{ scope.row.ipCity }}
        </template>
      </el-table-column>
      <el-table-column  label="访问次数">
        <template v-slot="scope">
             {{ scope.row.ipRepeat }}次
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { iplogApi } from '@/api/ip_log'
import store from '@/store'
export default {
    name: 'admin_ip_log',
    data(){
        return {
            ip_log:[],
            isLoading: true,
            user: store.state.user.userInfo
        }
    },
    methods:{
        async getIpLog(){
            try{
                const res = await iplogApi.getallIplog()
                this.setIsLoading()
                console.log(res);
                this.ip_log = res.data
            } catch(error){
                console.log(error);
            }
            
        },
        setIsLoading(){
            this.isLoading = !this.isLoading
        },
    },
    mounted(){
        this.getIpLog();
    },

}
</script>

<style>

</style>