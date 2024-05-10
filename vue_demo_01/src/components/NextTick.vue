<template>
  <div class="in">
    <div v-if="isShow">
        <input type="text" v-model="editValue" ref="inp" />
        <button>确认</button>
    </div>
    <div>
        <span>{{ title }}</span>
        <button @click="handleEdit">编辑</button>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            title :'的标题',
            isShow:false,
            editValue:''
        }
    },
    methods:{
        handleEdit(){
            this.isShow=true
            this.$nextTick(()=>{
                this.$refs.inp.focus()
            })
           
        }
    },

}
</script>

<style>

</style>