<template>
  <div>
    
      <router-link to="/MovieList">MovieList</router-link>|
      <router-link to="/Recommend">Recommendation</router-link>|
      <router-link to="/Community">Community</router-link>|
      <router-link to="/Login">로그인</router-link>|
  </div>
</template>

<script>
export default {
  name: "TesT"
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ebeef1;

}

nav {
  padding: 30px;
  font-size: 50px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

button {
  width: 100px;
  height: 100px;
}
</style>