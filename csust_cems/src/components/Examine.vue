<template>
  <PicturePop v-model="LicenseBigDialog" :imgSrc="imgSrc"/>
  <el-table class="submitList" :data="tableData" stripe border>
    <el-table-column prop="date" label="提交时间" /> 
    <el-table-column prop='evidence' label="加分材料" width="130" >
    <template #default="scope">
      <el-image :src="scope.row.evidence" @click="showBigImage(scope.row.evidence)" preview-src-list min-width="70" height="70" />
    </template>
    </el-table-column>
    <el-table-column prop="category" label="加分类别" width="130" />
    <el-table-column prop="summary" label="奖项名称" width="130"/>
    <el-table-column prop="unit" label="颁发单位" width="130" />
    <el-table-column prop="grade" label="获奖等级" width="130" />
    <el-table-column prop="people" label="奖项类型" width="130" />
    <el-table-column prop="score" label="所得分数" width="130" >
      <template #default="scope">
        <el-input
          v-model="scope.row.score"
          autosize
          type="textarea"
          placeholder="Please input"
        />
      </template>    
    </el-table-column>
    <el-table-column label="是否通过" width="130" >
      <template #default="scope">
        <button @click="submit(scope.$index)">通过</button>
      </template>
    </el-table-column>
    <el-table-column prop="notes" label="备注" width="130" >
      <template #default="scope">
        <el-input
          v-model="this.tableData[scope.$index].notes"
          autosize
          type="textarea"
          placeholder="Please input"
        />
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import {onMounted, ref} from 'vue'
import axios from 'axios';
import Cookies from 'js-cookie'
import PicturePop from './PicturePop.vue'

export default{
  name: 'Examine',
  components: {
    PicturePop
  },
  data() {
    return {
      tableData : [],
      LicenseBigDialog: false,
      imgSrc: '',
    };
  },
  methods:{
    showBigImage(src){
      this.LicenseBigDialog = true
      this.imgSrc = src
    },
    submit(index){
      axios.post('http://127.0.0.1:8000/ExamineSubmit', {date:this.tableData[index].date, evidence:this.tableData[index].evidence, notes:this.tableData[index].notes, score:this.tableData[index].score}).then(response =>{
        location.reload()  
      }).catch(error =>{
        alert("Something went wrong...")
      })
    }
  },
  created(){
    axios.post('http://127.0.0.1:8000/examine').then(response =>{
      this.tableData = response.data.res
    }).catch(error =>{
      alert("Something went wrong...")
    })    
  }
  
}
</script>

<style scoped>
  .submitList{
    width: 100%;
  }
</style>
