<template>
  <el-table :data="users" height="250" style="width: 100%">
      <el-table-column prop="username" label="用户名" width="180" />
      <el-table-column prop="email" label="用户邮箱" width="180" />
      <el-table-column prop="phoneNumber" label="用户手机" />
      <el-table-column prop="roleName" label="用户角色" />
      <el-table-column prop="updateTime" label="更新时间" />
      <el-table-column prop="id" label="操作">
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.row.id)">编辑</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.row.id)" >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 用户编辑 -->
    <el-dialog v-model="dialogFormVisible" title="用户编辑" width="500">
      <el-form :model="user_from" label-position="top">
        <el-form-item label="用户名">
          <el-input  v-model="user_from.username" autocomplete="off" />
        </el-form-item>
        <el-form-item label="用户邮箱">
          <el-input v-model="user_from.email" autocomplete="off" />
        </el-form-item>
        <el-form-item label="用户手机号">
          <el-input v-model="user_from.phoneNumber" autocomplete="off" />
        </el-form-item>
        <el-form-item label="用户角色ID">
            <el-select v-model="user_from.roleId" placeholder="请选择用户角色"  >
                <el-option v-for="item in roles" :key="item.id" :label="item.description" :value="item.id" />
            </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary" @click="postFrom()">提交</el-button>
        </div>
      </template>
    </el-dialog>
    <!-- 用户删除 -->
    <el-dialog v-model="dialogdelentVisible" title="用户删除" width="500">
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogdelentVisible = false">取消</el-button>
          <el-button type="primary" @click="deleteUser()">删除</el-button>
        </div>
      </template>
    </el-dialog>
</template>

<script>
import {userApi} from '@/api/user'
import {roleApi} from '@/api/role'
export default {
name: 'admin_Users_data',
    data () {
        return {
            roles:[],
            users:[],
            dialogFormVisible:false,
            dialogdelentVisible:false,
            user_from:{
                username:"",
                phoneNumber:"",
                email:"",
                roleId:""
            },
            user_from_user_id:"",
            loading: true
        }
    },
    methods:{
        async getAllUsers(){
            try{
                const res = await userApi.getAllUsers()
                console.log('用户列表:', res.data)
                this.users = res.data
                console.log(this.users);
            }catch (error) {
                console.error('获取用户列表错误:', error)
            }
        },
        handleEdit(id){
            this.user_from_user_id = id
            this.dialogFormVisible = true
            this.getAllUsers()
            console.log('编辑',id)
            this.findItemById(id)
        },
        handleDelete(id){
          // this.dialogdelentVisible = true
          this.deleteUser(id)
          this.getAllUsers()
          console.log('删除',id)
        },
        postFrom(){
            this.updateUserInfo(this.user_from,this.user_from_user_id)
            console.log(this.user_from)
            this.getAllUsers()
            this.dialogFormVisible = false
        },
        findItemById(targetId) {
            const item = this.users.find(item => item.id === targetId);
            if (item) {
                console.log('找到的数据：', item);
                this.user_from.email = item.email;
                this.user_from.phoneNumber = item.phoneNumber;
                this.user_from.username = item.username;
                this.user_from.roleId = item.roleId
                return item;
            } else {
                console.log('未找到数据');
                return null;
            }
        },
        async getRoles(){
            try {
                const res = await roleApi.getAllRole()
                console.log('角色列表:', res.data)
                this.roles = res.data
                console.log(this.roles);
            } catch (error) {
                console.error('获取角色列表错误:', error)
            }
        },
        async updateUserInfo(data,userId){
            try{
                const res = await userApi.updateUserInfo(data, userId)
                if(res.code == 400){
                  this.$message.error('更新失败'+ res.message)
                }else{
                  console.log('更新用户信息:', res.data)
                  this.$message.success('更新成功')
                  this.getAllUsers()
                }
            } catch (error) {
                console.log('更新用户信息错误:', error);
                
            }
        },
        async deleteUser(userid){
            try{
              const res = await userApi.deleteUser(userid)
              if(res.code == 400){
                  this.$message.error('删除失败'+ res.message)
                }else{
                  console.log('删除用户信息:', res.data)
                  this.$message.success('删除成功')
                  this.getAllUsers()
                }
            } catch (error) {
                console.log('删除用户信息错误:', error);
            }
        }
    },
    mounted(){
        this.getAllUsers()
        this.getRoles()
    }
}
</script>

<style>

</style>