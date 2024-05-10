<template>
  <div class="main">
    <div class="box" v-loading="isLoading">
        <ul>
            <li v-for="item in list" :key="item.id" class="news">
            <!-- <li v-for="item in list" :key="item.id" class="news">  {{ title }}  {{ item.source }}  {{ item.time }} :src="item.img"-->
                <div class="left">
                    <div class="title"> {{ item.title }} </div>
                    <div class="info">
                        <span>{{ item.source }}</span>
                        <span>{{ item.time }}</span>
                    </div>
                </div>
                <div class="right">
                    <img :src="item.img"  key="item.id" alt="name">
                </div>
            </li>
        </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            list:[],
            isLoading:true
        }
    },
    async created (){
        const res = await axios.get('http://hmajax.itheima.net/api/news')
        setTimeout(()=>{
            this.list=res.data.data
            this.isLoading=false
        },2000)
    },
    
    directives:{
        loading:{
            inserted(el,binding){
                binding.value ? el.classList.add('loading'):el.classList.remove('loading')
            },
            update(el,binding){
                binding.value ? el.classList.add('loading'):el.classList.remove('loading')
            } 
        }
    }
}
</script>

<style>
/* 伪类 - 蒙层效果 */
.loading:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: #fff url('./loading.gif') no-repeat center;
}

/* .box2 {
  width: 400px;
  height: 400px;
  border: 2px solid #000;
  position: relative;
} */

.box {
  width: 800px;
  min-height: 500px;
  border: 3px solid orange;
  border-radius: 5px;
  position: relative;
}
.news {
  display: flex;
  height: 120px;
  width: 600px;
  margin: 0 auto;
  padding: 20px 0;
  cursor: pointer;
}
.news .left {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-right: 10px;
}
.news .left .title {
  font-size: 20px;
}
.news .left .info {
  color: #999999;
}
.news .left .info span {
  margin-right: 20px;
}
.news .right {
  width: 160px;
  height: 120px;
}
.news .right img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

</style>