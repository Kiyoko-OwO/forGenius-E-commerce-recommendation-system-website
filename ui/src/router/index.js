import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Home from '../components/Home.vue'
import Userprofile from '../components/Userprofile.vue'
import Resetpassword from '../components/Resetpassword.vue'
import Forgotpassword from '../components/Forgotpassword.vue'
import ResetpasswordForgot from '../components/Resetpassword_forgot.vue'
import Intrest from '../components/Intrest.vue'
import Product from '../components/Product.vue'
import AddressBook from '../components/AddressBook.vue'
import AddressAdd from '../components/mod/AddressAdd.vue'
import AddressEdit from '../components/mod/AddressEdit.vue'
import Cart from '../components/Cart.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/', redirect: 'home'
  },
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
  },
  {
    path: '/resetpassword_forgot',
    component: ResetpasswordForgot
  },
  {
    path: '/intrest',
    component: Intrest
  },
  {
    path: '/product',
    component: Product
  }, {
    path: '/address',
    component: AddressBook
  }, {
    path: '/address/add',
    component: AddressAdd
  },{
    path: '/address/edit',
    component: AddressEdit
  },{
    path: '/cart',
    component: Cart
  }
]

const router = new VueRouter({
  routes
})

export default router
