<template>
  <div>
    <h1>My Detail Page</h1>
    <hr>
    <h2>{{ user.username }}</h2>
    <h3>포인트 : {{ user.point }}</h3>
    <div>
      <h4>팔로우 수 : {{ user.followings.length }} </h4>
    </div>
    <div>
      <h4>팔로워 수 : {{ user.followers.length }}</h4>
    </div>
    <hr>
    <button class="btn btn-primary" @click="gotoRandom">뽑기</button>
    <hr>

    <h2>좋아요 한 영화 목록</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="movie in user.movies" :key="movie.id">
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
        <div class="col" v-for="director in user.directors" :key="director.id">
          <DirectorCard :CARDhuman="director" />
        </div>
        <hr>
      </div>
    </div>
    <h2>좋아요 한 배우 목록</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="actor in user.actors" :key="actor.id">
          <ActorCard :CARDhuman="actor" />
        </div>
        <hr>
      </div>
    </div>
    <h2>내가 쓴 리뷰</h2>
    <div class="container">
      <div class="row">
        <div class="col" v-for="my_review in user.my_reviews" :key="my_review.id">
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
// import axios from 'axios';
import { mapState } from 'vuex';
import ActorCard from '@/components/ActorCard.vue'
import DirectorCard from '@/components/DirectorCard.vue'

export default {
  name:'MyDetailView',
  components:{
    ActorCard,
    DirectorCard,

  },
  data(){
    return {
      movie:null,
    }
  },
  computed:{
    ...mapState(['user'])
  },
  methods:{
    gotoRandom(){
      this.$router.push({name:"RandomProfileVue"})
    }
  },
  mounted(){
    console.log("3333")
    console.log(this.user)
    this.movie=this.user.movie
  }

}
</script>

<style>

</style>