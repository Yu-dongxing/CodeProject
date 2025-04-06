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
  // 根据文件id删除文件/ftp/delete
  deleteFileById(FileId) {
    return request({
      url: '/file/delete/'+FileId,
      method: 'delete'
    })
  }
}