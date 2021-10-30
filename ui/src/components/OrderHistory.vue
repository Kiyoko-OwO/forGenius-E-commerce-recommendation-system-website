<template>
  <h1>Order History</h1>
</template>

<script>
import Order from './mod/OrdHisCom.vue'
import { ord_view } from '../api/order'
export default {
    data () {
        return {
            cart : [],
            tokenForm: {
                token: ''
            },
            total_price: ''
        }
    },created () {
        this.loadOrd()
    },
    components: {
        Order
    },
    methods: {
        async loadOrd() {
            this.tokenForm.token = sessionStorage.getItem('token');
            ord_view(this.tokenForm).then( res => {
                console.log(res.data.data);
            }).catch( error => {
                this.$message.error('Failed');
            })
        }
    }
}
</script>

<style>

</style>