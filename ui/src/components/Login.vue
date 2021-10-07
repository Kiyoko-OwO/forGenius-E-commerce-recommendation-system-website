<template>
    <div class="login_container">
        <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
        <div class="login_box">
            <h1>LOGIN</h1>
        <el-form :model="loginForm" :rules="loginRules" label-position="left" label-width="225px" class="login_form">
            <el-form-item label="EMAIL ADDRESS"  class="username_change" prop="email">
              <el-input v-model="loginForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
            <el-form-item label="PASSWORD" class="password_change" prop="password">
              <el-input v-model="loginForm.password" type = "password">
              </el-input>
        </el-form-item>
        </el-form>
        <a href="" text-decoration:underline class="forget">FORGET MY PASSWORD</a>
        <el-button class='submit'>SUBMIT</el-button>
        <a href="#/signup" text-decoration:underline class="signup">SIGN UP</a>
        <a text-decoration:underline class="signup_1">DON'T HAVE AN ACCOUNT YET? PLEASE</a>
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
    var checkPassword = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('password cannot be empty'))
      }
    }
    return {
      loginForm: {
        email: '',
        password: ''
      },
      loginRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        password: [
          { validator: checkPassword, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    jumpHome () {
      this.$router.push('Home')
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
.signup{
    position: absolute;
    left: 77.5%;
    bottom:10%;
    color:black;
    transform: translate(-50%,0%);
    font-size: 15px;
    letter-spacing:.2em;
}
.signup_1{
    position: absolute;
    left: 45%;
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
    position: absolute;
    right: 55%;
    top:-7.5%;
    cursor: pointer;
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
</style>

<style>
input.el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>
