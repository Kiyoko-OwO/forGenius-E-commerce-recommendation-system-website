<template>
  <div class="cart-container">
      <Product v-for="obj in cart" :key="obj.id"
      :proName="obj.name"
      :proPrice="obj.price"
      :qua="obj.quantity">
      </Product>
      <el-button type="primary" @click="submitForm()">Check Out</el-button>
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
        }
    }
}
</script>

<style>
.cart-container {
    border: 1px solid black;
}
</style>