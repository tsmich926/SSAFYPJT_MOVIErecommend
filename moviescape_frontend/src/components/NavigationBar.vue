<template>
  <div>
     <nav class="navbar fixed-nav my_navBar"> <!--//여기에수정 -->
      <div class="scroll-wrapper">
        <router-link :to="{name:'HomeView'}">
          <img src="@/assets/MainLogo.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top">
          <p>
          MOVIESCAPE
          </p>
        </router-link>
        <!-- <a class="navbar-brand" href="/">
          
        </a> -->
        <router-link class="rout-bar" :to="{name:'MovieListView'}">영화</router-link>
        <!-- <router-link :to="{name:'GenreListView'}">GLV</router-link> -->
        <router-link class="rout-bar" to="/HumanListView">출연진</router-link>
        <router-link class="rout-bar" to="/RecommendView">영화 추천받기</router-link>
        <router-link class="rout-bar" to="/ReviewListView">리뷰</router-link>
        <router-link v-if="user" to="/MyDetailView">
          <img class="profile-image"  type="circle" :src="`${UserProfile}`" alt=""> &nbsp; {{user.username}}
        </router-link>
        <a v-if="user">point : {{user.point}}</a>
        <router-link class="rout-bar" v-show="!isLogin" to="/LoginView">로그인</router-link>
        <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>
        <img src="http://decoder.kr/wp-content/uploads/2020/03/decoder_smallver.gif" alt="Decoder / 디코더" width="50" height="50" >
        <MovieSearchItems/>
      </div>
    </nav>
    <router-view />
    <div class="footer_space"></div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import MovieSearchItems from '@/components/MovieSearchItems.vue';
export default {
  name: "NavigationBar",
  components:{
    MovieSearchItems,
  },
  computed: {
    ...mapState(['user']),
    isLogin() {
      return this.$store.getters.isLogin;
    },
    UserProfile(){
      if (this.user.profile_path=='default'){
        return 'http://localhost:8080/user/default.png'
      }else{
        return this.user.profile_path
      }
    },
  },
  methods: {
    LogOut() {
      this.$store.dispatch('LogOut');
    }
  }
}
</script>

<style>
.rout-bar{
  border: solid white 1px;
  border-radius: 3px;
  padding:10px;
}
.profile-image {
  height: 40px;
  width: 40px;
  object-fit: cover;
  border-radius: 50%;
  margin-right: 5px;
}
/* overflow-x: auto; */
#navbar-container {
  width: 100%;
}

nav a {
  font-weight: bold;
  color: #fff;
  text-decoration: none;
}

nav a.router-link-exact-active {
  background-color:#303133;
  color: rgb(255, 90, 0);
  /* border: solid #008080 1px; */
  /* color: #008080; */
  /* border: solid rgb(255, 90, 0) 1px; */
  border: solid white 1px;
  border-radius: 3px;
  padding:10px;
}

.my_navBar {
  justify-content: center;
  align-content: center;
  text-align: center;
  position: fixed;
  left: 0;
  top: 0;
  width: 95%;
  margin-top: auto;
  z-index: 9999;
  background-color:black;
}

.scroll-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

.scroll-wrapper > * {
  margin-right: 10px;
  white-space: nowrap;
}

.navbar-brand img {
  margin-right: 5px;
}

.btn-primary {
  background-color: #222;
  border-color: #fff;
}

.btn-primary:hover {
  background-color: #fff;
  color: #222;
}
</style>