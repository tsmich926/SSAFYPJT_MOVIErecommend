```
<template>
    <div class="row">
        <div class="col-md-5">
            <div class="card" style="width: 18rem;" @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
                <img :src="`https://image.tmdb.org/t/p/w500/${CARDactor.profile_path}`" class="card-img-top" alt="Actor Image">
                <div class="card-body">
                <h5 class="card-name">{{CARDactor.name }}</h5>
                </div>
            </div>
        </div>
        <!-- <div class="card" @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
          <img src="../assets/송강호.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">송강호</h5>
                              <button 
              type="button" 
              @click="likeActor(CARDactor)"
              class="btn btn-outline-primary"
            >
            좋아요❤
            </button>
          </div>
        </div> -->

        <!-- <button 
      type="button" 
      @click="toggleLike" 
      class="ml-4 flex items-center justify-center rounded-md py-3 px-3 text-gray-400 hover:bg-gray-100 hover:text-gray-500"
      v-if="isShow"
    >
      <HeartIcon 
        :class="{
          'h-6 w-6 flex-shrink-0': true,
          'text-red-500': liked,
          'text-gray-400': !liked
        }" 
        aria-hidden="true"
      />
      <span class="sr-only">찜</span>
    </button>
    <p>배우고르기</p>
          <div class="row row-cols-1 row-cols-md-6 g-4">
      <div class="col">
      </div>
      <div class="col">
        <div class="card"  @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
          <img src="../assets/logo.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card"  @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
          <img src="../assets/logo.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card"  @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
          <img src="../assets/logo.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
          </div>
        </div>
      </div>
        <div class="col">
    <div class="card"  @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
      <img src="../assets/logo.png" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
      </div>
    </div>
  </div>
            <div class="col">
        <div class="card"  @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
          <img src="../assets/logo.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
                <button 
              type="button" 
              @click="likeActor(actor)"
              class="btn btn-outline-primary"
            >
            좋아요❤
            </button>
          </div>
        </div>
      </div>
    </div> -->
    </div>
</template>

<script>
export default {
name:'HumanCard',
methods: {
    
    // toggleLike(actor) {
    //좋아요 로직---
    // },
    zoomInCard(event) {
      // 카드 확대하는 로직 구현
    event.target.classList.add('zoom-in');
    },
    zoomOutCard(event) {
      // 카드 축소하는 로직 구현
    event.target.classList.remove('zoom-in');

}
},
props:{
CARDactor:Object
    },

}


</script>


<style scoped>
    .row {
    display: flex;
    flex-wrap: wrap;
    margin: -15px;
    }

    .col-md-5 {
    width: 25%;
    padding: 15px;
    box-sizing: border-box;
    }
</style>
```