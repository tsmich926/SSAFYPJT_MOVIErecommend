<template>
  <div>
    <div class="search-wrapper">
      <div class="search-input-container">
        <input
          type="text"
          @keyup.enter="searchMovie"
          v-model.trim="SearchTitle"
          class="search-input"
          placeholder="영화를 검색하세요"
          style="min-width:400px;"
        />
        <input
          type="button"
          @click="searchMovie"
          class="search-button"
          value="검색"
        />
      </div>
      <div class="here">
        <img v-if="this.movie_id" :src="`https://image.tmdb.org/t/p/w500/${movie_poster_path}`" style="height:50px;" alt="">
      </div>
      <ul v-if="showResults" class="search-results">
        <li v-for="movie in searchResults" :key="movie.id" class="search-result-item">
          <div @click="gotoDetail(movie)" class="search-result-item-title">{{ movie.title }}
            <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" style="width:50px; height: 70px;" alt="">
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'MovieSearchItems',
  data(){
    return {
      content: null,
      title: null,
      SearchTitle: null,
      searchResults: [],
      showResults: false,
      movie_id: null,
      movie_poster: null,
    }
  },
  methods:{
    searchMovie() {
      if (this.SearchTitle) {
        const title = this.SearchTitle;
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/api/v1/movies/search/${title}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then((res) => {
            console.log("########입력")
            console.log(res)
            if (res.data.length<3){
              this.searchResults = res.data;
              this.showResults = true; // 검색 결과를 표시합니다
            }else{
              this.searchResults=[]
              for(let i=0; i<3; i++){
                this.searchResults.push(res.data[i]);
                this.showResults = true;
              }
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    toNull(){
      this.SearchTitle=null
    },
    gotoDetail(movie){
      const currentRoute = this.$router.currentRoute

      console.log("실험this.searchTitle")
      console.log(this.SearchTitle)
      // 현재 경로와 목표 경로가 동일한지 확인
      if (currentRoute.path !== `/MovieDetailView/${movie.id}`) {
        this.$store.commit('SAVE_MOVIE_ID', movie.id)
        this.SearchTitle=null
        console.log(this.SearchTitle)
        this.searchResults=[]
        this.$router.push(`/MovieDetailView/${movie.id}`)
      }
    }
  },
  computed: {
    movies() {
      return this.movie_list
    },
    movie_poster_path() {
      return this.movie_poster
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