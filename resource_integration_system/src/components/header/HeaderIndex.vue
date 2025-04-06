<!-- header -->
<template>
  <div class="header">
    <div class="header-left">
      <div class="logo">
      </div>
      <router-link to="/" class="title no-link-style">资源库</router-link>
    </div>
    <div class="header-search">
      <el-input
      v-model="search_keyword"
      style="max-width: 600px"
      placeholder="请输入关键字"
      class="input-with-select"
    >
      <template #append>
        <el-button @click="search()">
          <el-icon>
                <search/>
            </el-icon>
        </el-button>
      </template>
      <!-- <template #prepend>
        <el-select v-model="search_select" placeholder="选择" style="width: 115px">
          <el-option label="Restaurant" value="1" />
          <el-option label="Order No." value="2" />
          <el-option label="Tel" value="3" />
        </el-select>
      </template> -->
    </el-input>
    </div>
    <!-- 网页端链接 -->
    <div class="header-right">
      <!-- v-if="userInfo?.roleName == 'admin' || userInfo?.roleName == 'student'" -->
      <router-link to="/study" class="right-item no-link-style" >
        <el-icon><DataBoard /></el-icon>
        <span>学习任务</span>
      </router-link>
      <router-link to="/add" class="right-item no-link-style">
        <!-- <img src="@/assets/header-right/up2.svg" alt=""> -->
        <el-icon><UploadFilled /></el-icon>
        <span>添加资源</span>
      </router-link>
      <router-link to="/about" class="right-item no-link-style">
        <!-- <img src="@/assets/UpdateLog/log.svg" alt=""> -->
        <el-icon><MoreFilled /></el-icon>
        <span>更新日志</span>
      </router-link>
      <router-link to="/user" class="right-item no-link-style">
        <!-- <img src="@/assets/user/header-user.svg" alt=""> -->
        <el-icon><User /></el-icon>
        <span class="item-t">用户</span>
      </router-link>
    </div>
    <!-- 手机端链接 -->
    <div class="header-right-app">
      <el-dropdown trigger="click">
        <span class="header-right-app-ii">
          <!-- <img src="@/assets/header-right/list.svg" alt=""> -->
          <el-icon :size="20"><Expand /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item v-for="(item,index) in header_link" :key="index">
               <!-- 动态绑定图标 -->
              <el-icon>
                <component :is="item.icon" />
              </el-icon>
              <!-- <el-icon><House /></el-icon> -->
              <router-link :to="item.link" class="no-link-style" style="width: 100%;">{{ item.title }}</router-link>
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
// import  useStore  from '@/store/index'
import { useStore } from 'vuex'
import { computed } from 'vue'
export default {
  name: 'HeaderIndex',
  data() {
    return {
      header_link:[
      {id:1,icon:"HomeFilled",link:'/',title:'首页'},
      {id:2,icon:"Link",link:'/add',title:'添加资源'},
      {id:3,icon:"Notification",link:'/about',title:'更新日志'},
      {id:4,icon:"User",link:'/user',title:'用户'},
      {id:5,icon:"DataBoard",link:'/study',title:'学习任务'}
    ],
    search_keyword:'',
    search_select:['标签','标题'],
    userInfo:{}
    }
  },
  computed: {
    // userInfo() {
    //   // const store = useStore()
    //   console.log(useStore().state.user);
    //   return useStore().state.user.userInfo
    
    //   // const userInfo = useStore
      
    // }
  },
  setup() {
    const store = useStore()
    const userInfo = computed(() => store.state.user.userInfo)
    console.log(userInfo);
    return {
      userInfo,
    }
  },
  methods: {
    search(){
      this.$router.push({ path: '/search', query: { keyword: this.search_keyword } });
    },
    getUserInfo(){
      const us  = JSON.parse(localStorage.getItem('userInfo'))
      if(us){
        this.userInfo = us
        console.log(this.userInfo);
      }else{
        this.userInfo = {}
      }
      
    }
  },
  created(){
    // this.getUserInfo()
  }
}
</script>

<style scoped lang="less">
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 45px;
  background-color: var(--bg-200);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
}
.header-search{
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo img {
  height: 40px;
  margin-right: 10px;
}

.title {
  font-size: 18px;
  font-weight: bold;
  line-height: 60px;
}

.header-right {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  // border: 1px solid red;
  .right-item {
    box-sizing: border-box;
    padding: 5px;
    width: auto;
    height: 40px;
    // background-color: red;
    border-bottom: #42b983 solid 1px;
    margin-right: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    // border-radius: var(--border-radius-de);
    border-radius: 5px;
    img{
      width: 30px;
      height: 30px;
    }
    span{
      margin-left: 5px;
      font-weight: bold;
      line-height: 40px;
      // display: none;
    }
    .item-t{

    }
  }
  .right-item:hover{
    background-color: var(--primary-200);
    //点击切换鼠标
    cursor: pointer;
  }
}
.header-right-app{
  width: 40px;
  height: 40px;
  background-color: var(--primary-100);
  border-radius: var(--border-radius-de);
  display: flex;
  justify-content: center;
  align-items: center;
  // margin-right: -20px;
  img{
    width: 40px;
    height: 40px;
  }
}
.header-right-app:focus{
  background-color: var(--primary-200);
}
.about {
  margin-right: 20px;
}
.username {
  margin-right: 20px;
}

.logout {
  cursor: pointer;
  color: #666;
}

.logout:hover {
  color: #42b983;
}
/* 当屏幕宽度小于500px */
@media screen and (max-width: 600px) {
  .logo,.header-right,.header-search{
    display: none;
  }
}
/* 当屏幕宽度大于500px */
@media screen and (min-width: 500px) {
  .header-right-app{
    display: none;
  }
}

</style>
