import { createRouter, createWebHistory } from 'vue-router'
// import App from '../App.vue'
import MainIndex from '@/components/main/MainIndex.vue'
import store from '@/store'

const routes = [
  {
    path:'/',
    name:'MainIndex',
    component: MainIndex,
    //子路由-view/index
    // children:[
    //   {
    //     path:'main',
    //     name:'MainIndex',
    //     component: MainIndex
    //   }
    // ]
  },
  {
    path:'/about',
    name:'About',
    component: () => import('@/components/updataPage/updata.vue'),
  },
  {
    path:'/login',
    name:'Login',
    component: () => import('@/components/Login/login.vue'),
  },
  {
    // D:\c++ding ming\resource_integration_system\src\views\study.vue
    path:'/study',
    name:'study',
    component: ()=>import('@/views/study.vue'),
    meta: { requiresAuth: true }
  },
  {
    path:'/StudyDetails',
    name:'StudyDetails',
    component: ()=>import('@/components/Study_Details/index.vue'),
  },
  {
    path:'/add',
    name:'AddResouce',
    component: ()=>import('@/components/AddResouce/index.vue'),
    // meta: { requiresAuth: true }
  },
  {
    path:'/user',
    name:'UserControl',
    component:()=>import('@/views/userControl.vue'),
    meta: { requiresAuth: true }
  },
  // 添加 资源文件类型添加页面
  {
    path:'/addresourcefile',
    name:'AddResourceFile',
    component:()=>import('@/components/AddFileResource/index.vue'),
    meta: { requiresAuth: true }
  },
  // 添加资源搜索页面路由
  {
    path:'/search',
    name:'resouce_search',
    component:()=>import('@/components/resouce_search/index.vue'),
  },
  // 添加资源详情页面
  {
    path:'/detail',
    name:'resouce_detail',
    component:()=>import('@/components/Resouce_Details/index.vue'),
  },
   // 添加 404 错误页面路由
  {
    path: '/:pathMatch(.*)*',
    name: 'Err404',
    component: ()=>import('@/components/Err404/index.vue') 
  },
  //
  {
    path:'/500',
    name:'Err500',
    component:()=>import('@/components/Err500/index.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  const token = store.state.user.token
  
  if (to.meta.requiresAuth) {
    if (!token) {
      next('/login')
      return
    }
    
    if (!store.state.user.userInfo) {
      try {
        await store.dispatch('user/getUserInfo')
      } catch (error) {
        store.dispatch('user/logout')
        next('/login')
        return
      }
    }
  }
  
  if (to.path === '/login' && token) {
    next('/')
    return
  }
  
  next()
})

export default router
