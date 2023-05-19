<template>
  <div id="navbar-container">
    <nav class="navbar my_navBar fixed-nav">
      <div class="scroll-wrapper">
        <a class="navbar-brand" href="/">
          <img src="@/assets/escape.webp" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
          Moviescape
        </a>
        <router-link to="/MovieList">MovieList</router-link>
        <router-link to="/MovieDetailView">MovieDetail</router-link>
        <router-link to="/Recommend">Recommendation</router-link>
        <router-link to="/Community">Community</router-link>
        <router-link v-show="!isLogin" to="/Login">로그인</router-link>
        <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>
      </div>
    </nav>

    <!-- <nav class="navbar my_navBar fixed-nav">
      <div class="container-fluid scroll-wrapper">
        <a class="navbar-brand" href="/">
          <img src="@/assets/escape.webp" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
          Moviescape
        </a>
        <div class="scroll-wrapper">
        <router-link to="/MovieList">MovieList</router-link>
        <router-link to="/MovieDetailView">MovieDetail</router-link>
        <router-link to="/Recommend">Recommendation</router-link>
        <router-link to="/Community">Community</router-link>
        <router-link v-show="!isLogin" to="/Login">로그인</router-link>
        <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>
        </div>
      </div>
    </nav> -->

    <!-- <nav class="">
      <div class="scroll-wrapper">
        <router-link to="/MovieList">MovieList</router-link>
        <router-link to="/MovieDetailView">MovieDetail</router-link>
        <router-link to="/Recommend">Recommendation</router-link>
        <router-link to="/Community">Community</router-link>
        <router-link v-show="!isLogin" to="/Login">로그인</router-link>
        <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>
      </div>
    </nav> -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('LogOut');
    }
  }
}
</script>

<style scoped>
#navbar-container {
  /* overflow-x: auto; */
  width:100%;
  white-space: nowrap;
}

.horizontal-scroll {
  display: flex;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.5) transparent;
}

.horizontal-scroll::-webkit-scrollbar {
  height: 10px;
}

.horizontal-scroll::-webkit-scrollbar-track {
  background-color: transparent;
}

.horizontal-scroll::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}

.scroll-wrapper {
  display: inline-flex;
  padding: 10px;
  background-color: rgb(55, 58, 58);
}

.scroll-wrapper > * {
  margin-right: 10px;
}
</style>
