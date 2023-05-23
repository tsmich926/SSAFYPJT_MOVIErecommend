<template>
  <div class="container justify-content-center">
    <div class="row">
      <!-- <h1>HumanListItems</h1> -->
        <div class="col" v-for="actor in ITEMactors" :key="actor.pk" >
          <ActorCard :CARDhuman="actor"/>
        </div> 
    </div>
  </div>
</template>

<script>
import ActorCard from '@/components/ActorCard.vue'

export default {
  name:'ActorListItems',
  components:{
    ActorCard
  },

  props:{
    ITEMactors:Array
  },
  methods:{

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

  },

    }

}
</script>

<style>
.card{
  background-color: rgb(157, 178, 191);
  transition: transform 0.3s ease;
}


.card.zoom-in {
  transform: scale(1.1);
}

.card-title {
  color: black;
}
</style>