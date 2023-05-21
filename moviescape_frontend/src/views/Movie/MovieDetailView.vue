<template>
  <div class= "container">
    <h1>MovieDetailView</h1>
    <!-- {{movie}} -->
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="...">

    <!-- <MovieDetail /> -->

  </div>
</template>

<script>
import axios from 'axios'
// import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name:'MovieDetailView',
  components:{

    // MovieDetail
  },
  data(){
    return {
      movie:{},
    }
  },
  methods:{
    getDetailMovies(){ 
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${this.$route.params.movie_id}`,
      })
      .then((res)=>{
        console.log(res)
        this.movie=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.getDetailMovies()
  }
}
</script>

<style>

</style>