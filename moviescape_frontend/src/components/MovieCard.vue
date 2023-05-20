<template>
  <div class="container">
    <div class="card bg-secondary" style="width: 18rem;">
      <img :src="`https://image.tmdb.org/t/p/w500/${CARDmovie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title my-card-title">{{CARDmovie.title}}</h5>
        <p class="card-text my-card-text">{{CARDmovie.overview}}</p>
      </div>
    </div>
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
.my-card-title {
  display: inline-block;
  word-wrap: break-word;
}
</style>