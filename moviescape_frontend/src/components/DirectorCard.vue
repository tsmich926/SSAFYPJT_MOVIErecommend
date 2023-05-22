<template>
  <div class="">
      <div class="my-card-margin">
          <div class="card" style="width: 18rem;" @mouseenter="zoomInCard" @mouseleave="zoomOutCard" >
              <img @click="gotoDetail" :src="ImgURL" class="card-img-top" alt="Actor Image" style="height: 27rem;">
              <div class="card-body">
              <h5 class="card-name">{{CARDhuman.name}}</h5>
              <h5>좋아하는 사람 수 : {{LikeCnt}}</h5>
              <!-- <h5 class="card-name">{{CARDhuman.gender}}</h5> -->
              <button 
            type="button" 
            @click="likeHuman()"
            class="btn btn-outline-primary"
          >
          {{ IsLiked ? '❤': '🤍'}}
          </button>
              </div>
          </div>
      </div>
  </div>
</template>


<script>
import axios from 'axios';
import { mapState } from 'vuex';
export default {
  name: 'DirectorCard',
  data() {
    return {
      liked: false,
      // human:null,
      like_cnt:0,
      director:null,
      // user:{}
    }
  },
  computed: {
    ImgURL() {
      if (this.CARDhuman.profile_path == null) {
        return `/Not_Found_Img/nf3.jfif`
      } else {
        return `https://image.tmdb.org/t/p/w500${this.CARDhuman.profile_path}`
      }
    },
    ...mapState(['user']),
    IsLiked(){
      console.log("isLiked가 수행됩니다...")
      console.log(this.user.directors.includes(this.CARDhuman.id))
      console.log(this.user.directors, this.CARDhuman.id)
      return this.user.directors.includes(this.CARDhuman.id);
      // if (this.CARDhuman.pk in this.user.directors){
      //   return true
      // }
      // else{
      //   return false
      // }
    },
    LikeCnt(){
      return this.like_cnt
    }
  },
  methods: {
    zoomInCard(event) {
      event.target.classList.add('zoom-in');
    },
    zoomOutCard(event) {
      event.target.classList.remove('zoom-in');
    },
    likeHuman() {
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/directors/${this.CARDhuman.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log("director확인")
        console.log(res)
        console.log(res.data)
        this.director=res.data
        this.like_cnt=res.data.like_users.length
        this.$store.dispatch('SaveUser')
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getDirector(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/directors/${this.CARDhuman.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        this.director=res.data
        this.like_cnt=res.data.like_users.length
      })
      .catch(err=>{
        console.log(err)
      })
    },
    gotoDetail(){
      console.log(this.CARDhuman.id)
      if (this.CARDhuman.gender){
        this.$store.commit('SAVE_ACTOR_ID', this.CARDhuman.id)
        this.$router.push({
          name: "ActorDetailView",
        // params: {movie_id:this.CARDmovie.id},
        });
      }else{
        this.$store.commit('SAVE_DIRECTOR_ID', this.CARDhuman.id)
        this.$router.push({
          name: "DirectorDetailView",
        // params: {movie_id:this.CARDmovie.id},
        });
      }
    },
  },
  props: {
    CARDhuman: Object
  },
  mounted() {
    // props에서 전달된 데이터를 this.human에 할당
    this.getDirector()
  },
  created(){
    // this.user=this.$store.state.user
  }
}
</script>


<style scoped>
.my-card-margin{
  margin-bottom: 10px;
}
.row {
display: flex;
flex-wrap: wrap;
margin: -15px;
}

.col-md-3 {
width: 25%;
padding: 15px;
box-sizing: border-box;
}
</style>