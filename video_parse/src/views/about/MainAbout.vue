<template>
  <!-- 关于模块 -->
  <div class="About radius">
    <div class="about_L radius">
      <div class="L_a radius er">
        <div class="box blur_color radius" v-for="(item) in texxt " :key="item.id">
          <div class="her">
            <p>{{ item.title }}</p>
          </div>
          <div class="img"></div>
          <div class="desc"></div>
          
        </div>
      </div>
    </div>
    <div class="about_R radius">

    </div>
  </div>
</template>

<script>
export default {
    name:'MainAbout',
    data(){
        return{
          texxt:[
            {id:1,title:'测试'},
            {id:2,title:'测试'},
            {id:3,title:'测试'},
            {id:4,title:'测试'},
            {id:5,title:'测试'},
            {id:6,title:'测试'},
            {id:7,title:'测试'},
            {id:8,title:'测试'},
            {id:9,title:'测试'},
            {id:10,title:'测试'},
            {id:11,title:'测试'},
            {id:12,title:'测试'},
            {id:13,title:'测试'},
            {id:14,title:'测试'},
            {id:15,title:'测试'},
            {id:16,title:'测试'},
          ]
        }
    },

}
</script>

<style>
.About{
  width: 100%;
  height: 100%;
  display: flex;
  position: relative;
  /* background-color: aqua; */

}
.About .about_L{
  width: 80%;
  height: 100%;
  background-color: aqua;
  margin-right: 5px;
}
.About .about_L .L_a{
  width: 80%;
  height: 100%;
  margin-left: 10%;
  background-color: rgb(134, 194, 31);
  overflow: scroll;
}
.About .about_L .L_a .box{
  width: 50%;
  height: 100px;
  margin-left: 25%;
  /* background-color: black; */
  margin-top: 10px;
  margin-bottom: 10px;
  display:flex;

}
.About .about_R{
  /* position: relative; */
  float:right;
  width: 20%;
  height: 100%;
  background-color: aqua;
}
</style>