<template>
    <div class="reset_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="reset_box">
            <h1>RESET&nbsp;PASSWORD</h1>
        <el-form :model="resetForm" :rules="signupRules" label-position="left" label-width="225px" class="reset_form">
            <el-form-item label="OLD PASSWORD"  class="oldpassword_change" prop="oldpassword">
              <el-input v-model="resetForm.oldpassword">
              </el-input>
        </el-form-item>
            <el-form-item label="NEW PASSWORD" class="newpassword_change" prop="newpassword">
              <el-input v-model="resetForm.newpassword" type = "password" placeholder="6-12 characters contain uc,lc and number">
              </el-input>
        </el-form-item>
        </el-form>
        <el-button class='submit'>SUBMIT</el-button>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    var checkOldpassword = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('password cannot be empty'))
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
    return {
      resetForm: {
        oldpassword: '',
        newpassword: ''
      },
      signupRules: {
        oldpassword: [
          { min: 6, max: 12, message: 'the username should be 6-12 characters', trigger: 'blur' },
          { validator: checkOldpassword, trigger: 'blur' }
        ],
        newpassword: [
          { min: 6, max: 12, message: 'the password should be 6-12 characters', trigger: 'blur' },
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
        height: 35%;
        width: 20%;
        position: absolute;
        right: 55%;
        top:-7.5%;
}
.reset_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 30%;
    left: 15%;
}

.login_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
.oldpassword_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.newpassword_change /deep/ .el-form-item__label{
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
