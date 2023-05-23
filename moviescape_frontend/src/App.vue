<template>
  <div id="app" class="my_backgroundimg">
    <div class="nav_space"></div>
    <div class="my_content">
      <h1>Moviescape</h1>
      <h5>사용자 : {{user.username}}</h5>
      <NavigationBar />
    </div>
    <div class="footer_wrapper">
      <AppFooter />
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import AppFooter from '@/components/AppFooter.vue'

import { mapState } from 'vuex';
    
export default {
  name: 'app',
  components: {
    NavigationBar,
    AppFooter
  },
  computed:{
    ...mapState(['user']),
  }
}
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: rgb(71, 71, 71);
  color: white;
  overflow-x: auto;
}

.my_backgroundimg {
  background-image: url('@/assets/Backgroundimg3.jfif');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.my_content {
  max-width: 80%;
  text-align: center;
}

.nav_space {
  height: 56px;
}

.footer_wrapper {
  margin-top: auto;
  min-width: 100%;
}
</style>
