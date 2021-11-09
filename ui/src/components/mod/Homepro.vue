<template>
  <div class="home-pro">
    <div class="img" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
        <el-image
        style="width: 150px; height: 150px"
        :src="proPic"
        :fit="fit" @click="goProduct"></el-image>
    </div>
    <p @click="goProduct"> Product Name: {{proName}} </p>
    <p @click="goProduct"> Price: {{proPrice}}</p>
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
}
p {
  cursor: pointer;
}
</style>