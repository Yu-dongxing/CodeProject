import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createPinia } from 'pinia'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import { permission, role } from './directives/permission'

const app = createApp(App)
const pinia = createPinia()

app.use(router)
   .use(ElementPlus, {
     locale: zhCn,
   })
   .use(pinia)
   .directive('permission', permission)
   .directive('role', role)
   .mount('#app')
