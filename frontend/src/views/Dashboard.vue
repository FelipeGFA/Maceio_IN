<template>
    <div>
        <h1>DASHBOARD</h1>
        <p v-if="!isAuthenticated">Você precisa estar Logado para ver esta página.</p>
        <div v-if="isAuthenticated">
            <h1>PARABENS VOCE ESTÁ Logado</h1>
            <button @click="logout" v-if="isLogado">DESLOGAR</button> 
        </div>

    </div>

</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'; // Importa o Axios

export default {
  name: 'Dashboard', // Ou o nome do seu componente
  setup() {
    const router = useRouter();
    const isLogado = ref(false); // Começa como false


    onMounted(() => {
      isLogado.value = !!localStorage.getItem('token'); // true se tiver token, false se não tiver
    });

     // Use um computed para verificar o status de login
     const isAuthenticated = computed(() => !!localStorage.getItem('token'));


    const logout = () => {
      localStorage.removeItem('token');
      axios.defaults.headers.common['Authorization'] = ''; // Limpa o header
      isLogado.value = false; // Atualiza o estado reativo
       router.push('/login');
    };

    return {
      logout,
      isLogado, // Expõe isLogado para o template
      isAuthenticated
    };
  }
};
</script>