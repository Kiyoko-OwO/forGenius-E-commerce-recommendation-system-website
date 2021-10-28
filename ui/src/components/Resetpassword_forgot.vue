<template>
    <div class="reset_container">
        <div class="reset_box">
            <img class="logo" src=../assets/2.png alt="logo">
            <h1>RESET&nbsp;PASSWORD</h1>
        <el-form ref="resetFormRef" :model="resetForm" :rules="resetpasswordRules" label-position="left" label-width="225px" class="reset_form">
            <el-form-item label="CODE"  class="code_change" prop="reset_code">
              <el-input v-model="resetForm.reset_code">
              </el-input>
        </el-form-item>
            <el-form-item label="NEW PASSWORD" class="newpassword_change" prop="new_password">
              <el-input v-model="resetForm.new_password" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
            <el-form-item label="CONFIRM PASSWORD" class="password_change" prop="confirm_password">
              <el-input v-model="resetForm.confirm_password" type = "password" placeholder="input password again">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='submit' @click="reset">SUBMIT</el-button>
        </div>
    </div>
</template>

<script>
import { reset_password } from '../api/user'

export default {
  data () {
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Code cannot be empty'))
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
        if (!value) {
          callback(new Error('password cannot be empty'));
        } else if (value !== this.resetForm.new_password) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
    }
    return {
      resetForm: {
        reset_code: '',
        new_password: ''
      },
      resetpasswordRules: {
        reset_code: [
          { validator: checkCode, trigger: 'blur' }
        ],
        new_password: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
          { validator: checkPassword, trigger: 'blur' }
        ],
        confirm_password: [
          { validator: confirmPassword, trigger: 'blur'}
       ]
      }
    }
  },
  methods: {
    reset () {
      this.$refs.resetFormRef.validate(valid => {
        console.log(valid);
        console.log(this.resetForm);
        reset_password(this.resetForm).then ( res => {
          this.$message({message: 'Sucess!',type: 'success'});
          console.log(res.data);
          this.$router.push('/login');
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
    left: 52%;
    font-size: 40px;
    transform: translate(-50%,20%);
    font-weight:normal;
    font-family: 'segUi';
    letter-spacing:.2em;
}

.submit{
    position: absolute;
    left:50%;
    bottom:4%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
.reset_container {
    background-color: #d1dbda;
    height: 100%;
}
.reset_box{
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
.reset_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 30%;
    left: 15%;
}

.reset_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
.code_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.newpassword_change /deep/ .el-form-item__label{
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
