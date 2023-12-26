<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
  <div class="center-content">
    <span style="color: white;">{{ currentDate }}</span>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      radiationData: [],
      currentDate: '',
      chart: null, // 用于保存图表实例的引用
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
      let x1 = date.getDate();
      let x2 = date.getMonth() + 1;
      let x3 = date.getFullYear();
      let year = String(x3).padStart(2, '0');
      let month = String(x2).padStart(2, '0');
      let day = String(x1+1).padStart(2, '0');
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

      // 如果已经存在一个图表实例，则销毁它
      if (this.chart) {
        this.chart.destroy();
      }
      // 提取地区和辐射数据
      let labels = this.radiationData.map(data => data.Area);
      let dataValues = this.radiationData.map(data => parseInt(data.Radiation_Data));

      // 创建一个新的图表实例，并保存其引用
      this.chart = new Chart(ctx, {
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

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px; /* 按钮和日期文本之间的间距 */
}
</style>
