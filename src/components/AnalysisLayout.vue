<template>
  <div>
    <RadiationTable />
    <Analysis />
  </div>
</template>

<script>
import RadiationTable from './RadiatonTable.vue';
import Analysis from './analysis.vue';

export default {
  components: {
    RadiationTable,
    Analysis
  }
}
</script>
