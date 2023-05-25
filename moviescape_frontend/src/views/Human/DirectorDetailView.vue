<template>
  <div class= "container">
    <h1>DirectorDetailView</h1>
      <!-- {{movie}} -->
    <div class="row my-no-wrap ">
      <div type="circle" class="col my-container-width my-director">
        <img class="" width="400" height="500" :src="`https://image.tmdb.org/t/p/w500/${Director.profile_path}`" alt="...">
      </div>
    </div>
    <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
      {{ IsLiked ? '❤' : '🤍'}}
    </button>
    <div class="row my-no-wrap">
      <div class="col">
        <h2 class="my-no-wrap">감독 이름 : {{Director.name}}</h2>
      </div>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <div class="my-wrap"></div>
      </div>
    </div>
    <div class="row justify-content-center">
      <h1>영화 목록</h1>
      <MovieListItemsVue :ITEMmovies="Director.movies"/>
    </div>
    <div class="row justify-content-center">
      <h1>출연 배우</h1>
    </div>
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
        this.like_cnt=res.data.like_users.length
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
.my-director{
  display: flex;

}
.my-no-wrap{
  display: flex;
  flex-wrap: nowrap;
}
.my-container-pr{
  justify-content: center;
  align-content: center;
}
.my-container-width{
  width:600px;
}
/* .no-wrap{
  white-space: nowrap;  
} */
.my-wrap {
  white-space: normal;
}
</style>