<template>
    <div id="admin_container">
        <h1>Admin page</h1>
        <button @click="logOut">Log out</button>
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
        }
    }
}
</script>

<style>
#admin_container {
    background-color: #d1dbda;
    height: 100%;
}
</style>