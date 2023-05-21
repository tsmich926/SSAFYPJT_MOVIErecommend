<template>
  <div>
    <h1>CreateReviewView</h1>
    <div class="board-detail">
      <form action="">
        <div class="board-contents">
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" class="w3-input w3-border" placeholder="제목을 입력해주세요."><br>
          <label for="input">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="content" placeholder="리뷰를 작성해주세요."></textarea><br>
        </div>
      </form>
      <div class="common-buttons">
        <input type="button" @click="saveArticle" class="btn btn-primary" style="background-color: #008080;" value="작성완료">&nbsp;
        <input type="button" @click="gotoComunityView" class="btn btn-primary" style="background-color: #008080;" value="목록">&nbsp;

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default { 
  name:'CreateReviewView',
  data(){
    return{
      content:null,
      title:null,
    }
  },
  methods:{
    gotoComunityView(){
      this.$router.push({name:'Community'})
    },
    saveArticle(){
      const API ='http://127.0.0.1:8000'
      
      const title = this.title
      const content = this.content

      if(!title){
        alert('제목을 입력하세요')
      } else if (!content){
        alert('내용을 입력하세요')
        return
      }
    
      axios({
        method:'post',
        url:`${API}/api/v1/movies/38015/review/`,
        data: {
          title,
          content,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name:'ReviewListView'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  computed:{

  },

}
</script>

<style>

</style>