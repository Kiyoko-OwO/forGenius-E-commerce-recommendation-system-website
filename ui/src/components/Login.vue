<template>
    <div class="login_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="login_box">
            <h1>login</h1>
        <el-form model="loginForm" label-position="left" label-width="150px" class="login_form">
            <el-form-item label="email address"  class="username_change">
              <el-input v-model="loginForm.email">
              </el-input>
        </el-form-item>
            <el-form-item label="password">
              <el-input v-model="loginForm.password" type = "password" class="password_change">
              </el-input>
        </el-form-item>
        </el-form>
        <a href="" text-decoration:underline class="forget">FORGET MY PASSWORD</a>
        <el-button class='submit'>submit</el-button>
        <a href="" text-decoration:underline class="signup">SIGN UP</a>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        email: '',
        password: ''
      }
    }
  }
}
</script>

<style lang="less" scoped>

h1{
    position: absolute;
    left: 50%;
    font-family: 'segui';
    transform: translate(-50%,0%)
}

.forget{
    position: absolute;
    left: 63%;
    bottom:37%;
    color:black;
    font-family: 'segui';
    transform: translate(-50%,0%)
}

.signup{
    position: absolute;
    left: 80%;
    bottom:10%;
    color:black;
    font-family: 'segui';
    transform: translate(-50%,0%)
}

.submit{
    position: absolute;
    left:50%;
    bottom:13%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
}

.login_container {
    background-color: #d1dbda;
    height: 100%;

}

.login_box{
    background-color:#e7eae8;
    height: 375px;
    width: 650px;
    position: absolute;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);

}
.logo{
        height: 20%;
        width: 20%;
        position: absolute;
        right: 55%;
}
.login_form{
    margin: 100;
    width: 400px;
    position: absolute;
    border-radius: 80px;
    top: 30%;
    left: 20%;
}
.username{
      border-radius: 40px;
}
.email{
      border-radius: 30px;
}

.username_change /deep/ .el-form-item__label{
    font-family: "segui";
}
.password_change /deep/ .el-form-item__label{
    font-family: "segui";
}
</style>

<style>
input.el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>
