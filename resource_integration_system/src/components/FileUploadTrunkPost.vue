<template>
    <div>
      <input type="file" ref="fileInput" @change="handleFileSelect" />
      <button :disabled="isUploading" @click="uploadFile">
        {{ isUploading ? '上传中...' : '上传文件' }}
      </button>
      <div v-if="message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  import SparkMD5 from 'spark-md5'
  import axios from 'axios'
  
  export default {
    name: 'FileUploader',
    data() {
      return {
        selectedFile: null,
        isUploading: false,
        message: ''
      }
    },
    methods: {
      handleFileSelect(event) {
        this.selectedFile = event.target.files[0]
      },
  
      async calculateFileMD5(file) {
        return new Promise((resolve, reject) => {
          const chunkSize = 2 * 1024 * 1024
          const spark = new SparkMD5.ArrayBuffer()
          const fileReader = new FileReader()
          let currentChunk = 0
          const chunks = Math.ceil(file.size / chunkSize)
  
          function loadNext() {
            const start = currentChunk * chunkSize
            const end = start + chunkSize >= file.size ? file.size : start + chunkSize
            fileReader.readAsArrayBuffer(file.slice(start, end))
          }
  
          fileReader.onload = e => {
            spark.append(e.target.result)
            currentChunk++
            currentChunk < chunks ? loadNext() : resolve(spark.end())
          }
  
          fileReader.onerror = reject
          loadNext()
        })
      },
  
      async uploadChunk(chunk, chunkNumber, totalChunks, identifier) {
        const formData = new FormData()
        formData.append('file', chunk)
        formData.append('chunkNumber', chunkNumber.toString())
        formData.append('totalChunks', totalChunks.toString())
        formData.append('identifier', identifier)
  
        return axios.post('/api/upload/chunk', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
      },
  
      async mergeFile(identifier, fileName, totalChunks) {
        const params = new URLSearchParams()
        params.append('identifier', identifier)
        params.append('fileName', fileName)
        params.append('totalChunks', totalChunks.toString())
  
        return axios.post('/api/upload/merge', params, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
      },
  
      async uploadFile() {
        if (!this.selectedFile) {
          this.message = '请选择文件'
          return
        }
  
        try {
          this.isUploading = true
          this.message = '开始处理文件...'
  
          const identifier = await this.calculateFileMD5(this.selectedFile)
          const chunkSize = 2 * 1024 * 1024
          const totalChunks = Math.ceil(this.selectedFile.size / chunkSize)
          
          this.message = '开始上传分片...'
          const uploadTasks = []
          
          for (let i = 0; i < totalChunks; i++) {
            const chunkNumber = i + 1
            const start = i * chunkSize
            const end = Math.min(start + chunkSize, this.selectedFile.size)
            const chunk = this.selectedFile.slice(start, end)
            
            uploadTasks.push(
              this.uploadChunk(chunk, chunkNumber, totalChunks, identifier)
                .then(() => {
                  this.message = `分片 ${chunkNumber}/${totalChunks} 上传完成`
                })
            )
          }
  
          await Promise.all(uploadTasks)
          this.message = '所有分片上传完成，开始合并...'
  
          await this.mergeFile(identifier, this.selectedFile.name, totalChunks)
          this.message = '文件上传并合并成功！'
          this.$emit('upload-success')
        } catch (error) {
          console.error('上传失败:', error)
          this.message = `上传失败: ${error.message}`
          this.$emit('upload-error', error)
        } finally {
          this.isUploading = false
        }
      }
    }
  }
  </script>