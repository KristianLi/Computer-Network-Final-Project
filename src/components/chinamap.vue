<template>
  <div id="china_map" style="width: 100%; height: 800px;margin:auto"></div>
</template>

<script>
import * as echarts from "echarts";
import china from "../../china.json";
import axios from "axios";
echarts.registerMap("china", china);

export default {
  data() {
    return {
      MapDataList: [],
      currentDate:'',
    };
  },
  created() {
    this.getMapData();
  },
  mounted() {
    this.setMapData();
  },
  methods: {
    getMapData() {
      let date = new Date();
      let x3 = date.getFullYear();
      let x2= date.getMonth() + 1;
      let x1 = date.getDate();
      let year = String(x3).padStart(2, '0');
      let month = String(x2).padStart(2, '0');
      let day = String(x1).padStart(2, '0');
      this.currentDate = `${year}-${month}-${day}`;
      let path = `/Data/${this.currentDate}/re_data.json`
      axios.get(path ).then(response => {
        console.log(response);
        for (let i = 0; i < response.data.length; i++) {
          response.data[i].value = parseInt(response.data[i].value.split(" ")[0]);
        }
        this.MapDataList = response.data;
        console.log(this.MapDataList);
        // 请求完成后，渲染地图
        this.setMapData();
      }).catch(error => {
        console.log(error);
      });
    },
    setMapData() {
      this.chinachart = echarts.init(document.getElementById("china_map"));
      // 相关配置
      this.chartOption = {
        tooltip: { // 鼠标移到图里面的浮动提示框
          formatter(params) {
            let localValue;
            if (params.data) {
              localValue = params.data.value;
            } else {
              localValue = 0;
            }
            let htmlStr = `<div style='font-size:18px;'> ${params.name}</div>
                                <p style='text-align:left;margin-top:-4px;'>辐射值：${localValue}</p>`;
            return htmlStr;
          },
          backgroundColor: "#ff7f50", //提示标签背景颜色
          textStyle: { color: "#fff" }, //提示标签字体颜色
          padding: [5, 10, 0, 10],  // 设置上下的内边距为 5,0，左右的内边距为 10
        },
        visualMap: {
          show: true,
          bottom: 20,
          left: 100,
          // left: 50, top: '30%', right: 0, bottom: 0,  //定位的左上角以及右下角分别所对应的经纬度
          text: ["200", "0"],
          min: 0,
          itemHeight: 200,  //图形的高度，即长条的高度。
          color: [
            '#ee6666',//红色
            '#fc8452',//橙色
            '#fac858',//黄色
            '#9a60b4',//紫色
            '#ea7ccc',//淡紫
            '#3ba272',//绿色
            '#91cc75',//浅绿
            '#5470c6',//蓝色
            '#73c0de',//淡蓝
<<<<<<< HEAD
          ]
=======
          ],
          textstyle:{
          color: '#fff'
          }
>>>>>>> 5fe5ef1 (first commit)
        },
        geo: {
          map: "china", // 表示中国地图
          // roam: true, // 是否开启鼠标缩放和平移漫游
          zoom: 1.2, // 当前视角的缩放比例（地图的放大比例）
          label: {
            show: false
          },
          emphasis: {  // 地图区域的多边形 图形样式。
            borderColor: "#ffffff",//未选中的状态
            areaColor: "#D8E9FD", //背景颜色
            label: {
              show: true, //显示名称
            },
            itemStyle: {  //选中的状态// 高亮状态下的多边形和标签样式
              shadowBlur: 20,
              shadowColor: "rgba(0, 0, 0, 0.5)",
              borderColor: "#fff",
              areaColor: "#DA3A3A",
            },
          },
        },
        series: [
          {
            name: "地图", // 浮动框的标题（上面的formatter自定义了提示框数据，所以这里可不写）
            type: "map",
            geoIndex: 0,
            label: {
              show: true,
            },
            data: this.MapDataList,
          },
        ],
      };
      this.chinachart.setOption(this.chartOption);
    },
  }
}
</script>


<style>

</style>
