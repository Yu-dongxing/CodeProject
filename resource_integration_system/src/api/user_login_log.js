import request from '@/utils/request'

// 用户登录日志相关接口
export const UserLoginLog = {
  // 获取用户登录日志
  GetUserLoginLog() {
    return request({
      url: '/userloginlog/find/user',
      method: 'get'
    })
  },
}