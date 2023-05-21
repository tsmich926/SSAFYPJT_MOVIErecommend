<template>
    <div :class="['bg-secondary', 'card', 'my-card', { 'special-card': isSpecial }]" @click="gotoDetail">
      <div class="image-container">
        <img :src="`https://image.tmdb.org/t/p/w500/${CARDmovie.poster_path}`" class="card-img-top my-card-img" alt="...">
      </div>

      <!-- <div class="card-body">
        <h5 class="card-title my-card-title">{{CARDmovie.title}}</h5>
        <p class="card-text my-card-text">{{CARDmovie.overview}}</p>
      </div> -->
    </div>
</template>

<script>
export default {
  name:'MovieCard',
  data() {
    return {
      isSpecial: false // 특정 조건을 기반으로 스타일을 변경하기 위한 데이터 변수
    };
  },
  props:{
    CARDmovie:Object
  },
  components:{

  },
  methods:{
    checkSpecialCondition() {
      this.isSpecial = true;
      // 특정 조건을 체크하고 isSpecial 값을 변경하는 로직을 구현합니다
      // 예를 들어, 특정 조건이 충족되면 this.isSpecial = true; 로 변경할 수 있습니다
    },
    gotoDetail(){
      console.log(this.CARDmovie.id)
      this.$router.push({
        name: "MovieDetailView",
        params: {movie_id:this.CARDmovie.id},
      });

    }
  },
  mounted() {
    this.checkSpecialCondition(); // 컴포넌트가 마운트된 후에 특정 조건을 체크하여 스타일을 변경합니다
  }
}
</script>

<style scoped>
.image-container {
  /* position: absolute; */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-container:hover img {
  transform: rotateY(90deg); /* 회전 효과 */
  transition: transform 0.9s ease; /* 트랜지션 속성 설정 */
  transform-origin: left center; /* 왼쪽 끝을 축으로 회전 */
}

img:hover{
  /* animation : 효과(@keyframes 이름) 동작시간 */
	animation: fadeout 1s;
}
@keyframes fadeout {
/* 효과를 동작시간 동안 0 ~ 1까지 */
	from {
		opacity: 0.5;
	}
	to {
		opacity: 0;
	}
}
.my-card-img{
  width:100%;
  height: 100%;
  object-fit: cover; /* 이미지가 요소에 맞게 잘리지 않고 비율을 유지하도록 설정 */
}
.my-card-text {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}
.my-card-title {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}
.my-card {
  width: 18rem;
  height: 27rem;
  margin-bottom: 30px;
  padding: 0px;
  flex-shrink: 0;
  background-image: url("@/assets/door3.jfif"); 
  background-size: cover; /* 이미지가 카드에 맞게 조절되도록 설정합니다 */
  background-position: center; /* 이미지를 가운데로 정렬합니다 */
  background-repeat: no-repeat; /* 이미지를 반복하지 않도록 설정합니다 */
}
</style>