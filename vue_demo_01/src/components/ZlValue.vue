<template>
  <div>
    <h1 v-color >指令的值</h1>
  </div>
</template>

<script>
export default {
    data(){
        return {

        }
    },
    directives:{
        color:{
            inserted(el){
                console.log(el);
            }
        }
    }
}
</script>

<style>

</style>