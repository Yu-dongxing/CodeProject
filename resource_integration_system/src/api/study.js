import request from '@/utils/request'

// 学习任务相关接口
export const StudyApi = {
    // 获取所有学习任务
  getAllStudyTasks(){
    return request({
      url: '/task/find/all',
      method: 'get'
    })
  },
    // 根据id获取学习任务
  getStudyTaskById(id){
    return request({
      url: '/task/find/'+id,
      method: 'get'
    })
  },
  // 根据id更新任务
  updateStudyTask(data,id){
    return request({
      url: '/task/update/'+id,
      method: 'put',
      data
    })
  },
  // 添加学习任务
  addStudyTask(data){
    return request({
      url: '/task/add',
      method: 'post',
      data
    })
  },
  // 回答学习任务
  answerStudyTask(data){
    return request({
      url: '/task/Finish',
      method: 'post',
      data
    })
  },
  // 根据任务id获取回答任务
  getAnswerTaskById(id){
    return request({
      url: '/task/Finish/find/'+id,
      method: 'get'
    })
  },
//   根据id删除学习任务/task/delete/{id}
  deleteStudyTask(id){
    return request({
      url: '/task/delete/'+id,
      method: 'get'
    })
  },
  // 根据任务id获取所有回答/task/finish/findall/taskid/{taskid}
  getAllAnswerTaskByTaskId(id){
    return request({
      url: '/task/finish/findall/taskid/'+id,
      method: 'get'
    })
  }

}