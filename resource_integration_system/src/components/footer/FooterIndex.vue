<template>
  <div class="footer">
    <div class="title">
      <p>
        2025 © yudongxing
        <br>
        资源库系统版本_{{ version }}</p>
    </div>
  </div>
</template>

<script>

// 从package获取项目版本号
export default {
  name: 'FooterIndex',
  data () {
    return {
      version: process.env.VUE_APP_VERSION
    }
  },
  methods: {
  }
}
</script>

<style lang="less" scoped>
//底部版权栏目，使用绝对定位
.footer {
    height: 40px;
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    background-color: var(--bg-200);
    .title {
        text-align: center;
        font-size: 15px;
        line-height: 20px;
        color: var(--text-200);
        p{
          margin: 1px;
        }
    }
}
</style>
