<template>
  <div class="login-view">
    <h1>SignUpView</h1>
      <div class="userloginbox">
        <h2>MOVIESCAPE 회원가입</h2>
      <form v-on:submit.prevent="SignUp">
        <div class="form-group">
          <input type="text" placeholder="UserName" v-model="username">
        </div>
        <br>
        <div class="form-group">
          <input type="text" placeholder="Password" v-model="Password">
        </div>
        <br>
        <div class="form-group">
          <input type="submit" placeholder="PasswordConfirm" v-model="password2">
        </div>
        <br>
        <input type="submit" class="btn btn-primary" value="Sign up">
        <p class="signup-text" >Already have an account?</p>
          <router-link to="/Login">Login</router-link>
      </form>
      </div>
    </div>
</template>

<script>
export default {
  name:'SignUpView',
  data(){
    return {
      username:null,
      password1:null,
      password2:null
    }
  },
  methods: {
    SignUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,password1,password2
      }
      this.$store.dispatch('SignUp',payload)
    }
  }
}
</script>


<style scoped>
.login-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 50vh;
}

.userloginbox {
  width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 20px;
}


.form-control {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid hsl(0, 30%, 92%);
  border-radius: 4px;
}

.btn-primary {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  background-color: #063308;
  /* background: rgb(248, 47, 98); */
  color: #fff;
  cursor: pointer;
}

.signup-text {
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
}

.signup-text a {
  color: #e50914;
  text-decoration: none;
  font-weight: bold;
}

p {
  color: black;

}
</style>