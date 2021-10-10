<template>
  <div class="cart_container">
    <header>
        MY&nbsp;CART
    </header>
    <img class="logo" src=../assets/2.png alt="logo">
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
        <el-button type="primary" class="checkout" @click="submitForm()">Check Out</el-button>
    </div>
  </div>
</template>

<script>
import Product from './mod/CartPro.vue'
import imgObj from '../assets/2.png'
export default {
    data () {
        return {
            cart : [
                {
                    id: "10",
                    imgPath: imgObj,
                    name: "Sample name",
                    price: "123",
                    quantity: 2
                },
                {
                    id: "12",
                    imgPath: imgObj,
                    name: "Sample name2",
                    price: "30",
                    quantity: 1
                }
            ]
        }
    },
    components: {
        Product
    },
    methods: {
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
        }
    }
}
</script>


<style lang="less" scoped>
.cart-container {
    position: absolute;
    top:100px;
    border: 1px solid black;
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
}
.logo{
    height: 35%;    
    position: absolute;
    right: 80%;
    top:-13.5%;
    cursor: pointer;
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