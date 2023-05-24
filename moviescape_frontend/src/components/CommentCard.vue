<template>
  <div class="">
    <div class="comment-header">
      <span class="comment-author" @click="gotoUserDetail" ref="authorSpan" @mouseover="setCursor('pointer')" @mouseout="setCursor('auto')">{{ Comment.user.username }}</span>
      <span class="comment-date">{{ formatDate(Comment.created_at) }}</span>
    </div>
    <div class="comment-content">
      <template v-if="editing">
        <textarea v-model="editedComment" class="comment-edit-input"></textarea>
        <button class="comment-button edit-button" @click="saveComment">저장</button>
        &nbsp;&nbsp;
        <button class="comment-button delete-button" @click="cancelEdit">취소</button>
      </template>
      <template v-else>
        {{ Comment.comment }}
        <!-- {{Comment.user.id}} -->
      </template>
    </div>
    <div class="comment-buttons">
      <button v-if="myComment && !editing" class="comment-button edit-button" @click="startEdit">
        수정
      </button>
      &nbsp;&nbsp;
      <button v-if="myComment && !editing" class="comment-button delete-button" @click="deleteComment">
        삭제
      </button>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex';
import axios from 'axios';
export default {
  name: 'CommentCard',
  props: {
    comment: Object
  },
  data() {
    return {
      editing: false,
      editedComment:'',
      nowComment:null,
    };
  },
  computed: {
    ...mapState(['user']),
    myComment() {
      return this.user.username == this.Comment.user.username;
    },
    Comment(){
      return this.nowComment
    }
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
    setCursor(cursorType) {
      this.$refs.authorSpan.style.cursor = cursorType;
    },
    gotoUserDetail() {
      console.log(this.Comment.user.username);
      if (this.user.username == this.Comment.user.username) {
        this.$router.push({ name: 'MyDetailView' });
      } else {
        this.$router.push({ name: 'UserDetailView' });
        this.$store.commit('SAVE_USER_ID', this.Comment.user.id);
      }
    },
    startEdit() {
      this.editing = true;
      this.editedComment = this.Comment.comment;
    },
    deleteComment(){
      const comment_id=this.Comment.id
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/api/v1/comments/${comment_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log(res)
        this.$emit('commentDeleted', this.Comment.id);
      })
      .catch(err=>{
        console.log(err)
      })
    },
    saveComment() {
      // 저장 로직 구현
      // this.editedComment에 있는 수정된 내용을 저장한다고 가정
      // 저장 후 this.editing = false;를 호출하여 폼을 숨긴다 {
      const comment_id=this.Comment.id
      const comment=this.editedComment

      console.log("아오 잠좀자자")
      console.log(comment_id,comment)
      axios({
        method:'put',
        url: `http://127.0.0.1:8000/api/v1/comments/${comment_id}/`,
        data: {
          comment,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res=>{
        console.log(res)
        this.nowComment=res.data
        this.editing = false;
      })
      .catch(err=>{
        console.log(err)
      })
    },
    cancelEdit() {
      this.editing = false;
    }
  },
  created(){
    this.nowComment=this.comment
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

.comment-buttons {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

.comment-button {
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  font-size: 14px;
  cursor: pointer;
}

.edit-button {
  background-color: #008080;
  color: white;
}

.delete-button {
  background-color: rgb(255, 90, 0);
  color: white;
}

.comment-edit-input {
  margin-bottom: 10px;
  width: 100%;
}

.save-button {
  background-color: #008080;
}

.cancel-button {
  background-color: rgb(255, 90, 0);
}
</style>
