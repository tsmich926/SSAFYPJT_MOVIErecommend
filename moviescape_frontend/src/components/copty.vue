
<template>
  <div class="comment-board">
    <div class="comment-list">
      <div v-for="comment in comments" :key="comment.id" class="comment">
        <div class="comment-header">
          <span class="comment-author">{{ comment.author }}</span>
          <span class="comment-date">{{ formatDate(comment.date) }}</span>
        </div>
        <div class="comment-content">
          {{ comment.content }}
        </div>
      </div>
    </div>
    <div class="comment-form">
      <textarea v-model="newComment" placeholder="댓글을 입력하세요"></textarea>
      <button class="btn btn-primary" @click="addComment">댓글 달기</button>
    </div>
  </div>
</template>
<style scoped>
.comment-board {
  background-color: black;
  color: white;
  padding: 20px;
}

.comment-list {
  margin-bottom: 20px;
}

.comment {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 10px;
  margin-bottom: 10px;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 5px;
}

.comment-author {
  font-weight: bold;
}

.comment-date {
  font-size: 12px;
}

.comment-form {
  display: flex;
  margin-top: 20px;
}

.comment-form textarea {
  flex: 1;
  padding: 10px;
  resize: none;
  border: none;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
}

.comment-form button {
  margin-left: 10px;
}
</style>