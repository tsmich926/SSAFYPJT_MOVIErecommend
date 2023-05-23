<template>
  <div>
    <button class="btn btn-danger">{{Genre.name}}</button>
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

<style>

</style>