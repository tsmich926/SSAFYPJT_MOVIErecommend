<template>
  <div>
    <h1>MovieListItems</h1>
    <div>
      <div v-for="movie in ITEMmovies" :key="movie.pk" >
        <MovieCard :CARDmovie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
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