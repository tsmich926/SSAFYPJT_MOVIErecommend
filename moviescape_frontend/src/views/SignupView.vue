<template>
  <div class="usersignupbox">
      <form v-on:submit.prevent="SignUp">
        <h2>Create an account</h2>
        <input type="text" placeholder="UserName" v-model="username">
        <input type="password" placeholder="Password" v-model="password">
        <input type="submit" value="Sign up">
        <p>Already have an account?
          <router-link to="/Login">Login</router-link>
        </p>
      </form>
    </div>
</template>

<script>
export default {
  name:'SignUP',
  data(){
    return {
      username:null,
      password:null
    }
  },
  methods: {
    SignUp(){
      const username = this.username
      const password = this.password

      const payload = {
        username,password
      }
      this.$store.dispatch('SignUp',payload)
    }
  }
}
</script>

<style>

</style>