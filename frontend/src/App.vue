<template>
  <router-view/>
</template>

<script>
import axios from 'axios';

export default{
  name: 'App',
  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>


<style>

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

  main {
    padding: 20px;
    min-height: calc(100vh - 60px - 40px); /*Ajuste a altura do main*/
  }
</style>
