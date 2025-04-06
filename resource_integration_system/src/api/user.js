import request from '@/utils/request'

// 用户相关接口
export const userApi = {
  // 用户登录
  login(data) {
    return request({
      url: '/login',
      method: 'post',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        phoneNumber: data.phoneNumber.toString(), // 确保是字符串类型
        password: data.password.toString()  // 确保是字符串类型
      }
    })
  },

  // 用户注册
  register(data) {
    return request({
      url: '/sign',
      method: 'post',
      data: {
        username: data.username,
        password: data.password,
        phoneNumber: data.phoneNumber,
        roleId:data.roleId
      }
    })
  },

  // 获取用户信息
  getUserInfo() {
    return request({
      url: '/user/details',
      method: 'get',
    })
  },

  // 更新用户信息
  updateUserInfo(data, userId) {
    return request({
      url: '/admin/users/'+userId,
      method: 'put',
      data:{
        username:data.username,
        phoneNumber:data.phoneNumber,
        email:  data.email,
        roleId:data.roleId
    }
    })
  },
  //删除用户
  deleteUser(userId){
    return request({
      url: '/admin/users/'+userId,
      method: 'delete',
    })
  },
  // 修改密码
  updatePassword(data) {
    return request({
      url: '/user/password',
      method: 'put',
      data
    })
  },
  // 获取所有用户
  getAllUsers(){
    return request({
      url: '/admin/users',
      method: 'get',
    })
  },
  // /userloginlog/add
  // 添加登录日志
  addLoginLog() {
    return request({
      url: '/userloginlog/add',
      method: 'post',
    })
  },
} 