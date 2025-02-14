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

                    await axios.put(`http://127.0.0.1:8000/api/v1/pessoas/${this.pessoaLocal.id}/`, this.pessoaLocal);
                    this.$emit('pessoaAtualizada'); 
                } else {
                    
                    await axios.post('http://127.0.0.1:8000/api/v1/pessoas/', this.pessoaLocal);
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

<style scoped>
.centralizar {
  display: flex;
  flex-direction: column;
  align-items: center; 
}

form {
    width: 80%; 
    max-width: 500px; 
    margin: 0 auto; 
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
}


div {
  margin-bottom: 10px; 
}

label {
  display: block; 
  margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
select {
  width: 100%; 
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; 
}

button {
  background-color: #0D2F53;  
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer; 
  margin-right: 10px; 
  transition: background-color 0.3s ease; 
}

button:hover {
  background-color: #154773; 
}

button:active {
  background-color: #0a2342; 
  transform: translateY(1px); 
}
button[type="button"] {
    background-color: #ccc; 
    color: #333;
}

button[type="button"]:hover {
    background-color: #bbb; 
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  width: 80%; 
  max-width: 500px;
}

.close {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 24px;
  cursor: pointer;
  color: #888;
}
</style>