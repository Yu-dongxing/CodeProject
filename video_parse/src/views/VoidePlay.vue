<template>
  <!-- 视频解析系统中的视频详情和播放界面 -->
  <div class="voide_play bj blur_color radius er">
    <!-- 播放界面 -->
    <div class="play_L radius" >
      <!-- <iframe :src=mag    allowfullscreen='true' allow="autoplay" allowtransparency="true" frameborder="0" scrolling="no" sandbox="allow-scripts allow-same-origin allow-popups" class="radius"></iframe> -->
      <h1>{{ mag }}</h1>
    </div>
    <!-- 视频详情界面 -->
    <div class="play_R radius er ">
      <h1>{{ title }}</h1>
      <div class="jxjk" v-for="(item) in jx_jk" :key="item.id" @click="getput(item.url,jx_url)">
        <p style="color: aliceblue;">{{ item.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'VoidePlay',
    data(){
    return {
      jk_url:' ',
      jx_url:this.$route.query.voide_url,
      mag:'https://jx.777jiexi.com/player/?url='+this.$route.query.voide_url,
      title:this.$route.query.voide_title,
      jx_jk:[
        {id:1,title:"解析1",url:'https://jx.777jiexi.com/player/?url='},
        // {id:2,title:"解析2",url:'https://yparse.ik9.cc/index.php?url='},
        // {id:3,title:"解析3",url:'https://jx.777jiexi.com/player/?url='},
        // {id:4,title:"解析4",url:'https://jx.777jiexi.com/player/?url='},
      ],
    }
  },
  methods:{
    async  aqy() { 
            // if(!id){
            //     id=1;
            // } 
            try {  
                const response = await axios.get(  
                    'https://api.yuxs.top/spjx_api/jxjk_api/',  
                ); 
                if (Array.isArray(response.data.data)) {    
                        this.jx_jk = []; // 初始化this.video 数组    
                        response.data.data.forEach(item => {    
                            this.jx_jk.push(
                                { 
                                    id: item.id  , 
                                    title: item.name ,
                                    url:item.url,
                                });    
                        });
                        // console.log(this.jx_jk);
                        } else {  
                        console.error('data is not an array');  
                    }   
            } catch (error) {  
                console.error(error);  
            }  
        },
    getput(JK_url,JX_url){
      this.mag = JK_url+JX_url;
      console.log(this.mag);
    }
  },
  updated(){
    this.aqy();``
  },
  beforeMount(){
    this.aqy();
  },
  mounted() {  
        this.aqy();
    },

}
</script>

<style>
.voide_play1{
    /* display: flex;
    flex-wrap: wrap;
    flex-direction: row; */
    position: relative;
    z-index: 1;
    overflow: scroll;
    width: 100%;
}
.voide_play{
  width: 100%;
  height: 100%;
  display: flex;
  position: relative;
}
.voide_play h1{
    display: flex;
    justify-content: center;
}
.voide_play .play_L{
  width: 80%;
  /* background-color: aqua; */
  margin-right: 5px;
}
.voide_play .play_R{
  margin-left: 5px;
  width: 20%;
  background-color: aqua;
  overflow: scroll;
}
.voide_play .play_R .jxjk{
  width: 100%;
  /* height: 40px; */
  height: auto;
  background-color:black;
  margin-top: 10px;

}
.voide_play .play_R .jxjk:hover{
  background-color:rgb(127, 28, 28);
  cursor: pointer;
}
.r_Box{
    display: none;
}
.voide_play .jk{
  display: flex;
  width: 95%;
  height: 20px;
  margin-left: 2.5%;
  background-color: aqua;
}
iframe{
  margin-top: 10px;
}
.lllong{
  width: 100%;
  height: 100%;
  background:url("https://s1.aigei.com/src/img/gif/1a/1a5d97183a71412fa727379e4aab91bd.gif?imageMogr2/auto-orient/thumbnail/!282x282r/gravity/Center/crop/282x282/quality/85/%7CimageView2/2/w/282&e=1735488000&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:4-HK94znDMKtrCLCP6bkScHJWBw=");
  background-repeat: no-repeat;  /* 不重复背景图像 */  
  background-size: cover;        /* 使背景图像覆盖整个元素 */  
  background-position: center;   /* 将背景图像居中放置 */ 

}
</style>