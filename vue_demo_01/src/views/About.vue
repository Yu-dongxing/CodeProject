<template>
    <div class="baseB-1">
      我是b组件（发送方）1
      <button >发送通知</button>
      <!-- @click="clickSend" -->
    </div>
  </template>
  
  <script>
  export default {
    name:'FindAbout'
    // methods:{
    //     clickSend(){
    //         Bus.$emit('sendMsg','yuxs')
    //     }
    // }
  
  }
  </script>
  
  <style scoped>
  .baseB-1{
      width: 200px;
      height: 150px;
      padding: 10px;
      margin-top:10px ;
      border: 3px solid #000;
      border-radius: 5px;
      font-size: 20px;
  }
  </style>