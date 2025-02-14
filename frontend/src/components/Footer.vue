<template>
    <footer class="app-footer">
      <p>&copy; {{ anoAtual }} - Felipe Ávila</p>
      <p>Todos os direitos reservados.</p>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'AppFooter',
    data() {
      return {
        anoAtual: new Date().getFullYear(),
      };
    },
  };
  </script>
  