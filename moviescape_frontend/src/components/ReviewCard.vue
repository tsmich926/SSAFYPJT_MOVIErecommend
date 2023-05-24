<template>
  <tr>
      <!-- <tbody>
        <tr>
          <td class="noBorder">{{CARDreview.id}}  |</td>
          <a href="#"><td class="noBorder">  {{CARDreview.title }} </td></a>
          <td class="noBorder">|  {{CARDreview.content }}  |</td>
          <td class="noBorder">{{CARDreview.movie.title }}  |  </td>
          <a href="#" @click="gotoDetail" class="noBorder">{{CARDreview.user.username}}</a>
          <td class="noBorder">|  {{formatTime(CARDreview.created_at) }}</td>
        </tr>
      </tbody> -->

    <td >{{ CARDreview.id }}</td>
    <td >
      <a href="#" @click="gotoReviewDetail">{{ CARDreview.title }}</a>
    </td>
    <td > {{ CARDreview.content }} </td>
    <td >{{ CARDreview.movie.title }} </td>
    <td >
      <a href="#" @click="gotoDetail">{{ CARDreview.user.username }}</a>
    </td>
    <td > {{ formatTime(CARDreview.created_at) }}</td>
  </tr>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name:'ReviewCard',
  props:{
    CARDreview:Object
  },
  computed:{
    ...mapState(['user']),
  },
  methods: {
    formatTime(time) {
      const date = new Date(time);
      return date.toLocaleString();
    },
    gotoDetail(){
      console.log(this.CARDreview.user)
      if (this.user.username==this.CARDreview.user.username){
        this.$router.push({name:"MyDetailView"})
      }
      else{
        this.$router.push({name:"UserDetailView"})
        this.$store.commit('SAVE_USER_ID', this.CARDreview.user.id)
      }
    },
    gotoReviewDetail(){
      this.$router.push(`/ReviewDetailView/${this.CARDreview.id}`)
    }
  },
}
</script>

<style scoped>
    .searchWrap{border:1px solid #888; border-radius:5px; text-align:center; padding:20px 0; margin-bottom:40px;}
    .searchWrap input{width:60%; height:36px; border-radius:3px; padding:0 10px; border:1px solid #888;}
    .searchWrap .btnSearch{display:inline-block; margin-left:10px;}

  .table {
    background: white;
  }

  .container {
  padding: 20px;
}

.noBorder {
  border:none;
}
</style>