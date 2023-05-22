<template>
  <div class="">
      <tbody>
        <tr>
          <td class="noBorder">{{CARDreview.id}}</td>
          <a href="#"><td class="noBorder">{{CARDreview.title }}</td></a>
          <td class="noBorder">{{CARDreview.content }}</td>
          <td class="noBorder">{{CARDreview.movie.title }}</td>
          <td class="noBorder">{{CARDreview.user.username}}</td>
          <td class="noBorder">{{ formatTime(CARDreview.created_at) }}</td>
        </tr>
      </tbody>
  </div>
    <!-- <p>글 번호</p>
    <p>글 제목 : {{CARDreview.title }}</p>
    <p>글 내용:{{CARDreview.content }}</p>
    <p>영화:{{CARDreview.movie.title }}</p>
    <p>작성자:{{CARDreview.user.username}}</p>
    <p>작성시간:{{CARDreview.created_at}}</p> -->
    <!-- <img :src="`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`" alt=""> -->
  

</template>

<script>

export default {
  name:'ReviewCard',
  props:{
    CARDreview:Object
  },
  methods: {
    formatTime(time) {
      const date = new Date(time);
      return date.toLocaleString();
    }
  }
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