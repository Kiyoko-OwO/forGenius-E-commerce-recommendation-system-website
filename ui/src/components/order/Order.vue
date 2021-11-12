<template>
  <div >
    <div class="fix">
    <header>
        <img class="logo" src=../../assets/2.png alt="logo">
        <div class="title">
        ORDER&nbsp;
        </div>
        <el-button @click="jumpCart" class='return' type="primary">Return Cart</el-button>
    </header>
    <div class="order_contain">
    <h2>Address</h2>
      <div v-show="isEmpty">
          <p> Name: {{create_form.name}} </p> 
          <p> Address: {{create_form.address_line}}</p>
          <!-- <p> Country: {{create_form.country}}</p>
          <p> State: {{create_form.state}}</p>
          <p> Suburb: {{create_form.suburb}}</p>
          <p> Postal Code:{{create_form.post_code}}</p> -->
          <p> Phone Number: {{create_form.phone_number}}</p>
          <el-button @click="chooseDialogFormVisible = true" align="left" style="float:left">Choose</el-button>
          <el-dialog title="Address Book" :visible.sync="chooseDialogFormVisible" width="40%" class="editf" append-to-body>
            <div v-for="(item,ind) in addressbook" :key="ind">
                    <div class="block1"></div>
                    <p>Recipient's name: {{item.name}} </p> 
                    <p> Address: </p>
                    <p> {{item.address_line}}</p>
                    <p> Country: {{item.country}}</p>
                    <p> State: {{item.state}}</p>
                    <p> Suburb: {{item.suburb}}</p>
                    <p> Postal Code:{{item.post_code}}</p>
                    <p> Phone Number: {{item.phone_number}} </p> 
                    <el-button @click="chooseAdd(ind)" class="choose_in">Choose</el-button>
                    <div class="block"></div>
                    <div class="link-in"></div>
              </div>
            <div slot="footer" class="dialog-footer">
              <el-button @click="chooseDialogFormVisible = false">Cancel</el-button>
            </div>
          </el-dialog>
      </div>
      <el-button @click="jumpAdd" align="right">Add</el-button>
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
    </div>
    <el-button type="primary" @click="jumpPay" class="submit">Submit Order</el-button>
  </div>
  </div>
</template>

<script>
import { address_view } from '../../api/user'
import { cart_view } from '../../api/order'
import Product from '../mod/CartPro.vue'
import { cart_qua } from '../../api/order'
import { cart_del } from '../../api/order'
import { cart_create } from '../../api/order'
export default {
    inject:['reload'],
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
                address_line: '',
                phone_number: '',
                post_code: '',
                suburb: '',
                state: '',
                country: ''
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
        this.checkStat(),
        this.loadCart(),
        this.loadAddressBook()
    },
    methods: {
        async checkStat () {
            console.log(await this.check());
        },
        check () {
            // Simple Navigation Guards
            if (sessionStorage.getItem("token") != null) {
            } else {
            this.$router.push('/login')
            }
        },
        async loadCart() {
            this.tokenForm.token = sessionStorage.getItem('token');
            cart_view(this.tokenForm).then( res => {
                this.cart = res.data.data.cart;
                this.total_price = res.data.data.total;
                this.qua_form.token = sessionStorage.getItem('token');
                this.del_form.token = sessionStorage.getItem('token');
                this.create_form.token = sessionStorage.getItem('token');
            }).catch( error => {
                this.$message.error('You Need to Login First');
            })
        },
        async loadAddressBook() {
            // this.tokenForm.token = sessionStorage.getItem('token');
            address_view(this.tokenForm).then( res => {
                if (res.data.data.address_book.length > 0) {
                    this.isEmpty = true;
                    console.log(res);
                    this.addressbook = res.data.data.address_book;
                    this.addressbook = this.addressbook.slice().reverse()
                    this.create_form.name = this.addressbook[0].name;
                    this.create_form.address_line = this.addressbook[0].address_line;
                    this.create_form.phone_number = this.addressbook[0].phone_number;
                    this.create_form.post_code = this.addressbook[0].post_code;
                    this.create_form.suburb = this.addressbook[0].suburb;
                    this.create_form.state = this.addressbook[0].state;
                    this.create_form.country = this.addressbook[0].country;
                } else {
                    this.isEmpty = false;
                }
            }).catch( error => {
            })
        },
        add(index) {
            this.cart[index].quantity += 1;
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.total_price = this.total_price + this.cart[index].price;
            this.total_price = this.total_price.toFixed(2)
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id
            cart_qua(this.qua_form).then( res => {

            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        sub(index) {
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.cart[index].quantity > 1 && (this.cart[index].quantity -= 1) && (this.total_price = this.total_price - this.cart[index].price);
            this.total_price = this.total_price.toFixed(2)
            this.qua_form.quantity = this.cart[index].quantity;
            this.qua_form.product_id = this.cart[index].product_id;
            cart_qua(this.qua_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        del(index) {
            this.total_price = parseFloat(this.total_price);
            this.cart[index].price = parseFloat(this.cart[index].price);
            this.del_form.product_id = this.cart[index].product_id;
            cart_del(this.del_form).then( res => {
            }).catch( error => {
                this.$message.error('Failed');
            })
            this.total_price = this.total_price - (this.cart[index].quantity * this.cart[index].price)
            this.total_price = this.total_price.toFixed(2);
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
                sessionStorage.setItem('order', res.data.order_id);
                this.$router.push('/payment');
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        jumpAdd () {
            sessionStorage.setItem('from', 1);
            this.$router.push('/addressadd');
        }
    }  
}
</script>

<style lang="less" scoped>
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
.order_contain{
    position: relative;
    left:50%;
    transform: translate(-50%);
    width:500px;
}
.logo{
    height: 200%;
    position: relative;
    cursor: pointer;
    top:-60px;
    left:-600px;
    z-index:100;
}
.share_form{
    width:300px;
}
.return{
    height: 40%;
    position: relative;
    border-radius: 4px;
    padding: 2px 20px;
    left:480px;
    top:-370px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    border-color:#786662;
    cursor: pointer;

}
.submit{
    position: relative;
    left:52%;
    width:130px;
    font-size: 16px;
    height:40px;
    margin-top: 50px;
    margin-left: 80px;
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    padding-left: 19px;
    padding-top: 11px;
    border-color: #786662;
}
.cart-container{
    position: relative;
    left:47%;
    transform: translate(-50%);
    width:500px;
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
</style>

