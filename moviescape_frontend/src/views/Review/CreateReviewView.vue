<template>
  <div>
    <h2>새로운 글 등록</h2>
    <div class="board-detail">
      <form action="">
        <div class="board-contents">
          <div class="search-wrapper">
            <div class="search-input-container">
              <input
                type="text"
                @keyup.enter="searchMovie"
                v-model.trim="SearchTitle"
                class="search-input"
                placeholder="영화를 검색하세요"
                style="width:100%;"
              />
              <input
                type="button"
                @click="searchMovie"
                class="btn btn-primary"
                value="검색"
              />
            </div>
            <div class="here">
              <img v-if="this.movie_id" :src="`https://image.tmdb.org/t/p/w500/${movie_poster_path}`" style="height:50px;" alt="">
            </div>
            <ul v-if="showResults" class="search-results">
              <li v-for="movie in searchResults" :key="movie.id" class="search-result-item">
                <div @click="selectMovie(movie)" class="search-result-item-title">{{ movie.title }}
                  <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" style="width:50px; height: 70px;" alt="">
                </div>
              </li>
            </ul>
          </div>
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" class="input-field" placeholder="제목을 입력해주세요."><br>
          <label for="input">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="content" placeholder="리뷰를 작성해주세요."></textarea><br>
        </div>
      </form>
      <div class="common-buttons">
        <input type="button" @click="saveArticle" class="btn btn-primary" style="background-color: #008080;" value="작성완료">&nbsp;
        <input type="button" @click="gotoComunityView" class="btn btn-primary" style="background-color: #008080;" value="목록">&nbsp;
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default { 
  name: 'CreateReviewView',
  data() {
    return {
      content: null,
      title: null,
      SearchTitle: null,
      searchResults: [],
      showResults: false,
      movie_id: null,
      movie_poster: null,
      ratings: 0,
    }
  },
  methods: {
    setRating(value) {
      this.ratings = value; // ratings 값을 업데이트
      console.log(this.ratings)
    },    
    selectMovie(movie) {
      console.log(movie)
      this.movie_id = movie.id
      this.searchResults = []
      this.movie_poster = movie.poster_path
    },
    getPoint(){
      const point = 20
      const profile_path='default'
      const payload = {
        point,profile_path
      }

      this.$store.dispatch('GetPoint',payload)
    },
    saveArticle() {
      const API = 'http://127.0.0.1:8000'
      const title = this.title
      const content = this.content
      const movie_id = this.movie_id
      if (!title) {
        alert('제목을 입력하세요')
        return
      } else if (!content) {
        alert('내용을 입력하세요')
        return
      } else if (!movie_id) {
        alert('영화를 선택하세요')
        return
      }
      axios({
        method: 'post',
        url: `${API}/api/v1/movies/${movie_id}/review/`,
        data: {
          title,
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.getPoint()
          this.$router.push({ name: 'ReviewListView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
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
            this.searchResults = res.data;
            this.showResults = true; // 검색 결과를 표시합니다
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    gotoComunityView() {
      this.$router.push({
        name: "ReviewListView",
      });
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

<style>
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-size: 14px;
}

.input-field {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}
.search-wrapper {
  position: relative;
  margin-bottom: 10px;
}

.search-input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.search-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 8px;
}

.search-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #008080;
  color: #fff;
  cursor: pointer;
}

.search-results {
  position: absolute;
  z-index: 1;
  width: 100%;
  background-color: #fff;
  list-style-type: none;
  padding: 0;
  margin-top: 4px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.search-result-item {
  padding: 8px;
  cursor: pointer;
}

.search-result-item-title {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 4px;
  color: black;

}

.here img {
  width: 50px;
  height: 70px;
  object-fit: cover;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background-color: #222;
  border-color: #fff;
}

.btn-primary:hover {
  background-color: #fff;
  color: #222;
}
</style>
