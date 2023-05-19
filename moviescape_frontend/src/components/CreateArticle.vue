<template>
  <div>
    <div class="board-detail">
      <form action="">
        <div class="board-contents">
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" class="w3-input w3-border" placeholder="제목을 입력해주세요."><br>
          <input type="text" v-model="author" class="w3-input w3-border" placeholder="작성자를 입력해주세요." v-if="idx === undefined">
          <label for="input">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        </div>
      </form>

      <div class="board-contents">
        <textarea id="" cols="5" rows="5" v-model="contents" class="w3-input w3-border" style="resize: none;">
        </textarea>
      </div>
      <div class="common-buttons">
        <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnSave">저장</button>&nbsp;
        <button type="button" class="" v-on:click="fnList">목록</button>
        <button type="button" class="btn btn-primary" style="background-color: #008080;">저장</button>

      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>