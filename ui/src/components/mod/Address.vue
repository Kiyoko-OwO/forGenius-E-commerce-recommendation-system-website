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
    <el-button type="white" icon="el-icon-edit" @click="dialogFormVisible = true">Edit</el-button>
    <el-dialog title="Address Book" :visible.sync="dialogFormVisible" class="editf" width="30%" append-to-body>
      <el-form :model="editForm" ref="edit_FormRef" :rules="editRules">
           <el-form-item label="NAME" class="username_change" prop="name">
            <el-input v-model="editForm.name" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="ADDRESS" class="username_change" prop="address_line">
            <el-input v-model="editForm.address_line" autocomplete="off">
            </el-input>
          </el-form-item>
           <el-form-item label="COUNTRY" class="username_change" prop="country">
            <el-input v-model="editForm.country" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="STATE" class="username_change" prop="state">
            <el-input v-model="editForm.state" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="SUBURB" class="username_change" prop="suburb">
            <el-input v-model="editForm.suburb" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="POSTAL CODE" class="username_change" prop="post_code">
            <el-input v-model="editForm.post_code" autocomplete="off">
            </el-input>
          </el-form-item>
          <el-form-item label="PHONE NUMBER" class="username_change" prop="phone_number">
            <el-input v-model="editForm.phone_number" autocomplete="off">
            </el-input>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="white" @click="dialogFormVisible = false" icon="el-icon-circle-close">Cancel</el-button>
        <el-button type="white" @click="submitEdit" icon="el-icon-circle-check">Confim</el-button>
      </div>
    </el-dialog>
    
    <el-button type="white" icon="el-icon-delete" @click="delFn">Delete</el-button>
  </div>
</template>

<script>
// Mod page for address
import { address_edit } from '../../api/user'
export default {
    inject:['reload'],
    props: ['index', 'userName', 'addressId', 'addressDe', 'phoneNumber', 'suburb', 'post_code', 'state', 'country'],
    data () {
      // The rules for input value
          var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'))
      } else {
        callback()
      }
    }
    var checkAddress = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('address cannot be empty'))
      } else {
        callback()
      }
    }
    var checkPhone = (rule, value, callback) => {
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Phonenumber should be number'))
        }
      }, 100)
    }
    var checkState = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('State cannot be empty'))
      } else {
        callback()
      }
    }
    var checkSuburb = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Suburb cannot be empty'))
      } else {
        callback()
      }
    }
    var checkCountry = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Country cannot be empty'))
      } else {
        callback()
      }
    }
    var checkCode = (rule, value, callback) => {
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Postal code should be number'))
        }
      }, 100)
    }
      return {
        dialogFormVisible: false,
        editForm: {
          token: '',
          address_id: this.addressId,
          address_line: this.addressDe,
          country: this.country,
          name: this.userName,
          phone_number: this.phoneNumber,
          post_code: this.post_code,
          state: this.state,
          suburb: this.suburb
        },
      editRules: {        
        name: [
          { validator: checkName, trigger: 'blur' }
        ],        
        address_line: [
          { validator: checkAddress, trigger: 'blur' }
        ],
        phone_number: [
          { validator: checkPhone, trigger: 'blur'  }
        ],
        post_code: [
          { validator: checkCode, trigger: 'blur'  }
        ],
                suburb: [
          { validator: checkSuburb, trigger: 'blur'  }
        ],
                state: [
          { validator: checkState, trigger: 'blur'  }
        ],
                country: [
          { validator: checkCountry, trigger: 'blur'  }
        ]

      
       }
    
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
      // submit editted address
      submitEdit() {  
        this.$refs.edit_FormRef.validate(async (valid) =>{
        if(valid){
          this.editForm.token = sessionStorage.getItem('token');
          this.editForm.phone_number = this.editForm.phone_number.toString();
          // Main operation for edit
          address_edit(this.editForm).then( res => {
              this.$message({message: 'Sucess!',type: 'success'});
              this.dialogFormVisible = false;
              this.reload();
          }).catch( error => {
              this.$message.error('Failed');
          })
          }
        else{
          // user cannot submit if input did not pass the rules
          return false;
        }
    })
}}}
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
.editf{
  position: fixed;
}
</style>