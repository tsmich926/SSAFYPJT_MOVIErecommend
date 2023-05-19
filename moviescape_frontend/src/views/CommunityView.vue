<template>
  <div>
    <p>Community</p>
    <div>
      <p>게시글</p>
      <input type="button" value="게시글 작성" @click="gotoCreateArticle">
    </div>
    
    
  </div>
</template>

<script>

export default {

  components: { 
  },
  methods:{
    gotoCreateArticle(){
      this.$router.push({name:'CreateArticleView'})
    }
  }

}
</script>



<style>
.btn-save,
.btn-list {
  width: 200px; /* 원하는 너비 값으로 수정 */
  height: 100px; /* 원하는 높이 값으로 수정 */
}
</style>
