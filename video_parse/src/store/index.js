import { createApp } from 'vue'
import App from '@/App.vue'
import  vuex  from 'vuex'

const app = createApp(App)  

app.use(vuex)  

const store = new vuex.Store({
    state:{
        title:"视频解析系统",
        voide:[
            {id:1,title:"yuxs"},
            {id:2,title:"yuxs"},
        ]
    }
})

export default store