<template>
  <div class="my-cartpro">
    <p> Product Name: {{proName}} </p> 
    <p> Price: {{proPrice}}</p>
    <p> Quantity: {{qua}}</p>
    <el-button class="el-icon-remove-outline" circle></el-button>
    <el-button class="el-icon-circle-plus-outline" circle></el-button>

  </div>
</template>

<script>
export default {
    props: ['proName', 'proPrice', 'qua']
}
</script>

<style>
.my-cartpro {
  width: 400px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
}
</style>