<template>
  <div v-if="DetailUser" class="profile-page">
    <div class="user-info">
      <!-- <img class="profile-image" :src="user.profile_path" alt="Profile Image" /> -->
      <h2 class="username">{{ DetailUser.username }} 님</h2>
      <p class="point">💰: {{ DetailUser.point }} point</p>
      <p class="follower-count">팔로워: {{ DetailUser.followers.length }}명</p>
      <button class="edit-button" @click="follow">  {{ IsLiked ? '❤ ' : '🤍 '}} 팔로우</button>
      <br>
      <!-- <button class="btn btn-primary" @click="gotoRandom" >뽑기</button> -->

    </div>

    <div class="liked-movies">
      <h3>좋아요한 영화 </h3>
      <ul class="row">
        <li class="col" v-for="movie in DetailUser.movies" :key="movie.id">
          <p class="movie-title">{{movie.title}}</p>
          <img
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          class="card-img-top my-card-img" alt="..."
          style="width:120px; height:150px"
          >
        </li>
      </ul>
    </div>
    <div class="liked-movies">
      <h3>좋아요한 장르 </h3>
      <ul class="row">
        <li>
          <button class="btn my-padding" :style="{'background-color': IsLiked28 ? 'rgb(255, 90, 0)' : ''}" value="28">액션</button>
          <button class="btn my-padding" :style="[IsLiked12 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="12">모험</button>
          <button class="btn my-padding" :style="[IsLiked16 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="16">애니메이션</button>
          <button class="btn my-padding" :style="[IsLiked35 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="35">코미디</button>
          <button class="btn my-padding" :style="[IsLiked80 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="80">범죄</button>
          <button class="btn my-padding" :style="[IsLiked99 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="99">다큐멘터리</button>
          <button class="btn my-padding" :style="[IsLiked18 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="18">드라마</button>
          <button class="btn my-padding" :style="[IsLiked10751 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10751">가족</button>
          <button class="btn my-padding" :style="[IsLiked14 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="14">판타지</button>
          <button class="btn my-padding" :style="[IsLiked36 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="36">역사</button>
          <button class="btn my-padding" :style="[IsLiked27 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="27">공포</button>
          <button class="btn my-padding" :style="[IsLiked10402 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10402">음악</button>
          <button class="btn my-padding" :style="[IsLiked9648 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="9648">미스터리</button>
          <button class="btn my-padding" :style="[IsLiked10749 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10749">로맨스</button>
          <button class="btn my-padding" :style="[IsLiked878 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="878">SF</button>
          <button class="btn my-padding" :style="[IsLiked10770 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10770">TV 영화</button>
          <button class="btn my-padding" :style="[IsLiked53 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="53">스릴러</button>
          <button class="btn my-padding" :style="[IsLiked10752 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="10752">전쟁</button>
          <button class="btn my-padding" :style="[IsLiked37 ? {'background-color': 'rgb(255, 90, 0)'} : {}]" value="37">서부</button>
        </li>
      </ul>
    </div>
    <div class="liked-actors">
      <h4>좋아요한 영화배우 </h4>
      <ul class="row">
        <li class="col" v-for="actor in DetailUser.actors" :key="actor.id">
          <ActorCard :CARDhuman="actor" />
        </li>
      </ul>
    </div>
    <div class="liked-actors">
      <h4>좋아요한 감독 </h4>
      <ul class="row">
        <li class="col" v-for="director in DetailUser.directors" :key="director.id">
          <DirectorCard :CARDhuman="director" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';
import ActorCard from '@/components/ActorCard.vue'
import DirectorCard from '@/components/DirectorCard.vue'
export default {
  name:'UserDetailView',
  components:{
    ActorCard,
    DirectorCard
  },
  data(){
    return {
      movie:null,
      detailuser:null,
    }
  },
  computed:{
    ...mapState(['user']),
    DetailUser(){
      return this.detailuser
    },
    genres(){
      return this.DetailUser.genres
    },
    IsLiked(){
      return this.DetailUser.followers.some(follower => follower.id === this.user.id)
    },
    IsLiked28(){
      return (this.genres.some(genre => genre.id === 28))
    },
    IsLiked12(){
      return (this.genres.some(genre => genre.id === 12))
    },
    IsLiked16(){
      return (this.genres.some(genre => genre.id === 16))
    },
    IsLiked35(){
      return (this.genres.some(genre => genre.id === 35))
    },
    IsLiked80(){
      return (this.genres.some(genre => genre.id === 80))
    },
    IsLiked99(){
      return (this.genres.some(genre => genre.id === 99))
    }, 
    IsLiked18(){
      return (this.genres.some(genre => genre.id === 18))
    }, 
    IsLiked10751(){
      return (this.genres.some(genre => genre.id === 10751))
    },
    IsLiked14(){
      return (this.genres.some(genre => genre.id === 14))
    }, 
    IsLiked36(){
      return (this.genres.some(genre => genre.id === 36))
    }, 
    IsLiked27(){
      return (this.genres.some(genre => genre.id === 27))
    },
    IsLiked10402(){
      return (this.genres.some(genre => genre.id === 10402))
    },
    IsLiked9648(){
      return (this.genres.some(genre => genre.id === 9648))
    },
    IsLiked10749(){
      return (this.genres.some(genre => genre.id === 10749))
    },
    IsLiked878(){
      return (this.genres.some(genre => genre.id === 878))
    },
    IsLiked10770(){
      return (this.genres.some(genre => genre.id === 10770))
    },
    IsLiked53(){
      return (this.genres.some(genre => genre.id === 53))
    },
    IsLiked10752(){
      return (this.genres.some(genre => genre.id === 10752))
    },
    IsLiked37(){
      return (this.genres.some(genre => genre.id === 37))
    },
    is_followed() {
      return this.DetailUser.followers.map(item => item.id).includes(this.user.id);
    }
  },
  methods:{
    follow(){
      console.log(this.DetailUser.id)
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/user/${this.DetailUser.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log(res)
        this.getUser()
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getUser(){
      let user_id=this.$store.state.user_id
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/user/${user_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        this.detailuser=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
  },
  created(){
    this.getUser()
  },
  mounted(){
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
  background-color: #080808;
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