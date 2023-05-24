<template>
  <div class="col">
    <button class="btn btn-danger ">{{Genre.name}}</button>
  </div>
</template>

<script>
export default {
  name:'GenreItems',
  props:{
    Genre:Object
  },
  created(){
    console.log(this.Genre)
  }

}
</script>


<style scoped>

.genre-list {
  display: flex;
  flex-wrap: wrap;
}

.btn {
  margin-right: 10px;
  margin-bottom: 10px;
}
</style>