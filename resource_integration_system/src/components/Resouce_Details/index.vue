<template>
  <div class="details">
    <el-card shadow="hover" class="ccard display-center margin-top-10 title" >{{resource.name}}</el-card>
    <el-card shadow="hover" class="ccard display-center" v-if="resource.url !=''">
      <el-button tag="a" :href="this.resource.url" target="_blank" size="large" type="success">点击跳转<el-icon><CircleCheckFilled /></el-icon></el-button>
    </el-card>
    <el-card shadow="hover" class="ccard" >
      <!-- v-if="this.getWebsiteInfo(this.resource.url)" -->
      <template #header>
        <div class="card-header card-header">
          <el-icon  color="#409eff"><QuestionFilled /></el-icon>
          <el-text type="primary" size="large">资源说明</el-text>
        </div>
      </template>
      <div v-html="resource.desc"></div>
    </el-card>
    <el-card shadow="hover" class="ccard" v-if="resource.tab !='文件'">
      <!-- v-if="this.getWebsiteInfo(this.resource.url)" -->
      <template #header>
        <div class="card-header card-header">
          <el-icon color="#409eff"><Document /></el-icon>
          <el-text type="primary" size="large">资源详情</el-text>
        </div>
      </template>
      <el-text>网站标题：{{ url_info.title }}</el-text>
      <el-divider />
      <el-text>网站介绍：{{ url_info.description }}</el-text>
    </el-card>
    <el-card shadow="hover" class="ccard" v-if="resource.tab =='文件'">
      <template #header>
        <div class="card-header card-header">
          <el-icon color="#409eff"><FolderOpened /></el-icon>
          <el-text type="primary" size="large">资源文件列表</el-text>
        </div>
      </template>
      <div class="file">
        <el-tag size="large" v-for="file in resource.fileData" :key="file.id" class="file-item display-1" type="success" >
          <div class="item-m display-x-center">
            <el-icon><Document /></el-icon>
            <el-link type="success" :href="file.fileUrl" target="_blank">{{ file.fileName }}</el-link>
          </div>
        </el-tag>


        <!-- <el-alert v-for="file in this.resource.fileData" :key="file.id" :title="file.fileName" class="file-item" type="success" :closable="false" show-icon> -->
          <!-- <el-icon><Document /></el-icon> -->
        <!-- </el-alert> -->

        <!-- <el-alert v-for="file in this.resource.fileData" :key="file.id" :title="file.fileName" class="file-item" type="success" :closable="false" show-icon>
          <el-icon><Document /></el-icon>
          <el-button @click="downloadFile(file)" type="primary" size="small">下载</el-button>
        </el-alert> -->
        <!-- 文件展示 -->
      </div>
    </el-card>
    <el-card shadow="hover" class="ccard">
      <template #header>
        <div class="card-header card-header">
          <el-icon color="#409eff"><InfoFilled /></el-icon>
          <el-text type="primary" size="large">资源创建信息</el-text>
        </div>
      </template>
      <el-text>资源创建作者：{{ this.resource.author }}</el-text>
      <el-divider />
      <el-text>资源更新时间：{{ this.resource.updateTime }}</el-text>
      <el-divider />
      <el-text>资源创建时间：{{ this.resource.createTime }}</el-text>
    </el-card>
    
  </div>
</template>

<script>
import { resourceApi } from '@/api/resource'
export default {
  name:'resouce_detail',
  data(){
    return{
      // resouceId:'',
      resource:{},
      url_info:{}
    }
  },
  methods:{
    // 根据id获取资源库详情getResourceById(id)
    async getResourceById(id){
      try{
        const res = await resourceApi.getResourceById(id);
        if(res.code === 400){
          this.$router.push('/201');
          console.log(res);
        }else{
          this.resource = res.data;
          console.log(res);
          this.getWebsiteInfo(this.resource.url);
        }
        
      }catch(err){
        console.log(err);
      }
      
    },
    extractDomainurl(url) {
        // 使用URL构造函数解析URL
        const parsedUrl = new URL(url);
        // 返回域名
        return parsedUrl.hostname;
      },
      // 获取网站详细信息 https://api.ahfi.cn/api/websiteinfo?url=
      async getWebsiteInfo(url) {
        if(this.resource.tab =='文件'){
          console.log("不执行");
        }else{
          try {
            const response = await fetch(`https://api.ahfi.cn/api/websiteinfo?url=${url}`);
            const data = await response.json();
            this.url_info=data.data;
            console.log(data.data);
            return true;
            // 处理数据
          } catch (error) {
            console.error(error);
            return false;
          }
        }
      }

  },
  created() {
    // this.resouceId = this.$route.query.id; // 从路由的 query 中获取id
    this.getResourceById(this.$route.query.id);
    
  }
}
</script>

<style lang="less" scoped>
.margin-top-10{
  margin-top: 10px;
}
.title{
  font-size: large;
  font-weight: bold;
  color: var(--text-200);
}
.icon-q{
  color: var(--el-text-color);
}
.display-center{
  display: flex;
  justify-content: center;
  align-items: center;
}
.display-x-center{
    display: flex;
    align-items: center;
}
.file{
  display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.file-item{
  margin-top: 5px;
  margin-bottom: 5px;
}
.display-inline{
  // display: inline;
}
.details{
  // display: grid;
  // grid-template-columns: repeat(3, 1fr);
  // grid-gap: 10px;
}
.ccard{
  border-radius:15px ;
  margin-bottom: 10px;
  // aspect-ratio: 16/9;
}
.card-header{
  display: flex;
  align-items: center;
  color: var(--el-text-color);
}
</style>