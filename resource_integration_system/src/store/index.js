import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null
  },
  getters: {
    currentUser: state => state.user
  },
  mutations: {
    SET_USER (state, user) {
      state.user = user
    },
    CLEAR_USER (state) {
      state.user = null
    }
  },
  actions: {
    logout ({ commit }) {
      // 清除用户信息
      commit('CLEAR_USER')
      // 可以在这里添加清除token等逻辑
      localStorage.removeItem('token')
    }
  }
})
