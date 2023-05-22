<template>
  <div>
    <h1>CreateReviewView</h1>
    <h2>새로운 글 등록</h2>
    <div class="board-detail">
      <form action="">
        <div class="board-contents">
          <div class="search-wrapper">
            <v-text-field
              v-model="searchTerm"
              filled
              outlined
              rounded
              dense
              @focus="autoSearchList = true">
            </v-text-field>
            <!-- <input type="text" v-model.trim="searchTerm" class="search-input" placeholder="영화를 검색하세요"  @keyup.enter="searchMovie" > -->
              <transition name="top-slide" mode="in-out">
                <div class="justify-center align-center flex-column d-flex">
                  <v-list class="pa-0 ma-0 search-list" v-show="autoSearchList" light>
                    <v-list-item-group>
                      <v-hover v-slot="hover"
                    v-for="movie in movies"
                    :key="movie.pk" 
                      >   

                      <v-list-item
                  class="pa-3 pl-5 top-list"
                  :class="{ 'on-hover': hover }"
                  @click="searchTerm=movie.Title"
                    >

                    <v-card
                    class="search-list-img"
                    elevation="1"
                    tile
                >
                  <!-- <img
                      :src="item.bookThumb"
                      alt="bookThumb"
                      height="100%"
                      @click="detailView(item.bid)"
                  > -->
                </v-card>

                  <v-list-item-group />
                <v-hover/>
              </v-list-item-group>
            </v-list>
          </div>
        </transition>



            <!-- <input type="button" class="search-button" value="검색create"  @click="searchMovie">            
            <li v-for="movie in movies" :key="movie.pk" >
              <i class="search-result">{{movie.title}}영화를 선택하셨습니다</i>
            </li>
          <label for="title">제목</label>
            <input type="text" v-model.trim="title" class=" input-field " placeholder="제목을 입력해주세요."><br>
          <label for="input">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="content" placeholder="리뷰를 작성해주세요."></textarea><br> -->
          </div>
        </div>
      </form>
      <div class="common-buttons">
        <input type="button" @click="saveArticle" class="btn btn-primary" style="background-color: #008080;" value="작성완료">&nbsp;
        <!-- <input type="button" @click="gotoComunityView" class="btn btn-primary" style="background-color: #008080;" value="목록">&nbsp; -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default { 
  name:'CreateReviewView',
  data(){
    return{
      content:null,
      title:null,
      searchTerm:null,
      movie_list:null,
      showResults: false,
      
    }
  },
  methods:{
    // gotoComunityView(){
    //   this.$router.push({name:'ReviewListView'})

    
    saveArticle(){
      const API ='http://127.0.0.1:8000'
      
      const title = this.title
      const content = this.content

      if(!title){
        alert('제목을 입력하세요')
      } else if (!content){
        alert('내용을 입력하세요')
        return
      }
    
      axios({
        method:'post',
        url:`${API}/api/v1/movies/38015/review/`,
        data: {
          title,
          content,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name:'ReviewListView'})
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    searchMovie(){
      if (this.searchTerm) {
        const title=this.searchTerm
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/search/${title}/`

      })
      .then(res=> {
        this.movie_list=[]
        console.log(res)
        if (res.data.length<3){
          this.movie_list=res.data
        }
        else{
          for (let i=0; i<3; i++){
            this.movie_list.push(res.data[i])
          }
        }
        // this.movie_list=res.data
      })
      .catch(err=>{
        console.log(err)
      })
      }
    },
    
  },

  computed:{

    movies(){
      return this.movie_list
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
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}


</style>