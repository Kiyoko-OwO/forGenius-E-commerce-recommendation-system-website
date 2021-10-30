<template>
  <div>
      <p>=====Start of Order=====</p>
      <button @click="orderFn">Order id: {{ordId}}</button>
      <p>Paid: {{payStat}}</p>
      <div class="item" v-for="item in ordItem" :key="item.product_id">
        <p>Name: {{item.name}}
            ===Price: {{item.price}}
            ===Quantity: {{item.quantity}}
        </p>
      </div>
      <p>Total: {{ordTotal}}</p>
      <p>=====End of Order=====</p>
  </div>
</template>

<script>
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal'],
    created () {
        this.$emit('checker',this.index);
    },
    methods: {
        orderFn() {
            this.$emit("jump", this.index)
        }
    }
}
</script>

<style>

</style>