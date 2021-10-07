<template>
    <div id="profile_container">
        <header>
            <img id="logo" src=../assets/logoThin.png alt="logo">
        </header>
        <main>
            <img id="logo" src=../assets/logoThin.png alt="logo">
            <button class="resetPassword" v-on:click="jumpResetpassword">Reset PASSWORD</button>
            <button class="cart" v-on:click="jumpMycart">MY CART</button>
            <button class="address" v-on:click="jumpAddressbook">ADDRESS BOOK</button>
        </main>
        <footer></footer>
    </div>
</template>

<script>
export default {
  methods: {
    jumpResetpassword () {
      this.$router.push('/resetpassword')
    },
    jumpLog () {
      this.$router.push('Login')
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
