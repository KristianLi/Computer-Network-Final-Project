<script setup>
import RadiatonTable from "@/components/RadiatonTable.vue";
import Chinamap from "@/components/Chinamap.vue";
import analysis from "@/components/analysis.vue";
import Sidebar from './components/Sidebar.vue';

// 直接使用组件，无需导出
</script>

<template>
  <header>

  </header>

  <main>
    <Sidebar /> <!-- 侧边栏组件 -->
    <div class="content">
      <router-view /> <!-- 路由视图 -->
    </div>
  </main>
</template>

<style scoped>

main{
   background-image: url("../public/background6.jpg");
  background-repeat: no-repeat;
    background-size: cover;
}

header {
  line-height: 1.5;
}
.content {
  margin-left: 250px; /* Same as the width of the sidebar */
  padding: 1px 16px; /* Some padding */
  height: 1000px; /* Sample height */
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
.absolute-position {
  position: relative; /* 为了让子元素绝对定位相对于此元素 */
  /* background-image: url("../../public/background1.jpg"); /* */

}
.ChinaMap {
  position: absolute; /* 相对于父元素进行定位 */
  top: 100px;
  left: 0;
  width: 100%;
  height: 100%;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>


