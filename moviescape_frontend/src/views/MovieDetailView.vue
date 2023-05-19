<template>
  <div class= "container">
    <h1>wfweffwewf</h1>
    왜 안나와
    <MovieDetail />
  </div>
</template>

<script>
import MovieDetail from '../components/MovieDetail.vue'
export default {
  name:'MovieDetailView',
  componenets:{

    MovieDetail
  },
  data(){
    return {
      movies: []
    }
  }
}
</script>

<style>

</style>