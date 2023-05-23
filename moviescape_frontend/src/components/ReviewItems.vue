<template>
  <div>
    <div class="searchWrap" >
          <input type="text" v-model="keyword" @input="setSearchTerm" @keyup.enter="searchReview" /><a href="javascript:;" @click="searchReview" class="btnSearch btn">검색</a>
    <ul>

    </ul>
  </div>
    <div class="containerbar">
      <!-- <div class="table-responsive"> -->
        <table class="table my-table ">
          <thead>
          <tr>
            <th scope="col">No</th>
            <th scope="col">글제목</th>
            <th scope="col">글내용</th>
            <th scope="col">영화</th>
            <th scope="col">작성자</th>
            <th scope="col">작성시간</th>
          </tr>
        </thead>
        <tbody>
          <div v-for="review in ITEMreviews" :key="review.pk" >
            <ReviewCard :CARDreview="review"/>
          </div>
        </tbody>
        </table>
      </div>
    <!-- </div> -->  
  </div>
  
</template>

<script>
import ReviewCard from '@/components/ReviewCard.vue'
export default {
  name:'ReviewItems',
  components:{
    ReviewCard
  },
  data(){
    return {

    keyword:'',
    searchTerm: '',
    isFocus: false,
    selectedObj: null
    }
  },
  props:{
    ITEMreviews:Array
  },

  methods: {
    setSearchTerm(){
      console.log()
    },
    searchReview(){
      console.log()
    }

  }


}
</script>

<style scoped>
    .searchWrap{border:1px solid #888; border-radius:5px; text-align:center; padding:20px 0; margin-bottom:40px;}
    .searchWrap input{width:40%; height:36px; border-radius:3px; padding:0 10px; border:1px solid #888;}
    .searchWrap .btnSearch{display:inline-block; margin-left:10px;}

.containerbar {
  background: white;
  padding: 20px;
  width: 100%;
}
.my-table {
   white-space: nowrap;
}
/* .scroll-wrapper > * {
  margin-right: 10px;
  white-space: nowrap;
} */
</style>