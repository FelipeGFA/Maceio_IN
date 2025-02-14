<template>
      <div class="dashboard-container">
    <p v-if="!isAuthenticated" class="login-message">Você precisa estar Logado para ver esta página.</p>
    <div v-if="isAuthenticated" class="content-wrapper">

      <MainHeader />

      <div class="sfaz-section">
        <div class="sfaz-container">
            <h2 class="sfaz-title">Secretaria Municipal de Fazenda (Sefaz) de Maceió</h2>
            <p class="sfaz-intro">
              A <strong>Secretaria Municipal de Fazenda (Sefaz)</strong> de Maceió é o órgão responsável pela gestão das
              finanças públicas do município. Suas principais atividades incluem:
            </p>
            <ul class="sfaz-list">
              <li><span class="list-icon">&#128181;</span> <strong>Arrecadação de tributos:</strong> IPTU, ISS, ITBI, taxas e contribuições.</li>
              <li><span class="list-icon">&#128202;</span> <strong>Gestão financeira:</strong> planejamento, execução e controle do orçamento municipal.</li>
              <li><span class="list-icon">&#128179;</span> <strong>Controle da dívida pública:</strong> acompanhamento e negociação da dívida do município.</li>
              <li><span class="list-icon">&#9993;</span> <strong>Fiscalização tributária:</strong> combate à sonegação fiscal e promoção da justiça fiscal.</li>
              <li><span class="list-icon">&#128100;</span> <strong>Atendimento ao contribuinte:</strong> prestação de informações e serviços relacionados aos tributos municipais.</li>
              <li><span class="list-icon">&#9881;</span> <strong>Modernização da gestão fazendária:</strong> implementação de sistemas e processos para otimizar a arrecadação e a gestão dos recursos públicos.</li>
            </ul>
            <p class="sfaz-conclusion">
              A Sefaz desempenha um papel fundamental na garantia dos recursos necessários para a execução das políticas
              públicas e para o desenvolvimento do município de Maceió.
            </p>
          </div>
      </div>

      <div class="list-section">
              <PessoaList />
            </div>
          <button @click="logout" v-if="isLogado">DESLOGAR</button> 
        </div>
      <Footer />
    </div>

</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import MainHeader from '../components/MainHeader.vue';
import PessoaList from '../components/PessoaList.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'Dashboard', 
  components: {
    MainHeader,
    PessoaList, 
    Footer,
  },

  setup() {
    const router = useRouter();
    const isLogado = ref(false); 


    onMounted(() => {
      isLogado.value = !!localStorage.getItem('token'); 
    });

     
     const isAuthenticated = computed(() => !!localStorage.getItem('token'));


    const logout = () => {
      localStorage.removeItem('token');
      axios.defaults.headers.common['Authorization'] = ''; 
      isLogado.value = false; 
       router.push('/login');
    };

    return {
      logout,
      isLogado, 
      isAuthenticated
    };
  }
};
</script>