// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'
// import store from './store'
// import ElementPlus from 'element-plus';
// import 'element-plus/dist/index.css';

// createApp(App).use(store).use(router).use(ElementPlus).mount('#app')
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
// import UUID from "vue-uuid"; // 引入uuid
// import { v4 as uuidv4 } from 'uuid';

// 导入所有 Element Plus 图标
import * as Icons from '@element-plus/icons-vue';

const app = createApp(App);

// 全局注册所有图标
Object.keys(Icons).forEach((key) => {
  app.component(key, Icons[key]);
});
// .app.use(uuidv4)
app.use(store).use(router).use(ElementPlus).mount('#app');