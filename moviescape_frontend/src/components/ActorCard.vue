<template>
  <!-- <div class="">
    <div class="d-flex justify-content-center align-items-center">
      <div class="card my-card-margin" style="width: 18rem;" @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
        <img @click="gotoDetail" :src="ImgURL" class="card-img-top" alt="Actor Image" style="height: 27rem;">
        <div class="card-body text-center">
          <h5 class="card-name">{{CARDhuman.name}}</h5>
          <h5>좋아하는 사람 수: {{LikeCnt}}</h5>
          <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
            {{ IsLiked ? '❤' : '🤍'}}
          </button>
        </div>
      </div>
    </div>
  </div> -->
  <div>
        <!-- <ul type="listItem" class="custom-i8o1y5">
        <li class="custom-11zhy3w">
          <a title="조 라이트" class="custom-kbqkpi" href="/people/rQ7XLbbb7A">
          <div class="custom-kzzlk2">
            <div class="custom-1w7o208">
              <div height="62" type="circle" width="62" class="custom-1dm77tq">
                <img alt="감독 이미지" src="https://an2-img.amz.wtchn.net/image/v2/CeIRDTazPLOwvlTc7JG1eA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qUXdlREkwTUNKZExDSndJam9pTDNZeEwzQmxiM0JzWlM5bE9UTmhOemhtWVRreFpUQmxZV1F4WVRBMk9TNXFjR2NpZlEuOEJyR2l2UkFqUGhyV1dFQUVGZWN3UkdpR0MyS2ZjbVdmU0JoSGdHNGNQMA" class="custom-1mxmenj">
              </div>
            <div class="custom-11zhy3w">
              <div class="custom-15vtjyx">조 라이트</div>
              <div class="custom-hbs6kl-AccessoryModule">감독</div>
            </div>
            </div>
          </div>
          </a>
        </li>
        </ul> -->
  </div>
</template>


<script>
import axios from 'axios';
import { mapState } from 'vuex';
export default {
  name: 'ActorCard',
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
      return this.user.actors.some(actor => actor.id === this.CARDhuman.id);
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
    this.getActor()
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