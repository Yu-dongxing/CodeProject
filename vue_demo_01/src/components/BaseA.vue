<template>
  <div class="baseA">
    我是a组件（接收方）
  </div>
</template>

<script>
// import Bus from '../utils/EventBus.js'
export default {
    // created(){
    //     Bus.$on('sendMsg',(msg)=>{
    //         console.log(msg)
    //     })
    // }

}
</script>

<style scoped>
.baseA{
    width: 200px;
    height: 150px;
    padding: 10px;
    margin-top:10px ;
    border: 3px solid #000;
    border-radius: 5px;
    font-size: 20px;
}
</style>