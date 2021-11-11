<template>
  <div class="my-cartpro">
  <div class="detail">
    <p> Product ID: {{id}} </p> 
    <p> Product Name: {{name}} </p> 
    <p> Product Warranty: {{warr}} </p> 
    <p> Feature: </p>  
    <p> {{features}} </p> 
    <p> Description: </p>
    <p>{{description}}</p>
    <p> Delivery Date: {{delivery}}</p>
    <p> Sales Data: {{sales}}</p>
    <p> Price: {{price}}</p>
  </div>
    <div class="demo-image">
  <div class="img" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
    <el-image
      style="width: 400px; height: 400px"
      :src="editForm.picture"
      :fit="fit"></el-image>
  </div>
</div>
<div class="b"> 
    <el-button type="white" icon="el-icon-edit" @click="dialogFormVisible = true" class="edit">Edit</el-button>
    <el-dialog title="Product Management" :visible.sync="dialogFormVisible" width="40%" @close="closeDialog" class="editf" append-to-body>
      <el-form :model="editForm" ref="edit_FormRef" :rules="editRules">
        <p>Product ID: {{id}}</p>
        <el-form-item label="Name" prop="name">
          <el-input v-model="editForm.name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Feature" prop="features">
          <el-input v-model="editForm.features" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Description" prop="description">
          <el-input type="textarea" v-model="editForm.description" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Delivery date" prop="delivery_date">
          <el-input v-model="editForm.delivery_date" autocomplete="off" placeholder="The number of days it takes for delivery"></el-input>
        </el-form-item>
        <el-form-item label="Warranty" prop="warranty">
          <el-input v-model="editForm.warranty" autocomplete="off" placeholder="The warranty time"></el-input>
        </el-form-item>
        <el-form-item label="Price" prop="price">
          <el-input v-model="editForm.price" autocomplete="off" placeholder="More than 0 and at most two decimal places"></el-input>
        </el-form-item>
        <el-form-item label="Picture" prop="picture">
          <el-input v-model="editForm.picture" autocomplete="off" placeholder="Please input the url of picture"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitEdit">Confim</el-button>
      </div>
    </el-dialog>
    
    <el-button type="black" @click="deldialogFormVisible = true" icon="el-icon-delete" class="edit">Delete</el-button>
    <el-dialog :visible.sync="deldialogFormVisible" width="13%" @close="closeDialog" append-to-body>
      <div slot="footer" class="dialog-footer">
        <el-button type="white" @click="deldialogFormVisible = false">Cancel</el-button>
        <el-button type="white" @click="delFn">Confim</el-button>
      </div>
    </el-dialog>
  </div> 
  </div>
  

</template>

<script>
import { product_edit } from '../../api/admin'
export default {
    inject:['reload'],
    props: ['index', 'id', 'name', 'warr', 'description', 'delivery', 'sales', 'price','pic','features'],
    data () {
    var checkName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkFeature = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('Feature cannot be empty'))
      } else {
        callback()
      }
    }
    var checkDes = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('name cannot be empty'))
      } else {
        callback()
      }
    }
    var checkWarranty = (rule, value, callback) => {
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('The warranty should be number'))
        }
      }, 100)
    }
    var checkDelivery= (rule, value, callback) => {
      value = this.editForm.delivery_date
      const mailReg = /^\d+$/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('The date should be number of day'))
        }
      }, 100)
    }
    var checkSales= (rule, value, callback) => {
      const mailReg = /^\d+$/
      if (!value) {
        return callback(new Error('Sales cannot be empty'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('the sales should be number'))
        }
      }, 100)
    }
    var checkPrice= (rule, value, callback) => {
      const mailReg =  /^((0{1}\.\d{1,2})|([1-9]\d*\.{1}\d{1,2})|([1-9]+\d*))$/
      setTimeout(() => {
        if (mailReg.test(value) & value != 0) {
          callback()
        } else {
          callback(new Error('Should more than 0 and at most two decimal places'))
        }
      }, 100)
    }
      return {
        fits: [''],
        // url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        dialogFormVisible: false,
        deldialogFormVisible: false,
        editForm: {
          product_id: this.id,
          name: this.name,
          description: this.description,
          delivery_date: this.delivery,
          sales_data: this.sales,
          price: this.price,
          warranty: this.warr,
          picture: this.pic,
          features:this.features
        },
        editRules: {
        name: [
          { validator: checkName, trigger: 'blur' }
        ],
        warranty:[
          { validator: checkWarranty, trigger: 'blur'}
        ],
        delivery_date:[
          { validator: checkDelivery, trigger: 'blur'}
        ],
        sales:[
          { validator: checkSales, trigger: 'blur'}
        ],
        price:[
          { validator: checkPrice, trigger: 'blur'}
        ],
        description:[
          { validator: checkDes, trigger: 'blur'}
        ],
        features:[
          { validator: checkFeature, trigger: 'blur'}
        ]
      }
      }
    },
    watch: {
      id:function(newVal,oldVal){
        this.id = id;
      },
      name:function(newVal,oldVal){
        this.name = newVal;
      },
      description:function(newVal,oldVal){
        this.description = newVal;
      },
      warr:function(newVal,oldVal){
        this.warr = newVal;
      },
      delivery:function(newVal,oldVal){
        this.delivery = newVal;
      },
      sales:function(newVal,oldVal){
        this.sales = newVal;
      },
      price:function(newVal,oldVal){
        this.price = newVal;
      },
      price:function(newVal,oldVal){
        this.feature = newVal;
      }
    },
    methods: {
      delFn(){
        this.$emit("delPro", this.index);
        this.deldialogFormVisible =  false;
      },
      editFn(){
        this.$emit("editAdd", this.index)
      },
      closeDialog(){
      this.$refs['edit_FormRef'].resetFields();
      },
      submitEdit() {
      this.$refs.edit_FormRef.validate(async (valid) =>{
        if(valid){
        console.log(this.editForm);
        product_edit(this.editForm).then( res => {
            this.$message({message: 'Sucess!',type: 'success'});
            this.dialogFormVisible = false;
            this.reload();
        }).catch( error => {
            this.$message.error('Failed');
        })
        }
        else{
            console.log('error submit!!');
            return false;
        }
      })
    }
}}
</script>

<style lang="less" scoped>
.my-cartpro {
  width: 1400px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
  word-break:break-all;
  
}
.img{
  float:right;
}
.des{
  position: relative;
  width: 100px;
  left: 400px;
}
.edit{
position:relative;
left:40%;
}
.detail{
  float:left;
  width: 700px;
}
.b{
  clear:both;
}

</style>

<style >
.editf{
  position: fixed;
}
</style>
