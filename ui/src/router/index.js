import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Signup from '../components/Signup.vue'
import Home from '../components/Home.vue'
import Userprofile from '../components/Userprofile.vue'
import Resetpassword from '../components/Resetpassword.vue'
import Forgotpassword from '../components/Forgotpassword.vue'
import ResetpasswordForgot from '../components/Resetpassword_forgot.vue'
import Interest from '../components/Interest.vue'
import Product from '../components/Product.vue'
import AddressBook from '../components/AddressBook.vue'
import AddressAdd from '../components/mod/AddressAdd.vue'
import Cart from '../components/Cart.vue'
import AdminPage from '../components/AdminPage'
import Addproduct from '../components/mod/Addproduct'
import Manageproduct from '../components/Manageproduct'
import OrderHistory from '../components/OrderHistory'
import Order from '../components/Order'
import Payment from '../components/Payment'
Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

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
    path: '/resetpassword/forgot',
    component: ResetpasswordForgot
  },
  {
    path: '/interest',
    component: Interest
  },
  {
    path: '/product',
    component: Product
  }, {
    path: '/address',
    component: AddressBook
  }, {
    path: '/addressadd',
    component: AddressAdd
  },{
    path: '/cart',
    component: Cart
  },{
    path: '/admin',
    component: AdminPage
  },{
    path: '/addproduct',
    component: Addproduct
  },{
    path: '/manageproduct',
    component: Manageproduct
  },{
    path: '/user/order',
    component: OrderHistory
  },{
    path: '/order',
    component: Order
  },{
    path: '/payment',
    component: Payment
  }
]

const router = new VueRouter({
  routes
})

export default router
