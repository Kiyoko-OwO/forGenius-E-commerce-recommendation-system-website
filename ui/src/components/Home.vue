<template>
    <div id="home_container">
        <header>
            <img id="logo" src=../assets/logoThin.png alt="logo">
            <button class="signUp" v-on:click="jumpSign">Sign up</button>
            <button class="logIn" v-on:click="jumpLog">Log in</button>
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
        </main>
        <footer></footer>
    </div>
</template>

<script>
export default {
  data () {
    return {
      keywords: ''
    }
  },
  methods: {
    jumpSign () {
      this.$router.push('signup')
    },
    jumpLog () {
      this.$router.push('login')
    },
    jumpResult () {
      console.log('jump to result')
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
}
#slogon {
    position: absolute;
    left: 37%;
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
    width: 585px;
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
</style>
