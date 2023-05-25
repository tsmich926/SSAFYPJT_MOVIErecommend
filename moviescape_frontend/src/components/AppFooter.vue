<template>
  <div>
    <footer class="black-footer">
      <div class="footer-content">
        상호 : MOVIESCAPE ㅣ 공동 대표 : 손임현, 황수아 ㅣ 사업자번호 : 123-45-678910
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name:'AppFooter',
  data(){
    return{

    }
  }
}
</script>

<style>
.black-footer {
  background-color: black;
  color: white;
  padding: 20px;
}

.footer-content {
  display: flex;
  justify-content: center;
  align-items: center;
  
}

</style>