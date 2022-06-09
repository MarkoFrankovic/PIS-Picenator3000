import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },

  {
    path: '/admin',
    name: 'admin',
    component: () => import(/* webpackChunkName: "admin" */ '../views/AdminView.vue')
  },

  {
    path: '/korisnik',
    name: 'korisnik',
    component: () => import(/* webpackChunkName: "korisnik" */ '../views/KorisnikView.vue')
  },

  {
    path: '/komentari',
    name: 'komentari',
    component: () => import(/* webpackChunkName: "komentari" */ '../views/KomentariView.vue')
  },

  {
    path: '/pjesmebambus',
    name: 'pjesmebambus',
    component: () => import(/* webpackChunkName: "pjesmebambus" */ '../views/PjesmeViewBambus.vue')
  },

  {
    path: '/pjesmejaeger',
    name: 'pjesmejaeger',
    component: () => import(/* webpackChunkName: "pjesmejaeger" */ '../views/PjesmeViewJaeger.vue')
  },

  {
    path: '/pjesmegin',
    name: 'pjesmegin',
    component: () => import(/* webpackChunkName: "pjesmegin" */ '../views/PjesmeViewGin.vue')
  },

  {
    path: '/pjesmejack',
    name: 'pjesmejack',
    component: () => import(/* webpackChunkName: "pjesmejack" */ '../views/PjesmeViewJack.vue')
  },

  {
    path: '/pjesmemerlot',
    name: 'pjesmemerlot',
    component: () => import(/* webpackChunkName: "pjesmemerlot" */ '../views/PjesmeViewMerlot.vue')
  },

  {
    path: '/pjesmestock',
    name: 'pjesmestock',
    component: () => import(/* webpackChunkName: "pjesmestock" */ '../views/PjesmeViewStock.vue')
  },

  {
    path: '/pjesmetravarica',
    name: 'pjesmetravarica',
    component: () => import(/* webpackChunkName: "pjesmetravarica" */ '../views/PjesmeViewTravarica.vue')
  },

  {
    path: '/pjesmevoda',
    name: 'pjesmevoda',
    component: () => import(/* webpackChunkName: "pjesmevoda" */ '../views/PjesmeViewVoda.vue')
  },

  {
    path: '/pjesmevodka',
    name: 'pjesmevodka',
    component: () => import(/* webpackChunkName: "pjesmevodka" */ '../views/PjesmeViewVodka.vue')
  },

  
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
