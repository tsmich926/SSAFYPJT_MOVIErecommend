import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],

  state: { token:null,
    movie_id:null,
    actor_id:null,
    director_id:null,
    user_id:null,
    user:null,
    theme:null,
  },

  getters: {
    isLogin(state){
      return state.token ? true:false
    }
  },

  mutations: {
    SAVE_TOKEN(state,token){
      state.token = token
      router.push({name:'MovieList'})
    },
    SAVE_MOVIE_ID(state, movieId) {
      state.movie_id = movieId
    },
    SAVE_ACTOR_ID(state, humanId) {
      state.actor_id = humanId
    },
    SAVE_DIRECTOR_ID(state, humanId) {
      state.director_id = humanId
    },
    SAVE_USER(state,User){
      state.user=User
    },
    SAVE_USER_ID(state,User){
      state.user_id=User
    },
    LOG_OUT(state){
      state.user=null
      state.token=null
    }
  },

  actions: {
    // getpoint
    GetPoint(context,payload){
      const point=this.state.user.point+payload.point
      axios({
        method:'PUT',
        url:`${API_URL}/user/${this.state.user.id}/`,
        data:{
          point
        },
        headers:{
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res=>{
        // console.log("포인트 확인")
        // console.log(res)
        alert(`${payload.point} 포인트를 얻었습니다!`)
        context.commit('SAVE_USER',res.data)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    // logout
    LogOut(context){
      axios({
        method:'post',
        url:`${API_URL}/accounts/logout/`,        
      })
      .then(res=>{
        console.log(res)
        context.commit('LOG_OUT')
        router.push({name:"HomeView"})
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
          console.log(res.data)
          context.commit('SAVE_TOKEN',res.data.key)
          context.dispatch('SaveUser')
          router.push({name:"HomeView"})
        })
        .catch((err)=>{
          console.log(err)
          if(err.response.status==400){
            alert("로그인 정보가 올바르지 않습니다!")
          }
        })
    },
    SaveUser(context){
      console.log(context)
      axios({
        method:'get',
        url:`${API_URL}/user/my_user/`,
        headers:{
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res=>{
        console.log("login dataget되는지")
        console.log(res)
        context.commit('SAVE_USER',res.data)
      })
      .catch(err=>{
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
        },
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch('SaveUser')
        })
        .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
