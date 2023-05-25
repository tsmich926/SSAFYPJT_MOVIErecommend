<!-- Post.vue -->
<template>
  <div v-if="Review" class="post-container" style="padding-left:100px; padding-right:100px;">
    <div style="width:100%">
      <div class="post">
        <img @click="gotoMovieDetail" :src="`https://image.tmdb.org/t/p/w500/${Review.movie.poster_path}`" style="margin-bottom:20px; width:100%;" alt=""> 
        <h4 @click="gotoReviews" ref="authorDiv" style="margin-bottom:20px;" @mouseover="setCursor('pointer')" @mouseout="setCursor('auto')">
          목록가기
        </h4>
        <div class=" my-review-post">
          <h2 class="post-title">리뷰 : {{Review.title}}</h2>
          <div class="post-content">
            상세 리뷰 : {{Review.content}}
          </div>
          <div class="post-author">
            작성자: {{Review.user.username}}
          </div>
          <div class="post-date">
            작성일: {{formatDate(Review.created_at)}}
        </div>
        </div>
      </div>
      <div class="comment-board">
        <CommentListItems :ITEMcomments="ReviewComments" @commentDeleted="getReviewDetail()"/>
        <div class="comment-form">
          <textarea v-model="newComment" @keyup.enter="addComment" placeholder="댓글을 입력하세요"></textarea>
          <button class="btn btn-primary" @click="addComment">댓글 달기</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import CommentListItems from '@/components/CommentListItems.vue'
import axios from 'axios';
export default {
  components: {
    CommentListItems,
  },
  data(){
    return{
      review_id:null,
      review:null,
      comments:null,
      newComment:'',
    }
  },
  computed:{
    Review(){
      return this.review
    },
    ReviewComments(){
      return this.Review.comment_set
    }
  },
  methods: {
    gotoMovieDetail() {
      const movieId = this.Review.movie.id; // 이동할 영화의 ID를 동적으로 설정할 수 있음
      // console.log("MovieCard")
      // console.log(movieId)
      this.$router.push({ name: 'MovieDetailView', params: { id: movieId } });
    },
    setCursor(cursorType) {
      this.$refs.authorDiv.style.cursor = cursorType;
    },
    gotoReviews(){
      this.$router.push({name:'ReviewListView'})
    },
    addComment() {
      const review_id=this.$route.params.id
      console.log("RRRRRRRRRR")
      console.log(review_id)
      const comment=this.newComment
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${review_id}/comment/`,
        data: {
          comment,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log(res)
        this.newComment=null
        this.getReviewDetail()
      })
      .catch(err=>{
        console.log(err)
      })
    },
    formatDate(date) {
      // 날짜 형식을 원하는 형태로 변환하는 함수
      // 예: 2023-05-24 -> 2023년 5월 24일
      return new Date(date).toLocaleDateString('ko-KR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },
    getReviewDetail(){
      const review_id=this.review_id
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/reviews/${review_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        this.review=res.data
        console.log("리뷰의 response")
        console.log(res)
      })
      .catch(err=>{
        console.log(err)
      })
    },
  },
  created(){
    this.review_id = this.$route.params.id
    this.getReviewDetail()
  }
};
</script>
<style scoped>
.post-container {
  background-color: #000;
  color: #fff;
  border-radius: 5px;
  padding: 20px;
  display: flex;
  justify-content: center;
}

.post-title {
  font-size: 24px;
  margin-bottom: 10px;
  color: #0f9;
}

.post-content {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 10px;
}

.post-author,
.post-date {
  font-size: 14px;
  margin-bottom: 5px;
}

.post-date {
  color: #ccc;
}
.comment-board {
  background-color: black;
  color: white;
  padding: 20px;
}

.comment-list {
  margin-bottom: 20px;
}
.my-review-post{
  background-color: rgba(255, 255, 255, 0.1);
  margin-bottom: 10px;
  border-radius: 5px;
  width: 100%;
}
.comment {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 10px;
  margin-bottom: 10px;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}

.comment-author {
  font-weight: bold;
}

.comment-date {
  font-size: 12px;
}

.comment-form {
  display: flex;
  margin-top: 20px;
}

.comment-form textarea {
  flex: 1;
  padding: 10px;
  resize: none;
  border: none;
  background-color: white(255, 255, 255, 0.1);
  color: #0c0c0c;
}

.comment-form button {
  margin-left: 10px;
}
</style>