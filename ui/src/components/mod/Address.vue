<template>
  <div class="my-address">
    <p> Name: {{userName}} </p> 
    <p> Address: {{addressDe}}</p>
    <p> Phone Number: {{phoneNumber}}</p>
    <el-button type="primary" icon="el-icon-edit"></el-button>
    <el-button type="primary" icon="el-icon-delete"></el-button>
  </div>
</template>

<script>
export default {
    props: ['userName', 'addressId', 'addressDe', 'phoneNumber']
}
</script>

<style>
.my-address {
  width: 400px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
}
</style>