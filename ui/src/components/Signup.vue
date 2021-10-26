<template>
    <div class="signup_container">
        <div class="signup_box">
            <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
            <h1>REGISTER</h1>
        <el-form ref="signupFormRef" :model="signupForm" :rules="signupRules" label-position="left" label-width="225px" class="signup_form">
            <el-form-item label="USERNAME"  class="username_change" prop="name">
              <el-input v-model="signupForm.name" placeholder="6-12 characters">
              </el-input>
        </el-form-item>
            <el-form-item label="EMAIL ADDRESS"  class="email_change" prop="email">
              <el-input v-model="signupForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
            <el-form-item label="PASSWORD" class="password_change" prop="password">
              <el-input v-model="signupForm.password" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
            <el-form-item label="CONFIRM PASSWORD" class="password_change" prop="confirm_password">
              <el-input v-model="signupForm.confirm_password" type = "password" placeholder="input password again">
              </el-input>
        </el-form-item>
            <el-form-item label="EMAIL CODE" class="code_change" prop="code">
              <el-input v-model="signupForm.code" >
              </el-input>
        </el-form-item>
        <div class="block"></div>
        <el-form-item>
        <el-button class='send' @click="send">SEND</el-button>
        <el-button class='submit' @click="signup">SUBMIT</el-button>
        </el-form-item>
        </el-form>
        <a href="#/login" text-decoration:underline class="login">LOG IN</a>
        <a text-decoration:underline class="login_1">ALREADY REGISTERED, PLEASE</a>
        </div>
    </div>
</template>

<script>
import { signup } from '../api/user'

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
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'));
      } else {
        callback()
      }
    }
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('code cannot be empty'));
      } else {
        callback()
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
          callback(new Error('Invalid password'))
        }
      }, 100)
    }
    var confirmPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('password cannot be empty'));
        } else if (value !== this.signupForm.password) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
    }
    return {
      signupForm: {
        email: "",
	      name : "",
	      password: "",
        code: ""
      },
      signupRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        name: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkUsername, trigger: 'blur' }
        ],
        password: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
          { validator: checkPassword, trigger: 'blur' }
        ],
        confirm_password: [
          { validator: confirmPassword, trigger: 'blur'}
       ],
        code: [
          { validator: checkCode, trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    signup () {
      this.$refs.signupFormRef.validate(async valid => {
        if (valid) {
          // signup(this.signupForm).then ( res => {

          // }).catch( error => {

          // })
          signup(this.signupForm).then ( res => {
            this.$message({message: 'Sign up Sucess!',type: 'success'});
            sessionStorage.clear();
            console.log(res.data);
            sessionStorage.setItem('token',res.data.token);
            sessionStorage.setItem('username',res.data.username);
            this.$router.push('/interest');
          }).catch( error => {
            this.$message.error('Already registered, please log in');
          })
          // console.log(this.signupForm);
          // const res = await signup(this.signupForm);
          // console.log(res);
          // if (res.status == 200) {
          //   alert ("Sucess");
          //   console.log(res.data.token);
          //   sessionStorage.clear();
          //   sessionStorage.setItem('token',res.data.token);
          //   this.$router.push('userprofile');
          // }
        } else {
          console.log('error submit!!');
          return false;
        }
      })
    },
    jumpHome () {
      this.$router.push('Home');
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

.block{
    height: 80px;
}

.login{
    position: absolute;
    left: 73%;
    bottom:10%;
    color:rgb(0, 0, 0);
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
    left:15%;
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
.send{
    position: absolute;
    left:80%;
    height:30px;
    top:-115px;
    width:100px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    border-radius: 20px;
    letter-spacing:7px;
    padding-left: 22px;
    padding-top:8px;
    font-size:13px;
}
.signup_container {
    background-color: #d1dbda;
    height: 100%;
}
.signup_box{
    background-color:#e7eae8;
    height: 550px;
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
    top:-66%;
    cursor: pointer;
}
.signup_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 20%;
    left: 15%;
}
.username{
      border-radius: 40px;
}
.email{
      border-radius: 30px;
}

.signup_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
.email_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
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
.code_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.code_change{
  width: 400px
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
