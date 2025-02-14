# Projeto Vue.js - CRUD de Funcionários com Autenticação

Este projeto é uma aplicação web construída com Vue.js que implementa as operações CRUD (Create, Read, Update, Delete) para gerenciar informações de funcionários, juntamente com um sistema de autenticação de usuários.

## Visão Geral

A aplicação permite:

1.  **Registro de Usuários:** Novos usuários podem criar contas fornecendo um nome de usuário, e-mail e senha.
2.  **Login:** Usuários registrados podem fazer login com seu nome de usuário e senha.
3.  **Dashboard (Página Principal):**
    *   Exibe uma mensagem de boas-vindas e informações sobre a Secretaria Municipal de Fazenda (Sefaz) de Maceió (conteúdo estático, mas otimizado para fácil edição).
    *   Lista os funcionários cadastrados (CRUD).
    *   Permite adicionar novos funcionários.
4.  **CRUD de Funcionários:**
    *   **Listar:** Exibe uma tabela com os funcionários cadastrados, mostrando nome, setor e e-mail.
    *   **Adicionar:** Abre um formulário para cadastrar um novo funcionário.
    *   **Editar:** Permite modificar os dados de um funcionário existente.
    *   **Excluir:** Remove um funcionário da lista.
5.  **Logout:** Permite que o usuário saia da aplicação.
6.  **Header e Footer:** A aplicação possui um cabeçalho com links e informações, e um rodapé fixo.

## Tecnologias Utilizadas

*   **Front-end:**
    *   **Vue.js:** Framework JavaScript progressivo para construir interfaces de usuário.
    *   **Vue Router:** Roteador oficial do Vue.js para navegação entre páginas.
    *   **Vue Composition API:**  API moderna para organização e reutilização de lógica em componentes Vue.
    *   **Axios:** Cliente HTTP baseado em Promises para fazer requisições ao backend.
    *   **HTML, CSS:** Linguagens de marcação e estilização para a estrutura e aparência da aplicação.

*   **Back-end (Assumido):**
    *   **Django REST Framework (DRF):** Framework Python robusto para criar APIs RESTful. (Essa é uma forte suposição baseada no tratamento de erros, mas pode ser qualquer backend que forneça uma API similar).
    *   **API RESTful:** O backend expõe uma API RESTful para que o frontend possa interagir com os dados (usuários e funcionários).


## Pré-requisitos

