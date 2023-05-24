<template>
  <div id="app" class="my_backgroundimg">
    <div class="nav_space"></div>
    <div class="my_content">
      <div>
        <NavigationBar />
      </div>
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
  height: 100vh;
  /* pointer-events: none; */
  /* position: fixed; */
  top: 0;
  width: 100%;

  min-height: 100vh;
}

.my_content {
  max-width: 80%;
  max-height:80%;
  text-align: center;
}

.nav_space {
  height: 56px;
}


.footer_wrapper {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 95%;
  margin-top: auto;
}
</style>