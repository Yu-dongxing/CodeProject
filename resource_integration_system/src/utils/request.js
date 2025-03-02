import axios from 'axios'
import { ElMessage } from 'element-plus'
import store from '@/store'
import router from '@/router'

// 创建axios实例
const request = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: 500000 // 请求超时时间
})

// 请求拦截器
request.interceptors.request.use(
  config => {
    const token = store.state.user.token
    if (token) {
      // 根据实际需求修改header格式
       config.headers.Authorization = `Bearer ${encodeURIComponent(token)}`
    }
    return config
  },
  error => {
    console.error('请求错误:', error) 
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  response => {
    const res = response.data
    console.log('响应数据:', res) // 添加调试日志
    
    // 这里可以根据后端的响应结构统一处理
    if (res.code === 101) {
      // token过期
      store.dispatch('user/logout')
      router.push('/login')
      ElMessage.error('登录已过期，请重新登录')
      return Promise.reject(new Error('登录已过期'))
    }
    return res
  },
  error => {
    console.error('响应错误:', error)
    ElMessage({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    router.push('/500')
    return Promise.reject(error)
  }
)

export default request 