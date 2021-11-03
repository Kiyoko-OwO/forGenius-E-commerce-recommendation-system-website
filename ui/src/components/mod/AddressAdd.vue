<template>
    <div class="add_container">
      <div class="add_box">
            <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpAddress">
            <h1>ADD&nbsp;ADDRESS</h1>
      <el-form ref="add_FormRef" :rules="addRules" :model="addForm" class="add_form" label-position="left" label-width="225px">
          <el-form-item label="NAME" class="username_change" prop="name">
            <el-input v-model="addForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="ADDRESS" class="username_change" prop="address_line">
            <el-input v-model="addForm.address_line" autocomplete="off">
            </el-input>
          </el-form-item>
           <el-form-item label="COUNTRY" class="username_change" prop="country">
            <el-input v-model="addForm.country" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="STATE" class="username_change" prop="state">
            <el-input v-model="addForm.state" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="SUBURB" class="username_change" prop="suburb">
            <el-input v-model="addForm.suburb" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="POSTAL CODE" class="username_change" prop="post_code">
            <el-input v-model="addForm.post_code" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="PHONE NUMBER" class="username_change" prop="phone_number">
            <el-input v-model="addForm.phone_number" autocomplete="off">
            </el-input>
          </el-form-item>
          <div class="block"></div>
          <el-form-item>
          <el-button type="primary" @click="submitAdd" class="submit">CONFIRM</el-button>
          </el-form-item>
      </el-form>
      </div>
    </div>
</template>

<script>
import { address_add } from '../../api/user'
export default {
  data () {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'))
      } else {
        callback()
      }
    }
    var checkAddress = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('address cannot be empty'))
      } else {
        callback()
      }
    }
    var checkPhone = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('phonenumber cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Phonenumber should be number'))
        }
      }, 100)
    }
    var checkState = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('State cannot be empty'))
      } else {
        callback()
      }
    }
    var checkSuburb = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Suburb cannot be empty'))
      } else {
        callback()
      }
    }
    var checkCountry = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Country cannot be empty'))
      } else {
        callback()
      }
    }
    var checkCode = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Postal code cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Postal code should be number'))
        }
      }, 100)
    }
    return {
      addForm: {
        token: '',
        name: '',
        address_line: '',
        phone_number: '',
        country:'',
        state:'',
        suburb:'',
        post_code:''
      },
      addRules: {
        name: [
          { validator: checkName, trigger: 'blur' }
        ],
        address_line: [
          { validator: checkAddress, trigger: 'blur' }
        ],
        phone_number: [
          { validator: checkPhone, trigger: 'blur'  }
        ],
        post_code: [
          { validator: checkCode, trigger: 'blur'  }
        ],
                suburb: [
          { validator: checkSuburb, trigger: 'blur'  }
        ],
                state: [
          { validator: checkState, trigger: 'blur'  }
        ],
                country: [
          { validator: checkCountry, trigger: 'blur'  }
        ]
      }
    }
  },
  methods: {
    jumpAddress () {
      this.$router.push('/address')
    },
    submitAdd () {
        this.$refs.add_FormRef.validate(async (valid) => {
          if (valid) {
        this.addForm.token = sessionStorage.getItem('token');
        console.log(this.addForm);
        address_add(this.addForm).then( res => {
            this.$message({message: 'Add Address Sucess!',type: 'success'});
            if (sessionStorage.getItem('from') == 1) {
              sessionStorage.removeItem('from');
              this.$router.push('order');
            } else {
               this.$router.push('address');
            }
           
        }).catch( error => {
            this.$message.error('Failed');
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

.block{
    height: 60px;
}

h1{
    position: absolute;
    top:2%;
    left: 50%;
    font-size: 40px;
    transform: translate(-50%,20%);
    font-weight:normal;
    font-family: 'segUi';
    letter-spacing:.2em;
}
.add_container {
    background-color: #d1dbda;
    height: 100%;
}
.add_box{
    background-color:#e7eae8;
    height: 620px;
    width: 750px;
    position: absolute;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.logo{
    height: 50%;
    width: 40;
    position: relative;
    top:-35%;

    cursor: pointer;
}
.add_form{
    width: 530px;
    position: absolute;
    border-radius: 80px;
    top: 20%;
    left: 15%;
}

.username_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.el-form-item{
   margin-bottom:15px
}
.submit{
    position: relative;
    left:17%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    border-color: #786662;
    letter-spacing:10px;
    padding-left: 30px;
}
.add_form /deep/.timr.el-form .el-form-item__error {
  top: 30%;
  right: 25% !important;
  left: unset;
}
</style>

<style lang="less" scoped>
input.el-input__inner {
    border-radius:50px;
    height:30px;
}
</style>