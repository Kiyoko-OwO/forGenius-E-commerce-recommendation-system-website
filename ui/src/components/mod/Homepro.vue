<template>
  <div class="home-pro">
    <div class="img" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
        <el-image
        style="width: 250px; height: 250px"
        :src="proPic"
        :fit="fit" @click="goProduct"></el-image>
    </div>
    <p @click="goProduct"> {{proName}}</p>
    <p @click="goProduct"> <span>${{proPrice}}</span></p>
  </div>
</template>

<script>
export default {
    props: ['index', 'proName', 'proDescription', 'proSales_data', 'proPrice', 'proPic','proId'],
    methods: {
    },
    data(){
        return {
            fits: [''],
    }
    },
    methods: {
      goProduct () {
        sessionStorage.setItem('product',this.proId);
        this.$router.push('/product')
      }
    }
}
</script>

<style lang="less" scoped>
.home-pro {
  width: 300px;
  padding: 20px;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
  word-break:break-all;
  border: 4px solid bisque;
  border-style:groove;
}
p {
  cursor: pointer;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 20px;
}
span{
  color:red;
  font-size: 20px ;
  font-family: 'Courier New', Courier, monospace;
}
.img{
  position: relative;
  left:9%;
}
</style>