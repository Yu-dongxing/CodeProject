<template>
     <div class="container">
        <el-card :body-style="{ display: 'flex'}">
            <div class="header-avatar card">
                <el-avatar 
                    :size="60" 
                    :src="userInfo?.avatar || 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'"
                />
            </div>
            <div class="header-userinfo ">
                <div class="userinfo-name">
                    <el-text>{{ userInfo?.username || '未登录' }}</el-text>
                </div>
                <div class="userinfo-id">
                    <el-tag>ID: {{ userInfo?.id || 'N/A' }}</el-tag>
                </div>
            </div>
            <div class="header-actions card">
                <el-button type="danger" @click="handleLogout">退出登录</el-button>
            </div>
        </el-card>
    </div>
    <div class="control">
        <!-- <div class="control-table"></div>
        <div class="control-main"></div> -->
        <el-card>
            <el-tabs v-model="active"  @tab-click="handleClick">
                <el-tab-pane label="个人中心" name='1'>
                    <!-- <userControlServer></userControlServer> -->
                    <el-form :model="user_from" label-position="top">
                        <el-form-item label="用户名">
                            <el-input v-model="user_from.username"  autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="用户邮箱">
                            <el-input v-model="user_from.email"  autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="用户手机号">
                            <el-input v-model="user_from.phoneNumber"  autocomplete="off" />
                        </el-form-item>
                        <el-button @click="updateUserInfo(user_from,userInfo.id)">更新</el-button>
                    </el-form>
                </el-tab-pane>
                <el-tab-pane label="资源管理" name='2' v-if="userInfo?.roleName === 'admin'">
                    <admin_Resouce_data></admin_Resouce_data>
                </el-tab-pane>
                <el-tab-pane label="用户管理" name='3' v-if="userInfo?.roleName === 'admin'">
                    <admin_Users_data></admin_Users_data>
                </el-tab-pane>
                <el-tab-pane label="访问日志" name='4' >
                    <admin_ip_log></admin_ip_log>
                </el-tab-pane>
                <el-tab-pane label="待审核资源" name='5' v-if="userInfo?.roleName === 'admin'">
                    <admin_resouce_audit></admin_resouce_audit>
                </el-tab-pane>
                <el-tab-pane label="更新日志管理"  name='6' v-if="userInfo?.roleName === 'admin'" >
                    <admin_update_log_data/>
                </el-tab-pane>
                <!-- admin_sysinfo_date -->
                <el-tab-pane label="系统信息管理"  name='7' v-if="userInfo?.roleName === 'admin'">
                    <admin_sysinfo_date/>
                </el-tab-pane>
                <el-tab-pane label="学习任务管理"  name='8' v-if="userInfo?.roleName === 'admin'">
                    <Admin_Study_date/>
                </el-tab-pane>
                
            </el-tabs>
        </el-card>
        
    </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import {userApi} from '@/api/user'
import admin_Resouce_data from '../components/admin_Resouce_data/index.vue'
import admin_Users_data from '../components/admin_Users_data/index.vue'
import  admin_ip_log  from '@/components/admin_ip_log/index.vue'
import userControlServer from "@/components/userControlServer/index.vue"
import admin_resouce_audit from "@/components/admin_resouce_audit/index.vue"
import admin_update_log_data from "@/components/admin_update_log_data/index.vue"
import admin_sysinfo_date from '@/components/admin_sysinfo_date/index.vue'
import Admin_Study_date from '@/components/Admin_Study_date/index.vue'
export default {
    components: {
        admin_Resouce_data,
        admin_Users_data,
        userControlServer,
        admin_ip_log,
        admin_resouce_audit,
        admin_update_log_data,
        admin_sysinfo_date,
        Admin_Study_date
    },
    data(){
        return {
            active:'1',
            user_from:{
                username:this.userInfo?.username || '',
                email:this.userInfo?.email || '',
                phoneNumber:this.userInfo?.phoneNumber || '',
                roleId: this.userInfo?.roleId || '',
            }
        }
    },
    methods:{
        handleClick(tab, event){
            console.log(tab, event)
        },
        async updateUserInfo(data,userId){
            try{
                const res = await userApi.updateUserInfo(data, userId)
                if(res.code == 400){
                  this.$message.error('更新失败'+ res.message)
                }else{
                  console.log('更新用户信息:', res.data)
                  this.$message.success('更新成功')
                  
                }
            } catch (error) {
                console.log('更新用户信息错误:', error);
                
            }
        },
    },
  setup() {
    const store = useStore()
    const router = useRouter()
    const userInfo = computed(() => store.state.user.userInfo)
    console.log(userInfo);
    // this.user_from.email = userInfo.value.email
    // this.user_from.phone = userInfo.value.phone
    const handleLogout = () => {
      store.dispatch('user/logout')
      router.push('/login')
      ElMessage.success('已退出登录')
    }

    return {
      userInfo,
      handleLogout
    }
  }
}
</script>

<style scoped lang="less">
.container {
    /* min-height: 100vh; 最小高度占满整个视口 */
    .card{
        display: flex;
        align-items: center;
    }
    .container-header{
        width: 80%;
        margin-left: 10%;
        height: 100px;
        // background-color: var(--bg-300);
        // display: flex;
        // align-items: center;
        border-radius: 20px;
        box-sizing: border-box;
        padding: 10px;
        .header-userinfo{
            margin-left: 10px;
            width: 100%;

        }
        .header-actions{
            float: right;
        }
    }
}
.control{
    margin-top: 10px;
    .control-table{
        width: 100%;
        height: 80px;
        background-color: var(--primary-100);
        border-radius: 20px;
    }
    .control-main{
        width: 80%;
        height: 100%;
        margin-left: 10px;
        background-color: var(--bg-300);
        border-radius: 20px;
    }
}
</style>