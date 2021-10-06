<template>
    <div class="login_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="login_box">
        <el-form ref="form" :model="form" label-width="80px" class="loginForm">
            <el-form-item label="username" class="username">
              <el-input></el-input>
        </el-form-item>
            <el-form-item label="password">
              <el-input></el-input>
        </el-form-item>
        </el-form>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style >
.login_container {
    background-color: #d1dbda;
    height: 100%;

}

.login_box{
    background-color:#e7eae8;
    height: 375px;
    width: 650px;
    position: absolute;
    border-radius: 30px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);

}
.logo{
        height: 20%;
        width: 20%;
        position: absolute;
        right: 55%;
}
.loginForm{
    margin: 100;
    width: 400px;
    position: absolute;
    border-radius: 80px;
    top: 30%;
    left: 20%;
}
.username{
      border-radius: 40px;
}
</style>
