<template>
  <div>
    <h1>Intrest Filed</h1>
    <el-checkbox-group v-model="intest">
      <el-checkbox-button v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox-button>
    </el-checkbox-group>
    <el-button class='submit'>SUBMIT</el-button>
  </div>

</template>
<script>
  const tagOptions = ['Fastion', 'Toys', 'Hobby', 'DIY','Electronics', 'Media', 'Furniture', 'Appliance','Food','Personal Care'];
  export default {
    data () {
      return {
        cities: tagOptions,
        intest:[]
      };
    }
  }
</script>

<style>
.submit{
    position: absolute;
    left:50%;
    bottom:12%;
    height:50px;
    width:200px;
    transform: translate(-50%,-50%);
    border-radius: 10px;
    background: #786662;
    color: #fefefe;
    letter-spacing:10px;
    padding-left: 30px;
}
</style>