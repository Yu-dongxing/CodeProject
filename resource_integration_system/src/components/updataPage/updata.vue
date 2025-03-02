<template>
  <div class="updata-log-page">
    <el-timeline style="max-width: 600px">
      <el-timeline-item v-for="(item,index) in UpdataLog" :key="index" :timestamp="item.logCreatTime" placement="top" :type="item.type" :hollow="item.hollow">
        <!-- 'primary' | 'success' | 'warning' | 'danger' | 'info' -->
        <el-card class="ccard">
          <template #header>
            <div class=" card-header" >
              <el-icon style="margin-right: 5px;" color="#409eff"><Bell /></el-icon>
              <el-text type="primary" size="large">{{item.logTitle}}</el-text>
            </div>
          </template>
          <!-- <h4>{{ item.logTitle }}</h4> -->
          <p>{{ item.desc }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
    
</template>

<script>
import { Update_Log_Api } from '@/api/update_log';
export default {
  data() {
    return {
      UpdataLog:[]
    }
  },
  methods:{
    async getUpdataLog(){
      const res = await Update_Log_Api.getAllLog();
      console.log(res)
      this.UpdataLog =res.data;
    }
  },
  mounted() {
    
  },
  computed: {
    //通过计算属性实现倒序
    reversedUpdataLog() {
      return this.UpdataLog.slice().reverse();
    }
  },
  created() {
    this.getUpdataLog();
  },

}
</script>

<style>
.updata-log-page{
  margin-top: 25px;
}
.ccard{
  border-radius:15px ;
  margin-bottom: 10px;
  padding: 5px;
}
.card-header{
  display: flex;
  align-items: center;
  color: var(--el-text-color);
}
.header{
  padding: 5px;
}
.el-card__header{
  padding: 5px;
}
</style>