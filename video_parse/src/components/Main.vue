<template>
    <!-- 主显示区域 -->
    <div class="main_body blur_color radius">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name:'MaIn',
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
        width: 98%;
        height: 85vh;
        margin: 0 auto;
        margin-left: 1%;
        margin-top: 10px;
        position: fixed;
        z-index: 0;

    }
        
</style>