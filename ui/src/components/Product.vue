<template>
  <div class="address_container">
    <header>
        PRODUCT&nbsp;DETAIL
    </header>
    <img class="logo" src=../assets/2.png alt="logo">
    <div class="product_box">
        <img class="picture" v-bind:src="product.imgPath" alt="product image" />
        <h2>{{product.name}}</h2>
        <h3>Price: {{product.price}}</h3>
        <el-form :model="numberValidateForm" ref="numberValidateForm" label-width="100px" class="demo-ruleForm">
          <el-form-item
            label="Quantity"
            prop="quantity"
            :rules="[
            { required: true, message: 'Quantity cannot be null'},
            { type: 'number', message: 'Quantity need to be number'}
            ]"
          >
          <el-button class="el-icon-remove-outline" @click='deleteOne' circle></el-button>
          <el-input class="quaBox" type="quantity" v-model.number="numberValidateForm.quantity" autocomplete="off"></el-input>
          <el-button class="el-icon-circle-plus-outline" @click='addOne' circle></el-button>
          </el-form-item>
          <el-form-item class="save">
            <el-button type="primary" @click="submitForm('numberValidateForm')">Add Cart</el-button>
            <el-button @click="resetForm('numberValidateForm')">Reset</el-button>
          </el-form-item>
        </el-form>
    </div>
  </div>
</template>

<script>
import imgObj from '../assets/2.png'
export default {
    data () {
        return {
            product: {
              id: "10",
              imgPath: imgObj,
              name: "Sample name",
              price: "123"
            },
            numberValidateForm: {
              id:'',
              quantity: 1,
            }
        }
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.numberValidateForm.id = parseInt(this.product.id);
            console.log(this.numberValidateForm);
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      deleteOne () {
        this.numberValidateForm.quantity > 1 && (this.numberValidateForm.quantity -= 1)
      },
      addOne () {
        this.numberValidateForm.quantity += 1;
      }
    }
}
</script>

<style lang="less" scoped>
.picture {
    position: relative;
    height: 200px;
    width: 200px;
}
.el-icon-remove-outline {
  cursor: pointer;
}
.el-icon-circle-plus-outline{
  cursor: pointer;
}
.quaBox {
  width: 40px;
}
.address_container{
    background-color: #d1dbda;
    height: 100%;
}
header{
    height: 100px;
    width: 100%;
    position: fixed;
    left:0;
    top:0;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
}
.logo{
    height: 35%;    
    position: absolute;
    right: 80%;
    top:-13.5%;
    cursor: pointer;
}

.save{
  position: relative;
}
.product_box{
    position: relative;
    top:200px;
    border: 1px solid black;
    width:25%;
}
</style>