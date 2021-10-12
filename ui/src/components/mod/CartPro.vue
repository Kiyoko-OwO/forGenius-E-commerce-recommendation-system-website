<template>
  <div class="my-cartpro">
    <p> Product Name: {{proName}} </p> 
    <p> Price: {{proPrice}}</p>
    <p> Quantity: {{qua}}</p>
    <!--
    <el-button class="el-icon-remove-outline" circle @click="subFn"></el-button>
    <el-button class="el-icon-circle-plus-outline" circle @click="addFn"></el-button>
    <el-button class="el-icon-delete" circle @click="delFn"></el-button> -->
  </div>
</template>

<script>
export default {
    props: ['index', 'proName', 'proPrice', 'qua'],
    methods: {
      addFn(){
        this.$emit("addQua", this.index)
      },
      subFn(){
        this.$emit("subQua", this.index)
      },
      delFn(){
        this.$emit("delPro", this.index)
      }
    }
}
</script>

<style>
.my-cartpro {
  width: 500px;
  height: 200 px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
}
</style>