<template>
  <div class="address_container">
    <header>
        ADDRESS&nbsp;BOOK
    </header>
    <img class="logo" src=../assets/2.png alt="logo">
    <div id="address-container">
        <Address v-for="(obj,ind) in addressbook" :key="obj.address_id"
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
import Address from './Address.vue'
import { address_view } from '../api/user'
import { address_delete } from '../api/user'
export default {
    data () {
        return {
            addressbook : {},
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
        }

    }
}
</script>

<style lang="less" scoped>
#address-container {
    position: absolute;
    top:100px;
    border: 1px solid black;
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

.add{
    position: relative;
    left:50%;
    width: 100px;
    background: #786662;
    border-radius: 10px;
    color: #fefefe;
    letter-spacing:4px;
    padding-left: 26%;
    border-color: #786662;
}
</style>