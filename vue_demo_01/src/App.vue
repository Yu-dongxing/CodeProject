<template>
  <div class="App">
    <!-- <DemoAx></DemoAx> -->
    <!-- hesder 组件 -->
    <!-- <BaseA></BaseA>
    <BaseB></BaseB>
    <ZlValue></ZlValue>
    <ZdyZl></ZdyZl>
    <NextTick></NextTick>
    <YuxsHeader></YuxsHeader>
    <YuxsMain></YuxsMain>
    <YuxsFooter></YuxsFooter>
    <BaseSelect></BaseSelect> -->
    <div>
      <router-link to="/">返回</router-link><br>
      <router-link to="/About">关于</router-link><br>
      <!-- <a href="/My">我的</a><br> -->
      <router-link to="/My">我的</router-link><br>
      <router-link to="/Phone">联系</router-link><br>
      <router-link to="/404">404</router-link><br>
    </div>
    <div class="top">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// import YuxsFooter from './components/YuxsFooter.vue'
// import YuxsHeader from './components/YuxsHeader.vue'
// import YuxsMain from './components/YuxsMain.vue'
// import BaseA from './components/BaseA.vue'
// import BaseB from './components/BaseB.vue'
// import BaseSelect from './components/BaseSelect.vue'
// import  NextTick  from './components/NextTick.vue'
// import  ZdyZl  from './components/ZdyZl.vue'
// import ZlValue from './components/ZlValue.vue'
// import DemoAx from './components/DemoAx.vue'
export default {
    //components:{
      //YuxsHeader : YuxsHeader, 可以省略 -> YuxsHeader,
        // YuxsHeader,
        // YuxsFooter,
        // YuxsMain,
        // BaseA,
        // BaseB,
        // BaseSelect,
        // NextTick,
        // ZdyZl,
        // ZlValue,
        // DemoAx
 //   }
}
</script>

<style>
.App{
    width: 600px;
    height:auto;
    background-color: aqua;
    margin: 0 auto;
    padding: 20px;
    border-radius:10px ;
}
.App a.router-link-active{
  color: blue;
}
</style>