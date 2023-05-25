<template>
  <div class = "reviewlist">
    <hr>
    <div class="row"> 
      <p>게시글</p>
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
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
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
.reviewlist{
  background-color: black;
}
.btn-save,
.btn-list {
  width: 200px; /* 원하는 너비 값으로 수정 */
  height: 100px; /* 원하는 높이 값으로 수정 */
}
</style>