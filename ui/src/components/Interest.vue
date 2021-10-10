<template>
  <div>
    <h1>Interest Field</h1>
    <el-checkbox-group v-model="intest">
      <el-checkbox-button v-for="city in tags" :label="city" :key="city">{{city}}</el-checkbox-button>
    </el-checkbox-group>
    <el-button class='submit'>SUBMIT</el-button>
    <li v-for="item in intest" :key="item">
        <span>{{ item }}</span>
    </li>
  </div>

</template>
<script>
const tagOptions = ['Fastion', 'Toys', 'Hobby', 'DIY', 'Electronics', 'Media', 'Furniture', 'Appliance', 'Food', 'Personal Care']
export default {
  data () {
    return {
      tags: tagOptions,
      intest: []
    }
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
