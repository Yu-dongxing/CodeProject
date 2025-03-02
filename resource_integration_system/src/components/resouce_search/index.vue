<template>
  <div  v-loading="isLoading">
    <div class="search">
      <el-table :data="resouce_data"  style="width: 100%">
        <el-table-column prop="name" label="资源名称" width="180" />
        <el-table-column prop="author" label="作者" width="180" />
        <el-table-column prop="img" label="资源图片">
          <template #default="scope">
            <!-- <el-link :href="scope.row.img" target="_blank">
                <el-button>点击跳转</el-button>
            </el-link> -->
            <el-image :src="scope.row.img" fit="cover" style="width: 100px; height: 100px"></el-image>
          </template>
        </el-table-column>

        <el-table-column prop="tab" label="资源标签" >
          <template #default="scope">
                <el-tag>{{ scope.row.tab }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="url" label="资源地址" >
          <template #default="scope">
            <el-link :href="scope.row.url" target="_blank">
              <el-button>点击跳转</el-button>
            </el-link>
          </template>
        </el-table-column>
        <el-table-column prop="updateTime" label="更新时间" />
      </el-table>
    </div>
    
    <div class="search-card" v-if="resouce_data.length != 0" >
      <el-button 
      v-for="(item,index) in resouce_data" :key="index" 
      type="primary" 
      @click="goDetail(item.id)"
      target="_blank" 
      color="#626aef"
      >
      {{item.name}}
      </el-button>
    </div>
    <div class="search-nothing" v-else>
      <p>没有找到相关资源</p>
    </div>
  </div>
</template>

<script>
import { resourceApi } from '@/api/resource';
export default {
  name: 'resource_search',
  data() {
    return {
      keyword: '', // 用于存储关键字
      resouce_data:[],
      isLoading:true,
    };
  },
  methods:{
    //根据关键字搜索资源searchResource(keyword)
    async searchResource(keyword){
      try{
        this.isLoading = true
        const res = await resourceApi.searchResource(keyword);
        this.resouce_data = res.data;
        this.isLoading = false
        console.log(res);
      } catch(error){
        this.isLoading = false
        console.log(error);
      }
    },
    setIsLoading() {
      this.isLoading = !this.isLoading;
    },
    setTrueLoading() {
      this.isLoading = true;
    },
    // 资源详情跳转
    goDetail(id) {
        this.$router.push({ path: '/detail', query:  { id: id } }) // 跳转到资源详情页面，并传递资源ID参数
    },
  },
  watch: {
    // 监听 $route.query.keyword 的变化
    '$route.query.keyword': {
      handler(newVal, oldVal) {
        this.keyword = newVal; // 更新 keyword 数据
        this.searchResource(this.keyword); // 调用搜索资源的方法
        console.log(`关键字从 ${oldVal} 改为 ${newVal}`);
        // 在这里可以执行关键字改变后的逻辑，例如发起搜索请求等
      },
      immediate: true // 立即执行一次，确保初始值也被处理
    }
  },
  created() {
    this.keyword = this.$route.query.keyword; // 从路由的 query 中获取关键字
    console.log(this.keyword); // 打印关键字
  }
}
</script>

<style lang="less" scoped>
.el-button+.el-button {
    margin-left: 0px;
}
.search{
  display: none;
}
.search-card{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-template-rows: repeat(auto-fill, minmax(20px, 1fr));
  grid-gap: 10px;
}
</style>