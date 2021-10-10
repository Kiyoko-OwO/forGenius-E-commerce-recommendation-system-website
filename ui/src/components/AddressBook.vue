<template>
  <div id="address-container">
      <Address v-for="obj in addressbook" :key="obj.address_id"
      :userName="obj.name"
      :addressDe="obj.address"
      :phoneNumber="obj.phone_number"
      @delPro = 'del'
      >
      </Address>
      <el-button type="primary" @click="submitForm()">Save</el-button>
  </div>
</template>

<script>
import Address from './mod/Address.vue'
import { address_view } from '../api/user'
export default {
    data () {
        return {
            addressbook : {},
            tokenForm: {
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
        }
    }
}
</script>

<style>
#address-container {
    border: 1px solid black;
}
</style>