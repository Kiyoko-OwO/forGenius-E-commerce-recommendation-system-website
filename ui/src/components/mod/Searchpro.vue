<template>
  <div class="search-pro">
    <div class="img" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
        <el-image
        style="width: 250px; height: 250px"
        :src="proPic"
        :fit="fit"></el-image>
    </div>
    <p class="plink" @click="goProduct">{{proName}} </p>
    <p> <span>${{proPrice}}</span></p>
  </div>
</template>

<script>
export default {
    props: ['index', 'proName', 'proDescription', 'proSales_data', 'proPrice', 'proPic','proId'],
    methods: {
      goProduct () {
        sessionStorage.setItem('product',this.proId);
        this.$router.push('/product')
        sessionStorage.removeItem('sort');
      }
    },
    data(){
        return {
            fits: [''],
    }
    }
}
</script>


<style lang="less" scoped>
.search-pro {
  width: 300px;
  padding: 10px;
  border: 4px solid bisque;
  border-style:groove;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
  word-break:break-all;
  .img{
    margin-left:20px;
  }
}
.plink {
  cursor: pointer;
}
p {
  cursor: pointer;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-weight: 20px;
}
span{
  color:rgb(255, 115, 0);
  font-size: 20px ;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>