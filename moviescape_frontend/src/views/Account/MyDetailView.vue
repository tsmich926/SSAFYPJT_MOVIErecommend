<template>
  <div class="profile-page">
    <div class="user-info">
      <!-- <img class="profile-image" :src="user.profile_path" alt="Profile Image" /> -->
      <h2 class="username">{{ user.username }} 님</h2>
      <p class="point">💰: {{ user.point }} point</p>
      <p class="follower-count">팔로워: {{ user.followings.length }}명</p>
      <button class="edit-button" @click="gotoRandom">  🖊️사용자뽑기</button>
      <br>
      <!-- <button class="btn btn-primary" @click="gotoRandom" >뽑기</button> -->

    </div>

    <div class="liked-movies">
      <h3>좋아요한 영화 </h3>
      <ul class="row">
        <li class="col" v-for="movie in user.movies" :key="movie.id">
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
          <button  @click="like_genre(1)" class="btn my-btn" value="1">전체</button>
          <button  @click="like_genre(28)" class="btn my-btn" value="28">액션</button>
          <button  @click="like_genre(12)" class="btn my-btn" value="12">모험</button>
          <button  @click="like_genre(16)" class="btn my-btn" value="16">애니메이션</button>
          <button  @click="like_genre(35)" class="btn my-btn" value="35">코미디</button>
          <button  @click="like_genre(80)" class="btn my-btn" value="80">범죄</button>
          <button  @click="like_genre(99)" class="btn my-btn" value="99">다큐멘터리</button>
          <button  @click="like_genre(18)" class="btn my-btn" value="18">드라마</button>
          <button  @click="like_genre(10751)" class="btn my-btn" value="10751">가족</button>
          <button  @click="like_genre(14)" class="btn my-btn" value="14">판타지</button>
          <button  @click="like_genre(36)" class="btn my-btn" value="36">역사</button>
          <button  @click="like_genre(27)" class="btn my-btn" value="27">공포</button>
          <button  @click="like_genre(10402)" class="btn my-btn" value="10402">음악</button>
          <button  @click="like_genre(9648)" class="btn my-btn" value="9648">미스터리</button>
          <button  @click="like_genre(10749)" class="btn my-btn" value="10749">로맨스</button>
          <button  @click="like_genre(878)" class="btn my-btn" value="878">SF</button>
          <button  @click="like_genre(10770)" class="btn my-btn" value="10770">TV 영화</button>
          <button  @click="like_genre(53)" class="btn my-btn" value="53">스릴러</button>
          <button  @click="like_genre(10752)" class="btn my-btn" value="10752">전쟁</button>
          <button  @click="like_genre(37)" class="btn my-btn" value="37">서부</button>
        </li>
      </ul>
    </div>
    <div class="liked-actors">
      <h4>좋아요한 영화배우 </h4>
      <ul class="row">
        <li class="col" v-for="actor in user.actors" :key="actor.id">
          <ActorCard :CARDhuman="actor" />
        </li>
      </ul>
    </div>
    <div class="liked-actors">
      <h4>좋아요한 감독 </h4>
      <ul class="row">
        <li class="col" v-for="director in user.directors" :key="director.id">
          <DirectorCard :CARDhuman="director" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import ActorCard from '@/components/ActorCard.vue'
import DirectorCard from '@/components/DirectorCard.vue'





export default {
  name: 'MyDetailView',
  components: {
    ActorCard,
    DirectorCard,
  
  },
  data() {
    return {
      movie:null
    }
  },
  computed: {
    ...mapState(['user'])
  },
  methods: {
    gotoRandom(){
      this.$router.push({name:"RandomProfileVue"})
    },
    like_genre(genre_id){
      console.log(genre_id)
    }
  },
  mounted(){
    console.log('this.user')
    this.movie = this.user.movie
  }

  }
</script>

<style scoped>
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
  max-width: 700;
}

.user-info {
  background-color: #ededed;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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