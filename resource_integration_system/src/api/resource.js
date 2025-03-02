import request from '@/utils/request'

// 资源相关接口
export const resourceApi = {
  // 获取资源列表
  getResources() {
    return request({
      url: '/public/get/resourcefile',
      method: 'get'
    })
  },

  // 添加资源
  addResource(data) {
    return request({
      url: '/public/add',
      method: 'post',
      data
    })
  },

  // 根据id删除资源
  deleteResource(id) {
    return request({
      url: `/admin/delete/${id}`,
      method: 'get'
    })
  },

  // 更新资源
  updateResource(data,id) {
    return request({
      url: '/admin/update/'+id,
      method: 'put',
      data:{
        name: data.name,
        url: data.url,
        tab: data.tab,
        img: data.img,
        desc:data.desc,
      }
    })
  },
  // 根据id获取资源/public/get/{id}  /public/get/resourcefile/{id}
  getResourceById(id) {
    return request({
      url: '/public/get/resourcefile/'+id,
      method: 'get'
    })
  },
  // 关键字搜索/public/search/keyword?keyword=UI
  searchResource(keyword) {
    return request({
      url: '/public/search/keyword?keyword='+keyword,
      method: 'get'
    })
  },
  // 根据id审核资源库
  ResourceAuditById(id) {
  return request({
    url: '/admin/audit/'+id,
    method: 'put'
  })
  },
  // 查询待审核资源
  ResourceAudit(){
    return request({
      url: '/admin/audit/',
      method: 'get'
    })
  },
// 提交资源文件
  submitResourceFile(resourceData) {
    const formData = new FormData();
    
    // 如果有多个文件，需要逐个添加到FormData中
    if (Array.isArray(resourceData.files)) {
      resourceData.files.forEach((file, index) => {
        formData.append(`files`, file); // 为每个文件添加到FormData
      });
    } else {
      // 如果只有一个文件，直接添加
      formData.append('files', resourceData.files);
    }

    // 添加资源数据
    formData.append('resourceData', JSON.stringify(resourceData.resourceData));

    return request({
      url: '/admin/add',
      method: 'post',
      data: formData, // 提交的表单数据
    });
  },
  // 
  // 提交文件资源中的资源数据
  submitResourceData(resourceData) {
    return request({
      url: '/admin/add/new',
      method: 'post',
      data: resourceData
    })
  },
  // 提交文件资源中的文件数据
  submitResourceFiles(files,resourceUUID) {
    const formData = new FormData();
    // 如果有多个文件，需要逐个添加到FormData中
    if (Array.isArray(files)) {
      files.forEach((file, index) => {
        formData.append(`files`, file); // 为每个文件添加到FormData
      });
    } else {
      // 如果只有一个文件，直接添加
      formData.append('files', files);
    }
    return request({
      url: '/admin/add/new/files/'+resourceUUID,
      method: 'post',
      data: formData
    })
  },
  // 获取资源文件列表
  getResourceFiles(fileid) {
    return request({
      url: '/public/get/resourcefile/'+id,
      method: 'get'
    })
  },
  // 根据id删除资源文件/ftp/delete
  deleteResourceFile(id) {
    return request({
      url: '/ftp/delete?fileId='+id,
      method: 'delete'
    })
  }

} 