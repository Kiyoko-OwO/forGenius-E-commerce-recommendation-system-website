<template>
  <div id="address-container">
      <Address v-for="obj in addressbook" :key="obj.address_id"
      :userName="obj.name"
      :addressDe="obj.address"
      :phoneNumber="obj.phone_number"
      >
      </Address>
      <el-button type="primary" @click="submitForm()">Save</el-button>
  </div>
</template>

<script>
import Address from './mod/Address.vue'
export default {
    data () {
        return {
            addressbook : [
                {
                    name: "Cai",
                    address_id: "1",
                    address: "This is a random fake address",
                    phone_number: 12345678901,
                },
                {
                    name: "Yang",
                    address_id: "2",
                    address: "This is a random fake address",
                    phone_number: 12345678901,
                },
                {
                    name: "Ma",
                    address_id: "3",
                    address: "This is a random fake address",
                    phone_number: 12345678901,
                },
                {
                    name: "Guan",
                    address_id: "4",
                    address: "This is a random fake address",
                    phone_number: 12345678901,
                },
                {
                    name: "Chen",
                    address_id: "5",
                    address: "This is a random fake address",
                    phone_number: 12345678901,
                }
            ]
        }
    },
    components: {
        Address
    },
    methods: {
        submitForm() {
            console.log(this.addressbook)
        }
    }
}
</script>

<style>
#address-container {
    border: 1px solid black;
}
</style>