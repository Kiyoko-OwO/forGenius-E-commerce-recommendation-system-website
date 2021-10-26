<template>
  <div class="cart_container">
    <header>
        MY&nbsp;CART
    <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
    </header>
    <div class="cart-container">
        <Product v-for="(obj,ind) in cart" :key="obj.id"
        :proName="obj.name"
        :proPrice="obj.price"
        :qua="obj.quantity"
        :index = "ind"
        @addQua = 'add'
        @subQua = 'sub'
        @delPro = 'del'>
        </Product>
        <p>Total Price: $</p>
        <p>{{total_price}}</p>
        <el-button type="primary" class="checkout" @click="submitForm()">Check Out</el-button>
    </div>
  </div>
</template>

<script>
import Product from './mod/CartPro.vue'
import imgObj from '../assets/2.png'
import { car_view } from '../api/order'

export default {
    data () {
        return {
            cart : [],
            tokenForm: {
                token: ''
            },
            total_price: ''
        }
    },
    created () {
        this.loadCart()
    },
    components: {
        Product
    },
    methods: {
        async loadCart() {
            this.tokenForm.token = sessionStorage.getItem('token');
            car_view(this.tokenForm).then( res => {
                console.log(res.data.data);
                this.cart = res.data.data.cart;
                this.total_price = res.data.data.total;
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        submitForm() {
            console.log(this.cart);
        },
        add(index) {
            this.cart[index].quantity += 1;
        },
        sub(index) {
            this.cart[index].quantity > 1 && (this.cart[index].quantity -= 1);
        },
        del(index) {
            this.cart.splice(index, 1);
            console.log(this.cart);
        },
        jumpHome () {
            this.$router.push('Home');
        }

    }
}
</script>


<style lang="less" scoped>
.cart-container {
    position: absolute;
    top:100px;
    left:50%;
    transform: translate(-50%,0%);
}

.cart_container{
    background-color: #d1dbda;
    height: 100%;
}
header{
    height: 100px;
    width: 100%;
    position: fixed;
    left:0;
    top:0;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
    z-index: 50;
}
.logo{
    height: 300%;    
    position: absolute;
    right: 81%;
    top:-120.5%;
    cursor: pointer;
    z-index: 100;
}

.checkout{
    position: relative;
    left:75%;
    width: 130px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    letter-spacing:2px;
    padding-left: 25px;
    border-color: #786662;
}
</style>