<template>
    <div id="profile_container">
        <header>
            <img id="logo" src=../../assets/logoThin.png alt="logo" v-on:click="jumpHome">
            <div class="button_position">
            <el-button icon="el-icon-user" class="signUp" v-on:click="jumpSign" v-show="isGuest" type="white">Sign up</el-button>
            <el-button icon= "el-icon-user-solid" class="logIn" v-on:click="jumpLog" v-show="isGuest" type="white" >Log in</el-button>
            <el-button v-on:click="jumpHome" @click="logOut" v-show="isUser" type="white" icon="el-icon-switch-button">Log out</el-button>
            <el-button id="usern" v-show="isUser" @click="jumpProfile" icon="el-icon-user-solid" type="white">{{ username }}</el-button>
            <a href="http://127.0.0.1:8000/admin/login/?next=/admin/">
            </a>
            </div>
        </header>
        <main>
            <img id="logo" src=../../assets/logoThin.png alt="logo">
            <button class="resetPassword" v-on:click="jumpResetpassword">Reset PASSWORD</button>
            <button class="cart" v-on:click="jumpMycart">MY CART</button>
            <button class="address" v-on:click="jumpAddressbook">ADDRESS BOOK</button>
            <button class="order" v-on:click="jumpOrdHis">ORDER HISTORY</button>
            <button class="order" v-on:click="jumpUsernameChange">USERNAME CHANGE</button>
        </main>
        <footer></footer>
    </div>
</template>

<script>
import { logout } from '../../api/user'
export default {
  inject:['reload'],
  data () {
      return {
        tokenForm: {
            token: ''
        },
        username: '',
        isUser: false,
        isGuest: false
      }
  },
  created () {
    this.checkStat()
  },
  methods: {
    async checkStat () {
      console.log(await this.check());
    },
    check () {
      if (sessionStorage.getItem("username") != null) {
        this.isUser = true;
        this.isGuest = false;
        this.username = sessionStorage.getItem('username');
        return this.username;
      } else {
        this.isGuest = true;
        this.isUser = false;
        this.$message.error('You Need to Login First');
        this.$router.push('/login')
        return this.isUser;
      }
    },
    jumpSign () {
      this.$router.push('/signup')
    },
    jumpProfile () {
      this.$router.push('/userprofile')
    },
    jumpLog () {
      this.$router.push('/login')
    },
    jumpResetpassword () {
      this.$router.push('/resetpassword')
    },
    jumpMycart () {
      this.$router.push('/cart')
    },
    jumpAddressbook () {
      this.$router.push('/address')
    },
    jumpHome () {
      this.$router.push('/home')
    },
    jumpOrdHis () {
      this.$router.push('/user/order')
    },
    jumpUsernameChange(){
      this.$router.push('/usernamechange')
    },
    async logOut () {
      this.tokenForm.token = sessionStorage.getItem('token');
      logout(this.tokenForm).then ( res => {
          this.$message({message: 'Log out Sucess!',type: 'success'});
          sessionStorage.clear();
          this.$router.push('/home')
      }).catch( error => {
          this.$message.error('Log out Failed');
      })
    }
  }
}
</script>

<style lang="less" scoped>
*{
    font-family: 'segUi';
}
#profile_container {
    background-color: #d1dbda;
    height: 100%;
}
header {
    height: 100px;
    width: 1800px;
    margin: 0 auto;
}
header #logo {
    height: 50px;
    float: left;
    margin-top: 25px;
    margin-left:400px;
}
.button_position{
  float: right;
  margin-right:400px;
}
button {
    float: right;
    border-radius: 4px;
    padding: 2px 15px;
    margin-left: 16px;
    margin-top: 35px;
    border-color: grey;
    color: grey;
    cursor: pointer;
}
main {
    width: 1000px;
    margin: 0 auto;
}
main #logo {
    width: 800px;
    margin-left: 100px;
    margin-top: 0px;
}
</style>
