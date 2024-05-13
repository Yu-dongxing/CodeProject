<template>
  <div class="Fooer">
    <div class="bj blur_color">
      <p class="footer_p">BY::YUXS</p>
    </div>
  </div>
</template>

<script>
export default {
name:'FooterMy'
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
  color: var(--font--color);
}
</style>