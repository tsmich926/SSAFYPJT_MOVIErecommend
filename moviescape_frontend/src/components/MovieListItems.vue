<template>
  <div>
    <h1>MovieListItems</h1>
    <div>
      <div class="card" style="width: 18rem;">
        <img :src="`https://image.tmdb.org/t/p/w500/`" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">weeeeeeeeeeeeeeeeeeesdfzsdfasfdasdfasdf</h5>
          <p class="card-text">weeeeeeeeeeeeeeeeeeesdfzsdfasfdasdfasdfweeeeeeeeeeeeeeeeeeesdfzsdfasfdasdfasdfweeeeeeeeeeeeeeeeeeesdfzsdfasfdasdfasdf</p>
        </div>
      </div>
      <div class="card" style="width: 18rem;">
        <img src="`https://image.tmdb.org/t/p/w500/`" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>      
    </div>
    <div>
      <div v-for="movie in ITEMmovies" :key="movie.pk" >
        <!-- <MovieCard :CARDmovie="movie"/> -->
        <MovieCard :CARDmovie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
// import MovieCard from '@/components/test2.vue'
export default {
  name:'MovieListItems',
  components:{
    MovieCard
  },
  data(){
    return{

    }
  },
  props:{
    ITEMmovies:Array
  },
  methods:{
    

  }

}
</script>

<style>

</style>