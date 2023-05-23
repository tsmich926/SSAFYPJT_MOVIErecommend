<template>
  <div>
    <footer class="black-footer">
      <div class="footer-content">
        Footer 내용을 추가하세요
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