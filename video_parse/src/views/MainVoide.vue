<template>
    <!-- 视频解析系统 -->
    <div class="Voide radius ">
        <!-- 视频类型id -->
        <div class="v_l radius ">
            <div class="bj   radius "></div>
            <div class="v_l_l radius backgroud_img blur_color">
                <router-link class="l_fk transition_color_bkcolor radius blur_color " :to="{path:'/voide_id_'+item.id+'/'}"   v-for="(item) in video_spid" :key="item.id">
                    <div class="fk_a">
                        <img :src=" `/VoideIDsvg/${item.iconName}` " :alt=item.id>
                        <span>{{ item.title }}</span>
                    </div>
                </router-link>
            </div>
        </div>
        <!-- 视频列表 -->
        <div class="v_r radius backgroud_img blur_color">
            <router-view></router-view>
            <div class="r_Box bj blur_color radius">
                <div class="r_Box_01 Box_div">
                    <div class="Box_box radius blur_color" v-for="(item) in video" :key="item.id">
                        <div class="img">
                            <img src="" alt="">
                        </div>
                        <div class="desc " @click="get(item.url,item.title,item.id)">
                            <p class="desc_h1 transition_color_bkcolor text-ellipsis-2">{{ item.title }}</p>
                            <p class="desc_txt transition_color_bkcolor text-ellipsis-2">{{ item.desc }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import VoidePlay from "@/views/VoidePlay.vue"
import axios from 'axios'; // 安装了 axios  
export default {
    name:'MainVoide',
    components:{
        // VoidePlay,
    },
    data(){
        return {
            video:[],
            video_id:1,
            loaaing:true,
            video_spid:[
                {id:1,       title:"电影"      ,iconName: "dy.svg"},
                {id:2,       title:"电视剧"    ,iconName: "tv.svg"},
                {id:6,       title:"综艺"      ,iconName: "zy.svg"},
                {id:4,       title:"动漫"      ,iconName: "dm.svg"},
                {id:8,       title:"游戏"      ,iconName: "yx.svg"},
                {id:3,       title:"纪录片"    ,iconName: "jlp.svg"},
                {id:17,      title:"体育"      ,iconName: "ty.svg"},
                {id:261,     title:"风云榜"    ,iconName: "fyb.svg"},
                {id:50,      title:"热点"      ,iconName: "logo.svg"},
            ],
            video_sp:[
                {id:1,       title:"电影"      },
                {id:2,       title:"电视剧"    },
                {id:6,       title:"综艺"      },
                {id:4,       title:"动漫"      },
                {id:8,       title:"游戏"      },
                {id:3,       title:"纪录片"    },
                {id:17,      title:"体育"      },
                {id:261,     title:"风云榜"    },
                {id:52,      title:"热点"      },
                {id:53,      title:"热点"      },
                {id:54,      title:"热点"      },
                {id:55,      title:"热点"      },
                {id:5,      title:"热点"      },
                {id:50,      title:"热点"      },
                {id:560,      title:"热点"      },
                {id:53,      title:"热点"      },
                {id:51,      title:"热点"      },
                {id:50,      title:"热点"      },
                {id:57,      title:"热点"      },

            ],
            // video_id:0
        }
    },
    beforeCreate(){
        console.log("1yuxs");
    },
    created(){
        console.log("yuxs");
    },
    methods:{
        async  fetchData(id) { 
            if(!id){
                id=1;
            } 
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
                    }
                ); 
                if (Array.isArray(response.data.data)) {    
                        this.video = []; // 初始化this.video 数组    
                        response.data.data.forEach(item => {    
                            this.video.push(
                                { 
                                    id: item.id  , 
                                    title: item.display_name ,
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
                name: 'VoidePlay',
                query:{
                    voide_title:title,
                    voide_url:url,
                    voide_id:id
                }
            }); 
        },
        getidpage(id){
            this.fetchData(id);
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
.Voide{
    width: 100%;
    height: 100%;
    /* background-color: aqua; */
    /* margin: 0 auto; */
    /* position: fixed; */
    display: flex;
    
}
.Voide .v_l{
    width: 150px;
    height: 100%;
    /* background-color: black; */
    margin: 0px 5px 0px 0px;
    display: flex;
    position: relative;
}
.Box_div{
    width: 88%;
    height: 100%;
    margin: 0 auto;
}
.Voide .v_r{
    width: 100%;
    height: 100%;
    background-color: blue;
    /* margin-left: 5px; */
    /* display: flex; */
    position: relative;
    overflow: hidden;
    /* margin: 0 auto; */
}
.Voide .v_r .r_Box{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    position: relative;
    z-index: 1;
    overflow: scroll;
    width: 100%;
}
.Voide .v_r .r_Box .r_Box_01{
    display: flex;
    position: relative;
    /* row-gap: 21px; */
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    flex-direction: row;
    /* width: 90%;
    margin-left: 5%; */

}
.aqy{
    display: flex;
    position: relative;
    /* row-gap: 21px; */
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    flex-direction: row;
}
.Voide .v_r .r_Box .Box_box{
    display: flex;
    width: 200px;
    height: 300px;
    /* background-color: black; */
    position: relative;
    margin: 10px;
    /* overflow: hidden; */

    display: flex;
    flex-direction: column;
    align-items: center;
    /* margin: 10px 10px 10px 10px; */
    overflow: hidden;
}
.Voide .v_r .r_Box .Box_box .img{
    width: 100%;
    height: 260px;
    background: url("https://s1.aigei.com/src/img/gif/f3/f3716c9376c84262813749d18a5f282e.gif?imageMogr2/auto-orient/thumbnail/!560x560r/gravity/Center/crop/560x560/quality/85/%7CimageView2/2/w/560%7Cwatermark/3/image/aHR0cHM6Ly9zMS5haWdlaS5jb20vd2F0ZXJtYXJrL21pZGRsZS0xLUwxMC5wbmc_ZT0xNzM1NDg4MDAwJnRva2VuPVA3UzJYcHpmejExdkFrQVNMVGtmSE43Rnctb09aQmVjcWVKYXh5cEw6cE9JQ29KYkxTOF9YNVBqVWlJYTZWX0phVVRJPQ==/dissolve/100/gravity/Center/dx/6/dy/11&e=1735488000&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:AMJ9NRFN1Cv8doJJMpZDcx-HNLQ=");
    /* background-color: aqua; */
    background-repeat: no-repeat;  /* 不重复背景图像 */  
    background-size: cover;        /* 使背景图像覆盖整个元素 */  
    background-position: center;   /* 将背景图像居中放置 */  
}
.Voide .v_r .r_Box .Box_box .desc {
    display: flex;
    width: 100%;
    height: 40px;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.Voide .v_r .r_Box .Box_box .desc .desc_h1,
.Voide .v_r .r_Box .Box_box .desc .desc_txt{
    line-height: var(--line--height);
    color: var(--font--color);
    width: 100%;
    text-align: center;
}
.Voide .v_r .r_Box .Box_box .desc .desc_h1:hover,
.Voide .v_r .r_Box .Box_box .desc .desc_txt:hover{
    color: var(--font--hover--color);
    cursor: pointer;
    background-color: var(--backgroundcolor--hover);
}
.Voide .v_r .r_Box .Box_box .desc .desc_h1{
    background-color: var(--backgroundcolor);
    color: #000000bd;
    /* font-size: 18px; */
}
.Voide .v_r .r_Box .Box_box .desc .desc_txt{

}
.Voide .v_l .v_l_l{
    position: absolute;
    width: 120px;
    height: 100%;
    top: 0px;
    overflow: overlay;
    overflow-x: hidden;
    display: flex;
    flex-wrap: wrap;
}
.Voide .v_l .v_l_l::-webkit-scrollbar,
.Voide .v_r .r_Box::-webkit-scrollbar,
.r_Box_01 ::-webkit-scrollbar{
    width: 0;
    height: 0;
}
.fk_a::selection{
    color: #000;
    background-color: #000;
}
.Voide .v_l .v_l_l .l_fk{
    width: 110px;
    height: 60px;
    display: flex;
    margin-top: 5px;
    margin-bottom: 5px;
    padding: 5px;
    line-height: 60px;
    align-items: center;
}
a{
    color:#000;
}
.Voide .v_l .v_l_l .l_fk:hover,
a.router-link-active{
    color: var(--font--hover--color);
    /* cursor: pointer; */
    background-color: var(--backgroundcolor--hover);
}
.Voide .v_l .v_l_l .l_fk .fk_a{
    width: 120px;
    display: flex;
    margin-left: 20px;
    align-items: center;
}
.Voide .v_l .v_l_l .l_fk .fk_a img{
    width: 20px;
    height: 20px;
}
.Voide .v_l .v_l_l .l_fk .fk_a span{
    margin-left: 5px;
}
</style>