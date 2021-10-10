<template>
  <div id="address-container">
      <Address v-for="(obj,ind) in addressbook" :key="obj.address_id"
      :userName="obj.name"
      :addressDe="obj.address"
      :phoneNumber="obj.phone_number"
      :index = "ind"
      @delAdd = 'del'
      >
      </Address>
      <el-button type="primary" @click="submitForm()">Save</el-button>
  </div>
</template>

<script>
import Address from './mod/Address.vue'
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
            const res = address_delete(this.deleteForm);
            console.log(res);
        }

    }
}
</script>

<style>
#address-container {
    border: 1px solid black;
}
</style>