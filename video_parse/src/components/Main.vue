<template>
    <div class="main_body">
            <div class="lift_list backgroud_img">
                <div class="bj blur_color">
                </div>
                <div class="ll">
                    <div  v-for="(item, index) in video_lx"  :key="index++">
                        <router-link class="ah11" :to="{path:'/'+item.id}">
                            <div class="h11" >
                                <img class="Logo" :src=" `/VoideIDsvg/${item.iconName}` " :alt=item.id>
                                <!-- <img class="Logo" :src="getImageUrl(item.icon)" :alt=item.id> -->
                                <span>{{ item.title }}</span>
                            </div>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="main_list backgroud_img">
                <div class="bj blur_color"></div>
                <div class="BOOX radius over_over_0x_h">
                    <div class="header bx" style="z-index: 10;" @click="$router.back()">
                        <div class="h_l">
                            <div class="ttxt bj blur_color transition_color_bkcolor" >
                                <span>返回</span>
                            </div>
                        </div>
                    </div>
                        <!-- <keep-alive include="['MainVoide']"> -->
                            <router-view></router-view>
                        <!-- </keep-alive> -->
                </div>
            </div>
        </div>
</template>

<script>
export default {
    name:'FooterMy',
    data(){
        return {
            video_lx:[
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
            video_id:0
        }
    },
    methods:{
        //控制图像请求
        getImageUrl(iconPath) {  
            return require(`@/assets/${iconPath}`);  
        },
    }
}
</script>
<style>
    .main_body{
        width: 100%;
        margin-top: 10px;
        position: relative;
    }
        .lift_list{
                width: 120px;
                height: 85%;
                position: fixed;
                margin-left: 15px;
                border-radius: var(--boder-redis);
        }
        .main_list{
        width: 80%;
        height: 85%;
        margin-left: 150px;
        border-radius: var(--boder-redis);
        z-index: -10;
        position: fixed;
        }

    .ll{
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0px;
        border-radius: var(--boder-redis);
        overflow: overlay;
        /* padding: 5px; */
        overflow-x: hidden;
    }
    .BOOX{
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0px;
        }
        .BBox{
            width: 80%;
            height: 200px;
            background-color: #ffffff17;
            margin-top: 5px;
            margin-left: 10%;
        }
        .ll::-webkit-scrollbar ,.BOOX::-webkit-scrollbar{
            width: 0;
        }
        .ah11{
            background-color: #ffffff3d;
            color: #ffffff66;
            transition: background-color .2s ease;
            /* transition: color .2s ease; */
            display: flow;
        }
        .h11{
            /* width: 100%; */
            height: 50px;
            margin-top: 10px;
            padding: 10px;
            line-height: 50px;
            display: flex;
            align-items: center;
            /* transition: background-color .2s ease; */
            transition: color .2s ease;
        }
        .Logo{
            width: 25px;
            height: 25px;
            margin-right: 10px;
        }
        .h11:hover,.ll .router-link-active{
            background-color: #ffffff7b;
            color: #050202;
        }
        .bx{
            display: flex;

        }
</style>