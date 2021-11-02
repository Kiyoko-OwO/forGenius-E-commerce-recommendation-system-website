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
import { cart_view } from '../api/order'
import { cart_qua } from '../api/order'
import { cart_del } from '../api/order'


export default {
    data () {
        return {
            cart : [],
            tokenForm: {
                token: ''
            },
            total_price: '',
            qua_form: {
                token: '',
                product_id: '',
                quantity: ''
            },
            del_form: {
                token: '',
                product_id: ''
            },
            
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
            cart_view(this.tokenForm).then( res => {
                this.cart = res.data.data.cart;
                this.total_price = res.data.data.total;
                this.qua_form.token = sessionStorage.getItem('token');
                this.del_form.token = sessionStorage.getItem('token');
            }).catch( error => {
                this.$message.error('Failed1');
            })
        },
        submitForm() {
            console.log(this.cart);
            console.log(this.create_form);
            if (this.cart.length > 0) {
                this.$router.push('order');
            } else {
                this.$message.error('The cart is empty');
            }
        },
        add(index) {
            this.cart[index].quantity += 1;
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.total_price = this.total_price + this.cart[index].price;
            this.total_price = this.total_price.toFixed(2);
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id
            cart_qua(this.qua_form).then( res => {

            }).catch( error => {
                this.$message.error('Failed2');
            })
        },
        sub(index) {
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.cart[index].quantity > 1 && (this.cart[index].quantity -= 1) && (this.total_price = this.total_price - this.cart[index].price);
            this.total_price = this.total_price.toFixed(2);
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id;
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed3');
            })
        },
        del(index) {
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.del_form.product_id = this.cart[index].product_id;
            cart_del(this.del_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed');
            })
            this.total_price = this.total_price - (this.cart[index].quantity * this.cart[index].price)
            this.total_price = this.total_price.toFixed(2);
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