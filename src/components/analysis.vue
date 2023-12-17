<template>
  <div>
    <div class="response-content">
      <!-- 显示 JSON 文件中的响应内容 -->
      {{ jsonResponse }}
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
.response-content {
  white-space: pre-wrap; /* 保留换行符和空格 */
}
</style>
