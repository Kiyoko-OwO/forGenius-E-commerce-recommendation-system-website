<template>
    <div class="login_container">
        <div class="login_box">
          <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
            <h1>LOGIN</h1>
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-position="left" label-width="225px" class="login_form">
            <el-form-item label="EMAIL ADDRESS"  class="email_change" prop="email">
              <el-input v-model="loginForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
            </el-form-item>
            <el-form-item label="PASSWORD" class="password_change" prop="password">
              <el-input v-model="loginForm.password" type = "password">
              </el-input>
            </el-form-item>
            <div class="block"></div>
            <el-form-item>
              <el-button type="primary" class='submit' @click="submitForm('loginForm')">SUBMIT</el-button>
            </el-form-item>
        </el-form>
        <a  text-decoration:underline href="#/forgotpassword" class="forget">FORGET MY PASSWORD</a>
        <a href="#/signup" text-decoration:underline class="signup">SIGN UP</a>
        <a text-decoration:underline class="signup_1">DON'T HAVE AN ACCOUNT YET? PLEASE</a>
        </div>
    </div>
</template>

<script>
import { login } from '../api/user'

export default {
  data () {
    var checkEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+.com/
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
    var checkpassword = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('password cannot be empty'))
      } else {
         callback()
      }
    }
    return {
      dialogVisible: false,
      loginForm: {
        email: '',
        password: ''
      },
      loginRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        password: [
          { validator: checkpassword, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    jumpHome () {
      this.$router.push('Home')
    },
    submitForm(formName) {
        this.$refs[formName].validate(async (valid) => {
          if (valid) {
            login(this.loginForm).then( res => {
              this.$message({message: 'Log in Sucess!',type: 'success'});
              console.log(res.data);
              console.log(res.status);
              if (res.status == 255) {
                sessionStorage.clear();
                sessionStorage.setItem('token',res.data.token);
                sessionStorage.setItem('username',res.data.username);
                this.$router.push('/admin');
              } else {
                sessionStorage.clear();
                sessionStorage.setItem('token',res.data.token);
                sessionStorage.setItem('username',res.data.username);
                this.$router.push('/userprofile');
              }
            }).catch( error => {
              this.$message.error('Incorrect email or password');
            })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
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
.block {
  width: 1000px;
  height: 65px;
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
    left:7%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
    border-color: #786662;
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
    height: 90%;
    position: absolute;
    right: 64%;
    top:-83%;
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
.email_change /deep/ .el-form-item__label{
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
