<template>
  <div >
    <div class="fix">
    <header>
      <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpUser">
       <div class="title">
        ORDER&nbsp;HISTORY
       </div>
    </header>
  <div class="order_container">
      <Order v-for="(obj,ind) in order_list.slice().reverse()" :key="obj.order_id"
      :ordId="obj.order_id"
      :payStat="obj.paid"
      :ordItem="obj.item"
      :ordTotal="obj.total"
      :orderDate ="obj.order_date"
      :name="obj.name"
      :address_line="obj.address_line"
      :phone_number="obj.phone_number"
      :index = "ind"
      @checker = 'check'
      @jump = 'jumpToOrd'
      >

      </Order>
  </div>
 </div>
</div>
</template>

<script>
import Order from '../mod/OrdHisCom.vue'
import { ord_view } from '../../api/order'
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
        },
        jumpUser () {
            this.$router.push('/userprofile');
        },
    }
}
</script>

<style lang="less" scoped>
header{
    height: 100px;
    width: 100%;
    position: relative;
    left:0;
    top:0;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
    overflow: hidden;
}
.order_container{
    position: relative;
    left:50%;
    transform: translate(-50%);
    width:300px;
}
.logo{
    height: 200%;
    position: relative;
    cursor: pointer;
    top:-60px;
    left:-600px;
    z-index:100;
}
.fix{
    margin:0 auto;
    width:1750px;
}
.title{
    position: relative;
    top:-260px;
    height:100px;
    width:200x;
    left:49%;
    transform: translate(-50%);
    text-align: center;
}
</style>