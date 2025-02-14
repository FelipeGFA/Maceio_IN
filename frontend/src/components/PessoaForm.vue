<template>
    <div class="centralizar">
        <h2>{{ atualizando ? 'Editar Pessoa' : 'Adicionar Funcionário' }}</h2>
        <form @submit.prevent="salvarPessoa">
            <div>
                <label for="nome">Nome:</label>
                <input type="text" id="nome" v-model="pessoaLocal.nome" required>
            </div>
            <div>
                <label for="setor">Setor:</label>
                <select id="setor" v-model="pessoaLocal.setor" required>
                    <option value="" disabled>Selecione o setor</option>
                    <option value="contabilidade">Contabilidade</option>
                    <option value="financeiro">Financeiro</option>
                    <option value="atendimento">Atendimento</option>
                    <option value="orcamento">Orçamento</option>
                    <option value="ti">TI</option>
                </select>
            </div>
            <div>
                <label for="email">E-mail:</label>
                <input type="email" id="email" v-model="pessoaLocal.email" required>
            </div>
            <button type="submit">{{ atualizando ? 'Atualizar' : 'Salvar' }}</button>
            <button type="button" @click="cancelarEdicao" v-if="atualizando">Cancelar</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'PessoaForm',
    props: {
        pessoa: {
            type: Object,
            default: null 
        },
        atualizando: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            pessoaLocal: this.pessoa ? { ...this.pessoa } : {
                nome: '',
                setor: '',
                email: ''
            } 
        };
    },
    watch: {
        pessoa: {
            handler: function (novoPessoa) {
                if (novoPessoa) {
                    this.pessoaLocal = { ...novoPessoa };
                } else {
                    this.pessoaLocal = {  
                        nome: '',
                        setor: '',
                        email: ''
                    };
                }
            },
            deep: true  
        }
    },
    methods: {
        async salvarPessoa() {
            try {
                if (this.atualizando) {

                    await axios.put(`http://127.0.0.1:8000/api/pessoas/${this.pessoaLocal.id}/`, this.pessoaLocal);
                    this.$emit('pessoaAtualizada'); 
                } else {
                    
                    await axios.post('http://127.0.0.1:8000/api/pessoas/', this.pessoaLocal);
                    this.$emit('pessoaAdicionada'); 
                }
                
                this.pessoaLocal = {
                    nome: '',
                    setor: '',
                    email: ''
                };
            } catch (error) {
                console.error('Erro ao salvar pessoa:', error);
            }
        },
        cancelarEdicao() {
            
            this.$emit('cancelarEdicao');
        }
    }
};
</script>

