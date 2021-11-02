<template>
  <div class="order_item">
      <div class="block"></div>
      Order id: {{ordId}}
      <el-dialog :title="order_id" :visible.sync="dialogFormVisible" class="order_id">
        <div class="item" v-for="item in ordItem" :key="item.product_id">
        <p>Name: {{item.name}} </p>
        <p>Price: {{item.price}} </p>
         <p>Quantity: {{item.quantity}} </p>
        <div class="link-in"></div>
        </div>
        <div class="block"></div>
        Order Date: {{orderDate}}
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Price: {{ordTotal}}
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">Close</el-button>
        </div>
      </el-dialog>
      <p>Paid: {{payStat}}</p>
      <p>Order Date: {{orderDate}}</p>
      <el-button @click="orderFn" class="detail">Detail</el-button>
      <el-button @click="orderShare" class="detail">Share</el-button>
      <div class="block"></div>
      <div class="link-top"></div>
  </div>
</template>

<script>
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal','orderDate'],
    data () {
        return {
            dialogFormVisible: false,
            order_id: '###'
        }
    },
    created () {
        this.$emit('checker',this.index);
        this.order_id =  "Order Number: " + this.ordId.toString();
    },
    methods: {
        orderFn() {
            if (this.payStat === "Fail") {
                this.$router.push('/payment');
                sessionStorage.setItem('order', this.ordId);
            } else {
                this.dialogFormVisible = true
            }
           
        }
    }
}
</script>

<style lang="less" scoped>
    .link-top {
        position: relative;
        width: 400%;
        height: 1px;
        left:-130%;
        border-top: solid #0b0b0f 1px;
     }
    .link-in {
        position: relative;
        width: 100%;
        height: 1px;
        border-top: solid #0b0b0f 1px;
     }
     .block {
  height: 20px;
}
.detail{
    position: relative;
    left:100%;

}
</style>

<style>
.order_id{
    position: absolute;
    width: 1700px;
    left:400px;
}
</style>