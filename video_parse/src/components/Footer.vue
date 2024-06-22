<template>
  <!-- 底部代码模块 -->
  <div class="Fooer">
    <div class="bj blur_color">
      <p class="footer_p">BY::YUXS</p>
      <p class="footer_p">YUCMS@  V{{ qversion }}</p>
    </div>
  </div>
</template>

<script>
import config from "@/../package.json"
export default {
name:'FooterMy',
data(){
  return {
    qversion:config.version
  }
}
}

</script>

<style>
.Fooer{
  position: fixed;
  bottom: 0px;
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: center;
  /* background-color: aquamarine; */
}
.footer_p{
  display: flex;
  justify-content: center;
  /* color: var(--font--color); */
  color: #000;
}
</style>