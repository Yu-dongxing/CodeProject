import request from '@/utils/request'

// 资源相关接口
export const roleApi = {
  // 获取资源列表
  getAllRole() {
    return request({
      url: '/public/getRoles',
      method: 'get'
    })
  },
}