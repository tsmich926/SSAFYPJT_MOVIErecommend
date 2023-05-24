<!-- Post.vue -->
<template>
  <div v-if="Review" class="post-container">
    <div class="post">
      <h2 class="post-title">{{Review.title}}</h2>
      <div class="post-content">
        {{Review.content}}
      </div>
      <div class="post-author">
        작성자: {{Review.user.username}}
      </div>
      <div class="post-date">
        작성일: {{formatDate(Review.created_at)}}
      </div>
    </div>
    <div>
      <CommentListItems :ITEMcomments="ReviewComments"/>
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
      comment_content:null,
    }
  },
  computed:{
    Review(){
      return this.review
    },
    ReviewComments(){
      return this.Review.comments
    }
  },
  methods: {
    saveComment(){
      console.log("n")
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
    getReviewDetail(review_id){
      console.log(review_id)
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/reviews/${review_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        this.review=res.data
        console.log(res)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    gotoComunityView() {
      this.$router.push({
        name: "ReviewListView",
      });
    }
  },
  created(){
    this.review_id = this.$route.params.id
    this.getReviewDetail(this.review_id)
  }
};
</script>
<style scoped>
.post-container {
  background-color: #000;
  color: #fff;
  border-radius: 5px;
  padding: 20px;
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
</style>