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
  },
  // 文件分片上传
  mergeFileChunks(file,chunkNumber,totalChunks, fileMd5, fileName, fileAssociationId) {
    const formData = new FormData();
    
    formData.append('totalChunks', totalChunks);
    formData.append('fileMd5', fileMd5);
    formData.append('fileName', fileName);
    formData.append('FileAssociationId', fileAssociationId);
    formData.append("file", file);
    formData.append("chunkNumber", chunkNumber);

    return request({
      url: '/file/upload/chunk',
      method: 'post',
      data: formData
    })
  },
  //文件分片上传完成通知
  megerFileChunksSuccess(totalChunks,fileMd5,fileName,FileAssociationId){
    const data = new FormData();
    data.append('totalChunks', totalChunks);
    data.append('fileMd5', fileMd5);
    data.append('fileName', fileName);
    data.append('FileAssociationId', FileAssociationId);
    return request({
      url: '/file/upload/chunk/merge',
      method: 'post',
      data: data
    })
  }
}