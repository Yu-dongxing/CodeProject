<template>
    <div class="baseB">
      我是b组件（发送方）
      <button >发送通知</button>
      <!-- @click="clickSend" -->
    </div>
  </template>
  
  <script>
  export default {
    // methods:{
    //     clickSend(){
    //         Bus.$emit('sendMsg','yuxs')
    //     }
    // }
  
  }
  </script>
  
  <style scoped>
  .baseB{
      width: 200px;
      height: 150px;
      padding: 10px;
      margin-top:10px ;
      border: 3px solid #000;
      border-radius: 5px;
      font-size: 20px;
  }
  </style>