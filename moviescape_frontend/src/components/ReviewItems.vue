<template>
  <div>
    <div class="searchWrap" >
          <input class="searchbar" type="text" v-model="keyword" @input="setSearchTerm" @keyup.enter="searchReview" />
          <a href="javascript:;" @click="searchReview" class="btnSearch">검색🔍</a>
    <ul>
    </ul>
  </div>
    <div class="containerbar">
      <!-- <div class="table-responsive"> -->
        <table class="table my-table ">
          <thead>
          <tr class = "textcolor">
            <th scope="col">No</th>
            <th scope="col">글제목</th>
            <th scope="col">글내용</th>
            <th scope="col">영화</th>
            <th scope="col">작성자</th>
            <th scope="col">작성시간</th>
          </tr>
          </thead>
        <tbody>
          <ReviewCard v-for="review in ITEMreviews" :key="review.pk" :CARDreview="review"/>          
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
    /* .searchWrap{border:1px solid #888; border-radius:5px; text-align:center; padding:20px 0; margin-bottom:40px;} */
    .searchWrap input{width:40%; height:36px; border-radius:3px; padding:0 10px; border:3px solid #050505;} 
    .searchWrap .btnSearch{display:inline-block; margin-left:10px;}

.containerbar {
  background: rgb(7, 7, 7);
  padding: 20px;
  width: 100%;
}
.my-table {
  white-space: nowrap;
}

.textcolor {
  color: whitesmoke;

}

.btnSearch {
  display: inline-block;
  margin-left: 10px;
  background-color: transparent;
  cursor: pointer;

  padding: 8px 16px;
  border-radius: 4px;
  color: #fffdfd;
  cursor: pointer;
  font-size: 14px;
  text-decoration: none;
}


</style>


