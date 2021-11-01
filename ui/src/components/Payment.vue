<template>
  <div class="manage_container">
    <header>
        PAYMENT
       <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
    </header>
    <div class="payment-container">
    <el-button class="Pay">Pay</el-button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    jumpHome () {
      this.$router.push('/home')
    }
  }
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