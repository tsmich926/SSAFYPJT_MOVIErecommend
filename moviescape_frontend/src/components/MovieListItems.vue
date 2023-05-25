<template>
  <div>
    <div class="container justify-content-center text-center">
      <div class="row">
        <div class="col d-flex justify-content-center" v-for="movie in ITEMmovies" :key="movie.id">
          <MovieCard :CARDmovie="movie"/>
        </div>
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
/* .my-min-card{
  display:flex;
  justify-content: center;
  flex-grow: 0;
  min-width: 200px;
  min-height: 400px;
} */
</style>