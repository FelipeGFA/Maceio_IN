import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Registrar from '../views/Registrar.vue'
import Dashboard from '../views/Dashboard.vue'

const routes = [

  {
    path: '/login',
    name: 'login',
    component: Login,
    alias: ['/', '']
  },
  {
    path: '/registrar',
    name: 'registrar',
    component: Registrar
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
