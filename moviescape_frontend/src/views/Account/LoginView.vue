<template>
  <div>
    <h1>LoginView</h1>
    <div class="userloginbox">
      <form v-on:submit.prevent="LogIn">
        <input type="text" placeholder="userName" v-model="username" required>
        <input type="password" placeholder="userPassWord" v-model="password" required>
        <br>
        <input type="submit" value="Login">
        <p class="signup">don't have an account?
          <router-link to="/Signup">signup</router-link>
          <!-- <a href="javascript:void(0);" @click="toggleForm">Sign up</a> -->
        </p>
      </form>
    </div>

  </div>
</template>


<script>
export default {
  name: 'LoginView' ,
  data(){
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,password
      }

      this.$store.dispatch('LogIn',payload)
    },
    // logout()
  }
}


</script>

<style>

.userloginbox {
  width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>
