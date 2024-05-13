import { createRouter, createWebHistory } from 'vue-router'  
import Video from '@/views/MainVoide.vue'
import MainComp from '@/views/MainComp.vue'
const routes = [  
    { path: '/', component: Video },  
    // {name: 'Voide',path:'/voide',component: Video},
    {path:'/:page_id',component: Video},
    {name:'MainComp',path: '/:page_id/MainComp' ,component: MainComp}
    
]  

// 创建路由实例  
const router = createRouter({  
    history: createWebHistory(), // 使用 HTML5 history 模式  
    routes, // 路由配置  
})  
export default router