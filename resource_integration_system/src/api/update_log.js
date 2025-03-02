import request from '@/utils/request'

// 更新日志相关接口
export const Update_Log_Api = {
  // 获取更新日志列表
  getAllLog(){
    return request({
      url: '/public/updatelog/all',
      method: 'get'
    })
  },
  //添加更新日志
  addlog(data){
    // {
    //   "logTitle": "测试日志-2",
    //   "desc": "测试日志",
    //   "type": "success",
    //   "hollow": "true"
    // }
    return request({
      url:"/updatelog/add",
      method: 'post',
      data
    })
  },
  // 更新日志
  updateLog(id,data){
    return request({
      url: '/updatelog/update/'+id,
      method: 'put',
      data
    })
  },
  // 删除日志
  deleteLog(id){
    return request({
      url: '/updatelog/delete/'+id,
      method: 'get'
    })
  }
}