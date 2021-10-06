<template>
    <div class="login_container">
        <img class="logo" src=../assets/2.png alt="logo">
        <div class="login_box">
            <form action="" class="username">
            <input type="text" name="username">
            </form>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
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
.username{
    width: 1000px;
    position:absolute;
    border-radius: 30px;
    top: 0%;
    left: 40%;
}
</style>
