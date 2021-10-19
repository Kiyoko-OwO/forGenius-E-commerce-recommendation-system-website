<template>
  <div class="manage_container">
    <header>
        MANAGE&nbsp;PRODUCT
       <el-button class="addProduct" v-on:click="jumpAddproduct">ADD PROCDUCT</el-button>
       <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
    </header>
    <div class="manage-container">
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    jumpAddproduct () {
      this.$router.push('/addproduct')
    }
  }
}
</script>


<style lang="less" scoped>
.manage-container {
    position: absolute;
    top:100px;
    left:50%;
    transform: translate(-50%,0%);
}

.manage_container{
    background-color: #d1dbda;
    height: 100%;
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
    right: 80%;
    top:-120.5%;
    cursor: pointer;
    z-index: 100;
}

.addProduct{
    position: absolute;
    border-radius: 4px;
    padding: 2px 20px;
    margin-left: 10px;
    margin-top: 35px;
    border-color: grey;
    color: grey;
    cursor: pointer;
}

</style>