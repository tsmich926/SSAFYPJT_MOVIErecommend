<template>
  <div>
    <!-- <div class="card-body">
      <h1 class="card-title">{{CARDmovie.title}}</h1>
      <p class="card-text">{{CARDmovie.overview}}</p>
    </div> -->
    <!--  -->
    <div class="card" style="width: 18rem;">
      <img :src="`https://image.tmdb.org/t/p/w500/${CARDmovie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{CARDmovie.title}}</h5>
        <p class="card-text my-card-text">{{CARDmovie.overview}}</p>
      </div>
    </div>
<!--  -->
  </div>
</template>

<script>
export default {
  name:'MovieCard',
  props:{
    CARDmovie:Object
  },
  components:{

  },
  methods:{

  }

}
</script>

<style scoped>
/* .card_over{
  overflow-x: auto;
} */
.my-card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>