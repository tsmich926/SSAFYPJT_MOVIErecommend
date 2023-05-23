<template>
  <div class= "container justify-content-center align-items-center">
    <h1>MovieDetailView</h1>
      <!-- {{movie}} -->
    <div class="row my-no-wrap ">
      <div class="col my-container-width">
        <img class="" width="400" height="500" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="...">
      </div>
      <div class="col my-container-width">
        <iframe id="player" type="text/html" width="600" height="500"
          :src="`https://www.youtube.com/embed/${youtube_key}`"
          frameborder="0"></iframe>
      </div>
    </div>
    <div>
      <button class="btn btn-primary" @click="likeMovie">좋아요</button>
      <h4>좋아하는 유저 수 : {{ LikeCnt }}</h4>
    </div>
    <div class="rating-container">
      <label for="ratings">Rating</label>
      <div class="rating">
        <span v-for="i in 10"
          :key="i"
          class="rating-icon"
          :class="{ 'active': RatingScore >= i }"
          @click="setRating(i)">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 22 22" fill="#eee" class="css-fnwbjg">
            <g fill-rule="evenodd">
              <path d="M11 16.556L3.83 21.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 6.06c-.787-.569-.383-1.812.588-1.81l9.33.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 9.33-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L11 16.556z"></path>
            </g>
          </svg>
        </span>
      </div>
    </div>
      <h4>유저 평균 평점 : {{RatingAverage}}</h4>
    <div class="row my-no-wrap">
      <div class="col">
        <h2 class="my-no-wrap">{{movie.title}}</h2>
      </div>
    </div>
    <div class="row">
      <TestReview/>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <div class="my-wrap">{{movie.overview}}</div>
      </div>
    </div>
    <div class="row justify-content-center">
      <h1>영화 감독</h1>
      <DirectorListItems :ITEMdirectors="movie.directors"/>
    </div>
    <div class="row justify-content-center">
      <h1>출연 배우</h1>
      <ActorListItems :ITEMactors="movie.actors"/>
    </div>
    <div class="row">
      <h2>{{movie.genres}}</h2>
    </div>
    <div class="row">
      <div v-for="review in movie.reviews" :key="review.id">
        <h2>리뷰 유저 : {{review.user.username}} / 제목 : {{review.title}}</h2>
      </div>
      <!-- v-for review in movie.reviews
          <ReviewCard :reveiw="review"/>
       -->
    </div>


  </div>
</template>

<script>
import TestReview from '@/components/TestReview.vue'
import axios from 'axios'
import ActorListItems from '@/components/ActorListItems.vue'
import DirectorListItems from '@/components/DirectorListItems.vue'
// import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name:'MovieDetailView',
  components:{
    ActorListItems,
    DirectorListItems,
    TestReview
  },
  
  data(){
    return {
      movie:{},
      movie_id:null,
      youtubeEmbed:"https://www.youtube.com/embed/",
      y_key:null,
      searchList:[],
      like_cnt:0,
      rating:0,
      rating_pk:null,
      rating_average:0,
      is_rated:false,
      rating_cnt:0,
    }
  },
  computed:{
    youtube_key(){
      return this.y_key
    },
    LikeCnt(){
      return this.like_cnt
    },
    RatingScore(){
      // console.log(this.rating)
      return this.rating
    },
    RatingAverage(){
      return this.rating_average
    },
  },
  methods:{
    getRating(){
      axios({
          method:'get',
          url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_id}/getrating/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          // console.log("get ratting입니당당ㄷ")
          // console.log(res)
          // console.log(res.data.score)
          if (res.status==201){
            this.rating=res.data.score
            this.rating_id=res.data.pk
            this.is_rated=true
          }
        })
        .catch((err) => {
          console.log("내가 에러")
          console.log(err)
        })
    },
    setRating(rating){
      // console.log(this.rating)
      // console.log(typeof(this.rating))
      let rating_sum=this.rating_average*this.rating_cnt-this.rating
      this.rating=rating
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_id}/rating/`,
        data: {
          score:this.rating,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // console.log(res)        
        // console.log(this.rating_average,this.rating_cnt,this.rating)
        // console.log(rating_sum)
        this.rating=res.data.score
        this.rating_id=res.data.id
        if (!this.is_rated){
          this.is_rated=true
          this.rating_cnt+=1
        }
        this.rating_average=(rating_sum+this.rating)/this.rating_cnt
        console.log(this.rating_average)
      })
      .catch((err) => {
        console.log(err)
      }) 
    },
    likeMovie() {
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/movies/${this.movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        // console.log("movie확인")
        // console.log(res.data)
        this.movie=res.data
        this.like_cnt=res.data.like_users.length
        this.$store.dispatch('SaveUser')
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getDetailMovies(){ 
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${this.movie_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        // console.log("movieDetail")
        console.log(res)
        this.movie=res.data
        // console.log("like_users")
        // console.log(this.movie.like_users)
        this.like_cnt=this.movie.like_users.length
        this.rating_cnt=res.data.rating_count
        if (res.data.ratings){
          let ratings_sum=0
           res.data.ratings.forEach((rating) => {
            console.log("확인용")
            console.log(rating)
            ratings_sum+=rating.score
          })
          this.rating_average=ratings_sum/this.rating_cnt
        }
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getMovieTrailer(){
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${this.movie_id}/videos`,
        params: {
            // api_key: '77347a1bf275c0c7fd3a5066b945c759',
            api_key: 'b3628728851d758a9fb78c3d38b86613',
            language: 'Ko',
          },

      })
      .then(res=>{
        // console.log("##################")
        // console.log(res.data.results[0].key)
        // console.log("확인할 것")
        // console.log(res.data.results)
        // console.log(res.data.results[0].key)
        if (res.data.results){
          this.y_key=res.data.results[0].key
        }
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.movie_id=this.$store.state.movie_id
    // console.log(this.movie_id)
    this.getDetailMovies()
    this.getMovieTrailer()
    // console.log("getrating 실행중?")
    this.getRating()
  },
  mounted(){
    
  }
}
</script>

<style scoped>
.my-container-bottom{
  margin-bottom:40px;
}
.my-no-wrap{
  display: flex;
  flex-wrap: nowrap;
}
.my-container-pr{
  justify-content: center;
  align-content: center;
}
.my-container-width{
  width:600px;
}
/* .no-wrap{
  white-space: nowrap;  
} */
.my-wrap {
  white-space: normal;
}

.rating-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.rating-container label {
  margin-right: 10px;
}

.rating {
  display: flex;
}

.rating-icon {
  cursor: pointer;
}

.rating-icon svg {
  width: 16px;
  height: 16px;
}

.rating-icon.active svg {
  fill: #f8ca00;
}
</style>