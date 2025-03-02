<!-- 加载中组件 -->
<template>
  <div class="loaging">
    <div class="loaging-box">
      <div class="loaging-box-content">
        <div class="loaging-box-content-img">
          <img src="@/assets/images/loading.gif" alt="" />
        </div>
        <div class="loaging-box-content-text">加载中...</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoagingIndex',
  data() {
    return {}
  },
  created() {},
  mounted() {},
  methods: {}
}
</script>

<style lang="scss" scoped>
.loaging {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.3);
  z-index: 9999;
  .loaging-box {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100px;
    height: 100px;
    background: #fff;
    border-radius: 10px;
    .loaging-box-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      .loaging-box-content-img {
        width: 50px;
        height: 50px;
        img {
          width: 100%;
          height: 100%;
        }
      }
      .loaging-box-content-text {
        font-size: 14px;
        color: #666;
      }
    }
  }
}
</style>