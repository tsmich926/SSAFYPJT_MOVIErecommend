<template>
  <div>
    <div class="searchWrap">
      <div class="searchInputs">
        <button class="btn btn-outline-light" type="button" @click="gotoCreateArticle">글쓰기</button>
        <input class="searchbar" type="text" v-model="keyword" @input="setSearchTerm" @keyup.enter="searchReview" />
        <a href="javascript:;" @click="searchReview" class="btnSearch">검색🔍</a>
      </div>
    </div>
    <div class="containerbar">
      <table class="table my-table">
        <thead>
          <tr class="textcolor">
            <th scope="col">No</th>
            <th class="my-fas" scope="col">글제목</th>
            <th scope="col">글내용</th>
            <th scope="col">영화</th>
            <th scope="col">작성자</th>
            <th scope="col">작성시간</th>
          </tr>
        </thead>
        <tbody>
          <ReviewCard v-for="review in reviews" :key="review.pk" :CARDreview="review"/>
        </tbody>
      </table>
    </div>
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

    keyword:null,
    searchTerm: '',
    isFocus: false,
    selectedObj: null,
    toreviews:null
    }
  },
  props:{
    ITEMreviews:Array
  },
  computed:{
    reviews(){
      return this.toreviews
    }
  },
  methods: {
    gotoCreateArticle(){
      this.$router.push({name:'CreateReviewView'})
    },
    setSearchTerm(){
      console.log()
    },
    searchReview(){
      const keyword = this.keyword;
      if (keyword==null){
        this.toreviews = this.ITEMreviews
      }else if(keyword==''){
        this.toreviews = this.ITEMreviews
      }
      else{
      this.toreviews = this.ITEMreviews.filter(review => review.movie.title === keyword);
      }
    }

  },
  created(){
    this.toreviews=this.ITEMreviews
  }


}
</script>

<style scoped>
.my-fas{
  color: white;
}
.searchWrap {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 40px;
}

.searchInputs {
  display: flex;
  align-items: center;
}

.searchInputs > * {
  margin-right: 10px;
}

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
  border-radius: 10px;
  color: #fffdfd;
  cursor: pointer;
  font-size: 14px;
  text-decoration: none;
}

</style>


