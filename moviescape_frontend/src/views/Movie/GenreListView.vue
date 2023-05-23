<template>
  <div class= "my_MovieListView_BGC">
    <h1>내가 선호하는 장르 목록</h1>
    <div v-for="genre in Genres" :key="genre.id">
      <GenreItems :Genre="genre"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import GenreItems from '@/components/GenreItems.vue'
export default {
  name:'GenreListView',
  components:{
    GenreItems,
  },
  data(){
    return {
      genres:[],
    }
  },
  computed:{
    movie_list(){
      return this.movies
    },
    Genres(){
      return this.genres
    }
  },
  methods:{
    getWholeGenres(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v1/genres/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.genres=res.data
        console.log(this.genres)
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.getWholeGenres()
  }
}
</script>

<style scoped>
.my_MovieListView_BGC{
  background-color: #1C1918;
  border-radius: 5px;
}
</style>