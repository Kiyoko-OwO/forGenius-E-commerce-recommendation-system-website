<template>
  <div class="search-pro">
    <div class="img" v-for="fit in fits" :key="fit">
    <span class="demonstration">{{ fit }}</span>
        <el-image
        style="width: 150px; height: 150px"
        :src="123"
        :fit="fit"></el-image>
    </div>
    <p> Product Name: {{proName}} </p>
    <p> Description:</p>
    <p>{{proDescription}}</p>
    <p> Price: {{proPrice}}</p>
    <p> Sales Data: {{proSales_data}}</p>
  </div>
</template>

<script>
export default {
    props: ['index', 'proName', 'proDescription', 'proSales_data', 'proPrice'],
    methods: {
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
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
  word-break:break-all;
}

</style>