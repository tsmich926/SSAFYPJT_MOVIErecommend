<template>
  <div>
    <ul type="listItem" class="container justify-content-center custom-i8o1y5" style="text-align:center;">
      <li class="row custom-11zhy3w">
        <div class="col custom-1dm77tq">
          <div class="custom-image-wrapper" @click="gotoDetail">
            <div class="custom-image-circle">
              <img alt="감독 이미지" :src="ImgURL" class="custom-1mxmenj">
            </div>
          </div>
        </div>
        <div class="custom-11zhy3w">
          <div class="custom-15vtjyx">{{CARDhuman.name}}</div>
          <div class="custom-hbs6kl-AccessoryModule">감독</div>
          <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
            {{ IsLiked ? '❤' : '🤍'}}
          </button>
        </div>
      </li>
    </ul>
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
      like_cnt:0,
      director:null,
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
      // console.log("DirectorList의 isLiked가 수행됩니다...")
      // console.log(this.user.directors.includes(this.CARDhuman.id))
      // console.log(this.user.directors, this.CARDhuman.id)
      // console.log(this.user.directors, this.CARDhuman)
      // console.log("휴먼 아이디",this.CARDhuman.id)
      return this.user.directors.some(director => director.id === this.CARDhuman.id);
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
        // console.log("director확인")
        // console.log(res)
        // console.log(res.data)
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
.custom-11zhy3w{
  color: white;
}
.custom-image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 62px;
  overflow: hidden;
}

.custom-image-circle {
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background-color: #f5f5f51c; /* Set the background color of the circle */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.custom-1mxmenj {
  width: 100%;
  /* height: 100%; */
  border-radius: 50%; /* Add a border-radius to the image to make it circular */
}
</style>