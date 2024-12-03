<template>
  <div class="resources-page">
    <div class="page-header">
      <div class="header-left">
        <h2>电子资源库</h2>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/resources' }">全部文件</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div class="header-actions">
        <el-button type="primary" @click="uploadDialogVisible = true">
          <el-icon><Upload /></el-icon>上传资源
        </el-button>
        <el-button @click="folderDialogVisible = true">
          <el-icon><FolderAdd /></el-icon>新建文件夹
        </el-button>
      </div>
    </div>

    <el-card class="resource-container">
      <el-tabs v-model="activeView" class="resource-tabs">
        <el-tab-pane label="网格视图" name="grid">
          <el-row :gutter="20" class="resource-grid">
            <el-col :span="4" v-for="item in resources" :key="item.id">
              <div class="resource-item">
                <div class="resource-icon" :class="item.type">
                  <el-icon><component :is="getResourceIcon(item.type)" /></el-icon>
                </div>
                <div class="resource-info">
                  <div class="resource-name">{{ item.name }}</div>
                  <div class="resource-meta">{{ item.size }}</div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="列表视图" name="list">
          <el-table :data="resources" style="width: 100%">
            <el-table-column label="名称" min-width="200">
              <template #default="{ row: resource }">
                <div class="resource-name-cell">
                  <el-icon><component :is="getResourceIcon(resource.type)" /></el-icon>
                  <span>{{ resource.name }}</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="type" label="类型" width="100" />
            <el-table-column prop="size" label="大小" width="100" />
            <el-table-column prop="updateTime" label="修改时间" width="180" />
            <el-table-column label="操作" width="150" fixed="right">
              <template #default="{ row: resource }">
                <el-button link type="primary" @click="console.log('下载:', resource)">下载</el-button>
                <el-button link type="primary" @click="console.log('预览:', resource)">预览</el-button>
                <el-button link type="danger" @click="console.log('删除:', resource)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-card>

    <!-- 上传对话框 -->
    <el-dialog v-model="uploadDialogVisible" title="上传资源" width="500px">
      <el-upload
        class="resource-upload"
        drag
        action="/api/upload"
        multiple
      >
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">
          将文件拖到此处，或<em>点击上传</em>
        </div>
        <template #tip>
          <div class="el-upload__tip">
            支持各种格式的文档、图片、视频等文件
          </div>
        </template>
      </el-upload>
    </el-dialog>

    <!-- 新建文件夹对话框 -->
    <el-dialog v-model="folderDialogVisible" title="新建文件夹" width="400px">
      <el-form :model="folderForm" label-width="80px">
        <el-form-item label="文件夹名">
          <el-input v-model="folderForm.name" placeholder="请输入文件夹名称" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="folderDialogVisible = false">取消</el-button>
          <el-button type="primary" @click="createFolder">
            确认
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'ResourcePage'
}
</script>

<script setup>
import { ref } from 'vue'
import {
  Document,
  FolderOpened,
  Picture,
  VideoCamera,
  Upload,
  FolderAdd,
  UploadFilled
} from '@element-plus/icons-vue'

const activeView = ref('grid')
const uploadDialogVisible = ref(false)
const folderDialogVisible = ref(false)
const folderForm = ref({ name: '' })

// 模拟资源数据
const resources = ref([
  {
    id: 1,
    name: '课程文档.pdf',
    type: 'document',
    size: '2.5MB',
    updateTime: '2024-03-20 15:30'
  },
  {
    id: 2,
    name: '教学视频',
    type: 'folder',
    size: '--',
    updateTime: '2024-03-19 10:00'
  },
  {
    id: 3,
    name: 'Vue基础教程.mp4',
    type: 'video',
    size: '156MB',
    updateTime: '2024-03-18 14:20'
  },
  {
    id: 4,
    name: '课程截图.png',
    type: 'image',
    size: '1.2MB',
    updateTime: '2024-03-17 09:45'
  }
])

const getResourceIcon = (type) => {
  const icons = {
    document: Document,
    folder: FolderOpened,
    image: Picture,
    video: VideoCamera
  }
  return icons[type] || Document
}

const createFolder = () => {
  if (folderForm.value.name) {
    resources.value.push({
      id: Date.now(),
      name: folderForm.value.name,
      type: 'folder',
      size: '--',
      updateTime: new Date().toLocaleString()
    })
    folderDialogVisible.value = false
    folderForm.value.name = ''
  }
}
</script>

<style scoped>
.resources-page {
  padding: 24px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 24px;
}

.header-left h2 {
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.resource-container {
  background: white;
  border-radius: 8px;
}

.resource-tabs {
  padding: 20px;
}

.resource-grid {
  margin-top: 20px;
}

.resource-item {
  padding: 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  text-align: center;
}

.resource-item:hover {
  background-color: #f5f7fa;
}

.resource-icon {
  width: 60px;
  height: 60px;
  margin: 0 auto 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
}

.resource-icon .el-icon {
  font-size: 24px;
  color: white;
}

.resource-icon.document { background: linear-gradient(135deg, #1890ff 0%, #36cfc9 100%); }
.resource-icon.folder { background: linear-gradient(135deg, #faad14 0%, #ffc53d 100%); }
.resource-icon.image { background: linear-gradient(135deg, #52c41a 0%, #73d13d 100%); }
.resource-icon.video { background: linear-gradient(135deg, #722ed1 0%, #b37feb 100%); }

.resource-info {
  margin-top: 8px;
}

.resource-name {
  font-size: 14px;
  color: #1a1a1a;
  margin-bottom: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.resource-meta {
  font-size: 12px;
  color: #8c8c8c;
}

.resource-name-cell {
  display: flex;
  align-items: center;
  gap: 8px;
}

.resource-name-cell .el-icon {
  font-size: 18px;
  color: #8c8c8c;
}

.resource-upload {
  width: 100%;
}

:deep(.el-upload-dragger) {
  width: 100%;
}

:deep(.el-upload__tip) {
  margin-top: 12px;
  text-align: center;
}

/* 添加面包屑导航样式 */
.el-breadcrumb {
  margin-left: 16px;
  line-height: 1;
}

:deep(.el-breadcrumb__item) {
  display: inline-flex;
  align-items: center;
}

:deep(.el-breadcrumb__inner) {
  color: #606266;
  cursor: pointer;
}

:deep(.el-breadcrumb__inner:hover) {
  color: #409EFF;
}

:deep(.el-breadcrumb__item:last-child .el-breadcrumb__inner) {
  color: #303133;
  cursor: default;
}

:deep(.el-breadcrumb__item:last-child .el-breadcrumb__inner:hover) {
  color: #303133;
}
</style> 