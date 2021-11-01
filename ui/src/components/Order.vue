<template>
  <div >
    <header>
        ORDER&nbsp;
        <el-button @click="jumpCart" class='return' type="primary">Return Cart</el-button>
        <img class="logo" src=../assets/2.png alt="logo">
    </header>
    <div class="order_contain">
      <div v-show="isEmpty">
          <h2>Address</h2>
          <p> Name: {{create_form.name}} </p> 
          <p> Address: {{create_form.address}}</p>
          <p> Phone Number: {{create_form.phone_number}}</p>
          <el-button @click="chooseDialogFormVisible = true" align="left" style="float:left">Choose</el-button>
          <el-button @click="jumpAdd" align="right">Add</el-button>
          <el-dialog title="Address Book" :visible.sync="chooseDialogFormVisible" width="40%">
            <div v-for="(item,ind) in addressbook" :key="ind">
                   <div class="block1"></div>
                   <p>Recipient's name: {{item.name}} </p> 
                   <p>Address: {{item.address}} </p> 
                   <p>Phone Number: {{item.phone_number}} </p> 
                   <el-button @click="chooseAdd(ind)" class="choose_in">Choose</el-button>
                   <div class="block"></div>
                   <div class="link-in"></div>
              </div>
            <div slot="footer" class="dialog-footer">
              <el-button @click="chooseDialogFormVisible = false">Cancel</el-button>
            </div>
          </el-dialog>
      </div>
      <div class="cart-container">
        <h2 class="infor">Product information</h2>
        <Product v-for="(obj,ind) in cart" :key="obj.id"
        :proName="obj.name"
        :proPrice="obj.price"
        :qua="obj.quantity"
        :index = "ind"
        @addQua = 'add'
        @subQua = 'sub'
        @delPro = 'del'>
        </Product>
        <div class="price">
        <p>Total Price: $</p>
        <p>{{total_price}}</p>
        </div>
    </div>
    <div class="share">
      <h2 class="share_ti">Share Your Order</h2>
      <el-form ref='share_form' :model="share_form" :rules="share_formRules" class="share_form" label-position="left" label-width="90px" >
      <el-form-item label="EMAIL" class="email_change" prop="email">
      <el-input v-model="share_form.email" placeholder="input email address" ></el-input>
      </el-form-item>
      <el-button @click="share" align="right">Share Order</el-button>
      </el-form>
      <el-button type="primary" @click="jumpPay" class="submit">Submit Order</el-button>
    </div>
  </div>
  </div>
</template>

<script>
import { address_view } from '../api/user'
import { cart_view } from '../api/order'
import Product from './mod/CartPro.vue'
import { cart_qua } from '../api/order'
import { cart_del } from '../api/order'
import { cart_create } from '../api/order'
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
            cart : [],
            addressbook : [],
            tokenForm: {
                token: ''
            },
            create_form: {
                token: '',
                name: '',
                address: '',
                phone_number: ''
            },
            total_price: '',
            qua_form: {
                token: '',
                product_id: '',
                quantity: ''
            },
            del_form: {
                token: '',
                product_id: ''
            },
            chooseDialogFormVisible: false,
            isEmpty: true,
            share_form: {
                token: '',
                email: ''
            },
            share_formRules:{
               email: [
                    { validator: checkEmail, trigger: 'blur' }
                ]
            }
        }
    },
    components: {
        Product
    },
    created () {
        this.loadCart(),
        this.loadAddressBook()
    },
    methods: {
        async loadCart() {
            this.tokenForm.token = sessionStorage.getItem('token');
            cart_view(this.tokenForm).then( res => {
                this.cart = res.data.data.cart;
                this.total_price = res.data.data.total;
                this.qua_form.token = sessionStorage.getItem('token');
                this.del_form.token = sessionStorage.getItem('token');
                this.create_form.token = sessionStorage.getItem('token');
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        async loadAddressBook() {
            // this.tokenForm.token = sessionStorage.getItem('token');
            address_view(this.tokenForm).then( res => {
                if (res.data.data.address_book.length > 0) {
                    this.isEmpty = true;
                    this.addressbook = res.data.data.address_book;
                    this.addressbook = this.addressbook.slice().reverse()
                    this.create_form.name = this.addressbook[0].name;
                    this.create_form.address = this.addressbook[0].address;
                    this.create_form.phone_number = this.addressbook[0].phone_number;
                } else {
                    this.isEmpty = false;
                }
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        add(index) {
            this.cart[index].quantity += 1;
            this.total_price = this.total_price + this.cart[index].price;
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id
            cart_qua(this.qua_form).then( res => {

            }).catch( error => {
                this.$message.error('Failed2');
            })
        },
        sub(index) {
            this.cart[index].quantity > 1 && (this.cart[index].quantity -= 1) && (this.total_price = this.total_price - this.cart[index].price);
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id;
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed3');
            })
        },
        del(index) {
            this.del_form.product_id = this.cart[index].product_id;
            cart_del(this.del_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed');
            })
            this.total_price = this.total_price - (this.cart[index].quantity * this.cart[index].price)
            this.cart.splice(index, 1);
            console.log(this.cart);
        },
        chooseAdd(index) {
            this.create_form.name = this.addressbook[index].name;
            this.create_form.address = this.addressbook[index].address;
            this.create_form.phone_number = this.addressbook[index].phone_number;
            this.chooseDialogFormVisible = false;
        },
        jumpCart () {
            this.$router.push('/cart');
        },
        jumpPay () {
            cart_create(this.create_form).then( res => {
                this.$message({message: 'Order Placed',type: 'success'});
                this.$router.push('/payment');
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        jumpAdd () {
            sessionStorage.setItem('from', 1);
            this.$router.push('/addressadd');
        },
        share() {
            this.$refs.share_form.validate(async (valid) =>{
            if(!valid) return;
            else{
            this.$message({message: 'Shared',type: 'success'});
            this.share_form.email = "";
            }
            });
    }
    }  
}
</script>

<style lang="less" scoped>
header{
    height: 100px;
    width: 100%;
    position: absolute;
    left:0;
    top:-10px;
    z-index: 999;
    border-bottom:3px solid #ccc;
    text-align: center;
    line-height: 130px;
    font-weight:normal;
    font-family: 'segUi';
    font-size: 50px;
}
.order_contain{
    position: absolute;
    top:100px;
    left:38%;
}
.logo{
    height: 200%;    
    position: absolute;
    right: 80%;
    top:-56%;
    cursor: pointer;
}
.share_form{
    width:300px;
}
.return{
    position: relative;
    height:40px;
    left:500px;
    top:-10px;
    background: #786662;
    color: #fefefe;
    border-color: #786662;
}
.submit{
    position: relative;
    left:70%;
    width:130px;
    font-size: 16px;
    height:50px;
    margin-top: 70px;
    margin-left: 80px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    padding-left: 19px;
    padding-top: 11px;
    border-color: #786662;
}
.cart-container{
    position: relative;
    left: -12px;
}
.price{
    position: relative;
    left: 75%;
}
.infor{
    position: relative;
    left: 15px;
}
.email_change{
    position: relative;
    width:500px;
}
.email_change /deep/ .el-form-item__label{
    font-family: 'segUi';
    position: relative;
    letter-spacing:.1em;
    top:2px;
    font-size: 18px;
}

    .link-in {
        position: relative;
        width: 100%;
        height: 1px;
        border-top: solid #0b0b0f 1px;
     }
     .block {
  height: 20px;
}
     .block1 {
  height: 10px;
}
.choose_in{
    position: relative;
    left:80%;
}
</style>


