<template>
  <div class="my-cartpro">
    <div class="img" v-for="fit in fits" :key="fit">
     <span class="demonstration">{{ fit }}</span>
        <el-image
          style="width: 100px; height: 100px"
          :src="123"
          :fit="fit"></el-image>
    </div>
    <p> Product Name: {{proName}} </p> 
    <p> Price: {{proPrice}}</p>
    <p> Quantity: {{qua}}</p>
    <el-button class="el-icon-minus" circle @click="subFn"></el-button>
    <el-button class="el-icon-plus" circle @click="addFn"></el-button>
    <el-button class="el-icon-close" circle @click="delFn"></el-button>
  </div>
</template>

<script>
export default {
    data() {
      return{
          fits: [''],
      }
    },
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


<style lang="less" scoped>
.my-cartpro {
  width: 450px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
  word-break:break-all;
}
.img{
  float: right;
}
</style>