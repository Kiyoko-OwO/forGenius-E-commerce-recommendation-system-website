<template class="ad">
  <div class="address_container">
    <header>
        <img class="logo" src=../assets/2.png alt="logo" v-on:click="jumpHome">
        ADDRESS&nbsp;BOOK
    </header>
    
    <div id="address-container">
        <Address v-for="(obj,ind) in addressbook.slice().reverse()" :key="obj.address_id"
        :userName="obj.name"
        :addressDe="obj.address"
        :phoneNumber="obj.phone_number"
        :addressId="obj.address_id"
        :index = "ind"
        @delAdd = 'del'
        >
        </Address>
        <el-button type="primary" class="add" @click="add()">Add</el-button>
    </div>
  </div>
</template>

<script>
import Address from './mod/Address.vue'
import { address_view } from '../api/user'
import { address_delete } from '../api/user'
export default {
    data () {
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
        jumpHome () {
            this.$router.push('Home');
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
    position: relative;
    left:70%;
    top: 30px;
    width: 130px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    letter-spacing:2px;
    padding-left: 25px;
    border-color: #786662;
}
</style>