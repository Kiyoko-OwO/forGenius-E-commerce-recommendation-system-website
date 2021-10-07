<template>
    <div id="home_container">
        <header>
            <img id="logo" src=../assets/logoThin.png alt="logo">
            <button class="signUp" v-on:click="jumpSign">Sign up</button>
            <button class="logIn" v-on:click="jumpLog">Log in</button>
        </header>
        <main>
            <img id="logo" src=../assets/logoThin.png alt="logo">
        </main>
        <footer></footer>
    </div>
</template>

<script>
export default {
  methods: {
    jumpSign () {
      this.$router.push('Signup')
    },
    jumpLog () {
      this.$router.push('Login')
    }
  }
}
</script>

<style>
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
    margin-top: 0px;
}
</style>
