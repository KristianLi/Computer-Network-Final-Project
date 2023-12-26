<template>
  <div class="sidebar">
    <router-link to="/">地图</router-link>
    <router-link to="/analysis">分析</router-link>
    <router-link to="/predict">预测</router-link>
  </div>
</template>

<script setup>
// script setup 表示使用组合式API
</script>

<style scoped>
.sidebar {
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 250px; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  background-color: #111; /* Black */
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 20px;
}

.sidebar a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
}

.sidebar a:hover {
  color: #f1f1f1;
}
</style>
