<!-- header -->
<template>
  <div class="header">
    <div class="header-left">
      <div class="logo">
        <!-- <img src="../../assets/logo.png" alt="logo" /> -->
      </div>
      <div class="title">资源库系统</div>
    </div>
    <div class="header-right">
      <div class="user">
        <div class="username">{{ user.username }}</div>
      </div>
      <div class="logout">退出</div>
      <!--  @click="handleLogout" -->
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'HeaderIndex',
  computed: {
    ...mapGetters(['currentUser']),
    user () {
      return this.currentUser || { username: '未登录' }
    }
  },
  methods: {
    ...mapActions(['logout']),
    async handleLogout () {
      await this.logout()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 60px;
  background-color: var(--bg-200);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-left {
  display: flex;
  align-items: center;
}

.logo img {
  height: 40px;
  margin-right: 10px;
}

.title {
  font-size: 18px;
  font-weight: bold;
  line-height: 60px;
}

.header-right {
  display: flex;
  align-items: center;
}

.username {
  margin-right: 20px;
}

.logout {
  cursor: pointer;
  color: #666;
}

.logout:hover {
  color: #42b983;
}
/* 当屏幕宽度小于500px */
@media screen and (max-width: 500px) {
  .logo,.header-right{
    display: none;
  }
}
</style>
