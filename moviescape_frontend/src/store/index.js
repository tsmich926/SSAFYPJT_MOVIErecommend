import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  plulgins: [
    createPersistedState(),
  ],
  state: { token:null
  },
  getters: {
    isLgin(state){
      return state.token ? true: false
    }
  },
  mutations: {
    SAVE_TOKEN(state,token){
      state.token = token
      router.push({name:'MovieList'})
    }
  },
  actions: {
    login(context,payload){
      const username = payload.username
      const password = payload.password
    
      axios({
        method:'post',
        // url:`${}/accounts/login`,
        data:{
          username,password
        }
      })
        .then((res)=>{
          context.commit('SAVE_TOKEN',res.data.key)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    SignUp(context,payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method:'post',
        // url:`${}/accounts/login`,
        data: {
          username,password
        }
      })
        .then((res)=>{
          context.commit('SAVE_TOKEN',res.data.key)
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  modules: {
  }
})
