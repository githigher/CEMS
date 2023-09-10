<template>
  <el-row class="tac">
    <el-col :span="24">
      <el-menu
        default-active="/home/HomePage"
        :router="true"
        class="el-menu-vertical-demo"
      >
        <el-menu-item router index="/home/HomePage" v-if="!this.is_admin">
          <el-icon><HomeFilled /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="/home/SubmitApplication" v-if="!this.is_admin">
          <el-icon><Edit /></el-icon>
          <span>提交申请</span>
        </el-menu-item>
        <el-menu-item index="/home/SubmitList" v-if="!this.is_admin">
          <el-icon><Document /></el-icon>
          <span>提交列表</span>
        </el-menu-item>
        <!-- <el-menu-item index="/home/deduct">
          <el-icon><CloseBold /></el-icon>
          <span>扣分查询</span>
        </el-menu-item> -->
        <el-menu-item index="/home/DataVisualization" v-if="!this.is_admin">
          <el-icon><PieChart /></el-icon>
          <span>数据可视化</span>
        </el-menu-item>
        <el-menu-item index="/home/examine" v-if="this.is_admin">
          <el-icon><Checked /></el-icon>
          <span>审核列表</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script lang="ts">
import Cookies from 'js-cookie'
import {
  CloseBold,
  Document,
  Edit,
  HomeFilled,
  PieChart,
  Checked
} from '@element-plus/icons-vue'
export default{
  name: 'Deduct',
  data() {
    return {
      is_admin:'true'
    };
  },
  methods: {

  },
  created(){
    this.is_admin = Cookies.get('UserId').includes('admin')
  }
};
</script>

<style>

</style>