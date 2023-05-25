<template>
  <div>
      <ul type="listItem" class="custom-i8o1y5">
      <li class="custom-11zhy3w">
        <a title="조 라이트" class="custom-kbqkpi">
        <div class="custom-kzzlk2">
          <div class="custom-1w7o208">
            <div height="62" type="circle" width="62" class="custom-1dm77tq">
              <img  @click="gotoDetail" alt="배우 이미지" :src="ImgURL" class="custom-1mxmenj" >
            </div>
            <div class="custom-11zhy3w">
              <div class="custom-15vtjyx">{{CARDhuman.name}}</div>
              <div class="custom-hbs6kl-AccessoryModule">감독</div>
              <button type="button" @click="likeHuman()" class="btn btn-outline-primary">
              {{ IsLiked ? '❤' : '🤍'}}
              </button>
            </div>
          </div>
        </div>
        </a>
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
/* .my-card-margin{
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
 */



.custom-1os014q {
    margin: 0px 0px 32px;
    background-color: black;
}


.custom-efczeh {
    display: flex;
    position: relative;
    -webkit-box-pack: justify;
    justify-content: space-between;
    align-items: flex-end;
    font-size: initial;
    margin-bottom: 5px;
}

.custom-1lhv0ae {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    min-width: 0px;
}

.custom-55smc4 {
    color: rgb(255, 255, 255);
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 26px;
}

.custom-1ynili3 {
    display: inline-block;
    vertical-align: top;
    margin: 3px 0px 0px 8px;
}

.custom-1fbr3zd-ShowMoreButton {
    flex-shrink: 0;
    padding-bottom: 3px;
    margin-left: 6px;
}

.custom-ss4kux {
    color: rgb(132, 134, 141);
    font-size: 15px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 20px;
}

.custom-i8o1y5 {
    /* display: grid; */
    column-gap: 20px;
    grid-template-columns: repeat(2, 1fr);
}

.custom-11zhy3w {
    overflow: hidden;
}

.custom-kbqkpi {
    display: block;
    text-decoration: none;
}

.custom-1w7o208 {
    display: grid;
    position: relative;
    flex: 1 1 0%;
    -webkit-box-align: center;
    /* align-items: center; */
    overflow: hidden;
}

.custom-1dm77tq {
    display: flex;
    position: relative;
    flex-shrink: 0;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    width: 62px;
    height: 62px;
    border-radius: 50%;
    margin-right: 14px;
    overflow: hidden;
}

.custom-1mxmenj {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.custom-15vtjyx {
    color: rgb(255, 255, 255);
    font-size: 16px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 22px;
    white-space: nowrap;
    /* overflow: hidden; */
    text-overflow: ellipsis;
    text-decoration: none;
    overflow: hidden;
}


.custom-hbs6kl-AccessoryModule {
    color: rgb(132, 134, 141);
    font-size: 13px;
    font-weight: 400;
    letter-spacing: 0px;
    line-height: 18px;
    white-space: nowrap;
    margin-top: 2px;
    overflow: hidden;
    text-overflow: ellipsis;
}


</style>