<template>
  <div class="ma">
    <div  class="voide  radius blur_color" v-for="(item,index) in video" :key="index++" >
        <div class="iimg">
            <img src="" alt="">
            <!-- <iframe :src="item.img" frameborder="0"></iframe>:to="{ path: '/' + $route.params.page_id + '/url='+ item.url}" -->
        </div>
            <div class="txt">
                    <span @click="get(item.url,item.title,item.tv_id)">{{ item.title }}</span>
            </div>
        <div class="desc">
            <span>{{ item.desc }}</span>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // 安装了 axios  
export default {
    name:'MainVoide',
    data(){
        return {
            video:[],
            video_id:1
        }
    },
    methods:{
        async  fetchData(id) {  
            try {  
                const response = await axios.get(  
                    'https://mesh.if.iqiyi.com/portal/videolib/pcw/data',  
                    {  
                        params: {  
                            scale: 150,  
                            channel_id: id,  
                            ret_num: 60,  
                            page_id: 1,  
                            market_release_date_level: 2024,  
                        },  
                        // 添加 headers  
                        //  headers: {  
                        //     'authority':'mesh.if.iqiyi.com',
                        //  },  
                    }  
                ); 
                if (Array.isArray(response.data.data)) {    
                        this.video = []; // 初始化this.video 数组    
                        response.data.data.forEach(item => {    
                            this.video.push(
                                { 
                                    id: item.id  , 
                                    title: item.title ,
                                    img:item.album_image_url_hover,
                                    desc:item.desc,
                                    url:item.page_url,
                                    tv_id:item.tv_id
                                });    
                        });
                        } else {  
                        console.error('data is not an array');  
                    }   
            } catch (error) {  
                console.error(error);  
            }  
        }, 
        get(url,title,id){
            this.$router.push({ 
                name: 'MainComp',
                query:{
                    voide_title:title,
                    voide_url:url,
                    voide_id:id
                }
            }); 
        }
    },
    watch: {  
        '$route.params.page_id': 'fetchData' // 当 page_id 发生变化时，调用 fetchData 方法  
    },  
    mounted() {  
        this.fetchData(this.$route.params.page_id);  
    },
}
</script>

<style>
.ma{    
    width: 90%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    margin-left:5%;
    position: relative;
    z-index: 1;
}
.voide{
    width: 150px;
    height: 250px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 10px 10px 10px 10px;
    overflow: hidden;
}
.desc{
    color: #e6e6e6d0;
    display: flex;
    justify-content: center;
    width: 150px;
    height: 20px;
    /* overflow: hidden;*/
}
.txt{
    background-color: #ffffff88;
    width: 100%;
    height: 25px;
    line-height: 25px;

    display: flex;
    justify-content: center;

}
.txt span,.desc span{
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
}
.txt:hover{
    background-color: #ffffffbf;
    cursor: pointer;
}
.voide .iimg{
    width: 100%;
    height: 180px;
    background: url("../assets/772.webp");
    /* background-color: aqua; */
    background-repeat: no-repeat;  /* 不重复背景图像 */  
    background-size: cover;        /* 使背景图像覆盖整个元素 */  
    background-position: center;   /* 将背景图像居中放置 */  
}
iframe{
    width: 100%;
    height: 180px;
}
</style>