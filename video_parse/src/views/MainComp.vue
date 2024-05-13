<template>
  <div class="Comp">
    <div class="cc bj blur_color">
      <h1>视频详情--{{ title }}</h1>
      <!-- <iframe :src=mag frameborder="0"></iframe> {{ this.$store.state.title }} ---->
      <iframe :src=mag    allowfullscreen='true' allow="autoplay" allowtransparency="true" frameborder="0" scrolling="no" sandbox="allow-scripts allow-same-origin allow-popups"> </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name:'MainComp',
  data(){
    return {
      mag:'https://jx.777jiexi.com/player/?url='+this.$route.query.voide_url,
      title:this.$route.query.voide_title
    }
  }
}
</script>

<style>
.Comp{
    width: 90%;
    height: 100%;
    margin-left: 5%;
    /* background-color: black; */
    position: relative;
}
.cc h1{
  display: flex;
  justify-content: center;
}
iframe{
  height: 100%;
  width: 100%;
}
</style>