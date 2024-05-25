import { createRouter, createWebHistory } from 'vue-router'  
import MainVoide from '@/views/MainVoide.vue'
import VoidePlay from '@/views/VoidePlay.vue'
import MainAbout from '@/views/about/MainAbout.vue'
import MainVlog from '@/views/vlog/MainVlog'
import MainPhone from '@/views/Phone/MainPhone'
const routes = [  
    //默认路由
    {
        path:'/',
        // component:'/voide_id_1/'
        redirect:'/voide_id_1/',
    },
    //一级首页路由
    {
        path: '/voide_id_:page_id/',
        component:MainVoide,
        //首页二级路由
        children:[
            //视频播放路由
            // {
            //     name:'VoidePlay',
            //     path: '/voide_id_:page_id/VoidePlay' ,
            //     component:VoidePlay
            // },
        ]
    }, 
    //视频播放路由
    {
        name:'VoidePlay',
        path: '/voide_id_:page_id/VoidePlay' ,
        component:VoidePlay
    },
    //一级关于路由
    {
        path:'/MainAbout',
        component:MainAbout
    },
    //一级日志路由
    {
        path:'/MainVlog',
        component:MainVlog
    },
    //一级联系路由
    {
        path:'/MainPhone',
        component:MainPhone
    },
    
]  

// 创建路由实例  
const router = createRouter({  
    history: createWebHistory(), // 使用 HTML5 history 模式  
    routes, // 路由配置  
})  
export default router