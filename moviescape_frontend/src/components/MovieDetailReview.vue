<template>
  <div class="review-container">
    <div class="review-content">
      <div class="review-header" @click="gotoUserDetail" ref="authorDiv" @mouseover="setCursor('pointer')" @mouseout="setCursor('auto')">
        <img class="profile-image" type="circle" :src="UserProfile" alt="">
        <div class="review-username">{{ review.user.username }}</div>
      </div>
      <div @click="gotoReviewDetail" class="review-details">
        <div  class="review-title">
          <span class="title-label">제목:</span>
          <span>{{ review.title }}</span>
        </div>
        <div class="review-text">
          <span class="content-label">내용:</span>
          <span>{{ review.content }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'MovieDetailReview',
  props: {
    review: Object,
  },
  computed: {
    ...mapState(['user']),
    UserProfile() {
      if (this.review.user.profile_path === 'default') {
        return 'http://localhost:8080/user/default.png';
      } else {
        return this.review.user.profile_path;
      }
    },
  },
  methods:{
    gotoReviewDetail() {
      this.$router.push(`/ReviewDetailView/${this.review.id}`);
    },
    setCursor(cursorType) {
      this.$refs.authorDiv.style.cursor = cursorType;
    },
    gotoUserDetail() {
      console.log(this.review.user);
      if (this.user.username == this.review.user.username) {
        this.$router.push({ name: 'MyDetailView' });
      } else {
        this.$router.push({ name: 'UserDetailView' });
        this.$store.commit('SAVE_USER_ID', this.review.user.id);
      }
    },
  }
};
</script>

<style scoped>
.review-container {
  margin-bottom: 20px;
  margin-right:20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.review-content {
  display: flex;
  align-items: center;
}

.review-header {
  display: flex;
  align-items: center;
}

.profile-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

.review-username {
  font-weight: bold;
}

.review-details {
  margin-top: 5px;
  margin-left: 25%;
}

.review-title {
  font-size: 18px;
  text-align: center;
}

.title-label {
  font-weight: bold;
  margin-right: 5px;
}

.review-text {
  margin-top: 5px;
  text-align: center;
}

.content-label {
  font-weight: bold;
  margin-right: 5px;
}
</style>