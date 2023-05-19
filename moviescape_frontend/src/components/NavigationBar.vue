<template>
  <div id="app">
    <nav>
      <!-- <router-link to="/">Home</router-link> | -->
      <router-link to="/MovieList">MovieList</router-link>|
      <router-link to="/Recommend">Recommendation</router-link>|
      <router-link to="/Community">Community</router-link>|
      <router-link to="/Login">로그인</router-link>|
      <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>|
      <!-- <TesT /> -->
      <router-view />
    </nav>
    <input type="text " placeholder="영화를 검색해 보세요" v-model="keyword">
    <input type="submit" value="검색">
  </div>
</template>

<script>
// import TesT from '@/components/TesT.vue'
export default {
  components:{
    // TesT
  },
  name: "NavigationBar",
  computed:{
    isLogin(){
      return this.store.$getters.isLogin
    }
  },
  methods:{
    LogOut(){
      this.$store.dispatch('LogOut',payload)
    },
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ebeef1;

}

nav {
  padding: 30px;
  font-size: 50px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

button {
  width: 100px;
  height: 100px;
}
</style>