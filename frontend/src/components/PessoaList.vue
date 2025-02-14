<template>
  <div>
    <h1>Funcionarios cadastrados</h1>
    <table v-if="pessoas.length > 0" border="1" class="tabela">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Setor</th>
          <th>E-mail</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pessoa in pessoas" :key="pessoa.id">
          <td>{{ pessoa.nome }}</td>
          <td>{{ pessoa.setor_display }}</td>
          <td>{{ pessoa.email }}</td>
          <td>
            <button @click="iniciarEdicao(pessoa)">Editar</button>
            <button @click="confirmarExclusao(pessoa)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>Nenhum funcionário cadastrado.</p>

    <div v-if="pessoaParaExcluir">
      <p>Deseja realmente excluir {{ pessoaParaExcluir.nome }}?</p>
      <button @click="excluirPessoa()">Sim</button>
      <button @click="cancelarExcluir()">Não</button>
    </div>


    <PessoaForm
      v-if="pessoaParaEditar"
      :pessoa="pessoaParaEditar"
      :atualizando="true"
      @pessoaAtualizada="getPessoas"
      @cancelarEdicao="finalizarEdicao"
    />
  </div>

    <button @click="alternarFormularioAdicao">
      {{ mostrarFormularioAdicao ? 'Cancelar' : 'Adicionar Funcionário'}}
    </button>
    
    <PessoaForm
      v-if="mostrarFormularioAdicao"
      :atualizando="false"
      @pessoaAdicionada="getPessoas"
      @cancelarEdicao="mostrarFormularioAdicao = false"
    />
</template>

<script>
import axios from 'axios';
import PessoaForm from './PessoaForm.vue';

export default {
  name: 'PessoaList',
  components: {
    PessoaForm
  },
  data() {
    return {
      pessoas: [],
      mostrarFormularioAdicao: false,
      pessoaParaExcluir: null,
      pessoaParaEditar: null,
    };
  },
  mounted() {
    this.getPessoas();
  },
  methods: {
    async getPessoas() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/pessoas/'); 
        console.log('Dados recebidos:', response.data); 
        this.pessoas = response.data;
      } catch (error) {
        console.error('Erro ao obter pessoas:', error);
        
      }
    },
    alternarFormularioAdicao() {
      this.mostrarFormularioAdicao = !this.mostrarFormularioAdicao;
      if (this.mostrarFormularioAdicao) {
        this.pessoaParaEditar = null;
      }
    },
    iniciarEdicao(pessoa) {
      this.pessoaParaEditar = { ...pessoa };
      this.mostrarFormularioAdicao = false;
    },
    finalizarEdicao() {
      this.pessoaParaEditar = null;
    },
    confirmarExclusao(pessoa) {
      this.pessoaParaExcluir = pessoa;
    },
    cancelarExcluir() {
      this.pessoaParaExcluir = null;
    },
    async excluirPessoa() {
      if (!this.pessoaParaExcluir) return;
      try {
        await axios.delete(`http://127.0.0.1:8000/api/v1/pessoas/${this.pessoaParaExcluir.id}/`); 
        this.getPessoas();
        this.pessoaParaExcluir = null;
      } catch (error) {
        console.error('Erro ao excluir pessoa:', error);
      }
    },
  },
};
</script>

<style scoped>

.tabela {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.tabela th,
.tabela td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.tabela th {
  background-color: #f2f2f2;
}


.tabela button {
  background-color: #0D2F53; 
    color: white;
    padding: 6px 10px;  
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 5px; 
    transition: background-color 0.3s ease;
}

.tabela button:hover {
  background-color: #154773;  
}

.tabela button:active {
     background-color: #0a2342; 
    transform: translateY(1px);
}

.tabela button:last-child { 
  background-color: #c0392b; 
}

.tabela button:last-child:hover {
  background-color: #a93226; 
}


.add-button {
    background-color: #27ae60; 
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 20px; 
    transition: background-color 0.3s ease;
    display: block; 
    margin-left: auto;  
    margin-right: auto;
}

.add-button:hover {
  background-color: #1e8449; 
}
.add-button:active {
  background-color: #145a32;
  transform: translateY(1px);
}



div[v-if="pessoaParaExcluir"] {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  z-index: 2000; 
}

div[v-if="pessoaParaExcluir"] button {
   background-color: #0D2F53; /* Azul */
    color: white;
    padding: 6px 10px;  
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 5px; 
    transition: background-color 0.3s ease;
}
div[v-if="pessoaParaExcluir"] button:hover{
  background-color: #154773;  
}
</style>