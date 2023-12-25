
<template>
  <div>
    <canvas ref="chartCanvas" ></canvas>
  </div>
  <div class="center-content">
    <button @click="leti_decrease" :disabled="isButtonHidden">--</button>
    <span id="dateshow">{{ currentDate }}</span>
    <button @click="leti_increase" :disabled="isButtonHidden2">++</button>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';
export default {
  data() {
    return {
      i:0,
      j:0,
      k:0,
      c:0,
      radiationData: [],
      currentDate:'',
      chart: null, // 用于保存图表实例的引用
      isButtonHidden: false, // 控制按钮显示和隐藏的状态
      isButtonHidden2: true,
    };
  },
  created() {
    this.getCurrentDate();
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    leti_increase() {
      // 隐藏按钮并延迟 2 秒后显示
      this.isButtonHidden = true;
      this.isButtonHidden2 = true;
      setTimeout(() => {
        this.isButtonHidden = false;
        if(this.c>0)this.isButtonHidden2 = false;
      }, 1000);

      this.i++;
      this.c--;
      this.getCurrentDate();
      this.fetchData();
    },
    leti_decrease() {
      // 隐藏按钮并延迟 2 秒后显示
      this.isButtonHidden = true;
      this.isButtonHidden2 = true;
      setTimeout(() => {
        if(this.c<14)this.isButtonHidden=false;
        if(this.c>0)this.isButtonHidden2 = false;
      }, 1000);

      this.i--;
      this.c++;
      this.getCurrentDate();
      this.fetchData();
    },
    getCurrentDate() {
      const date = new Date();
      let x1=date.getDate();
      let x2=date.getMonth()+1;
      let x3=date.getFullYear();
      if (x1+this.i<=0){
        this.j--;
        switch ((x2-1)%12){
          case 1:this.i+=31;break;
          case 2:{
            if(x3%4===0&&x3%100!==0||x3%400===0)this.i+=29;
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
      if(x2+this.j===2 && x1+this.i>28){
        if((x3+this.k)%4===0&&(x3+this.k)%100!==0||(x3+this.k)%400===0)this.i-=29;
        else this.i-=28;
        this.j++;
      }
      if(x2+this.j===4||x2+this.j===6||x2+this.j===9||x2+this.j===11 && x1+this.i>30){
        this.i-=30;
        this.j++;
      }
      if(x2+this.j===1||x2+this.j===3||x2+this.j===5||x2+this.j===7||x2+this.j===8||x2+this.j===10||x2+this.j===12 && x1+this.i>31){
        this.i-=31;
        this.j++;
      }
      if (x2+this.j>12) {
        this.j-=12;
        this.k++;
      }
      else if (x2+this.j===0) {
       this.j+=12;
       this.k--;
      }
      let year = String(x3+this.k).padStart(2, '0');
      let month = String(x2+this.j).padStart(2, '0');
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
            backgroundColor: 'rgba(54, 162, 235, 1)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
          }]
        },
          options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              grid: {
            color: 'rgba(255, 255, 255, 1)' // 设置Y轴网格线的颜色，这里是半透明红色
         },
          ticks: {
          color: 'rgba(255, 255, 255, 1)' // 设置Y轴刻度标签的颜色，这里是半透明红色
         }
        },
            y: {
              beginAtZero: true,
              grid: {
            color: 'rgba(255, 255, 255, 1)' // 设置Y轴网格线的颜色，这里是半透明红色
          },
          ticks: {
        color: 'rgba(255, 255, 255, 1)' // 设置Y轴刻度标签的颜色，这里是半透明红色
         }
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
#dateshow{
   color: aliceblue;
}

</style>


