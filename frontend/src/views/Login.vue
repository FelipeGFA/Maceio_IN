<template>
  <div class="form-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Usuário:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Senha:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Entrar</button>
      <p>
        Não possui conta?
        <router-link to="/registrar">Registrar</router-link>
      </p>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async login() {
      this.error = ''; 
      try {
        const response = await axios.post('/api/v1/token/login', {
          username: this.username,
          password: this.password,
        });

        const token = response.data.auth_token;
        localStorage.setItem('token', token);
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        this.$router.push('/dashboard');

      } catch (error) {
        
        this.error = error.response?.data?.detail ||
          error.response?.data?.non_field_errors?.[0] || 
          'Usuário ou senha inválidos.';
           if(!this.error){
              this.error = 'Erro ao conectar com o servidor.';
           }

      }
    },
  },
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
