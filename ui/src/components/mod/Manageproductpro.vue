<template>
  <div class="my-cartpro">
    <p> Product ID: {{id}} </p> 
    <p> Product Name: {{name}} </p> 
    <p> Product warr: {{warr}} </p> 
    <p> Description: {{description}}</p>
    <p> Delivery date: {{delivery}}</p>
    <p> Sales Data: {{sales}}</p>
    <p> Price: {{price}}</p>  
  </div>
</template>

<script>
export default {
    props: ['index', 'id', 'name', 'warr', 'description', 'delivery', 'sales', 'price'],
}
</script>

<style>
.my-cartpro {
  width: 500px;
  height: 200 px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 5px;
  margin: 10px;
  font-family: 'segUi';
}
</style>