<template>
  <div class="App">
    <!-- hesder 组件 -->
    <BaseA></BaseA>
    <BaseB></BaseB>
    <YuxsHeader></YuxsHeader>
    <YuxsMain></YuxsMain>
    <YuxsFooter></YuxsFooter>
  </div>
</template>

<script>
// import YuxsFooter from './components/YuxsFooter.vue'
// import YuxsHeader from './components/YuxsHeader.vue'
// import YuxsMain from './components/YuxsMain.vue'
// import BaseA from './components/BaseA.vue'
import BaseB from './components/BaseB.vue'
export default {
    components:{
      //YuxsHeader : YuxsHeader, 可以省略 -> YuxsHeader,
        // YuxsHeader,
        // YuxsFooter,
        // YuxsMain,
        // BaseA,
        BaseB
    }
}
</script>

<style>
.App{
    width: 600px;
    height:700px;
    background-color: aqua;
    margin: 0 auto;
    padding: 20px;
    border-radius:10px ;
}
</style>