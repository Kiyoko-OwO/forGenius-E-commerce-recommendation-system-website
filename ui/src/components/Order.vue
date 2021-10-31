<template>
  <div>
      <h1>Real Order Page</h1>
      <el-button @click="jumpCart">Return</el-button>
      <el-input v-model="share_form.email" placeholder="input email address"></el-input>
      <el-button @click="share">Share</el-button>
      <div v-show="isEmpty">
          <h2>Address</h2>
          <p> Name: {{create_form.name}} </p> 
          <p> Address: {{create_form.address}}</p>
          <p> Phone Number: {{create_form.phone_number}}</p>
          <el-button @click="chooseDialogFormVisible = true">Choose</el-button>
          <el-dialog title="Address Book" :visible.sync="chooseDialogFormVisible">
            <div v-for="(item,ind) in addressbook" :key="ind">
                  Recipient's name: {{item.name}} ===
                  Address: {{item.address}} ===
                  Phone Number: {{item.phone_number}} ===
                  <el-button @click="chooseAdd(ind)">Choose</el-button>
              </div>
            <div slot="footer" class="dialog-footer">
              <el-button @click="chooseDialogFormVisible = false">Cancel</el-button>
            </div>
          </el-dialog>
      </div>
      <el-button @click="jumpAdd">Add</el-button>
      <div class="cart-container">
        <Product v-for="(obj,ind) in cart" :key="obj.id"
        :proName="obj.name"
        :proPrice="obj.price"
        :qua="obj.quantity"
        :index = "ind"
        @addQua = 'add'
        @subQua = 'sub'
        @delPro = 'del'>
        </Product>
        <p>Total Price: $</p>
        <p>{{total_price}}</p>
    </div>
      <el-button type="primary" @click="jumpPay">Submit Order</el-button>
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
            this.$message({message: 'Shared',type: 'success'});
            this.share_form.email = "";
        }
    }
    
    
}
</script>

<style>

</style>