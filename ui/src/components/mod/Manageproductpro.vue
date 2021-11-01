<template>
  <div class="my-cartpro">
    <p> Product ID: {{id}} </p> 
    <p> Product Name: {{name}} </p> 
    <p> Product Warranty: {{warr}} </p> 
    <p> Description: {{description}}</p>
    <p> Delivery Date: {{delivery}}</p>
    <p> Sales Data: {{sales}}</p>
    <p> Price: {{price}}</p>
    <div class="demo-image">
  <div class="block" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
    <el-image
      style="width: 100px; height: 100px"
      :src="editForm.picture"
      :fit="fit"></el-image>
  </div>
</div>  
    <el-button type="primary" icon="el-icon-edit" @click="dialogFormVisible = true"></el-button>
    <el-dialog title="Product Management" :visible.sync="dialogFormVisible" width="100%">
      <el-form :model="editForm">
        <el-form-item label="Product Id" >
          <el-input v-model="editForm.product_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Name" >
          <el-input v-model="editForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Description">
          <el-input type="textarea" v-model="editForm.description" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Delivery data" >
          <el-input v-model="editForm.delivery_date" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Warranty" >
          <el-input v-model="editForm.warranty" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Sales Data" >
          <el-input v-model="editForm.sales_data" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Price" >
          <el-input v-model="editForm.price" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Picture" >
          <el-input v-model="editForm.picture" autocomplete="off"></el-input>
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
import { product_edit } from '../../api/admin'
export default {
    inject:['reload'],
    props: ['index', 'id', 'name', 'warr', 'description', 'delivery', 'sales', 'price','pic'],
    data () {
      return {
        fits: [''],
        // url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        dialogFormVisible: false,
        editForm: {
          product_id: this.id,
          name: this.name,
          description: this.description,
          delivery_date: this.delivery,
          sales_data: this.sales,
          price: this.price,
          warranty: this.warr,
          picture: this.pic
        },
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
      }
    },
    methods: {
      delFn(){
        this.$emit("delPro", this.index)
      },
      editFn(){
        this.$emit("editAdd", this.index)
      },
      submitEdit() {
        console.log(this.editForm);
        product_edit(this.editForm).then( res => {
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
.my-cartpro {
  width: 500px;
  height: 200 px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
}
</style>