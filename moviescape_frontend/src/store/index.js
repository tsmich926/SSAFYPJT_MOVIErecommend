import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plulgins: [
    createPersistedState(),
  ],

  state: { token:null
  },

  getters: {
    isLogin(state){
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
    // logout
    LogOut(context){
      axios({
        method:'post',
        url:`${API_URL}/accounts/logout/`,        
      })
      .then(res=>{
        console.log(res)
        this.$store.state.token=null
      })
      .catch(err=>{
        console.log(err)
      })
    },
    // login
    LogIn(context,payload){
      const username = payload.username
      const password = payload.password
    
      axios({
        method:'post',
        url:`${API_URL}/accounts/login/`,
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
    //SignUp
    SignUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
