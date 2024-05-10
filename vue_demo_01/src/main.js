import { createApp } from 'vue'   
import App from './App.vue'  
import BaseA from './components/BaseA.vue' 
import Router from './router/index.js'


// import { createRouter, createWebHistory } from 'vue-router'  
// // 假设你有一个路由配置数组  
// const routes = [  
//     // ... 定义你的路由，例如：  
//     // { path: '/', component: App },  
//     { path: '/About', component: About }, 
//     { path: '/My', component: My }, 
//     { path: '/Phone', component: Phone}, 
// ]  
// // 创建路由实例  
// const router = createRouter({  
//     history: createWebHistory(), // 使用 HTML5 history 模式  
//     routes, // 路由配置  
// })  
// 创建 Vue 应用实例  


const app = createApp(App)  
  
// 使用路由插件  
app.use(Router)  
  
// 注册全局组件  
app.component('BaseA', BaseA)  
  
// 挂载应用  
app.mount('#app')
