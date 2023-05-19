<template>
  <div class= "container">
    <div class="row">
        <div class="card-body">
          <h1 class="card-title">movie.title</h1>
          <p class="card-text">movie.overview</p>
        </div>
      <!-- </div> -->
    </div>
    <MovieDetail />
  </div>
</template>

<script>
export default {
  name:'MovieList',
  componenets:'MovieDetail',
  data(){
    return {
      movies: []
    }
  }
}
</script>

<style>

</style>