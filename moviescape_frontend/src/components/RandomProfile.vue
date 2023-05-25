<template>
  <div>
    <div>
      <h1>랜덤 profile뽑기입니다~</h1>
    </div>
    <input v-model="term" type="text" @keyup.enter="getRandomProfile">
    <div>
      <img :src="MyProfile" alt="">
    </div>
  </div>
</template>

<script>
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
    }
  },
  methods:{
    getRandomProfile(){

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
        console.log('Image URLs:', images);
      }else{
        alert("꽝!")
      }
    })
    .catch(error => {
      // 오류 처리
      console.error('API Error:', error);
    });
    }
  }
}
</script>

<style>

</style>