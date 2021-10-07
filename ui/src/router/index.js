import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Home from '../components/Home.vue'
import Userprofile from '../components/Userprofile.vue'
import Resetpassword from '../components/Resetpassword.vue'
import Forgotpassword from '../components/Forgotpassword.vue'
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
    path: '/userprofile',
    component: Userprofile
  },
  {
    path: '/resetpassword',
    component: Resetpassword
  },
  {
    path: '/forgotpassword',
    component: Forgotpassword
  }
]

const router = new VueRouter({
  routes
})

export default router
