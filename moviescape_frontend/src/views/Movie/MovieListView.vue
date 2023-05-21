<template>
  <div class= "my_MovieListView_BGC">
    <h1>MovieListView</h1>
    <div>
      <MovieListItems :ITEMmovies="movie_list"/>
    </div>
    <infinite-loading @infinite="getWholeMovies"></infinite-loading>
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import MovieListItems from '@/components/MovieListItems.vue'
export default {
  name:'MovieListView',
  components:{
    MovieListItems,
    InfiniteLoading
  },
  data(){
    return {
      movies:[],
      page:0,
    }
  },
  computed:{
    movie_list(){
      return this.movies
    }
  },
  methods:{
    getWholeMovies($state){ 
      if (window.innerHeight + window.pageYOffset < document.body.offsetHeight - 300) {
        return  // 스크롤이 맨 밑에 닿기 전에 300px 이상 위에서는 호출하지 않음
      }     
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v1/movies/',
        params:{
          page:this.page
        }
      })
      .then((res)=>{
        console.log(res)
        if (res.data.length){
          this.page+=1
          console.log(res)
          this.movies.push(...res.data)
          $state.loaded();
        }else{
          $state.complete()
        }
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  // created(){
  //   this.getWholeMovies()
  // }
}
</script>

<style scoped>
.my_MovieListView_BGC{
  background-color: #1C1918;
  border-radius: 5px;
}
</style>