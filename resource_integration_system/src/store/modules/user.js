import { userApi } from '@/api/user'

const state = {
  token: localStorage.getItem('token'),
  userInfo: null
}

const mutations = {
  SET_TOKEN(state, token) {
    state.token = token
    if (token) {
      localStorage.setItem('token', token)
    } else {
      localStorage.removeItem('token')
    }
  },
  SET_USER_INFO(state, userInfo) {
    state.userInfo = userInfo
    if(userInfo){
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
    }else{
      localStorage.removeItem('userInfo')
    }
  }
}

const actions = {
  // 用户登录
  async login({ commit }, loginForm) {
    try {
      const res = await userApi.login(loginForm)
      console.log('登录响应:', res)
      if (res.code === 200) {
        commit('SET_TOKEN', res.data)
        return res
      } else {
        throw new Error(res.msg || '登录失败')
      }
    } catch (error) {
      console.error('登录失败:', error)
      throw error
    }
  },
  //用户注册register
  async register({ commit }, registerForm) {
    try {
      const res = await userApi.register(registerForm)
      console.log('注册响应:', res)
      if (res.code === 200) {
        commit('SET_TOKEN', res.data)
        return res
      } else {
        throw new Error(res.msg || '注册失败')
      }
    } catch (error) {
      console.error('注册失败:', error)
      throw error
    }
  },
  // 获取用户信息
  async getUserInfo({ commit }) {
    try {
      const res = await userApi.getUserInfo()
      console.log('获取用户信息响应:', res)
      if (res.code === 200 && res.data) {
        commit('SET_USER_INFO', res.data)
        return res.data
      } else {
        throw new Error(res.message || '获取用户信息失败')
      }
    } catch (error) {
      console.error('获取用户信息失败:', error)
      throw error
    }
  },

  // 退出登录
  logout({ commit }) {
    commit('SET_TOKEN', '')
    commit('SET_USER_INFO', null)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
} 