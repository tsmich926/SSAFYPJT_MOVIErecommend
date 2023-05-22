<template>
  <div class= "container">
    <h1>ActorDetailView</h1>
      <!-- {{movie}} -->
    <div class="row my-no-wrap ">
      <div class="col my-container-width my-director">
        <img class="" width="400" height="500" :src="`https://image.tmdb.org/t/p/w500/${Actor.profile_path}`" alt="...">
      </div>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <h2 class="my-no-wrap">배우 이름 : {{Actor.name}}</h2>
      </div>
    </div>
    <div class="row my-no-wrap">
      <div class="col">
        <div class="my-wrap"></div>
      </div>
    </div>
    <div class="row justify-content-center">
      <h1>영화 목록</h1>
      <MovieListItemsVue :ITEMmovies="Actor.movies"/>
    </div>
    <div class="row justify-content-center">
      <h1>출연 배우</h1>
    </div>
    <div class="row">
      <h2></h2>
    </div>
    <div class="row">
      <h2></h2>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
import MovieListItemsVue from '@/components/MovieListItems.vue'
// import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name:'HumanDetailView',
  components:{
    MovieListItemsVue
  },
  data(){
    return {
      actor:{},
      actor_id:null,
      searchList:[]
    }
  },
  computed:{
    Actor(){
      return this.actor
    }
  },
  methods:{
    getDetailActor(){ 
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/actors/${this.actor_id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        console.log(res.data)
        this.actor=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
  },
  created(){
    this.actor_id=this.$store.state.actor_id
    console.log(this.actor_id)
    this.getDetailActor()
  }
}
</script>

<style scoped>
.my-director{
  display: flex;

}
.my-no-wrap{
  display: flex;
  flex-wrap: nowrap;
}
.my-container-pr{
  justify-content: center;
  align-content: center;
}
.my-container-width{
  width:600px;
}
/* .no-wrap{
  white-space: nowrap;  
} */
.my-wrap {
  white-space: normal;
}
</style>