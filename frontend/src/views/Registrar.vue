<template>
  <div class="form-container">
    <h1>Registrar</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="usuário">Usuario:</label>
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
       <p>Já possui conta?<router-link to="/login">Login</router-link></p>

      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="success-message">
        {{ errorMessage }}
      </div>
    </form>
  </div>
  </template>

<script>
import axios from 'axios';

export default{
  name: 'Resgistrar',
  data(){
    return{
      username: '',
      email: '',
      password: '',
      successMessage: '', 
      errorMessage: ''
    }
  },
  methods: {
    async submitForm() {
      const formData = {
        username: this.username,
        email: this.email,
        password: this.password
      }

      try {
        const response = await axios.post('/api/v1/users/', formData);

        if (response.status >= 200 && response.status < 300) { 
          this.successMessage = 'Usuário registrado com sucesso! Redirecionando...';
            
          this.username = '';
          this.email = '';
          this.password = '';
         
          setTimeout(() => { 
            this.$router.push('/login');
          }, 2000);
        } else {
          
            console.log(response);
            this.errorMessage = "Ocorreu um erro." + response.data
          this.successMessage = ''; 
        }
      
      } catch (error) {
        
        console.error(error);
          if (error.response) {
              
              this.errorMessage = `Erro ${error.response.status}: ${error.response.data.username || error.response.data.email || error.response.data.password || 'Erro desconhecido'}`;
          } else if (error.request) {
              
              this.errorMessage = "Não foi possível conectar ao servidor. Verifique sua conexão com a internet.";
          } else {
             
              this.errorMessage = "Ocorreu um erro ao processar a requisição.";
          }
          this.successMessage = '';
      }
    }
  }
};
</script>