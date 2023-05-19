<template>
  <div>
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
        <input type="button" class="btn btn-primary" style="background-color: #008080;" value="작성">&nbsp;
        <input type="button" @click="gotoComunityView" class="btn btn-primary" style="background-color: #008080;" value="목록">&nbsp;

      </div>
    </div>
  </div>
</template>

<script>
export default { 
  name:'CreateArticle',
  data(){
    return{
      content:null,
      title:null,
    }
  },
  methods:{
    gotoComunityView(){
      this.$router.push({name:'Community'})
    }
  },
  computed:{

  },

}
</script>

<style>

</style>