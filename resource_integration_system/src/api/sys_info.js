import request from '@/utils/request'

// 系统信息相关接口
export const sysinfoApi = {
  // 根据id获取系统信息
  findByID(id) {
    return request({
      url: '/public/sysinfo/findbuid/'+id,
      method: 'get'
    })
  },
  // 获取系统欢迎信息
  getSysWelcomeInfo() {
    return request({
      url: '/public/sysinfo/findbuid/6',
      method: 'get'
    })
  },
  // 获取ICP备案备案信息
  getICPBaAiInfo() {
    return request({
      url: '/public/sysinfo/findbuid/4',
      method: 'get'
    })
  },
  // 获取皖公网安备案备案信息
  getGWABaAiInfo() {
    return request({
      url: '/public/sysinfo/findbuid/5',
      method: 'get'
    })
  },
  // 获取系统版权信息
  getSysCopyrightInfo() {
    return request({
      url: '/public/sysinfo/findbuid/7',
      method: 'get'
    })
  },
//   查询所有系统信息
  getAllSysInfo() {
    return request({
      url: '/public/sysinfo/all',
      method: 'get'
    })
  },
//   根据id更新系统信息
  updateSysInfo(id,data) {
    return request({
      url: '/sysinfo/update/'+id,
      method: 'post',
      data
    })
  }
}