<template class="ad">
  <div class="address_container">
    <div class="fix">
    <header>
        <img class="logo" src=../../assets/2.png alt="logo" v-on:click="jumpUser">
        <div class="title">
        ADDRESS&nbsp;BOOK
        </div>
        <el-button type="brown" class="add" @click="add()" >ADD ADDRESS</el-button>
    </header>
    
    <div id="address-container">
        <Address v-for="(obj,ind) in addressbook" :key="obj.address_id"
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
  </div>
</template>

<script>
// Main page for address book
import Address from '../mod/Address.vue'
import { address_view } from '../../api/user'
import { address_delete } from '../../api/user'
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
        // Load address book
        async loadAddressBook () {
            this.tokenForm.token = sessionStorage.getItem('token');
            // Main operation to get address from backend
            const { data } = await address_view(this.tokenForm);
            console.log(data);
            this.addressbook = data.data.address_book;
            this.addressbook = this.addressbook.slice().reverse();
        },
        // Delete an address
        del(index) {
            // Operation to delete in frontend
            this.deleteForm.address_id = this.addressbook[index].address_id;
            this.deleteForm.token = this.tokenForm.token;
            this.addressbook.splice(index, 1);
            // Operation to delete in backend
            address_delete(this.deleteForm).then( res => {
                this.$message({message: 'Delete Sucess!',type: 'success'});
            }).catch( error => {
                this.$message.error('Failed');
            })
        },
        add() {
            this.$router.push('/addressadd');
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
#address-container {
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
.title{
    position: relative;
    top:-260px;
    height:100px;
    width:200x;
    left:49%;
    transform: translate(-50%);
    text-align: center;

}
.add{
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
.fix{
    margin:0 auto;
    width:1750px;
}

</style>