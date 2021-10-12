<template>
    <div class="fogot_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="fogot_box">
            <h1>FORGOT&nbsp;PASSWORD</h1>
        <el-form ref="forgotFormRef" :model="forgotForm" :rules="forgotRules" label-position="left" label-width="225px" class="forgot_form">
            <el-form-item label="EMAIL ADDRESS"  class="email_change" prop="email">
              <el-input v-model="forgotForm.email" placeholder="contains “@” and end with “.com”">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='send' @click="forgot">SEND CODE</el-button>
        </div>
    </div>
</template>

<script>
import { send_code } from '../api/user'

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
    return {
      forgotForm: {
        email: ''
      },
      forgotRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    forgot () {
      this.$refs.forgotFormRef.validate(valid => {
        console.log(valid)
        console.log(this.forgotForm);
        send_code(this.forgotForm).then ( res => {
          this.$message({message: 'Sucess!',type: 'success'});
          console.log(res);
          this.$router.push('/resetpassword/forgot');
        }).catch( error => {
          this.$message.error('Failed');
        })
      })
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

.send{
    position: absolute;
    left:50%;
    bottom:12%;
    height:50px;
    width:240px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.fogot_container {
    background-color: #d1dbda;
    height: 100%;
}
.fogot_box{
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
}
.forgot_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 37%;
    left: 15%;
}
.username{
      border-radius: 40px;
}
.email{
      border-radius: 30px;
}

.forgot_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
.email_change /deep/ .el-form-item__label{
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
