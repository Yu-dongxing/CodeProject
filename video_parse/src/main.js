import { createApp } from 'vue'
import App from './App.vue'
import Router from './router/index.js'
import Store from './store/index.js'

const app = createApp(App)  
// 使用路由插件  
app.use(Router)  
app.use(Store)
  
// 注册全局组件  
// app.component('BaseA', BaseA)  
  
// 挂载应用  
app.mount('#app')