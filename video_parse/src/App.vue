<template>
    <!-- 主人口模块 -->
  <div class="main">
    <Header></Header>
    <Main></Main>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Main from '@/components/Main.vue'
import Footer from '@/components/Footer.vue'
export default {
    components:{
        Header,
        Main,
        Footer
    }
}
</script>

<style>
    *{
        padding: 0;
        margin: 0;
        /* color: #ffffff66; */
    }
    .main{
        position: relative;
    }
    body{
        /* background-color: aqua; */
        background: var(--body--background);
        /* backdrop-filter:blur(20px); */
        /* background:url("../public/backgroundimg/20240604106cbm.webp"); */
        /* background-repeat: no-repeat;  
        background-size: cover;        
        background-position: center;    */
    }
    html{
        /* background-image:url("../public/backgroundimg/167414.png"); */
        background-repeat: no-repeat;  
        background-size: cover;        
        background-position: center;   
    }
    /* a链接无下划线 */
    a{
    text-decoration-line: none;
    }
    /* 设定固定颜色，字体 */
    :root{
        --header--margin:60px;
        --box-1-heigth:96px;
        --box-1-width:96px;
        --box-heigth:96px;
        --box-width:96px;
        /*  */
        --body--background: linear-gradient(90deg, rgba(44, 216, 213, 1) 0%, rgba(197, 193, 255, 0.74) 56%, rgba(255, 186, 195, 0.74) 100%);
        --boder-redis:20px;
        --main--height:1000px;
        --blur:1px;
        --blur--color:rgba(255, 255, 255, 0.20);
        --font--color:rgba(255, 255, 255, 0.50);
        --font--hover--color:rgba(255, 255, 255, 0.70);
        --backgroundcolor:rgb(255 174 174 / 62%);
        --backgroundcolor--hover:rgba(255,255,255,0.50) ;
        --line--height:20px;
        --font-a-color:rgb(0, 0, 0);
        /* --body--background-img:url("../public/backgroundimg/2024060728g8nh.webp"); */
    }
    /* 高斯模糊样式 */
    .blur_color{
        background-color: var(--blur--color);
        /* backdrop-filter:blur(var(--blur)); */
    }
    /* 圆角样式 */
    .radius,
    div{
        border-radius: var(--boder-redis);
    }
    /*  */
    .over_over_0x_h{
            overflow: overlay;
            overflow-x: hidden;
    }   
    .transition_color_bkcolor{
        /* transition: background-color 0.5s ease, color 0.5s  ease,box-shadow 0.5s  ease;  */
        transition-property: background-color, color, box-shadow,border;  
        transition-duration: 0.2s;  
        transition-timing-function: ease;
    }
    .er::-webkit-scrollbar{
        width: 0;
        height: 0;
    }
    .backgroud_img{
        /* background:url("https://github.githubassets.com/assets/bg-a352b7ab2e3b.png"); */
        background-repeat: no-repeat;  /* 不重复背景图像 */  
        background-size: cover;        /* 使背景图像覆盖整个元素 */  
        background-position: center;   /* 将背景图像居中放置 */ 
    }
    .body_backgroud_img{
        background:url("../public/backgroundimg/2024060728g8nh.webp");
        background-repeat: no-repeat;  /* 不重复背景图像 */  
        background-size: cover;        /* 使背景图像覆盖整个元素 */  
        background-position: center;   /* 将背景图像居中放置 */ 
    }
    .bj{
            width: 100%;
            height: 100%;
            border-radius: var(--boder-redis);
            position: relative;
    }
    .header{
        width: 100%;
        height: 50px;
        top: 0;
        backdrop-filter: blur(20px);
        background-color: rgba(255, 255, 255, 0.20);
        border-radius: 0px 0px 30px 30px;
        position: sticky;
    }
/*字数超出 */
.text-ellipsis-2 {
  overflow: hidden;
  -webkit-line-clamp: 1;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}
iframe{
  height: 90%;
  width: 90%;
  margin-left:5% ;
}
p{
    text-indent: 10px;
}
.p_w_text-indent{
    text-indent: 0;
}
a.router-link-active{
    color: var( --font-a-color);
    /* cursor: pointer; */
    background-color: var(--backgroundcolor--hover);
}
.close::after{
    content: 'X';
    font-weight: bolder;
    display: flex;
    justify-content: center;
    align-items: center;
    line-height: 20px;
}
</style>