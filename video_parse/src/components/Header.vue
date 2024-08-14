<template>
  <!-- 头区域模块 -->
  <div class="header hh">
    <!-- logo模块（返回功能） -->
    <div class="h_l">
      <div @click="$router.back()" class="ttxt  bj blur_color transition_color_bkcolor" style="display: flex;flex-direction: column;" title="返回">
        <span>内容管理系统</span>
        <span style="font-size: 10px;color: #ff0000;">(CMS)</span>
        <!-- <span></span> -->
      </div>
    </div>
    <!-- 中间区域点击功能模块 -->
    <div class="h_l">
      <router-link :to="{path:item.rout}" class="ttxt bj blur_color transition_color_bkcolor" v-for="(item) in list_l" :key= item.id>
        <span>{{ item.title }}</span>
      </router-link>
    </div>
    <!-- 靠右其他模块 -->
    <div class="h_r">
      <div class="ttxt bj blur_color transition_color_bkcolor" v-for="(item) in list_r" :key= item.id>
        <img :src=" `/${item.iconName}.svg` " :alt=item.id class="icon">
        <span>{{ item.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:'HeaderMy',
    data(){
      return {
        list_l:[
          {id:1 , title:"首页"  ,rout:'/MainAbout/'},
          {id:2 , title:"视频解析"  ,rout:'/voide_id_1/'},
          {id:3 , title:"日志"  ,rout:'/MainVlog/'},
          {id:4 , title:"关于"  ,rout:'/MainPhone/'},
        ],
        list_r:[
          {id:1 , title:"其他"  ,iconName:"logo" ,width:20},
          {id:2 , title:"搜索"  ,iconName:"search",width:20},
        ]
      }
    },
    methods:{
        // 控制图像请求  
        getImageUrl(iconPath) {  
          if (iconPath && typeof iconPath === 'string') {  
            return require(`@/assets/${iconPath}`);  
          } else {  
                // 可以返回一个默认图像的路径或空字符串，取决于你的需求  
                // 例如，如果你有一个默认图标，可以这样返回：  
                return require('@/assets/logo.svg');  
          }  
      }
    }
}
</script>

<style>

.h_l,.h_r{
  display: flex;
  align-items: center;
  justify-content: center;
}
.h_r{
    display: flex;
    justify-content: flex-end;
    float: right;
    position: relative;
    right: 0px;
}
.h_l .ttxt,.h_r .ttxt{
    width: 100px;
    height: 40px;
    /* background-color: aqua; */
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 10px;
    
}
.h_l .ttxt:hover,.h_r .ttxt:hover{
  background-color: var(--backgroundcolor--hover);
  cursor: pointer;
  /* color:var(--font--hover--color); */
  color: #008cff;
  box-shadow: 2px 2px 5px rgb(255, 255, 255);
}
.hh{
    display: flex;
    /* align-items: center; */
    justify-content: space-between;
}
.icon{
  width: 20px;
  height: 20px;
  margin-right: 10px;
}
.h_r .ttxt{
  display: flex;
}
</style>