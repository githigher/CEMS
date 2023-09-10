<template>
  <div class="echarts">
    <v-chart
      class="chart"
      :option = "option"
    />
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie'

export default{
  name: 'BonusPoints',
  data() {
    return {
      data:[],
    };
  },
  computed: {
    option () {
        return {
        title: {
            text: '加分情况展示'
        },
        tooltip: {
            axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value'
        },
        yAxis: {
            type: 'category',
            data: ['劳育', '体育', '德育']
        },
        series: [
            {
            name: '加分',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: this.data.map(d => d.value),
            }
        ]
        }
    }
  },
  methods: {

  },
  created(){
    axios.post('http://127.0.0.1:8000/GetBonusPoints', {id: Cookies.get("UserId")}).then(response =>{
        this.data = response.data.res
    }).catch(error =>{
        alert("Something went wrong...")
    })    
  }
};
</script>

<style scoped>
  .chart {
    height: 400px;
  }
</style>
