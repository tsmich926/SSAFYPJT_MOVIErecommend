<template>
  <div class="comment-list">
    <div v-for="comment in ITEMcomments" :key="comment.id" class="comment">
      <CommentCard :comment="comment" @commentDeleted="handleCommentDeleted" />
    </div>
  </div>
</template>

<script>
import CommentCard from '@/components/CommentCard.vue';

export default {
  name: 'CommentListItems',
  components: {
    CommentCard,
  },
  props: {
    ITEMcomments: Array,
  },
  data() {
    return {
      comments: [],
    };
  },
  methods: {
    handleCommentDeleted(commentId) {
      // 해당 commentId를 가진 댓글의 인덱스를 찾습니다.
      // const index = this.comments.findIndex((comment) => comment.id === commentId);
      // if (index !== -1) {
      //   // comments 배열에서 댓글을 제거합니다.
      //   this.comments.splice(index, 1);
      // }
      console.log(commentId)
      this.$emit('commentDeleted');
      // this.comments = this.comments.filter((comment) => comment.id !== commentId);
    },
  },
  mounted(){
    this.comments = this.ITEMcomments
  },
  created() {
    this.comments = this.ITEMcomments;
  },
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
