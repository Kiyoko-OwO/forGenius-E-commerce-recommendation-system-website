<template>
  <div class="my-address">
    <p> Name: {{userName}} </p> 
    <p> Address: </p>
    <p> {{addressDe}}</p>
    <p> Country: {{country}}</p>
    <p> State: {{state}}</p>
    <p> Suburb: {{suburb}}</p>
    <p> Postal Code:{{post_code}}</p>
    <p> Phone Number: {{phoneNumber}}</p>
    <!-- Form -->
    <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisible = true"></el-button>
    <el-dialog title="Address Book" :visible.sync="dialogFormVisible">
      <el-form :model="editForm">
        <el-form-item label="Name" >
          <el-input v-model="editForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Address" >
          <el-input v-model="editForm.address" autocomplete="off"></el-input>
        </el-form-item>
           <el-form-item label="COUNTRY" prop="country">
            <el-input v-model="editForm.country" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="STATE" prop="state">
            <el-input v-model="editForm.state" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="SUBURB"  prop="suburb">
            <el-input v-model="editForm.suburb" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="POSTAL CODE" prop="post_code">
            <el-input v-model="editForm.post_code" autocomplete="off">
            </el-input>
          </el-form-item>
        <el-form-item label="Phone Number">
          <el-input v-model="editForm.phone_number" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitEdit">Confim</el-button>
      </div>
    </el-dialog>
    
    <el-button type="primary" icon="el-icon-delete" @click="delFn"></el-button>
  </div>
</template>

<script>
import { address_edit } from '../../api/user'
export default {
    inject:['reload'],
    props: ['index', 'userName', 'addressId', 'addressDe', 'phoneNumber'],
    data () {
      return {
        dialogFormVisible: false,
        editForm: {
          token: '',
          name: this.userName,
          address: this.addressDe,
          phone_number: this.phoneNumber,
          address_id: this.addressId
        },
      }
    },
    watch: {
      userName:function(newVal,oldVal){
        this.userName = newVal;
      },
      addressDe:function(newVal,oldVal){
        this.addressDe = newVal;
      },
      phoneNumber:function(newVal,oldVal){
        this.phoneNumber = newVal;
      },
      addressId:function(newVal,oldVal){
        this.addressId = newVal;
      }
    },
    methods: {
      delFn(){
        this.$emit("delAdd", this.index)
      },
      editFn(){
        this.$emit("editAdd", this.index)
      },
      submitEdit() {
        this.editForm.token = sessionStorage.getItem('token');
        console.log(this.editForm);
        this.editForm.phone_number = this.editForm.phone_number.toString();
        address_edit(this.editForm).then( res => {
            this.$message({message: 'Sucess!',type: 'success'});
            this.dialogFormVisible = false;
            this.reload();
        }).catch( error => {
            this.$message.error('Failed');
        })
      }
    }
}
</script>

<style lang="less" scoped>
.my-address {
  width: 400px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  word-break:break-all;
}
</style>