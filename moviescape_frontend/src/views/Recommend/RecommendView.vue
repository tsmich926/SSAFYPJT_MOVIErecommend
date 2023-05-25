<template>
  <div class="profile-page">
    
    <div class="liked-movies">
      <h3>좋아요한 장르 </h3>
      <ul class="row">
        <button class="btn btn-primary" @click="click">뽑기</button>
        <li>
          <button @click="like_genre('all')" class="btn my-padding" :style="{'background-color': IsLikedall ? 'rgb(255, 90, 0)' : ''}" value="28">전체</button>
          <button @click="like_genre(28)" class="btn my-padding" :style="{'background-color': IsLiked28 ? 'rgb(255, 90, 0)' : ''}" value="28">액션</button>
          <button @click="like_genre(12)" class="btn my-padding" :style="[IsLiked12 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="12">모험</button>
          <button @click="like_genre(16)" class="btn my-padding" :style="[IsLiked16 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="16">애니메이션</button>
          <button @click="like_genre(35)" class="btn my-padding" :style="[IsLiked35 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="35">코미디</button>
          <button @click="like_genre(80)" class="btn my-padding" :style="[IsLiked80 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="80">범죄</button>
          <button @click="like_genre(99)" class="btn my-padding" :style="[IsLiked99 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="99">다큐멘터리</button>
          <button @click="like_genre(18)" class="btn my-padding" :style="[IsLiked18 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="18">드라마</button>
          <button @click="like_genre(10751)" class="btn my-padding" :style="[IsLiked10751 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10751">가족</button>
          <button @click="like_genre(14)" class="btn my-padding" :style="[IsLiked14 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="14">판타지</button>
          <button @click="like_genre(36)" class="btn my-padding" :style="[IsLiked36 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="36">역사</button>
          <button @click="like_genre(27)" class="btn my-padding" :style="[IsLiked27 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="27">공포</button>
          <button @click="like_genre(10402)" class="btn my-padding" :style="[IsLiked10402 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10402">음악</button>
          <button @click="like_genre(9648)" class="btn my-padding" :style="[IsLiked9648 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="9648">미스터리</button>
          <button @click="like_genre(10749)" class="btn my-padding" :style="[IsLiked10749 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10749">로맨스</button>
          <button @click="like_genre(878)" class="btn my-padding" :style="[IsLiked878 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="878">SF</button>
          <button @click="like_genre(10770)" class="btn my-padding" :style="[IsLiked10770 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10770">TV 영화</button>
          <button @click="like_genre(53)" class="btn my-padding" :style="[IsLiked53 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="53">스릴러</button>
          <button @click="like_genre(10752)" class="btn my-padding" :style="[IsLiked10752 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10752">전쟁</button>
          <button @click="like_genre(37)" class="btn my-padding" :style="[IsLiked37 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="37">서부</button>
        </li>
      </ul>
    </div>
    <div class="liked-movies">
      <ul v-if="movie" class="row:">
        <li>
          <h2 style="padding:20px;">추천 영화</h2>
          <img @click="gotoDetail(movie)" style='width:100%; height:100%;' :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="영화이미지" class="custom-uc27kv">
        </li>
      </ul>    
    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex';
