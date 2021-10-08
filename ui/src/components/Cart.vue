<template>
  <div class="cart-container">
      <Product v-for="obj in cart" :key="obj.id"
      :proName="obj.name"
      :proPrice="obj.price"
      :qua="obj.quantity">
      </Product>
      <button>Check Out</button>
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
    }
}
</script>

<style>
.cart-container {
    border: 1px solid black;
}
</style>