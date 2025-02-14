<template>
  <div class="form-container">
    <h1>Registrar</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="usuario">Usuario:</label>
        <input type="text" id="usuario" v-model="username" required />
      </div>

      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>

      <div>
        <label for="senha">Senha:</label>
        <input type="password" id="senha" v-model="password" required />
      </div>

      <button type="submit">Registrar</button>
      <p>
        Já possui conta?<router-link to="/login">Login</router-link>
      </p>

      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Resgistrar', 
  data() {
    return {
      username: '',
      email: '',
      password: '',
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async submitForm() {
      this.successMessage = ''; 
      this.errorMessage = '';
      try {
        const response = await axios.post('/api/v1/users/', {
          username: this.username,
          email: this.email,
          password: this.password,
        });

        if (response.status >= 200 && response.status < 300) {
          this.successMessage = 'Usuário registrado com sucesso! Redirecionando...';

          
          this.username = '';
          this.email = '';
          this.password = '';

          setTimeout(() => {
            this.$router.push('/login');
          }, 2000);
        }
      } catch (error) {
        
        if (error.response) {
          const data = error.response.data;
           
           this.errorMessage = data.username?.[0] ||
                            data.email?.[0] ||
                            data.password?.[0] ||
                            data.detail || 
                            `Erro ${error.response.status}: Erro desconhecido`;


        } else if (error.request) {
          this.errorMessage = "Não foi possível conectar ao servidor.";
        } else {
          this.errorMessage = "Erro ao processar a requisição.";
        }
      }
    },
  },
};
</script>

<style scoped>
  
  .success-message {
    color: green;
    margin-top: 10px;
  }

  .error-message{
    color: red;
    margin-top: 10px;
  }
</style>
