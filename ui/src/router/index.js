import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Home from '../components/Home.vue'
import Intrest from '../components/Intrest.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/signup',
    component: Signup
  },
  {
    path: '/home',
    component: Home
  },
  {
    path: '/intrest',
    component: Intrest
  }
]

const router = new VueRouter({
  routes
})

export default router
