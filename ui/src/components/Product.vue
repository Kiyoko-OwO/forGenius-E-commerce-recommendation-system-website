<template>
  <div>
      <h1>Product detail</h1>
      <img v-bind:src="product.imgPath" alt="product image" />
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
        <el-input type="quantity" v-model.number="numberValidateForm.quantity" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('numberValidateForm')">Add Cart</el-button>
          <el-button @click="resetForm('numberValidateForm')">Reset</el-button>
        </el-form-item>
      </el-form>
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
              quantity: '',
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
      }
    }
}
</script>

<style>
img {
    height: 100px;
    width: 100px;
}
</style>