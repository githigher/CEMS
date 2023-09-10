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
  name: 'ComprehensiveCapability',
  data() {
    return {
      data:[],
    };
  },
  computed: {
    option () {
        return {
            title: {
                text: '综合能力展示'
            },
            radar: {
                indicator: [
                { name: '思想政治与道德素养', max: 10},
                { name: '学科竞赛与技能培训', max: 10},
                { name: '社会实践与志愿服务', max: 10},
                { name: '文化活动', max: 10},
                { name: '学生干部任职', max: 10},
                { name: '体育活动', max: 10},
                { name: '劳育活动', max: 10}
                ]
            },
            series: [
                {
                    type: 'radar',
                    data: [
                        {
                            value: this.data.map(d => d.value),
                        }
                    ]
                }
            ]
        }
    }
  },
  methods: {

  },
  created(){
    axios.post('http://127.0.0.1:8000/GetComprehensiveCapability', {id: Cookies.get("UserId")}).then(response =>{
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