*   **Node.js e npm:** Você precisa ter o Node.js (versão 16 ou superior) e o npm (gerenciador de pacotes do Node.js) instalados em seu sistema.  Você pode baixá-los em [https://nodejs.org/](https://nodejs.org/).
*   **Um backend:** O projeto *requer* um backend funcional que forneça a API RESTful.  O código assume um backend Django REST Framework, mas você pode adaptar o frontend para qualquer backend compatível. *Você precisa ter o backend rodando para que o frontend funcione.*
*   **(Opcional) Um editor de código:**  Recomendamos o VS Code ([https://code.visualstudio.com/](https://code.visualstudio.com/)) com as extensões Vetur ou Volar para Vue.js.

## Configuração e Execução (Frontend)

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```

2.  **Instale as Dependências:**
    ```bash
    npm install
    ```

3.  **Configure a URL da API (Importante):**

    *   Se você tiver um arquivo `.env` na raiz do projeto, defina a variável `VUE_APP_API_BASE_URL` com a URL base do seu backend.  Por exemplo:
        ```
        VUE_APP_API_BASE_URL=http://localhost:8000
        ```
    *   Se você *não* usar um arquivo `.env`, pode configurar a URL diretamente no arquivo `src/api/index.js` (ou onde você configurou o Axios).
    *  Se você ainda não tiver esse arquivo, crie em /src/api/index.js:
      ```javascript
      // src/api/index.js
      import axios from 'axios';

      const api = axios.create({
        baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000', // Ou a URL direta
      });

      // Interceptor para adicionar o token de autenticação às requisições
      api.interceptors.request.use(
        (config) => {
          const token = localStorage.getItem('token');
          if (token) {
            config.headers['Authorization'] = `Token ${token}`;
          }
          return config;
        },
        (error) => {
          return Promise.reject(error);
        }
      );

      export default api;

      // Exemplo de funções para chamadas à API (adapte para suas necessidades)
      export const getUsers = () => api.get('/api/v1/users/');
      export const createUser = (data) => api.post('/api/v1/users/', data);
      export const loginUser = (data) => api.post('/api/v1/token/login', data); //ou a rota de autenticação
      export const getPessoas = () => api.get('/api/v1/pessoas/'); // Ajuste a rota.
      export const createPessoa = (data) => api.post('/api/v1/pessoas/', data);
      export const updatePessoa = (id, data) => api.put(`/api/v1/pessoas/${id}/`, data);  //PUT
      export const deletePessoa = (id) => api.delete(`/api/v1/pessoas/${id}/`);

      ```

    *  **MUITA ATENÇÃO:**  Substitua `/api/v1/pessoas/` pelas rotas *corretas* fornecidas pelo seu backend.

4. **Importe o arquivo `api` criado no passo 3:**
    Nos componentes que usam o Axios, você precisará usar o import criado. Exemplo de como importar no arquivo `PessoaForm.vue`:

    ```javascript
    //... restante do seu arquivo
    <script>
    import { ref, onMounted } from 'vue';
    import api from '../api'; // Importe api invés de axios

    export default {
      name: 'PessoaForm',
      props: {
        pessoa: {
    //... restante do seu arquivo.
      },
    };
    </script>
    ```
    Faça o mesmo para os outros componentes.

5.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    npm run serve
    ```
    Isso iniciará o servidor de desenvolvimento do Vue CLI.  A aplicação estará disponível em `http://localhost:8080` (ou outra porta, se a 8080 estiver ocupada). O console mostrará a URL correta.

6.  **Certifique-se de que seu BACKEND esteja rodando:** O frontend se comunicará com o backend, então ele *precisa* estar em execução.

## Deploy (Implantação)

Para implantar a aplicação em um ambiente de produção, você precisará:

1.  **Build:** Crie uma versão otimizada para produção:
    ```bash
    npm run build
    ```
    Isso gerará uma pasta `dist` com os arquivos estáticos que você precisa implantar.

2.  **Servidor Web:** Você precisará de um servidor web (como Nginx, Apache, Netlify, Vercel, etc.) para servir os arquivos estáticos da pasta `dist`. O processo exato depende do servidor que você escolher.

3.  **Configuração do Backend:** Certifique-se de que seu backend também esteja implantado e configurado corretamente.  Você precisará ajustar a URL da API no frontend (no arquivo `.env` ou diretamente no código) para apontar para o endereço do backend em produção.

## Considerações e Melhorias Futuras

*   **Validação de Formulários (Frontend e Backend):** Adicione validação mais robusta nos formulários de registro, login e criação/edição de funcionários.  Use bibliotecas como VeeValidate (para Vue) e implemente validação no backend também.
* **Paginação:** Caso haja possibilidade da tabela `PessoaList` conter muitas linhas, implemente uma paginação, dividindo a lista de pessoas em diversas páginas.
*   **Estilização:** A aplicação tem estilos básicos, mas pode ser aprimorada com um design mais profissional e responsivo.
*   **Testes:** Adicione testes unitários e de integração para garantir a qualidade e estabilidade do código.
*   **Internacionalização (i18n):** Se a aplicação precisar ser traduzida para outros idiomas, considere usar uma biblioteca de i18n como `vue-i18n`.
* **Mensagens de feedback:** Use uma biblioteca (ou crie um componente) para mensagens de Sucesso/Erro, algo do tipo um Toast.
