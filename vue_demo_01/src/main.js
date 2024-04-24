// import { createApp } from 'vue'
// // import { createApp, VueElement } from 'vue'
// import App from './App.vue'
// import BaseA from './components/BaseA.vue'

// createApp(App).mount('#app')

// App.component('BaseA',BaseA)
import { createApp } from 'vue'  
import App from './App.vue'  
import BaseA from './components/BaseA.vue'  
  
const app = createApp(App)  
  
// 注册全局组件  
app.component('BaseA', BaseA)  
  
// 挂载应用  
app.mount('#app')
