<template>
  <div id="app">
    <HeaderIndex/>
    <MainIndex/>
    <FooterIndex/>
  </div>
</template>

<script>
import HeaderIndex from './components/header/HeaderIndex.vue'
import FooterIndex from './components/footer/FooterIndex.vue'
import MainIndex from './components/main/MainIndex.vue'
export default {
  name: 'app',
  components: {
    HeaderIndex,
    FooterIndex,
    MainIndex
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
</style>
