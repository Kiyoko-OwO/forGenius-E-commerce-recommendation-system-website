<template>
  <div class="order_item">
      <div class="block"></div>
      Order id: {{ordId}}
      <el-dialog :title="order_id" :visible.sync="dialogFormVisible" class="editf" width="30%" append-to-body>
        <div class="item" v-for="item in ordItem" :key="item.product_id">
        <div class="img" v-for="fit in fits" :key="fit">
        <span class="demonstration">{{ fit }}</span>
          <el-image
            style="width: 100px; height: 100px"
            :src="123"
            :fit="fit"></el-image>
        </div>
        <div class="item1">
        <p>Name: {{item.name}} </p>
        <p>Price: {{item.price}} </p>
        <p>Quantity: {{item.quantity}} </p>
        </div>
        <div class="link-in"></div>
        </div>
        <p> Buyer Name: {{name}}</p>
        <p> Address: {{address_line}}</p>
        <p> Phone Number: {{phone_number}}</p>
        <div class="block"></div>
        Order Date: {{orderDate}}
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total Price: {{ordTotal}}
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">Close</el-button>
        </div>
      </el-dialog>
      <p>Paid: {{payStat}}</p>
      <p>Order Date: {{orderDate}}</p>
      <el-button @click="orderFn" class="detail">Detail</el-button>
      <el-button @click="orderShare" class="detail">Share</el-button>
      <el-dialog title="Share Order" :visible.sync="sharedialogFormVisible" class="editf"  width="30%" append-to-body>
      <el-form :model="shareForm" ref="share_FormRef" :rules="shareRules">
        <el-form-item label="Receiver Name" prop="receiver_name">
          <el-input v-model="shareForm.receiver_name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Email" prop="to_email">
          <el-input v-model="shareForm.to_email" autocomplete="off" ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="resetShare">Cancel</el-button>
        <el-button type="primary" @click="submit">Confim</el-button>
      </div>
      </el-dialog>
      <div class="block"></div>
      <div class="link-top"></div>
  </div>
</template>

<script>
import { ord_share } from '../../api/order'
export default {
    props: ['index', 'ordId', 'payStat', 'ordItem','ordTotal','orderDate','name','address_line','phone_number'],
    data () {
    var checkEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+\.com/
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('Please enter the correct email format'))
        }
      }, 100)
    }
    var checkUsername = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('username cannot be empty'));
      } else {
        callback()
      }
    }
        return {
            fits: [''],
            dialogFormVisible: false,
            sharedialogFormVisible: false,
            order_id: '###',
        shareForm: {
          token: "",
	        order_id: "",
	        to_email: "",
	        receiver_name: ""
        },
        shareRules: {
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        receiver_name:[
          { validator: checkUsername, trigger: 'blur'}
        ]
        }
            
        }
    },
    created () {
        this.$emit('checker',this.index);
        this.order_id =  "Order Number: " + this.ordId.toString();
    },
    methods: {
        orderFn() {
            if (this.payStat === "Fail") {
                this.$router.push('/payment');
                console.log(this.ordId);
                sessionStorage.setItem('order', this.ordId);
            } else {
                this.dialogFormVisible = true
            }
        },
        orderShare() {
            this.sharedialogFormVisible = true
        },
        closeDialog(){
            this.$refs['share_FormRef'].resetFields();
        },
        resetShare () {
          this.shareForm.to_email = "";
          this.shareForm.receiver_name = "";
          this.sharedialogFormVisible = false;
        },
        submit () {
          this.shareForm.order_id = this.ordId;
          this.shareForm.token = sessionStorage.getItem('token');
          console.log(this.shareForm);
          ord_share(this.shareForm).then ( res => {
          this.$message({message: 'Share Sucess!',type: 'success'});
              this.sharedialogFormVisible = false;
              this.shareForm.to_email = "";
              this.shareForm.receiver_name = "";
          }).catch( error => {
              this.$message.error('Share Failed');
          })
        }
    }
}
</script>

<style lang="less" scoped>
.link-top {
    position: relative;
    width: 300%;
    height: 1px;
    left:50%;
    transform: translate(-50%);
    border-top: solid #0b0b0f 1px;
}
.link-in {
    position: relative;
    width: 100%;
    height: 1px;
    border-top: solid #0b0b0f 1px;
}
.block {
   height: 20px;
}
.detail{
   position: relative;
   left:100%;

}
.editf{
   position: fixed;
} 
.img{
   float:right;
   margin-right:20px;
   margin-top:-5px;
}
</style>

<style>

</style>