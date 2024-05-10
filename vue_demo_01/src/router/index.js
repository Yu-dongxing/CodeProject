// import { createApp } from 'vue'  
import { createRouter, createWebHistory } from 'vue-router'  
// import App from './App.vue'  
import About from '@/views/About'
import My from '@/views/My.vue'
import Phone from '@/views/Phone.vue'
import Not from '@/views/Not.vue'
  
// 假设你有一个路由配置数组  
const routes = [  
    // ... 定义你的路由，例如：  
    { path: '/', component: '/My' },  
    { path: '/About', component: About }, 
    { path: '/My', component: My }, 
    { path: '/Phone', component: Phone}, 
    { path: '/:catchAll(.*)', component: Not}
]  
  
// 创建路由实例  
const router = createRouter({  
    history: createWebHistory(), // 使用 HTML5 history 模式  
    routes, // 路由配置  
})  
  
// // 创建 Vue 应用实例  
// const app = createApp(App)  
  
// // 使用路由插件  
// app.use(router)  

export default router