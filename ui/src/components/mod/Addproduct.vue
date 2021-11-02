<template>
    <div class="add_container">
      <div class="add_box">
            <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpManage">
            <h1>ADD&nbsp;PRODUCT</h1>
      <el-form ref="add_FormRef" :rules="addRules" :model="addForm" class="add_form" label-position="left" label-width="225px">
          <el-form-item label="NAME" class="change" prop="name">
            <el-input v-model="addForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="DESCRIPTION" class="change_description" prop="description">
            <el-input type="textarea" v-model="addForm.description" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="WARRANTY" class="change" prop="warranty" >
            <el-input v-model="addForm.warranty" autocomplete="off" placeholder="The warranty time">
            </el-input>
          </el-form-item>
          <el-form-item label="DELIVERY DATE" class="change" prop="delivery_date">
            <el-input v-model="addForm.delivery_date" autocomplete="off" placeholder="The number of days it takes for delivery">
            </el-input>
          </el-form-item>
          <el-form-item label="PRICE" class="change" prop="price">
            <el-input v-model="addForm.price" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="PICTURE" class="change" prop="picture" >
            <el-input v-model="addForm.picture" autocomplete="off" placeholder="Please input the url of picture">
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
import { product_add } from '../../api/admin'
export default {
  data () {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkDes = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkWarranty = (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('warranty cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the warranty should be number'))
        }
      }, 100)
    }
    var checkDelivery= (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('number of day cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the data should be number of day'))
        }
      }, 100)
    }
    var checkSales= (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Sales cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the sales should be number'))
        }
      }, 100)
    }
    var checkPrice= (rule, value, callback) => {
      const mailReg =  /^(?:[1-9][0-9]*\.[0-9]+|0\.(?!0+$)[0-9]+)$/
      if (!value) {
        return callback(new Error('Price cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the price should be number'))
        }
      }, 100)
    }
    return {
      addForm: {
        name: '',
        description:'',
        warranty: '',
        delivery_date:'',
        price:'',
        picture: ''
      },
      addRules: {
        name: [
          { validator: checkName, trigger: 'blur' }
        ],
        warranty:[
          { validator: checkWarranty, trigger: 'blur'}
        ],
        delivery_date:[
          { validator: checkDelivery, trigger: 'blur'}
        ],
        sales:[
          { validator: checkSales, trigger: 'blur'}
        ],
        price:[
          { validator: checkPrice, trigger: 'blur'}
        ],
        description:[
          { validator: checkDes, trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    jumpManage () {
      this.$router.push('/manageproduct')
    },
    submitAdd () {
        this.$refs.add_FormRef.validate(async (valid) => {
        if (valid) {
        this.addForm.token = sessionStorage.getItem('token');
        console.log(this.addForm);
        product_add(this.addForm).then( res => {
            this.$message({message: 'Add product Sucess!',type: 'success'});
            this.$router.push('/manageproduct');
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
    height: 600px;
    width: 750px;
    position: absolute;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.logo{
    height: 70%;
    position: absolute;
    right: 64%;
    top:-53%;
    cursor: pointer;
}
.add_form{
    width: 500px;
    position: absolute;
    border-radius: 80px;
    top: 25%;
    left: 15%;
}
.change /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.change_description /deep/ .el-form-item__label{
    font-family: 'segUi';
    letter-spacing:.1em;
    font-size: 18px;
}
.change_description /deep/ .el-form-item__input{
      height: 100%;
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
    border-color: #786662;
    color: #fefefe;
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