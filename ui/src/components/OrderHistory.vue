<template>
  
  <div>
      <h1>Order History</h1>
      <Order v-for="(obj,ind) in order_list.slice().reverse()" :key="obj.order_id"
      :ordId="obj.order_id"
      :payStat="obj.paid"
      :ordItem="obj.item"
      :ordTotal="obj.total"
      :orderDate ="obj.order_date"
      :index = "ind"
      @checker = 'check'
      @jump = 'jumpToOrd'
      >

      </Order>
  </div>
</template>

<script>
import Order from './mod/OrdHisCom.vue'
import { ord_view } from '../api/order'
export default {
    data () {
        return {
            order_list : [],
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
                this.order_list = res.data.data.order_list;
            }).catch( error => {
                this.$message.error('No order exists');
            })
        },
        check(index) {

            if (this.order_list[index].paid == 1) {
                this.order_list[index].paid = "Success";
            } else {
                this.order_list[index].paid = "Fail";
            }
        },
        jumpToOrd(index) {
            this.$router.push('order/detail');
        }
    }
}
</script>

<style>

</style>