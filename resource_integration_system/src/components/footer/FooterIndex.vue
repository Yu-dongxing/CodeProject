<template>
  <div class="footer">
    <div class="title">
      <el-text>
        <el-tag type="warning"> {{ bq.infoView ? bq.infoView : '2025 © YuDongXing'}}</el-tag>
      <br/>
      <!-- infoP https://beian.mps.gov.cn/#/query/webSearch?code=34170202000557-->
        <el-tag type="danger">
          <el-link :underline="false" :href="gwa.infoP ? gwa.infoP :'https://beian.mps.gov.cn/#/query/webSearch?code=34170202000557'" rel="noreferrer" target="_blank">
            <img src="../../assets/baanImg/baanIMG.png" style="width: 15px;height: 15px;">
            {{ gwa.infoView ? gwa.infoView : '皖公网安备34170202000557号'}}
          </el-link> 
          <span>&nbsp;·&nbsp;{{ icp.infoView ? icp.infoView : '皖ICP备2024037036号-2 ' }}</span>
        </el-tag>
      </el-text>
    </div>
  </div>
</template>

<script>
import {sysinfoApi} from '@/api/sys_info'
// 从package获取项目版本号
export default {
  name: 'FooterIndex',
  data () {
    return {
      version: process.env.VUE_APP_VERSION,
      icp:{},
      gwa:{},
      bq:{}
    }
  },
  methods: {
    // getICPBaAiInfo() 获取icp备案信息
    async getGWABaAiInfo() {
      const res = await sysinfoApi.getICPBaAiInfo()
      if(res.data){
        this.icp=res.data
      }else{
        this.icp={};
      }
      // console.log(res)
    },
    // getGWABaAiInfo() 获取公安备案信息
    async getICPBaAiInfo() {
      const res = await sysinfoApi.getGWABaAiInfo()
      if(res.data){
        this.gwa=res.data
      }else{
        this.gwa={};
      }
      // console.log(res)
    },
    // getSysCopyrightInfo() 获取系统版权信息
    async getSysCopyrightInfo() {
      const res = await sysinfoApi.getSysCopyrightInfo()
      if(res.data){
        this.bq=res.data
      }else{
        this.bq={};
      }
      // console.log(res)
    },
    getall(){
      this.getICPBaAiInfo()
      this.getGWABaAiInfo()
      this.getSysCopyrightInfo()
    }
  },
  mounted() {
    this.getall()
  },
  watch: {
    // 监听路由变化
    '$route'(to, from) {
      this.getall()
    }
  },
  created() {
    this.getall()
  }
}
</script>

<style lang="less" scoped>
//a链接，不显示下划线，不显示颜色
// a:link {
//     text-decoration: none;
// }
// a:visited {
//     text-decoration: none;
// }
// a:hover {
//     text-decoration: none;
// }
// a {
//     text-decoration: none;
// }
//底部版权栏目，使用绝对定位
.footer {
    height: auto(50px);
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    background-color: var(--bg-010);
    .title {
        text-align: center;
        font-size: 15px;
        line-height: 20px;
        color: var(--text-200);
        p{
          margin: 1px;
        }
    }
}
</style>
