<template>
  <div>
    <RadiationTable />
    <Analysis />
  </div>
</template>

<script>
import RadiationTable from './RadiatonTable.vue';
import Analysis from './Analysis.vue';

export default {
  components: {
    RadiationTable,
    Analysis
  }
}
</script>
