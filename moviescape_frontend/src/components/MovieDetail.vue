<template>
  <div>
    <p>pppp</p>
    <h1>검색할 제목을 입력</h1>
    <input type="text" v-model="title" >
    <button @click="getMovie"></button>
    <div>
      <div v-for="movie in movies" :key="movie.pk">
        <h3>제목예정</h3>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'MovieDetail',
  data(){
    return{
      title:null,
      movielist:null,
    }
  },
  methods:{
    getMovie(){
      const title=this.title
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/search/${title}/`

      })
      .then(res=> {
        console.log(res)
        // this.movielist=res
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  computed:{
    movies(){
      return this.movielist
    }
  }

}
</script>

<style>

</style>