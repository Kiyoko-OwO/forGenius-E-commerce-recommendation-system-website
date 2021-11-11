<template>
    <div class="fix">
    <header>
        <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpHome">
        <div class="title">
        PRODUCT&nbsp;DETAIL
       </div>
    </header>
    <main>
    <div class="product_box">
        <div class="img" v-for="fit in fits" :key="fit">
          <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 550px; height: 700px"
            :src="product.picture"
            :fit="fit"></el-image>
        </div>
        <div class="inf_box">
        <div class="inf">
        <h2>{{product.name}}</h2>
        <p>{{product.description}}</p>
        <!-- <h3>Feature:</h3>
        <p>{{product.feature}}</p> -->
        <h3>Warranty: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span> {{product.warranty}} year(s)</span></h3>
        <h3>Delivery date: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>{{product.delivery_date}}</span></h3>
        <p class="price">$ {{product.price}}</p>
        <h3>Feature: 
          <el-button class="feature" v-for="feature in features" :key="feature" @click='searchFe(feature)' type="white">
          {{feature}}
          </el-button>
        </h3>
        <el-form :model="numberValidateForm" ref="numberValidateForm" label-width="100px" class="demo-ruleForm">
          <el-form-item
            label="Quantity"
            prop="quantity"
            :rules="[
            { required: true, message: 'Quantity cannot be null'},
            { type: 'number', message: 'Quantity need to be number'}
            ]"
          >
          <el-button class="el-icon-remove-outline" @click='deleteOne' circle type="white"></el-button>
          <el-input class="quaBox" type="quantity" v-model.number="numberValidateForm.quantity" autocomplete="off"></el-input>
          <el-button class="el-icon-circle-plus-outline" @click='addOne' circle type="white"></el-button>
          </el-form-item>
            <el-button icon="el-icon-s-goods" class="addcart" @click="submitForm('numberValidateForm')" type="black">Add Cart</el-button>
            <el-button icon="el-icon-refresh-right" class="reset" @click="resetForm('numberValidateForm')" type="white">Reset </el-button>
        </el-form>
      </div>
    </div>
    </div>
    </main>
    <div class="block"></div>
    <footer>
 <div class="recommendation_container">
          <div>
            <div class="tittle_container">
              <div class="tittle">
              <p>RECOMMENDATION</p>
              </div>
              <div class="l_tittle">
              <p>THE PRODUCTS</p>
              <div class="line">
              </div>
              </div>  
            </div>
            <div class="product_container">
              <Home v-for="(obj,ind) in products" :key="obj.product_id"
              :proName="obj.name"
              :proDescription="obj.description"
              :proPrice="obj.price"
              :proPic="obj.picture"
              :proId="obj.product_id"
              :index="ind"
              > </Home>
            </div>
          </div>
        </div>
    </footer>
   </div>
   
</template>

<script>
import Home from '.././mod/Homepro.vue'
import { cart_add } from '../../api/order'
import { product_view } from '../../api/product'
import { rec_guest } from '../../api/product'
import { rec_user } from '../../api/product'
export default {
     components: {
        Home
    },
    data () {
        return {
            tokenForm: {
              token: ''
            },
            fits: [''],
            product: {},
            numberValidateForm: {
              token: '',
              product_id:'',
              quantity: 1
            },
            product_id_form:{
              product_id: 1
            },
            features: [],
            products: []
        }
    },
    created () {
        this.loadProduct(),
        this.loadRec()
    },
    methods: {
      async loadProduct () {
          this.product_id_form.product_id = sessionStorage.getItem('product');
          product_view(this.product_id_form).then ( res => {
            this.product = res.data.data;
            this.features = this.product.features.split(" ");
          }).catch( error => {
            console.log(error);
          })
      },
      async loadRec () {
      if (sessionStorage.getItem('token' != null)) {
        this.tokenForm.token = sessionStorage.getItem('token');
        rec_user(this.tokenForm).then ( res => {
          this.products = res.data.products;
          this.products = this.products.slice(0, 3);
        }).catch( error => {
        })
      }
      else {
        rec_guest(this.tokenForm).then ( res => {
          this.products = res.data.products;
          this.products = this.products.slice(0, 3);
        }).catch( error => {
        })
      }
    },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.numberValidateForm.product_id = this.product_id_form.product_id;
            this.numberValidateForm.token = sessionStorage.getItem('token');
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
        sessionStorage.removeItem('product');
        this.$router.push('Home');
      }, searchFe(feature) {
        sessionStorage.setItem('word',feature);
        this.$router.push('/search')
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
  margin-left: 20px;
  margin-right:20px;
  width: 260px;
}
header{
    height: 100px;
    width: 100%;
    position: relative;
    left:0;
    top:0;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
    overflow: hidden;
}
.logo{
    height: 200%;
    position: relative;
    cursor: pointer;
    top:-60px;
    left:-600px;
    z-index:100;
}

.product_box{
    margin-top:20px;
    width:1700px;
    word-break:break-all;
}
.img{
  float:left;
  margin-left:200px;
}
.inf{
  margin:0 auto;
  word-break:break-all;
  width:500px;
  padding-bottom: 30px;
}
.fix{
    margin:0 auto;
    width:1750px;
}
.title{
    position: relative;
    top:-260px;
    height:100px;
    width:200x;
    left:49%;
    transform: translate(-50%);
    text-align: center;
}
.feature{
    border-radius: 20px;
}
span{
  font-size: 14px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
.addcart{
  position: relative;
  left:10px;
  width:480px;
  letter-spacing: 4px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  background-color:black;
  color:white
}
.reset{
  position: relative;
  width:480px;
  letter-spacing: 4px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  
}
.price{
  color:red;
  font-size: 20px ;
  font-family: 'Courier New', Courier, monospace;
}
.inf_box{
  float:right;
  background-color: #e7eae8;
  width:600px;
  margin-right:100px;
}
.recommendation_container{
  position: relative;
  background-color: white;
  margin:0 auto;
  height:700px;
  width:1700px;
}
.tittle_container{
  float: left;
  width:500px;
  height:600px;
}
.product_container{
  float: right;
  width:1200px;
  display: flex;
  flex-wrap: wrap;
}
.tittle{
  position: relative;
  left:30%;
  top:40%;
  transform:translate(0,-50%) ;
  font-size: 25px;
}
.example{
  margin-top:-300px;
}
.l_tittle{
  font-size: 5px;
  position: relative;
  left:34%;
  top:40%;
  transform:translate(0,-50%) ;
}
.line{
  height:2px;
  width:89px;
  position: relative;
  left:-1%;
  top:40%;
  transform:translate(0,-50%) ;
  background-color:rgb(0, 217, 255);
}
.recommendation_container{
  background-color: white;
  margin:0 auto;
  height:700px;
  width:1700px;
  clear:both;

}
.tittle_container{
  float: left;
  width:500px;
  height:600px;
}
.product_container{
  float: right;
  width:1200px;
  display: flex;
  flex-wrap: wrap;
}
.tittle{
  position: relative;
  left:30%;
  top:40%;
  transform:translate(0,-50%) ;
  font-size: 25px;
}
.example{
  margin-top:-300px;
}
.l_tittle{
  font-size: 5px;
  position: relative;
  left:34%;
  top:40%;
  transform:translate(0,-50%) ;
}
.line{
  height:2px;
  width:89px;
  position: relative;
  left:-1%;
  top:40%;
  transform:translate(0,-50%) ;
  background-color:rgb(0, 217, 255);
}
</style>
