// /file/find/uuid/{fileuuid}

import request from '@/utils/request'

// 文件相关接口
export const FileApi = {
  // 根据uuid查询文件
  findFileByUuid(FileUuid) {
    return request({
      url: '/file/find/uuid/'+FileUuid,
      method: 'get'
    })
  },
}