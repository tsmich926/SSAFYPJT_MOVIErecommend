<template>
  <div class="container my-back-ground">
    <h1 class="my-director-name">{{ Director.name }}</h1>
    <div class="row justify-content-center">
      <div class="col">
        <div class="my-director custom-1dm77tq">
          <img width="400" height="500" :src="`https://image.tmdb.org/t/p/w500/${Director.profile_path}`" alt="...">
        </div>
      </div>
    </div>
    <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
      {{ IsLiked ? '❤' : '🤍'}}
    </button>
    <div>
      <h2 v-if="Director.like_users">
        {{Director.name}}를 좋아하는 사람들 : {{Director.like_users.length}}
      </h2>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <div class="my-wrap"></div>
      </div>
    </div>
    <div class="row justify-content-center list">
      <h1>영화 목록</h1>
      <div>
        <MovieListItemsVue :ITEMmovies="Director.movies"/>
      </div>
    </div>
    <div class="row justify-content-center"></div>
    <div class="row">
      <h2></h2>
    </div>
    <div class="row">
      <h2></h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex';
import MovieListItemsVue from '@/components/MovieListItems.vue'
// import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name:'HumanDetailView',
  components:{
    MovieListItemsVue
  },
  data(){
    return {
      director:{},
      director_id:null,
      searchList:[]
    }
  },
  computed:{
    ...mapState(['user']),
    Director(){
      return this.director
    },
    IsLiked(){
      return this.user.directors.some(director => director.id === this.Director.id);
    },
  },
  methods:{
    likeHuman() {
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/directors/${this.Director.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        // console.log("director확인")
        // console.log(res)
        // console.log(res.data)
        this.director=res.data
        // this.like_cnt=res.data.like_users.length
        this.$store.dispatch('SaveUser')
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getDetailDirector(){ 
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/directors/${this.director_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log("####directordetail")
        console.log(res.data)
        this.director=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
  },
  created(){
    this.director_id=this.$store.state.director_id
    console.log(this.director_id)
    this.getDetailDirector()
  }
}
</script>

<style scoped>
.my-no-wrap {
  display: flex;
  flex-wrap: nowrap;
}

.my-director {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  margin: 0 auto 30px;
  overflow: hidden;
  position: relative;
}

.my-director img {
  width: 100%;
  height: auto;
  object-fit: cover;
}
.my-back-ground{
  padding-top: 10px;
  background-color: black;
  border-radius: 10px;
}
.my-director-name {
  margin-top:1px;
  /* position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%); */
  background-color: rgba(252, 252, 252, 0.7);
  color: #fff;
  padding: 5px 10px;
  font-size: 30px;
  font-family: "Noto Sans KR", "Apple SD Gothic Neo", "Nanum Gothic", "Malgun Gothic", sans-serif;
  font-weight: 600;
}

h1 {
  margin-top: 150px;
}
</style>