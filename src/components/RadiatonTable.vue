<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';
import GetCurrentDate from './getCurrentDate.vue';
export default {
  data() {
    return {
      radiationData: [],
      currentDate:''
    };
  },
  created() {
    this.getCurrentDate();
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    getCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
    },
    fetchData() {
      axios.get(`/Data/${this.currentDate}/radiation_data2.json`) // JSON 文件的路径
        .then(response => {
          this.radiationData = response.data;
          this.renderChart();
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    renderChart() {
      const ctx = this.$refs.chartCanvas.getContext('2d');

      // 提取地区和辐射数据
      const labels = this.radiationData.map(data => data.Area);
      const dataValues = this.radiationData.map(data => parseFloat(data.Radiation_Data));

      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Radiation Data',
            data: dataValues,
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  }
};
</script>

<style>
canvas {
  width: 100%;
  height: 400px; /* 调整图表高度 */
}
</style>
