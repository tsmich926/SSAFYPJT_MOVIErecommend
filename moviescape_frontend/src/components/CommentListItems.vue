
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

<script>
export default {
  name: 'CommentBoard',
  props:{
    ITEMcomments:Array
  },
  data() {
    return {
      comments: [
        { id: 1, author: '사용자1', date: '2023-05-24', content: '예쁜 게시판 댓글입니다.' },
        { id: 2, author: '사용자2', date: '2023-05-23', content: '멋진 게시판이네요!' },
        { id: 3, author: '사용자3', date: '2023-05-22', content: '이 게시판을 좋아합니다.' }
      ],
      newComment: ''
    };
  },
  methods: {
    formatDate(date) {
      // 날짜 형식을 원하는 형태로 변환하는 함수
      // 예: 2023-05-24 -> 2023년 5월 24일
      return new Date(date).toLocaleDateString('ko-KR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },
    addComment() {
      if (this.newComment.trim() !== '') {
        const newId = this.comments.length + 1;
        const newComment = {
          id: newId,
          author: '새로운 사용자',
          date: new Date().toISOString().slice(0, 10),
          content: this.newComment.trim()
        };
        this.comments.push(newComment);
        this.newComment = '';
      }
    }
  }
};
</script>

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