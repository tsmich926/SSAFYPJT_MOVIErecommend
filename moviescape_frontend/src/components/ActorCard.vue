<template>
  <div>
    <ul type="listItem" class="container justify-content-center custom-i8o1y5" style="text-align:center;">
      <li class="row" style="width:140px;">
        <div class="col custom-1dm77tq">
          <div class="custom-image-wrapper" @click="gotoDetail">
            <div class="custom-image-circle">
              <img alt="배우 이미지" :src="ImgURL" class="custom-1mxmenj">
            </div>
          </div>
        </div>
        <div class="col custom-11zhy3w">
          <div class="custom-info-wrapper">
            <div class="custom-center-wrapper">
              <div class="custom-15vtjyx">{{CARDhuman.name}}</div>
              <div class="custom-heart-wrapper">
                <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
                  {{ IsLiked ? '❤' : '🤍'}}
                </button>
              </div>
            </div>
            <div class="custom-hbs6kl-AccessoryModule">배우</div>
          </div>
        </div>
      </li>
    </ul>
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
  background-color: #f5f5f51c; /* 원의 배경 색상 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.custom-1mxmenj {
  width: 100%;
  border-radius: 50%; /* 이미지에 원형 테두리를 추가하여 원형으로 보이도록 설정 */
}

.custom-11zhy3w {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 10px;
}

.custom-info-wrapper {
  display: flex;
  flex-direction: column;
  margin-right: 10px;
  color: white;
}

.custom-center-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.custom-15vtjyx {
  white-space: nowrap; /* 글자가 넘칠 경우 줄바꿈하지 않고 한 줄에 표시되도록 설정 */
  overflow: hidden;
  text-overflow: ellipsis; /* 글자가 넘칠 경우 생략 부호 (...) 표시 */
}

.custom-heart-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}
</style>