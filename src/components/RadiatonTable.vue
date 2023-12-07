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
      i:0,
      j:0,
      k:0,
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
    leti_increase(){
      this.i++;
    },
    leti_decrease(){
      this.i--;
    },
    getCurrentDate() {
      const date = new Date();
      let x1=date.getDate();
      let x2=date.getMonth();
      let x3=date.getFullYear();
      if (x1+this.i<=0){
        this.j--;
        switch ((x2-1)%12){
          case 1:this.i+=31;break;
          case 2:{
            if(x3%4==0&&x3%100!=0||x3%400==0)this.i+=29;
            else this.i+=28;
          }break;
          case 3:this.i+=31;break;
          case 4:this.i+=30;break;
          case 5:this.i+=31;break;
          case 6:this.i+=30;break;
          case 7:this.i+=31;break;
          case 8:this.i+=31;break;
          case 9:this.i+=30;break;
          case 10:this.i+=31;break;
          case 11:this.i+=30;break;
          case 12:this.i+=31;break;
          default:break;
        }
      }
      if(x2==2 && x1+this.i>28){
        if(x3%4==0&&x3%100!=0||x3%400==0)this.i-=29;
        else this.i-=28;
        this.j++;
      }
      if(x2==4||x2==6||x2==9||x2==11 && x1+this.i>30){
        this.i-=30;
        this.j++;
      }
      if(x2==1||x2==3||x2==5||x2==7||x2==8||x2==10||x2==12 && x1+this.i>31){
        this.i-=31;
        this.j++;
      }
      if (x2 + 1+this.j>12) {
        this.j-=12;
        this.k++;
      }
      else if (x2 + 1+this.j<0) {
       this.j+=12;
       this.k--;
      }
      let year = String(x3+this.k).padStart(2, '0');
      let month = String(x2 + 1+this.j).padStart(2, '0');
      let day = String(x1+this.i).padStart(2, '0');
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
