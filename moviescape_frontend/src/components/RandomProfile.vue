<template>
  <div class="container justify-content-center align-items-center my_MovieListView_BGC">
    <div class="my-center-content">
      <h1>랜덤 profile뽑기입니다~</h1>
      <input style="margin-bottom:10px;" v-model="term" type="text" @keyup.enter="getRandomProfile">
      <button @click="getRandomProfile" class="btn" style="background-color: #008080;">
        뽑기
      </button>
      <div class="my-profile-back row justify-content-center">
        <img class="col" :src="MyProfile" alt="">
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex';
import axios from 'axios'
export default {
  // API 요청
  name:'RandomProfile',
  data(){
    return{
      term:null,
      userimg:null,
    }
  },
  computed:{
    MyProfile(){
      return this.userimg
    },
    ...mapState(['user']),
  },
  methods:{
    getPoint(url){
      const point = -100
      const profile_path=url
      const payload = {
        point,profile_path
      }

      this.$store.dispatch('GetPoint',payload)
    },
    getRandomProfile(){
      if(this.user.point<100){
        alert("포인트가 부족합니다!")
        return
      }else{
        axios({
          mehtod:'get',
          url:'https://api.unsplash.com/search/photos',
          headers: {
            Authorization:' Client-ID FqbNMPmM9i4RuvkJ9UFw72czSeVHAzq0yGmQs1eri2s' // YOUR_ACCESS_KEY는 Unsplash에서 발급받은 API 키로 대체해야 합니다.
          },
          params: {
            // 필요한 매개변수 설정
            query: `${this.term}`, // 검색어 (예: "영화 포스터")
            orientation: 'squarish', // 이미지 방향 (가로 방향)
            count: 1, // 가져올 이미지 개수 (5개)
            lang:'ko'
          }
        })
        .then(response => {
          // 응답 처리
          console.log(response)
          if (response.data.results[0]){
            
            const images = response.data.results[0].urls.regular; // 이미지 URL 목록 가져오기
            this.userimg=images
            this.getPoint(this.userimg)
            console.log('Image URLs:', images);
          }else{
            alert("꽝!")
            this.getPoint('default')
          }
        })
        .catch(error => {
          // 오류 처리
          console.error('API Error:', error);
        });
      }
    }
  }
}
</script>

<style scoped>
.my_MovieListView_BGC {
  background-color: #1C1918;
  border-radius: 5px;
  width: 1000px;
  height: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
  /* padding-top: */
}

.my-center-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.my-profile-back {
  width: 900px;
  height: 900px;
  border: white 1px solid;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.my-margin-bottom {
  margin-bottom: 20px;
}

/* 드롭다운 스타일링 */
select {
  padding: 10px;
  font-size: 16px;
  border: none;
  width: 50%;
  border-radius: 5px;
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center;
}

option {
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center;
}
</style>