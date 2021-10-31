<template>
  <div>
      <p>=====Start of Order=====</p>
      <button @click="orderFn">Order id: {{ordId}}</button>
      <el-dialog :title="order_id" :visible.sync="dialogFormVisible">
        <div class="item" v-for="item in ordItem" :key="item.product_id">
        <p>Name: {{item.name}}
            ===Price: {{item.price}}
            ===Quantity: {{item.quantity}}
        </p>
        </div>
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">Close</el-button>
        </div>
      </el-dialog>
      <p>Paid: {{payStat}}</p>
      
      <p>Total: {{ordTotal}}</p>
      <p>=====End of Order=====</p>
  </div>
</template>

<script>
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal'],
    data () {
        return {
            dialogFormVisible: false,
            order_id: '###'
        }
    },
    created () {
        this.$emit('checker',this.index);
    },
    methods: {
        orderFn() {
            if (this.payStat === "Fail") {
                this.$message.error('Failed');
                this.$router.push('order/payment');
            } else {
                this.dialogFormVisible = true
            }
           
        }
    }
}
</script>

<style>

</style>