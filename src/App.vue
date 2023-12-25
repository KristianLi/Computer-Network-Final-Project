<script setup>
import RadiatonTable from "@/components/RadiatonTable.vue";
import Chinamap from "@/components/chinamap.vue";
import analysis from "@/components/analysis.vue";
</script>

<template>
  <header>

  </header>

  <main>
    <div class="absolute-position">
      <Chinamap />
    </div>
    <div>
      <RadiatonTable />
    </div>

    <div>
      <analysis />
    </div>
  </main>
</template>

<style scoped>
<<<<<<< HEAD
=======
main{
      background-image: url("../../public/background6.jpg");
      background-repeat: no-repeat center;
      background-size: cover;
}
>>>>>>> 5fe5ef1 (first commit)
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
.absolute-position {
  position: relative; /* 为了让子元素绝对定位相对于此元素 */
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
