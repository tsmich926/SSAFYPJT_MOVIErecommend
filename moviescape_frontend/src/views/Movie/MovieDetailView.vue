<template>
  <div class= "container justify-content-center align-items-center">
    <h1>MovieDetailView</h1>
      <!-- {{movie}} -->
    <div class="row my-no-wrap ">
      <div class="col my-container-width">
        <img class="" width="400" height="500" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="...">
      </div>
      <div class="col my-container-width">
        <iframe id="player" type="text/html" width="600" height="500"
          :src="`https://www.youtube.com/embed/${youtube_key}`"
          frameborder="0"></iframe>
      </div>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <h2 class="my-no-wrap">{{movie.title}}</h2>
      </div>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <div class="my-wrap">{{movie.overview}}</div>
      </div>
    </div>
    <div class="row justify-content-center">
      <h1>영화 감독</h1>
      <DirectorListItems :ITEMdirectors="movie.directors"/>
    </div>
    <div class="row justify-content-center">
      <h1>출연 배우</h1>
      <HumanListItems :ITEMhumans="movie.actors"/>
    </div>
    <div class="row">
      <h2>{{movie.genres}}</h2>
    </div>
    <div class="row">
      <h2>{{movie.reviews}}</h2>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
import HumanListItems from '@/components/HumanListItems.vue'
import DirectorListItems from '@/components/DirectorListItems.vue'
// import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name:'MovieDetailView',
  components:{
    HumanListItems,
    DirectorListItems
  },
  data(){
    return {
      movie:{},
      movie_id:null,
      youtubeEmbed:"https://www.youtube.com/embed/",
      y_key:null,
      searchList:[]
    }
  },
  computed:{
    youtube_key(){
      return this.y_key
    }
  },
  methods:{
    getDetailMovies(){ 
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${this.movie_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log("movieDetail")
        console.log(res)
        this.movie=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getMovieTrailer(){
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${this.movie_id}/videos`,
        params: {
            api_key: '77347a1bf275c0c7fd3a5066b945c759',
            language: 'Ko',
          },

      })
      .then(res=>{
        console.log("##################")
        console.log(res.data.results[0].key)
        this.y_key=res.data.results[0].key
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.movie_id=this.$store.state.movie_id
    console.log(this.movie_id)
    this.getDetailMovies()
    this.getMovieTrailer()
  }
}
</script>

<style scoped>
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