import _ from 'lodash';
import axios from 'axios';
export default {
  name:'RecommendView',
  components:{
  },
  data(){
    return{
      genre_list:[],
      movie:null,
      selected_all:false,
    }
  },
  methods:{
    getPoint(){
      const point = -50
      const profile_path=this.user.profile_path
      const payload = {
        point,profile_path
      }

      this.$store.dispatch('GetPoint',payload)
    },
    gotoDetail(movie){
      // this.$store.commit('SAVE_MOVIE_ID', movie.id)
      const movieId = movie.id; // 이동할 영화의 ID를 동적으로 설정할 수 있음
      // console.log("MovieCard")
      // console.log(movieId)
      this.$router.push({ name: 'MovieDetailView', params: { id: movieId } });
    },
    click(){
      //뽑기 method 입니다.
      const genre_id=_.sample(this.genres)
      console.log(genre_id)
      if (!genre_id){
        alert("장르를 선택해 주세요!")
        return
      }else{
        if (this.user.point<50){
          alert("포인트가 부족합니다!")
          return
        }else{
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/recommend/${genre_id}/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
          .then((res) => {
            this.getPoint()
            console.log(res)
            this.movie=res.data
            if (res.status==206){
              alert("원하는 장르는 아니지만 추천해 드리겠습니다!")
            }
          })
          .catch(err => {
            console.log(err)
          })
        }
      }
    },
    like_genre(value){
      if (value=='all'){
        console.log(this.genre_list)
        console.log(this.genre_list==[1,28,12,16,35,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,10752,37])
        if (this.selected_all){
          this.genre_list=[]
          this.selected_all=false
        }else{
          this.selected_all=true
          this.genre_list=[1,28,12,16,35,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,10752,37]
        }
      }else
      {
        console.log(value)
        if(this.genre_list.includes(value)){
        // 이미 좋아하는 장르에 해당하는 값이 있는 경우
          const index = this.genre_list.indexOf(value);
          if (index > -1) {
            this.genre_list.splice(index, 1); // 해당 값 제거
            this.selected_all=false
          }
          }else{
            this.genre_list.push(value)
          } 
      }
    }
  },
  computed:{
    ...mapState(['user']),
    genres(){
      return this.genre_list
    },
    IsLikedall(){
      return this.selected_all
    },
    IsLiked28(){
      return (this.genres.includes(28))
    },
    IsLiked12(){
      return (this.genres.includes(12))
    },
    IsLiked16(){
      return (this.genres.includes(16))
    },
    IsLiked35(){
      return (this.genres.includes(35))
    },
    IsLiked80(){
      return (this.genres.includes(80))
    },
    IsLiked99(){
      return (this.genres.includes(99))
    }, 
    IsLiked18(){
      return (this.genres.includes(18))
    }, 
    IsLiked10751(){
      return (this.genres.includes(10751))
    },
    IsLiked14(){
      return (this.genres.includes(14))
    }, 
    IsLiked36(){
      return (this.genres.includes(36))
    }, 
    IsLiked27(){
      return (this.genres.includes(27))
    },
    IsLiked10402(){
      return (this.genres.includes(10402))
    },
    IsLiked9648(){
      return (this.genres.includes(9648))
    },
    IsLiked10749(){
      return (this.genres.includes(10749))
    },
    IsLiked878(){
      return (this.genres.includes(878))
    },
    IsLiked10770(){
      return (this.genres.includes(10770))
    },
    IsLiked53(){
      return (this.genres.includes(53))
    },
    IsLiked10752(){
      return (this.genres.includes(10752))
    },
    IsLiked37(){
      return (this.genres.includes(37))
    },
  },



}
</script>



<style scoped>
.my-padding{
  margin:5px;
}
/* .my-btn{
  background-color: rgb(255, 90, 0) ;
  color: rgb(255, 90, 0);
} */
.profile-page {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.user-info {
  text-align: center;
  margin: 20px;
}

.profile-image {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 50%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.username {
  font-size: 24px;
  margin-top: 10px;
  color: #333;
}

.point,
.follower-count {
  margin-top: 5px;
  color: #777;
}

.liked-actors,
.liked-movies {
  text-align: center;
  margin-top: 20px;
  width: 400px;
}

h3 {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #fcfafa;
}

h4 {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 30px;
  color: #fcfafa;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 5px;
  color: #555;
}


/* 2 */

.profile-page {
  /* background-color: #080808; */
  padding: 20px;
  /* border: solid white; */
  border-radius: 10px;
  /* max-width: 700px; */
}

.user-info {
  background-color: #ededed;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  
  border: solid white;
}

.username {
  color: #333;
  font-weight: bold;
  margin-top: 50px;
}

.point,
.follower-count {
  color: #777;
}

.liked-actors,
.liked-movies {
  background-color: #050505;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: solid 1px white;
  margin: 5px;
  min-width: 900px;
}

ul {
  margin-top: 10px;
}

li {
  padding: 5px;
  border-radius: 3px;
  /* background-color: #f0f0f0; */
}


.btn{

    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    color: #fff;
    cursor: pointer;
    font-size: 14px;
    margin-top: 20px;
}

.edit-button {
  background-color: #008080;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.edit-button:hover {
  background-color: #003d3d;
}


.movie-title{
  width: 120px;
  white-space: nowrap; 
  overflow: hidden;
  text-overflow: ellipsis; 
  align-items: center;
  justify-content: center;
}

.my-card-img {
  display: flex;
  align-items: center;
  justify-content: center;
  /* width: 100px;
  height: 100px; */
} 


/* 3 */

</style>