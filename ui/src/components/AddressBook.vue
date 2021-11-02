<template class="ad">
  <div class="address_container">
    <header>
        <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpUser">
        ADDRESS&nbsp;BOOK
        <el-button type="primary" class="add" @click="add()">Add</el-button>
    </header>
    
    <div id="address-container">
        <Address v-for="(obj,ind) in addressbook.slice().reverse()" :key="obj.address_id"
        :userName="obj.name"
        :addressDe="obj.address_line"
        :phoneNumber="obj.phone_number"
        :addressId="obj.address_id"
        :country="obj.country"
        :state="obj.state"
        :suburb="obj.suburb"
        :post_code="obj.post_code"
        :index = "ind"
        @delAdd = 'del'
        >
        </Address>
    </div>
  </div>
</template>

<script>
import Address from './mod/Address.vue'
import { address_view } from '../api/user'
import { address_delete } from '../api/user'
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
    var checkFeature= (rule, value, callback) => {
      if (!value) {
        return callback(new Error('feature cannot be empty'))
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
      const mailReg =  /^((0{1}\.\d{1,2})|([1-9]\d*\.{1}\d{1,2})|([1-9]+\d*))$/
      if (!value) {
        return callback(new Error('Price cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value) & value != 0) {
          callback()
        } else {
          callback(new Error('the price should be number'))
        }
      }, 100)
    }
        return {
            addressbook : [],
            tokenForm: {
                token: ''
            },
            deleteForm : {
                address_id: '',
                token: ''
            }
        }
    },
    created () {
        this.loadAddressBook()
    },
    components: {
        Address
    },
    methods: {
        async loadAddressBook () {
            this.tokenForm.token = sessionStorage.getItem('token');
            const { data } = await address_view(this.tokenForm);
            console.log(data);
            this.addressbook = data.data.address_book;
        },
        del(index) {
            this.deleteForm.address_id = this.addressbook[index].address_id;
            this.deleteForm.token = this.tokenForm.token;
            this.addressbook.splice(index, 1);
            address_delete(this.deleteForm).then( res => {
                this.$message({message: 'Delete Sucess!',type: 'success'});
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        add() {
            this.$router.push('addressadd');
        },
        jumpUser () {
            this.$router.push('/userprofile');
        }
    }
}
</script>

<style lang="less" scoped>

.address_container{
    background-color: #d1dbda;
    min-height: 100%;
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
#address-container {
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
.add{
   height: 40%;
    position: absolute;
    border-radius: 4px;
    padding: 2px 20px;
    margin-left: 300px;
    margin-top: 40px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    border-color:#786662;
    cursor: pointer;
}

</style>