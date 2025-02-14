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
        const response = await axios.get('http://127.0.0.1:8000/api/v1/pessoas/'); // Verifique se a URL está correta
        console.log('Dados recebidos:', response.data); // Log para verificar os dados
        this.pessoas = response.data;
      } catch (error) {
        console.error('Erro ao obter pessoas:', error);
        // Se houver um erro, exiba uma mensagem para o usuário.
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
        await axios.delete(`http://127.0.0.1:8000/api/v1/pessoas/${this.pessoaParaExcluir.id}/`); // Verifique a URL
        this.getPessoas();
        this.pessoaParaExcluir = null;
      } catch (error) {
        console.error('Erro ao excluir pessoa:', error);
      }
    },
  },
};
</script>
