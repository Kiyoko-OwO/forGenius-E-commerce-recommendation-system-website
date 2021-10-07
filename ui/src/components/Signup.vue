<template>
    <div class="login_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="login_box">
            <h1>REGISTER</h1>
        <el-form :model="loginForm" :rules="signupRules" label-position="left" label-width="225px" class="login_form">
            <el-form-item label="USERNAME"  class="username_change" prop="username">
              <el-input v-model="loginForm.username" placeholder="6-12 characters">
              </el-input>
        </el-form-item>
            <el-form-item label="EMAIL ADDRESS"  class="username_change" prop="email">
              <el-input v-model="loginForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
            <el-form-item label="PASSWORD" class="password_change" prop="password">
              <el-input v-model="loginForm.password" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='submit'>SUBMIT</el-button>
        <a href="#/login" text-decoration:underline class="login">LOG IN</a>
        <a text-decoration:underline class="login_1">ALREADY REGISTERED, PLEASE</a>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    var checkEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
      if (!value) {
        return callback(new Error('email address cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Please enter the correct email format'))
        }
      }, 100)
    }
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'))
      }
    }
    var checkPassword = (rule, value, callback) => {
      const mailReg = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])/
      if (!value) {
        return callback(new Error('password cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Invalid email'))
        }
      }, 100)
    }
    return {
      loginForm: {
        username: '',
        email: '',
        password: ''
      },
      signupRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        username: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkUsername, trigger: 'blur' }
        ],
        password: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkPassword, trigger: 'blur' }
        ]
      }
    }
  }
}
</script>

<style lang="less" scoped>

h1{
    position: absolute;
    left: 50%;
    font-size: 40px;
    transform: translate(-50%,20%);
    font-weight:normal;
    font-family: 'segUi';
    letter-spacing:.2em;
}
.forget{
    position: absolute;
    left: 66%;
    bottom:37%;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
}
.login{
    position: absolute;
    left: 73%;
    bottom:10%;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
}
.login_1{
    position: absolute;
    left: 47%;
    bottom:10%;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
}
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
.login_container {
    background-color: #d1dbda;
    height: 100%;
}
.login_box{
    background-color:#e7eae8;
    height: 425px;
    width: 750px;
    position: absolute;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.logo{
        height: 35%;
        width: 20%;
        position: absolute;
        right: 55%;
        top:-7.5%;
}
.login_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 30%;
    left: 15%;
}
.username{
      border-radius: 40px;
}
.email{
      border-radius: 30px;
}

.login_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
.username_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.password_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-form-item{
   margin-bottom:15px
}
</style>

<style>
input.el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>
