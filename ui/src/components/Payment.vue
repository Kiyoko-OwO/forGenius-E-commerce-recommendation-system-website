<template>
  <div class="manage_container">
    <header>
        PAYMENT
       <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
    </header>
    <div class="payment-container">
      <el-select v-model="value" clearable placeholder="Choose payment method">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button class="Pay" @click="submitForm()">Pay</el-button>
    </div>
  </div>
</template>

<script>
import { ord_pay } from '../api/order'
export default {
  data () {
    return {
      pay_from: {
        token: '',
        order_id: ''
      },
      options: [{
          value: 'paypal',
          label: 'Paypal'
        }, {
          value: 'debit',
          label: 'Debit Card'
        }, {
          value: 'credit',
          label: 'Credit Card'
        }, {
          value: 'gift',
          label: 'Gift Card'
        }],
        value: ''
      }
  },
  created () {
    this.loadOrder()
  },
  methods: {
    loadOrder() {
      this.pay_from.token = sessionStorage.getItem('token');
      this.pay_from.order_id = sessionStorage.getItem('order');
      sessionStorage.removeItem('order');
    },
    jumpHome () {
      this.$router.push('/home')
    },
    submitForm() {
      ord_pay(this.pay_from).then( res => {
        this.$message({message: 'Payment Done',type: 'success'});
        this.$router.push('/userprofile')
      }).catch( error => {
          this.$message.error('Failed');
      })
    }
  },
  
}
</script>


<style lang="less" scoped>
.payment-container {
    position: absolute;
    top:100px;
    left:50%;
    transform: translate(-50%,0%);
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

.Pay{
    height: 45px;
    width: 100px;
    position: absolute;
    border-radius: 4px;
    padding: 2px 20px;
    margin-left: -50px;
    margin-top: 40px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    border-color:#786662;
    cursor: pointer;
}

</style>