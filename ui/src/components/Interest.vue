<template>
  <div class="interest_container">
    <header>
        PLEASE CHOOSE YOUR INTEREST FIELD
    </header>
    <img class="logo" src=../assets/2.png alt="logo">
    <div>
      <el-checkbox-group v-model="interestForm.interest" class="checkbox">
        <el-checkbox-button v-for="int in tags" :label="int" :key="int">{{int}}</el-checkbox-button>
      </el-checkbox-group>
      <el-button class='submit' @click="submitForm()">SUBMIT</el-button>
      <li v-for="item in interestForm.interest" :key="item" class="choose">
          <span>{{ item }}</span>
      </li>
      </div>
  </div>


</template>
<script>
import { interest_add } from '../api/user'
const tagOptions = ['Fastion', 'Toys', 'Hobby', 'DIY', 'Electronics', 'Media', 'Furniture', 'Appliance', 'Food', 'Personal Care']
export default {
  data () {
    return {
      tags: tagOptions,
      intest: [],
      interestForm: {
        token : '',
        interest: []
      }
    }
  },
  methods: {
    submitForm() {
      this.interestForm.token = sessionStorage.getItem('token');
      interest_add(this.interestForm).then ( res => {
          this.$message({message: 'Sucess!',type: 'success'});
          this.$router.push('Home');
      }).catch( error => {
          this.$message.error('Failed');
      })
    }
  }
}
</script>

<style lang="less" scoped>
.submit{
    position: absolute;
    left:50%;
    bottom:12%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.interest_container{
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
}
.logo{
    height: 35%;    
    position: absolute;
    right: 80%;
    top:-13.5%;
    cursor: pointer;
}
.checkbox{
  position: relative;
  top:100px;
}
.choose{
  position: relative;
  top:160px;
  background-color:#e7eae8;
}
</style>
