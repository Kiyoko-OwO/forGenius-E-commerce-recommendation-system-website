<template>
  <div class="manage_container">
    <header>
        MANAGE&nbsp;PRODUCT
       <el-button class="addProduct" v-on:click="jumpAddproduct">ADD PROCDUCT</el-button>
       <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpAdmin">
    </header>
    <div class="manage-container">
      <manage />
    </div>
  </div>
</template>

<script>
import manage from './mod/Manageproductpro.vue'
export default {
    components: {
        manage
    },
  methods: {
    jumpAddproduct () {
      this.$router.push('/addproduct')
    },
    jumpAdmin () {
      this.$router.push('/admin')
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
    right: 81%;
    top:-120.5%;
    cursor: pointer;
    z-index: 100;
}

.addProduct{
    height: 40%;
    position: absolute;
    border-radius: 4px;
    padding: 2px 20px;
    margin-left: 300px;
    margin-top: 40px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    border-color:#786662;
    cursor: pointer;
}

</style>