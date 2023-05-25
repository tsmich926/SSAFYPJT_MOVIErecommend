<template>
  <div class= "my_MovieListView_BGC">
    <h1 style="margin-bottom:50px; padding-top:30px;">영화 목록</h1>
    <div>
      <div class="my-margin-bottom">
        <select v-model="selectedItem" @change="selectItem">
          <option value="1">전체</option>
          <option value="28">액션</option>
          <option value="12">모험</option>
          <option value="16">애니메이션</option>
          <option value="35">코미디</option>
          <option value="80">범죄</option>
          <option value="99">다큐멘터리</option>
          <option value="18">드라마</option>
          <option value="10751">가족</option>
          <option value="14">판타지</option>
          <option value="36">역사</option>
          <option value="27">공포</option>
          <option value="10402">음악</option>
          <option value="9648">미스터리</option>
          <option value="10749">로맨스</option>
          <option value="878">SF</option>
          <option value="10770">TV 영화</option>
          <option value="53">스릴러</option>
          <option value="10752">전쟁</option>
          <option value="37">서부</option>
        </select>
      </div>
      <MovieListItems :ITEMmovies="movie_list"/>
    </div>
    <infinite-loading ref="infiniteLoading" @infinite="getWholeMovies"></infinite-loading>
    <p>Data 로딩 완료</p>
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import MovieListItems from '@/components/MovieListItems.vue'

export default {
  name: 'MovieListView',
  components: {
    MovieListItems,
    InfiniteLoading
  },
  data() {
    return {
      movies: [],
      page: 0,
      selectedItem: "1",
      is_completed:false
    }
  },
  computed: {
    movie_list() {
      return this.movies
    }
  },
  methods: {
    selectItem() {
      this.movies = []
      console.log(this.movies)
      this.page = 0
      this.is_completed=false
      this.getWholeMovies()
    },
    getWholeMovies($state) {
      if (window.innerHeight + window.pageYOffset < document.body.offsetHeight - 300) {
        return
      }
      if (!this.is_completed){
        if (this.selectedItem == '1') {
          axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/movies/',
            params: {
              page: this.page
            },
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              if (res.data.length) {
                this.page += 1
                this.movies.push(...res.data)
                $state.loaded();
              } else {
                this.is_completed=true
                // $state.complete()
              }
            })
            .catch(err => {
              console.log(err)
            })
        } else {
          const genre_id = this.selectedItem
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/genres/${genre_id}/`,
            params: {
              page: this.page
            },
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              if (res.data.length) {
                this.page += 1
                this.movies.push(...res.data)
                $state.loaded();
              } else {
                this.is_completed=true
                // $state.complete()
              }
            })
            .catch(err => {
              console.log(err)
            })
        }
      }
    }
  },
}
</script>


<style scoped>
.my_MovieListView_BGC {
  background-color: #1C1918;
  border-radius: 5px;
}
.my-margin-bottom{
  margin-bottom: 20px;
}

/* 드롭다운 스타일링 */
select {
  padding: 10px;
  font-size: 16px;
  border: none;
  width: 50%;
  border-radius: 5px;
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center; /* 옵션을 왼쪽에 정렬 */
}

option {
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center; /* 옵션을 왼쪽에 정렬 */
}
</style>