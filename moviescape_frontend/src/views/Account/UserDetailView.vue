<template>
  <div v-if="DetailUser">
    <h1>USER Detail Page</h1>
    <hr>
    <h2>{{ DetailUser.username }}</h2>
    <h3>포인트 : {{ DetailUser.point }}</h3>
    <div>
      <h4>팔로우 수 : {{ DetailUser.followings.length }} </h4>
    </div>
    <div>
      <h4>팔로워 수 : {{ DetailUser.followers.length }}</h4>
    </div>
    <button @click="follow" class="btn" :class="[{'btn-primary':!is_followed},{'btn-secondary':is_followed}]">팔로잉</button>
    <hr>
    <h2>좋아요 한 영화 목록</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="movie in DetailUser.movies" :key="movie.id">
          <img
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          class="card-img-top my-card-img" alt="..."
          style="width:300px; height:450px"
          >  
        </div>
        <hr>
      </div>
    </div>
    <h2>좋아요 한 감독 목록</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="director in DetailUser.directors" :key="director.id">
          <DirectorCard :CARDhuman="director" />
        </div>
        <hr>
      </div>
    </div>
    <h2>좋아요 한 배우 목록</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="actor in DetailUser.actors" :key="actor.id">
          <ActorCard :CARDhuman="actor" />
        </div>
        <hr>
      </div>
    </div>
    <h2>유저가 쓴 리뷰</h2>
    {{DetailUser.followers}}
    <div class="container">
      <div class="row">
        <div class="col" v-for="my_review in DetailUser.my_reviews" :key="my_review.id">
          <h4>
          {{ my_review }}
          </h4>
        </div>
        <hr>
      </div>
    </div>
    <!-- <h3>{{ user.movie }}</h3> -->
    <!-- <h3>{{ this.movie.id }}</h3> -->
    <!-- <h3>{{ user.movie.id }}</h3> -->
    <!-- <h3>{{ user.movie.poster_path }}</h3> -->
    <hr>
    <!-- <h3>{{user}}</h3> -->
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

<style>

</style>