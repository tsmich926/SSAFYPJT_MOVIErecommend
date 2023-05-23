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
  name: 'HumanCard',
  data() {
    return {
      liked: false,
      like_cnt:0,
      actor:null,
    }
  },
  props: {
    CARDhuman: Object
  },
  computed: {
    ...mapState(['user']),
    ImgURL() {
      if (this.CARDhuman.profile_path == null) {
        return `/Not_Found_Img/nf3.jfif`
      } else {
        return `https://image.tmdb.org/t/p/w500${this.CARDhuman.profile_path}`
      }
    },
    IsLiked(){
      return this.user.actors.includes(this.CARDhuman.id);
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
        url:`http://127.0.0.1:8000/api/v1/actors/${this.CARDhuman.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log("actor확인")
        console.log(res.data)
        this.director=res.data
        this.like_cnt=res.data.like_users.length
        this.$store.dispatch('SaveUser')
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getActor(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/actors/${this.CARDhuman.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        this.actor=res.data
        this.like_cnt=res.data.like_users.length
      })
      .catch(err=>{
        console.log(err)
      })
    },
    gotoDetail(){
      this.$store.commit('SAVE_ACTOR_ID', this.CARDhuman.id)
      this.$router.push({
        name: "ActorDetailView",
      });
    }
  },
  mounted() {
    this.actor = this.CARDhuman;
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