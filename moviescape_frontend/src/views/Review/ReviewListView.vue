<template>
  <div class = "reviewlist">
    <p>ReviewListView</p>
    <!-- <div v-for="review in review_list" :key="review.title"> -->
      <!-- <h3>리뷰제목 : {{review.title}}</h3>
      <br>
      <h3>리뷰내용 : {{review.content}}</h3>
      <hr>
      <img :src="`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`" alt=""> -->
      <!-- {{review.likes}}
      <br>
      {{review.movie.title}}
      <br>
      {{review.movie.overview}} -->
      <hr>
    <!-- </div> -->
    <div class="row"> 
      <p>게시글</p>
      <!-- <input type="button" value="게시글 작성" @click="gotoCreateArticle"> -->
      <div class="d-flex">
        <button class="btn btn-outline-light" type="button" @click="gotoCreateArticle">글쓰기</button>
      </div>
      <ReviewItems :ITEMreviews="review_list"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewItems from '@/components/ReviewItems.vue'

export default {
  name:'ReviewListView',
  
  components: { 
    ReviewItems    
  },
  data(){
    return{
      reviews:null,
    }
  },
  computed:{
    review_list(){
      return this.reviews
    }
  },
  methods:{
    gotoCreateArticle(){
      this.$router.push({name:'CreateReviewView'})
    },
    getReviews(){
      const API ='http://127.0.0.1:8000'
      axios({
        method:'get',
        url:`${API}/api/v1/reviews/`,
      })
      .then(res=>{
        console.log(res)
        this.reviews=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.getReviews()
  }
}
</script>



<style scoped>
.btn-save,
.btn-list {
  width: 200px; /* 원하는 너비 값으로 수정 */
  height: 100px; /* 원하는 높이 값으로 수정 */
}
</style>