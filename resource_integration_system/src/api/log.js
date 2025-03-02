import request from '@/utils/request'

// 日志相关接口
export const logApi = {
  // 上传用户日志
  postLog(data) {
    return request({
      url: '/public/log/add',
      method: 'post',
      data
    })
  },
// 查询所有日志
  getalllog(){
    return request({
      url: '/public/log/all',
      method: 'get'
    })
  }
}