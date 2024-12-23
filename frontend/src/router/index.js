import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddtoNumber from '@/views/AddtoNumber.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/tasklist',
      name: 'tasklist',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/TaskList.vue')
    },
    {
      path: '/newcomponant',
      name: 'newcomp',
      component: () => import('../views/NewCompotant.vue')
    },
    {
      path: '/newcomp',
      name: 'newc',
      component: () => import('../views/OneComp.vue')
    },
    {
      path: '/calculation',
      name: 'calcul',
      component: AddtoNumber
    },
  ]
})

export default router
