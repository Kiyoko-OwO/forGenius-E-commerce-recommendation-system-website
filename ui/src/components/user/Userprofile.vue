<template>
    <div id="profile_container">
        <header>
            <img id="logo" src=../../assets/logoThin.png alt="logo" @click="jumpHome">
            <button class="signUp" v-on:click="jumpSign" v-show="isGuest">Sign up</button>
            <button class="logIn" v-on:click="jumpLog" v-show="isGuest">Log in</button>
            <button @click="logOut" v-show="isUser">Log out</button>
            <button id="usern" v-show="isUser">{{ username }}</button>
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
        return this.isUser;
      }
    },
    jumpSign () {
      this.$router.push('signup')
    },
    jumpLog () {
      this.$router.push('login')
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
      this.$router.push('home')
    },
    jumpOrdHis () {
      this.$router.push('user/order')
    },
    jumpUsernameChange(){
      this.$router.push('/usernamechange')
    },
    async logOut () {
      this.tokenForm.token = sessionStorage.getItem('token');
      logout(this.tokenForm).then ( res => {
          this.$message({message: 'Log out Sucess!',type: 'success'});
          sessionStorage.clear();
          this.$router.push('home')
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
    width: 1000px;
    margin: 0 auto;
}
header #logo {
    height: 50px;
    float: left;
    margin-top: 25px;
}
button {
    float: right;
    border-radius: 4px;
    padding: 2px 15px;
    margin-left: 50px;
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
