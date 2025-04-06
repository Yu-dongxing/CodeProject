<template>
    <div id="index" >
      <HeaderIndex/>
      <el-scrollbar height="calc(100vh - 110px)" class="MAIN">
        <div class="search_App">
        <Search_App/>
        </div>
          <router-view></router-view> <!-- 使用Vue Router的router-view组件，用于展示当前路由对应的组件内容 -->
      </el-scrollbar>
      <FooterIndex/>
    </div>
  </template>
  
  <script>
  import HeaderIndex from './components/header/HeaderIndex.vue'
  import FooterIndex from './components/footer/FooterIndex.vue'
  import Search_App from '@/components/Search_App/index.vue'
  import axios from 'axios';
  import { iplogApi } from '@/api/ip_log'
  import {sysinfoApi} from '@/api/sys_info'
  export default {
    name: 'index',
    data(){
      return {
        userIp:'',
        ip_access_log:{
          ipAddress: "",//地址
          ipCity: "",//城市
          ipProvince: "",//省份
          ipUserDevice: "",//用户设备
          ipUserAgent: ""//用户代理
        }
      }
    },
    methods:{
      // 获取IP地址api
      getUserInfo() {
        axios.get('https://ip.011102.xyz')
          .then(response => {
            console.log(response.data);
            const ipData = response.data.IP;
            const headers = response.data.Headers;
            const security = response.data.Security;
  
            this.ip_access_log.ipAddress = ipData.IP;
            this.ip_access_log.ipCity = ipData.City;
            this.ip_access_log.ipProvince = ipData.Region;
            this.ip_access_log.ipUserDevice = headers['sec-ch-ua-platform'] || 'Unknown';
            this.ip_access_log.ipUserAgent = headers['user-agent'];
            this.onSubmit(this.ip_access_log);
          })
          .catch(error => {
            console.error('Failed to fetch IP:', error);
          });
      },
      // 上传日志api-postLog(data)
      async onSubmit(data) {
          try {
            const res = await iplogApi.postIpLog(data)
            // console.log("上传成功",res);
          } catch (error) {
            // console.error('上传失败:', error)
          }
        },
        // 获取系统欢迎信息
        async getSysWelcomeInfo() {
          try {
            const res = await sysinfoApi.getSysWelcomeInfo();
            console.log("系统欢迎信息",res);
            this.$notify({
              title: res.data.infoView,
              dangerouslyUseHTMLString: true,
              message: res.data.infoDesc,
              type: 'success',
            });
          } catch (error) {
            console.log(error);
          }
        },
      open1() {
        const less = "https://github.com/Yu-dongxing/ResourceLibrarySystem-Vue/issues"
        this.$notify({
          title: '欢迎访问资源库系统！',
          dangerouslyUseHTMLString: true,
          message: '本系统为个人学习项目，数据来源于网络搜集，如有侵权，请联系删除<br>如出现问题请跳转<a href="'+less+'" target="_blank"><button>反馈</button></a>页面',
          type: 'success',
        });
      },
    },
    // watch:{
    //   userIp(newVal,oldVal){
    //     if(newVal !== oldVal){
          
    //     }
    //   }
    // },
    components: {
      HeaderIndex,
      FooterIndex,
      Search_App
    },
    beforeCreate() {
      // console.log('创建前')
    },
    created() {
      // console.log('创建后')
      this.getUserInfo()
      this.getSysWelcomeInfo()
    }
  
  }
  </script>
  
  <style>
  .search_App{
      display: none;
  }
  #app {
      font-family: var(--el-font-family);
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      margin: 0;
      padding: 0;
      --border-radius-de: 10px;
      --border-radius-min: 15px;
      --border-radius-max: 20px;
      --box-shadow-de: 0 2px 4px rgba(0, 0, 0, .1);
      transition: all 3s ease;
      
  }
  /* 取消 router-link 的点击文字效果 */
  .no-link-style {
    text-decoration: none; /* 取消下划线 */
    color: inherit; /* 继承父元素的颜色 */
    cursor: pointer; /* 鼠标悬停时显示指针 */
  }
  
  /* 可选：取消 hover 时的样式 */
  .no-link-style:hover {
    text-decoration: none;
    color: inherit;
  }
  .MAIN{
      transition: all 3s ease;
      margin-top: 0px;
      box-sizing: border-box;
      padding: 5px;
      /* height: calc(100vh - 70px - 40px - 10px); */
      width: 100%;
      background-color: var(--bg-100);
      /* overflow: auto; */
      border-radius: 10px;
  }
  /* 当屏幕宽度小于500px */
  @media screen and (max-width: 600px) {
    .search_App{
      display: block;
    }
  }
  </style>
  