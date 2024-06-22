<template>
  <!-- 开发日志 -->
  <div class="MainVlog">
    <div class="M_V">
    </div>
  </div>
</template>
<script>
export default {
    name:'MainVlog',
    data(){
      return{
        Liist:[
          {id:1,desc:"231231232"},
        ]
      }
    },

}
</script>

<style>
.MainVlog{

}
.MainVlog .M_V{
  width: 100%;
  height: 200px;
  background-color: black;
}
</style>