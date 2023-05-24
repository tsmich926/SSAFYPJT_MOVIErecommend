<template>
  <div class= "container justify-content-center align-items-center">
    <h1>MovieDetailView</h1>
      <!-- {{movie}} -->
    <div class="custom-0">
      <header class="custom-4ekwdf">
        <div class="custom-19pxr9t">
          <section type = "portrait" class="custom-1b2a0k5">
            <div type = "portrait" class="custom-1fbu1vu" >
              <img style='width:100%; height:100%;' :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="영화이미지" class="custom-uc27kv">
            </div>
            <div class= "custom-1qxls6i">
              <h1 class="custom-1rhk36" >{{movie.title}}</h1>
              <p class="custom-1hb39aj">
                <span class="custom-0">
                  <a v-for='genre in movie.genres' :key="genre.id" class="custom-1ev3txx">{{genre.name}} &nbsp;</a>
                  · 
                  <span class="custom-16k1fda">유저 평균 평점:{{RatingAverage}}</span>
                </span > 
              </p>
              <!-- <p> -->
                <div class="rating-container">
                  <label for="ratings">별점:</label>
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
              <!-- </p> -->
              <p class="custom-1cfj8mp">
                {{movie.overview}}
              </p>
            </div>
          </section>
          <div class="custom-10tp89e">
            <section class="custom-1mscwm6">
              <div class="custom-sa68ux">
                <a class="custom-1updnc7">
                  보러가기
                </a>
              </div>
              <div class="custom-sa68ux" >
                <button  class="wished custom-okxqa8" type="button"> 좋아요 </button>
                <p>좋아하는 유저수</p>
                <hr>
                <p>{{ LikeCnt }}</p>
              </div>
            </section> 
          </div>
        </div>
      </header>
      <section class="custom-atrls1">
        <section class="custom-rdh9ic">
          <section class="custom-1os014q"> 
            <div class="custom-efczeh">
              <div class="custom-1lhv0ae">
                <div>
                  <h1 class="custom-55smc4">
                    관련 동영상
                  </h1>
                </div>
              
              </div>
            </div>
            <ul class="custom-nhnj2n">
              <li>
                <iframe id="player" type="text/html" width="600" height="500"
          :src="`https://www.youtube.com/embed/${youtube_key}`"
          frameborder="0"></iframe>
                  <div class="custom-1ngnn9r">
                    <div class="custom-c9eeru">
                      <div aria-hidden="true" class="custom-7v1m1m">
                        <p class="custom-1ponucs">숨긴 영화 설명 ... . ..</p>

                      </div>
                    </div>
                  </div>
              </li>
            </ul>
          </section>
        </section>
      </section>
      <section class="custom-1os014q">
      <div class="custom-efczeh">
          <div class="custom-1lhv0ae">
              <div>
                  <h1 class="custom-55smc4">
                    감독/출연
                    <div class="custom-1ynili3"></div>
                      <DirectorListItems :ITEMdirctors="movie.directors"/>
                      <ActorListItems :ITEMactors="movie.actors"/>
                  </h1>
              </div>
          </div>
      </div>
          <div class="custom-1fbr3zd-ShowMoreButton">
            <a role="button" class="custom-ss4kux" href="/contents/mOk6ZMW/credits">더보기</a>
          </div>
      <!-- <ul type="listItem" class="custom-i8o1y5">
        <li class="custom-11zhy3w">
          <a title="조 라이트" class="custom-kbqkpi" href="/people/rQ7XLbbb7A">
          <div class="custom-kzzlk2">
            <div class="custom-1w7o208">
              <div height="62" type="circle" width="62" class="custom-1dm77tq">
                <img alt="조 라이트의 이미지" src="https://an2-img.amz.wtchn.net/image/v2/CeIRDTazPLOwvlTc7JG1eA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qUXdlREkwTUNKZExDSndJam9pTDNZeEwzQmxiM0JzWlM5bE9UTmhOemhtWVRreFpUQmxZV1F4WVRBMk9TNXFjR2NpZlEuOEJyR2l2UkFqUGhyV1dFQUVGZWN3UkdpR0MyS2ZjbVdmU0JoSGdHNGNQMA" class="custom-1mxmenj">
              </div>
            <div class="custom-11zhy3w">
              <div class="custom-15vtjyx">조 라이트</div>
              <div class="custom-hbs6kl-AccessoryModule">감독</div>
            </div>
            </div>
          </div>
          </a>
        </li>
      <li class="custom-11zhy3w">
        <a title="브렌다 블레신" class="custom-kbqkpi" href="/people/j04dqLrZGp">
          <div class="custom-kzzlk2">
            <div class="custom-1w7o208">
                <div height="62" type="circle" width="62" class="custom-1dm77tq">
                  <img alt="브렌다 블레신의 이미지" src="https://an2-img.amz.wtchn.net/image/v2/wms-8tWaVXWeLOMNvWB-eQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qUXdlREkwTUNKZExDSndJam9pTDNZeEwzQmxiM0JzWlM5aFltSmxNMlU0TjJFMk9UazNNamd6TVdKallpNXFjR2NpZlEuQnZpVkltWDdVTFlIUGhjUndwWWVVTXY0N25peGRyZkpHMzhpMFQ1T1UzOA" class="custom-1mxmenj">
                </div>
                  <div class="custom-11zhy3w">
                    <div class="custom-15vtjyx">브렌다 블레신</div>
                    <div class="custom-hbs6kl-AccessoryModule">조연 · Mrs. 베넷</div>
                  </div>
              </div>
            </div>
          </a>
        </li>
      </ul> -->
  </section>                         
      <section class="custom-hgckol">
        <div class="custom-efczeh">
          <div class="custom-1lhv0ae">
            <div>
              <h1 class="custom-55smc4">
                MOVIESCAPE 사용자 평
              </h1>
            </div>
          </div>
        </div>
        <ul class="custom-syergp">
          <li>
            <article class="custom-13frh63"> 
              <div class="custom-6fc8lh">
                <a href="#">
                  <img src="@/assets/logo.png" alt="user프로필" class="custom-nhnvgi">
                </a>
              </div>
              <div class="custom-yp9swi">
                <div class="custom-1sg2lsz">
                  <div class="custom-ex2l60" v-for="review in movie.reviews" :key="review.id">
                    <a href="#">{{review.user.username}}</a>
                  </div>
                  <div class="custom-lz79eo" v-for="review in movie.reviews" :key="review.id">
                    <p class="LinesEllipsis ">
                      {{review.title}}
                      <wbr>
                    </p>
                  </div>
                </div>
              </div>
            </article>
          </li>
        </ul>
      </section>
    </div>
    <ActorListItems/>
    <DirectorListItems/>
    <TestReview />
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
  beforeRouteUpdate(to,from,next){
    this.movie_id=to.params.id
    this.getDetailMovies(this.movie_id)
    next()
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
            this.rating_pk=res.data.pk
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
        this.rating_pk=res.data.id
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
    getDetailMovies(movie_id){ 
      this.getMovieTrailer(movie_id)
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${movie_id}`,
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
    getMovieTrailer(movie_id){
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/movie/${movie_id}/videos`,
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
    this.movie_id = this.$route.params.id
    // this.movie_id=this.$store.state.movie_id
    // console.log(this.movie_id)
    this.getDetailMovies(this.movie_id)
    // console.log("getrating 실행중?")
    this.getRating()
  },
  mounted(){
    // this.getDetailMovies(this.movie_id)
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

a {
  text-decoration: none;
}




.btn {
  border: none;
}

.showbtn {
    flex-shrink: 0;
    padding-bottom: 3px;
    margin-left: 6px;
}


.custom-btn{
  color: rgb(1, 3, 8);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    text-decoration: none;
    transition: color 0.3s;
}

.custom-btn:hover {
  color: red; /* 호버 시 색상 변경 */
}


.custom-1b2a0k5 {
    display: flex;
    align-items: flex-start;
    max-width: 1680px;
    padding-bottom: 30px;
    padding-right: 40px;
    padding-left: 40px;
    margin: 99px auto 0px; }

.custom-1fbu1vu {
    display: inline-block;
    position: relative;
    vertical-align: top;
    /* width: 450px; */
    height: 400px;
    border-radius: 4px;
    object-fit: cover;
    margin: 0px 40px 0px 0px;
    overflow: hidden; }


.custom-uc27kv {
  vertical-align: top;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

img {
    border-style: none;
}

.custom-1qxls6i {
    display: flex;
    flex: 1 1 0%;
    flex-direction: column;
    align-items: center;
}

.custom-1rhk36 {
    position: relative;
    top: 4px;
    font-family: Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Nanum Gothic", "Malgun Gothic", sans-serif;
    font-size: 64px;
    font-weight: 900;
    line-height: 81px;

    color: white;
    flex-direction: column;
    align-items: flex-start;
}

/* @media screen and (max-width: 79em)
.custom-1hb39aj {
    flex-direction: column;
    align-items: flex-start;
} */

.custom-1hb39aj {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    color: rgb(186, 186, 193);
    font-size: 30px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    white-space: pre;
    margin: 10px 0px 30px; 
    
    flex-direction: column;
    align-items: flex-start;
    }



.custom-1cfj8mp {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 9;
    color: rgb(186, 186, 193);
    font-size: 25px;
    font-weight: 400;
    letter-spacing: 0.5px;
    line-height: 30px;
    max-width: 600px;
    margin: 5px 0px 0px;
    overflow: hidden;
    align-items: flex-start;
}

.custom-10tp89e {
    background: rgba(0, 0, 0, 0.3);
    border-top: 1px solid rgb(27, 28, 29);
    border-bottom: 1px solid rgb(27, 28, 29);
}

div {
    display: block;
}

.custom-4ekwdf {
    position: relative;
    z-index: 2;
}

header {
    display: block;
}

.custom-19pxr9t {
    position: relative;
    z-index: 2;
}

.custom-1mscwm6 {
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
    max-width: 1680px;
    padding: 16px 40px;
    margin: 0px auto;}

  .custom-sa68ux {
  display: grid;
  grid-auto-flow: column;
  gap: 12px;
}

.custom-1updnc7 {
    display: flex;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    border: 0px;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 20px;
    background: rgb(248, 47, 98);
    color: rgb(255, 255, 255);
    padding: 10px 16px;
}


.custom-sa68ux {
    display: grid;
    grid-auto-flow: column;
    gap: 12px;
}

.custom-okxqa8 {
    display: flex;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 20px;
    background: transparent;
    color: rgb(255, 255, 255);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 9px 15px; }

.custom-atrls1 {
    display: flex;
    max-width: 1680px;
    padding-right: 20px;
    padding-left: 20px;
    margin: 0px auto;
}

.custom-0 {
    /* -webkit-flex: 1;
    -ms-flex: 1; */
    flex: 1;
    background: #000;
}


.custom-rdh9ic {
    width: 100%;
    margin: 0px;
}

.custom-1os014q {
    margin: 0px 0px 32px;
}

.custom-efczeh {
    display: flex;
    position: relative;
    -webkit-box-pack: justify;
    justify-content: space-between;
    align-items: flex-end;
    font-size: initial;
    margin-bottom: 5px;
}

.custom-1lhv0ae {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    min-width: 0px;
}

.custom-55smc4 {
    color: rgb(248, 245, 245);
    font-size: 40px;
    font-weight: 700;
    letter-spacing: 1px;
    line-height: 26px;
}

.custom-nhnj1n {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

.custom-nhnj2n {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

.custom-1ngnn9r {
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.custom-c9eeru {
    display: flex;
    position: relative;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    padding-top: 56.33%;
}


.custom-1ponucs {
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0px;
    text-decoration: none;
    line-height: 18px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
}

.custom-7v1m1m {
    display: flex;
    position: absolute;
    bottom: 0px;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    width: 100%;
    height: 100%;
}

.custom-1mxmenj {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.custom-1os014q {
    margin: 0px 0px 32px;
}

.custom-efczeh {
    display: flex;
    position: relative;
    -webkit-box-pack: justify;
    justify-content: space-between;
    align-items: flex-end;
    font-size: initial;
    margin-bottom: 5px;
}

.custom-1lhv0ae {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    min-width: 0px;
}

.custom-55smc4 {
    color: rgb(255, 255, 255);
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 26px;
}

.custom-1fbr3zd-ShowMoreButton {
    flex-shrink: 0;
    padding-bottom: 3px;
    margin-left: 6px;
}

.custom-ss4kux {
    /* color: rgb(132, 134, 141);
    font-size: 30px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px; */

    
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 0px;
    line-height: 20px;
    background: transparent;
    color: rgb(255, 255, 255);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 9px 15px;
    
}

.layout__flex-left {
    justify-content: flex-start;
    display: flex;
    align-items: center;
}

.custom-13frh63 {
    display: flex;
    align-items: flex-start;
    padding: 8px 0px;
}

.custom-6fc8lh {
    margin: 0px 8px 0px 0px;
}


.custom-nhnvgi {
    width: 38px;
    height: 38px;
    border-radius: 50%;
}

.custom-yp9swi {
    flex: 1 1 0%;
}

custom-1sg2lsz {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
}

.custom-ex2l60 {
    color: rgb(255, 255, 255);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    margin: 0px 4px 8px 0px;
}

.custom-lz79eo {
    color: rgb(132, 134, 141);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    white-space: pre-wrap;
    margin: 4px 0px;
}


/* 
p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
} */


.LinesEllipsis {

    color: rgb(132, 134, 141);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    white-space: pre-wrap;
    margin: 4px 0px;
    /* justify-content: flex-start;
    align-content: flex-start; */
}

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  outline: none;
  padding: 0;
}

.heart-icon {
  fill: white;
  stroke: black;
  stroke-width: 30;
  transition: all 0.5s;
}

.filled {
  fill: red;
  stroke: none;
  transition: all 0.5s;
}

/* @-webkit-keyframes like {
  0%   { transform: scale(1); }
  90%   { transform: scale(1.2); }
  100% { transform: scale(1.1); }
} */

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  outline: none;
  padding: 0;
}

.heart-icon {
  fill: transparent;
  stroke: black;
  stroke-width: 30;
  transition: all 0.5s;
}

.active .heart-icon {
  fill: red;
  stroke: none;
  transition: all 0.5s;
}


.custom-ex2l60[data-v-469af010] {
    color: rgb(248, 245, 245);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
    margin: 0px 4px 8px 0px;
}

</style>