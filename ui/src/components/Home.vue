<template>
    <div id="home_container">
        <header>
            <img id="logo" src=../assets/logoThin.png alt="logo" v-on:click="addFn">
            <div class="button_position">
            <button class="signUp" v-on:click="jumpSign" v-show="isGuest" >Sign up</button>
            <button class="logIn" v-on:click="jumpLog" v-show="isGuest">Log in</button>
            <button v-on:click="jumpHome" @click="logOut" v-show="isUser">Log out</button>
            <button id="usern" v-show="isUser" @click="jumpProfile">{{ username }}</button>
            </div>
            <a href="http://127.0.0.1:8000/admin/login/?next=/admin/">
            <button class="logIn" v-show="isOk">Admin Log in</button>
            </a>
        </header>
        <main>
          <div>
            <img id="logo" src=../assets/logoThin.png alt="logo">
          </div>
          <span id="slogon">DISCOVER YOUR PRODUCT</span>
          <div class="search">
            <form action="" class="parent">
              <input type="text" v-model="keywords" placeholder="search keywords">
              <input type="submit" v-on:click="jumpResult" value="SEARCH">
            </form>
          </div>
          <button v-on:click="jumpProduct" class="example">Product example</button>
        </main>
        <div class="recommendation_container">
          <div>
            <div class="tittle_container">
              <div class="tittle">
              <p>RECOMMENDATION</p>
              </div>
              <div class="l_tittle">
              <p>THE PRODUCTS</p>
              <div class="line">
              </div>
              </div>  
            </div>
            <div class="product_container">
              <Home v-for="(obj,ind) in products" :key="obj.product_id"
              :proName="obj.name"
              :proDescription="obj.description"
              :proPrice="obj.price"
              :proPic="obj.picture"
              :proId="obj.product_id"
              :index="ind"
              > </Home>
            </div>
          </div>
        </div>
        <footer>
         <img class="foot" src=../assets/home_foot.jpeg alt="foot">
        </footer>
    </div>
</template>

<script>
import { logout } from '../api/user'
import { rec_guest } from '../api/product'
import { rec_user } from '../api/product'
import Home from './mod/Homepro.vue'
export default {
   components: {
        Home
    },
  inject:['reload'],
  data () {
    return {
      tokenForm: {
            token: ''
      },
      keywords: '',
      counter: 1,
      isOk: false,
      isUser: false,
      isGuest: false,
      username: '',
      products: []
    }
  },
  created () {
    this.checkStat(),
    this.loadRec()
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
    async loadRec () {
      if (this.isGuest == true) {
        rec_guest(this.tokenForm).then ( res => {
          this.products = res.data.products;
        }).catch( error => {
        })
      }
      else if (this.isUser == true) {
        this.tokenForm.token = sessionStorage.getItem('token');
        rec_user(this.tokenForm).then ( res => {
          this.products = res.data.products;
        }).catch( error => {
        })
      }
    },
    jumpSign () {
      this.$router.push('/signup')
    },
    jumpLog () {
      this.$router.push('/login')
    },
    jumpResult () {
    if(!this.keywords){
      alert("Please input search keywords")
      return
    }else{
      sessionStorage.setItem('word',this.keywords);
      this.$router.push('/search')
    }},
    jumpProfile () {
      this.$router.push('/userprofile')
    },
    jumpProduct () {
      this.$router.push('/product')
    },
    addFn(){
      if (this.counter == 5) {
        this.isOk = true;
      } else {
        this.counter++;
      }
    },
    jumpHome () {
      this.$router.push('home')
    },
    async logOut () {
      logout(this.tokenForm).then ( res => {
          this.$message({message: 'Log out Sucess!',type: 'success'});
          sessionStorage.clear();
          this.tokenForm.token = "";
          this.reload();
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
#home_container {
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
}
#slogon {
    float: left;
    margin-left: 300px;
    letter-spacing:10px;
}

.search {
    width: 1000px;
    height: 50px;
    margin: 50px auto;
}

.parent {
    width: 100%;
    height: 50px;
    top: 4px;
    position: relative;
}

.parent>input:first-of-type {
    width: 550px;
    height: 40px;
    border: 1px solid #ccc;
    font-size: 16px;
    outline: none;
    border-radius: 20px;
    margin-left: 150px;
    background-color:rgb(238, 238, 236);
    padding-left: 10px;
    margin-right: 5px;
}

.parent>input:first-of-type:focus {
    border: 1px solid #786662;
}

.parent>input:last-of-type {
    width: 100px;
    height: 40px;
    position: absolute;
    background:#786662;
    color: #fff;
    font-size: 16px;
    outline: none;
    border-radius: 20px;
    border-color: #786662;
    cursor: pointer;
}
.recommendation_container{
  background-color: white;
  margin:0 auto;
  height:650px;
  width:1700px;

}
.tittle_container{
  float: left;
  width:500px;
  height:600px;
}
.product_container{
  float: right;
  width:1200px;
  display: flex;
  flex-wrap: wrap;
}
.tittle{
  position: relative;
  left:30%;
  top:40%;
  transform:translate(0,-50%) ;
  font-size: 25px;
}
.example{
  margin-top:-300px;
}
.l_tittle{
  font-size: 5px;
  position: relative;
  left:34%;
  top:40%;
  transform:translate(0,-50%) ;
}
.line{
  height:2px;
  width:89px;
  position: relative;
  left:-1%;
  top:40%;
  transform:translate(0,-50%) ;
  background-color:rgb(0, 217, 255);
}
footer{
  padding-top:20px;
  width:1800px;
  margin:0 auto;
  img{
    width:100%;
  }
}
</style>
