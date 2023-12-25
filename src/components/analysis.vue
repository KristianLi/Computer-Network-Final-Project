<template>
  <div>
    <div class="box">
      <p>
        {{ jsonResponse }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      jsonResponse: '',
      currentDate: ''
    };
  },
  mounted() {
    this.getCurrentTime();
    // 使用反引号以及 ${} 来正确解析模板字符串
    fetch(`/Data/${this.currentDate}/analysis.json`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); // 正确处理 JSON 数据
        })
        .then(data => {
          this.jsonResponse = data.response; // 假设 JSON 数据结构为 { response: '...' }
        })
        .catch(error => {
          console.error('Error fetching the JSON file:', error);
        });
  },
  methods: {
    getCurrentTime() {
      let date = new Date(); // 获取当前日期
      let year = String(date.getFullYear()).padStart(2, '0');
      let month = String(date.getMonth() + 1).padStart(2, '0');
      let day = String(date.getDate()).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
    }
  }
};
</script>

<style>



.box
{
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  position: relative;
  display: flex;
  padding: 20px;
  justify-content: center;
  align-items: center;
  background: rgba(0,0,0,0.5);
  max-width: 96%;
  margin: 10px auto;
  overflow: hidden;
  border-radius: 20px;

}
.box:before{
  content: '';
  position: absolute;
  width: 100%;
  height: 125%;
  background: linear-gradient(315deg,#00ccff,#d400d4);
  animation: animate 6s linear infinite
}
@keyframes animate {
  0%
  {
    transform: rotate(0deg);
  }
  100%
  {
    transform: rotate(360deg);
  }
}
.box:after{
  content: '';
  position: absolute;
  inset : 6px;
  background: #0e1538;
  border-radius: 15px;
  z-index: 2;
}
p{
  white-space: pre-wrap; /* 保留换行符和空格 */
  position: relative;
  z-index: 2;
  color: #fff;
  z-index: 4;
}


</style>
