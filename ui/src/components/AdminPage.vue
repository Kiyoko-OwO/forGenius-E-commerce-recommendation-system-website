<template>
    <div id="admin_container">
        <header>
            <button @click="logOut">Log out</button>
            <button id="usern">{{ username }}</button>
        </header>
        <main>
            <img id="logo" src=../assets/logoThin.png alt="logo">
            <button class="manageProduct" v-on:click="jumpManageproduct">MANAGE PRODUCT</button>
        </main>
        <footer></footer>
    </div>
</template>

<script>
import { logout } from '../api/user'
export default {
    data () {
        return {
            tokenForm: {
                token: ''
            },
        }
    },
    created () {
        this.username = sessionStorage.getItem('username');
    },
    methods: {
        logOut () {
            this.tokenForm.token = sessionStorage.getItem('token');
            logout(this.tokenForm).then ( res => {
                this.$message({message: 'Log out Sucess!',type: 'success'});
                sessionStorage.clear();
                this.$router.push('home')
            }).catch( error => {
                this.$message.error('Log out Failed');
            })
        },
        jumpManageproduct () {
            this.$router.push('/manageproduct')
        }
  }
}
</script>

<style lang="less" scoped>
*{
    font-family: 'segUi';
}
#admin_container {
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