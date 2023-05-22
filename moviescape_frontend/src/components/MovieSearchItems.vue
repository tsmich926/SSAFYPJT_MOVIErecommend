<template>
  <div>
    <input type="text" v-model="title" @input="getMovie">
    <button @click="toNull">초기화</button>
    <div class="my-absolute-position">
      <div class="" v-for="movie in movies" :key="movie.pk">
       <div>
          <h3>
            <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="">
          </h3>
          <h3>{{movie.title}}</h3>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'MovieSearchItems',
  data(){
    return{
      title:null,
      movie_list:null,
    }
  },
  methods:{
    getMovie(){
      const title=this.title
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/search/${title}/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=> {
        console.log(res)
        this.movie_list=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    toNull(){
      this.title=null
    }
  },
  computed:{
    movies(){
      return this.movie_list
    }
  }

}
</script>

<style scoped>
.my-absolute-position {
  position: absolute;
  /* 다른 스타일 설정 */
}

.my-floating-element {
  position: absolute;
  top: 0;
  left: 0;
  /* 다른 스타일 설정 */
}
</style>