<template>
  <div>
    <!-- Your component content -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentDate: ''
    };
  },
  created() {
    this.getCurrentDate();
  },
  methods: {
    getCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
    }
  }
};
</script>

<style>
/* Your component styles */
</style>
