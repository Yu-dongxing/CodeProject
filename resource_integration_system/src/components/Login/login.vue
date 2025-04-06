<template>
    <div class="login">
        <el-card class="login-lift-from" shadow="hover">
            <div class="from-title">
                <p>{{isLoginOrSign?"登录":"注册" }}</p>
            </div>
            <!-- 登录 -->
            <div class="from-input" v-if="isLoginOrSign">
                <el-form label-position="top">
                    <el-form-item label="手机号：">
                        <el-input class="input" 
                            v-model="login_from.phone"  
                            placeholder="请输入手机号" 
                            clearable
                            >
                            <template #prepend>
                                <el-icon><User /></el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item label="密码：">
                        <el-input class="input" 
                            type="password" 
                            v-model="login_from.password"  
                            placeholder="请输入密码" 
                            clearable
                            show-password>
                            <template #prepend>
                                <el-icon><Lock /></el-icon>
                            </template>
                            
                        </el-input>
                    </el-form-item>
                </el-form>
            </div>
            <!-- 注册 -->
            <div class="from-input" v-else>
                <el-form label-position="top">
                    <el-form-item label="姓名:">
                        <el-input class="input" 
                        v-model="sign_from.username"  
                        placeholder="请输入姓名" 
                        clearable
                        /></el-form-item>
                <el-form-item label="手机:"><el-input class="input" 
                v-model="sign_from.phone"  
                placeholder="请输入手机号" 
                clearable
                /></el-form-item>
                <el-form-item label="密码:"><el-input class="input" 
                type="password" 
                v-model="sign_from.password"  
                placeholder="请输入密码" 
                clearable
                show-password
                /></el-form-item>
                <el-form-item label="确认密码:"><el-input class="input" 
                type="password" 
                v-model="sign_from.aspassword"  
                placeholder="请再次输入密码" 
                clearable
                show-password
                /></el-form-item>
                <el-form-item label="选择角色:">
                    <el-select v-model="sign_from.roleId" placeholder="请选择角色">
                    <el-option
                        v-for="item in roles"
                        :key="item.id"
                        :label="item.description"
                        :value="item.id"
                        >
                    </el-option>
                </el-select>
                </el-form-item>
                </el-form>
                
                
                
                <!-- 输入密码时调用两个密码检查函数 -->
                
                
                <!-- <el-radio-group v-model="sign_from.roleId">
                    <el-radio v-for="(item,index) in roles" :key="index" :value="item.id">{{ item.description }}</el-radio>
                </el-radio-group> -->
                
                
            </div>
            <div class="from-button">
                <el-button class="button" type="primary" @click="loginOrsign()">{{isLoginOrSign?"登录":"注册" }}</el-button>
            </div>
            <div class="from-isLoginOrSign" @click="SetisLoginOrSign()">
                <el-text>{{isLoginOrSign?"没有账号？点击注册！":"已有账号，点击登录！" }}</el-text>
            </div>
        </el-card>
        <div class="login-right-contion">
            <!-- <el-image class="imge" src="/png/sql-5.png" fit="cover" width="100%" height="100%"></el-image> -->
            <img class="imge" src="../../assets/png/sql-5.png" alt="">
        </div>
    </div>
</template>

<script>
import {roleApi} from '@/api/role'
export default {
    name: 'login',
    data(){
        return{
            login_from:{
                phone:'',
                password: ''
            },
            sign_from:{
                username:'',
                password:'',
                aspassword:'',
                phone:'',
                roleId:2
            },
            roles:[],
            isLoginOrSign:true,
        }
    },
    methods:{
        SetisLoginOrSign(){
            this.getRoles()
            this.isLoginOrSign = !this.isLoginOrSign
            this.clearForm()
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
        // 添加用户登录日志
        async loginOrsign(){
            if (this.isLoginOrSign) {
                // 登录逻辑
                if (!this.checkLogin()) return
                
                try {
                    const loginData = {
                        phoneNumber: this.login_from.phone.toString(),
                        password: this.login_from.password.toString()
                    }
                    
                    console.log('发送登录请求:', loginData)
                    const res = await this.$store.dispatch('user/login', loginData)
                    console.log('登录响应:', res)
                    
                    if (res.code === 200) {
                        await this.$store.dispatch('user/getUserInfo')
                        this.$message.success('登录成功')
                        this.$router.push('/')
                    } else {
                        this.$message.error(res.msg || '登录失败')
                    }
                } catch (error) {
                    console.error('登录错误:', error)
                    this.$message.error(error.msg || '登录失败')
                }
            } else {
                // 注册逻辑
                if (!this.checkSign()) return
                if (!this.checkPassword()) return

                try {
                    const signData = {
                        username: this.sign_from.username,
                        password: this.sign_from.password,
                        phoneNumber: this.sign_from.phone,
                        roleId: this.sign_from.roleId
                    }
                    console.log("发送注册请求：",signData);
                    await this.$store.dispatch('user/register', signData)
                    this.$message.success('注册成功')
                    this.isLoginOrSign = true
                    this.clearForm()
                } catch (error) {
                    this.$message.error(error.msg || '注册失败')
                }
            }
        },
        //检查注册时两个密码是否一致
        checkPassword(){
            if(this.sign_from.password != this.sign_from.aspassword){
                this.$message.error('两次密码不一致')
                return false
            }
            return true
        },
        //登录检查
        checkLogin(){
            if(this.login_from.phone == '' || this.login_from.password == ''){
                this.$message.error('请输入完整信息')
                return false
            }
            return true
        },
        //注册检查
        checkSign(){
            if(this.sign_from.username == '' || 
               this.sign_from.password == '' || 
               this.sign_from.aspassword == '' || 
               this.sign_from.phone == ''){
                this.$message.error('请输入完整信息')
                return false
            }
            return true
        },
        //清空表单
        clearForm(){
            this.login_from = {
                phone:'',
                password: ''
            }
            this.sign_from = {
                username:'',
                password:'',
                aspassword:'',
                phone:'',
            }
        }
    },
    mounted(){
    },
    computed:{
        roleList(){
        }
    }
}
</script>

<style lang="less">
p{
    // margin: 0;
}
.login{
    display: flex;
    width: calc(100vw - 20px);
    height: calc(100vh - 140px);
    box-sizing: border-box;
    padding: 10px;
    .login-lift-from{
        width: 50%;
        height: 100%;
        // border: 1px solid red;
        box-sizing: border-box;
        padding: 10px;
        // display: flex;
        // flex-direction: column;
        // align-items: center;
        .from-title{
            height: 50px;
            width: 100%;
            // background-color: aqua;
            display: flex;
            justify-content: center;
            align-content: center;
            p{
                line-height: 20px;
                font-size: 20px;
                font-weight: bolder;
            }
        }
        .from-input{
            .input-text{
                p{
                    color: rgba(0, 0, 0, 0.538);
                }
            }
            .input{
            }
        }
        .from-button{
            margin-top: 10px;
            .button{
                width: 100%;
            }
        }
        .from-isLoginOrSign{}
    }
    .login-right-contion{
        width: 50%;
        height: 100%;
        // aspect-ratio: 16/9;
        img{
            width: 100%;
            height: 100%;
            // aspect-ratio: 16/9;
        }
        // border: 1px solid red;
    }
}
/* 当屏幕宽度小于500px */
@media screen and (max-width: 500px) {
  .login-right-contion{
    display: none;
  }
  .login .login-lift-from {
    width: 100%;
}
}
</style>