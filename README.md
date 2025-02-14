Este projeto é uma aplicação web completa que combina um frontend em Vue.js com um backend em Django REST Framework para implementar um sistema CRUD (Create, Read, Update, Delete) para gerenciar informações de funcionários, incluindo autenticação de usuários.

## Visão Geral

A aplicação permite:

1.  **Registro de Usuários:** Novos usuários podem criar contas.
2.  **Login:** Usuários registrados podem fazer login.
3.  **Dashboard:**
    *   Exibe informações sobre a Secretaria de Fazenda (Sefaz) de Maceió.
    *   Lista, adiciona, edita e exclui funcionários.
4.  **Logout:** Sair da aplicação.

## Tecnologias

*   **Front-end:**
    *   Vue.js
    *   Vue Router
    *   Vue Composition API
    *   Axios
    *   HTML, CSS

*   **Back-end:**
    *   Django REST Framework (DRF)
    *   API RESTful
## Pré-requisitos

*   **Node.js e npm:** (Para o frontend)
*   **Python 3.7+:** (Para o backend)
*   **Ambiente Virtual Python (Recomendado):** Use `venv` ou `virtualenv`.
*   **Editor de Código:** VS Code (com extensões para Vue e Python) é recomendado.

## Configuração e Execução

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```

2.  **Configure o Backend (Django):**

    *   **Crie um ambiente virtual (recomendado):**
        ```bash
        python3 -m venv venv
        source venv/bin/activate  # Linux/macOS
        venv\Scripts\activate    # Windows
        ```

    *   **Instale as dependências do backend:**
        ```bash
        cd backend
        pip install -r requirements.txt
        ```

    *   **Execute as migrações:**
        ```bash
        python manage.py migrate
        ```

 3.  **Configure o Frontend (Vue):**

    
   **Navegue até a pasta do frontend:**
        
        cd ../frontend  # Ou a pasta correta do seu frontend
      

   **Instale as dependências do frontend:**
        
        npm install
        
4.  **Inicie o Servidor de Desenvolvimento do Vue:**
    ```bash
    npm run serve
    ```

    A aplicação Vue estará disponível em `http://localhost:8080` (ou outra porta).
