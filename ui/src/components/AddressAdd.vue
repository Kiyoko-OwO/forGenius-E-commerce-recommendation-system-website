<template>
  <div>
    <h1>Address Add</h1>
    <el-form :model="addForm">
        <el-form-item label="Name" >
          <el-input v-model="addForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Address" >
          <el-input v-model="addForm.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Phone Number">
          <el-input v-model="addForm.phone_number" autocomplete="off"></el-input>
        </el-form-item>
        <el-button type="primary" @click="submitAdd">Confim</el-button>
      </el-form>
  </div>
  
</template>

<script>
import { address_add } from '../api/user'
export default {
  data () {
    return {
      addForm: {
        token: '',
        name: '',
        address: '',
        phone_number: ''
      }
    }
  },
  methods: {
    submitAdd() {
      this.addForm.token = sessionStorage.getItem('token');
      console.log(this.addForm);
      address_add(this.addForm).then( res => {
          this.$message({message: 'Sucess!======',type: 'success'});
          this.$router.push('address');
      }).catch( error => {
          this.$message.error('Failed=====');
      })
    }
  }
}
</script>

<style>

</style>