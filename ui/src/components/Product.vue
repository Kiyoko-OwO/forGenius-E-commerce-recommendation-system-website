<template>
  <div class="address_container">
    <header>
        PRODUCT&nbsp;DETAIL
        <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
    </header>
    
    <div class="product_box">
        <div class="block" v-for="fit in fits" :key="fit">
          <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 100px; height: 100px"
            :src="product.picture"
            :fit="fit"></el-image>
        </div>
        <h2>Name: {{product.name}}</h2>
        <h3>Description:</h3>
        <p>{{product.description}}</p>
        <h3>Warranty: {{product.warranty}}</h3>
        <h3>Delivery date: {{product.delivery_date}}</h3>
        <h3>Price: $ {{product.price}}</h3>
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
import { cart_add } from '../api/order'
import { product_view } from '../api/product'
export default {
    data () {
        return {
            fits: [''],
            product: {},
            numberValidateForm: {
              token: '',
              product_id:'',
              quantity: 1
            },
            product_id_form:{
              product_id: 5
            }
        }
    },
    created () {
        this.loadProduct()
    },
    methods: {
      async loadProduct () {
          console.log(this.product_id_form);
          product_view(this.product_id_form).then ( res => {
            console.log(res.data);
            this.product = res.data.data
          }).catch( error => {
            console.log(error);
          })
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.numberValidateForm.product_id = this.product_id_form.product_id;
            this.numberValidateForm.token = sessionStorage.getItem('token');
            console.log(this.numberValidateForm);
            cart_add(this.numberValidateForm).then( res => {
              this.$message({message: 'Sucess!',type: 'success'});
              this.$router.push('cart');
            }).catch( error => {
              this.$message.error('Failed');
            })
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
      },
      jumpHome () {
            this.$router.push('Home');
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
  width: 100px;
}
.address_container{
    background-color: #d1dbda;
    height: 100%;
}
header{
    height: 100px;
    width: 100%;
    position: absolute;
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
    height: 300%;    
    position: absolute;
    right: 81%;
    top:-120.5%;
    cursor: pointer;
    z-index: 100;
}

.save{
  position: relative;
}
.product_box{
    position: relative;
    top:200px;
    border: 1px solid black;
    width:25%;
    word-break:break-all;
}
</style>