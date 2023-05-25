<template>
  <div>
    <article class="custom-13frh63">
      <div class=" custom-6fc8lh">
        <a href="https://pedia.watcha.com/ko-KR/users/36lvXDY3BvXdn" rel="noopener noreferrer" target="_blank" title="왓챠피디아 - Saerom Kim">
          <img alt="Saerom Kim" src="https://an2-img.amz.wtchn.net/image/v2/BdZpvyD57kh3473wd0Xp4Q.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1UQXdlREV3TUNKZExDSndJam9pTDNZeUwzTjBiM0psTDNWelpYSXZNelpzZGxoRVdUTkNkbGhrYmk5d2NtOW1hV3hsTHpFMk1qazVPVEU0TURnMU56Z3lNRGszT1RJaWZRLnVHMVpuXzdXMjl0aVN4LXlFZXhMTDlJX3ZIVmMxdjFPOUV2LWtLREFNRjQ" class="custom-nhnvgi">
          <!-- <img alt="Saerom Kim" :src="`${user.profile_path}`" class="custom-nhnvgi"> -->
        </a>
      </div>
      <div class="custom-yp9swi" v-for="review in reviews" :key="review.id">
        <div class="custom-1sg2lsz">
          <div class="custom-ex2l60">
            <a href="https://pedia.watcha.com/ko-KR/users/36lvXDY3BvXdn" rel="noopener noreferrer" target="_blank" title="왓챠피디아 - Saerom Kim">{{review.user.username}}</a>
          </div>
          <div size="10" class="custom-16jrvw7">
          </div>
        </div>
        <div class="d-flex justify-content-start custom-lz79eo">
          <p class="LinesEllipsis  ">{{review.title}}<wbr></p>
        </div>
      </div>
    </article>
  </div>
</template>
<script>
export default {
  name:'MovieDetailReview',
  props:{
    reviews:Object,
  }

}
</script>

<style>
.custom-13frh63 {
    display: flex;
    align-items: center; /* Vertically center the items */
    padding: 8px 0px;
}
.custom-6fc8lh {
    margin: 0px 8px 0px 0px;
}
.custom-yp9swi {
    flex: 1 1 0%;
}

.LinesEllipsis {
    display: flex;
    align-items: center; /* Vertically center the text */
    justify-content: center; /* Horizontally center the text */
    height: 100%; /* Set the height to 100% of the parent container */
    margin: 0; /* Remove default margin */
}
</style>